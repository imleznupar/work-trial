"""Pulpie on a Modal L4 GPU for the final test eval. Self-contained: imports nothing from this repo; only the test
pages' HTML strings are sent to the container as call arguments.

pulpie 0.0.2, default model orange-small (feyninc/pulpie-orange-small, HF revision pinned). html2text is installed
because pulpie only converts to markdown when it is available (otherwise it returns HTML).

  modal run eval/pulpie_modal.py --mode check   3 test pages; compared with a local CPU run (eval/outputs/_pulpie_cpu)
  modal run eval/pulpie_modal.py --mode final   all 210 test pages -> eval/outputs/pulpie/

One container (max_containers=1), pages sequential (batch 1), one untimed warm-up page. Records container startup,
model load, per-page GPU latency (cuda-synchronized), throughput and an estimate of billed GPU time.
"""
import json
import pathlib
import time

import modal

REPO, REV = "feyninc/pulpie-orange-small", "15ead3350a66e9f15745b7e6619370e3437a5fb0"
SCALEDOWN_S = 10
L4_USD_PER_S = 0.000222  # modal.com/pricing


def download_model():
    from huggingface_hub import snapshot_download
    path = snapshot_download(REPO)
    assert REV in path, f"hub main moved: {path} (expected {REV})"


image = (modal.Image.debian_slim(python_version="3.12")
         .pip_install("pulpie==0.0.2", "torch==2.14.1", "transformers==4.57.6", "tokenizers==0.22.2",
                      "safetensors==0.8.0", "huggingface_hub==0.36.2", "accelerate==1.15.0", "beautifulsoup4==4.15.0",
                      "selectolax==0.4.13", "lxml==6.1.3", "html2text==2025.4.15")
         .run_function(download_model)
         .env({"HF_HUB_OFFLINE": "1"}))
app = modal.App("pulpie-test-eval", image=image)


@app.cls(gpu="L4", timeout=600, scaledown_window=SCALEDOWN_S, max_containers=1)
class Pulpie:
    @modal.enter()
    def load(self):
        self.enter_ts = time.time()
        import torch
        from pulpie import Extractor
        t = time.perf_counter()
        self.ex = Extractor(model="orange-small", device="cuda")
        torch.cuda.synchronize()
        self.load_ms = (time.perf_counter() - t) * 1000
        self.gpu = torch.cuda.get_device_name(0)
        self.warm = False

    @modal.method()
    def extract(self, items, warmup_html=None):
        import importlib.metadata as md
        import torch
        warm_ms = None
        if not self.warm and warmup_html:
            t = time.perf_counter()
            self.ex.extract(warmup_html)
            torch.cuda.synchronize()
            warm_ms, self.warm = (time.perf_counter() - t) * 1000, True
        out = []
        for pid, html in items:
            err, mdown = "", ""
            t = time.perf_counter()
            try:
                mdown = self.ex.extract(html).markdown
            except Exception as e:  # noqa: BLE001
                err = f"{type(e).__name__}: {e}"[:300]
            torch.cuda.synchronize()
            out.append({"page_id": pid, "markdown": mdown, "ms": (time.perf_counter() - t) * 1000, "error": err})
        return {"results": out, "load_ms": self.load_ms, "gpu": self.gpu, "enter_ts": self.enter_ts,
                "warmup_ms": warm_ms, "end_ts": time.time(),
                "versions": {p: md.version(p) for p in ("pulpie", "torch", "transformers", "html2text")}}


@app.local_entrypoint()
def main(mode: str = "check"):
    here = pathlib.Path(__file__).resolve().parent
    test = next(d for d in (here.parent / "labeling loop/data/test", here.parent / "labeling/data/test") if d.exists())
    anns = [json.loads(l) for l in open(test / "annotations.jsonl")]
    read = lambda a: (test / "snapshots" / f"{a['snapshot_id']}.html").read_bytes().decode("utf-8", errors="replace")  # noqa: E731
    sel = anns[:3] if mode == "check" else anns
    items = [(a["page_id"], read(a)) for a in sel]
    warm = read(anns[-1])
    t0 = time.time()
    p = Pulpie()
    calls, results = [], []
    for i in range(0, len(items), 20):
        r = p.extract.remote(items[i:i + 20], warmup_html=warm)
        calls.append({"enter_ts": r["enter_ts"], "end_ts": r["end_ts"], "load_ms": r["load_ms"],
                      "warmup_ms": r["warmup_ms"], "gpu": r["gpu"], "versions": r["versions"]})
        results += r["results"]
    t1 = time.time()
    ms = sorted(x["ms"] for x in results)
    enter = calls[0]["enter_ts"]
    s = {"mode": mode, "pages": len(results), "gpu": calls[0]["gpu"], "versions": calls[0]["versions"],
         "hf_revision": REV, "containers": len({c["enter_ts"] for c in calls}),
         "container_startup_s": enter - t0, "model_load_s": calls[0]["load_ms"] / 1000,
         "warmup_page_ms": calls[0]["warmup_ms"],
         "per_page_ms": {"mean": sum(ms) / len(ms), "median": ms[len(ms) // 2], "p95": ms[int(0.95 * (len(ms) - 1))],
                         "max": ms[-1]},
         "throughput_pages_per_s": len(ms) / (sum(ms) / 1000), "end_to_end_wall_s": t1 - t0,
         "billed_gpu_s_estimate": (calls[-1]["end_ts"] - enter) + SCALEDOWN_S, "usd_per_s": L4_USD_PER_S,
         "errors": sum(bool(x["error"]) for x in results),
         "note": "billed estimate = container uptime from @enter to last call + scaledown window; container_startup_s "
                 "(scheduling + image boot before @enter) is billed too and added in billed_gpu_usd_estimate"}
    s["billed_gpu_usd_estimate"] = (s["billed_gpu_s_estimate"] + s["container_startup_s"]) * L4_USD_PER_S
    out = here / "outputs" / ("_pulpie_check" if mode == "check" else "pulpie")
    out.mkdir(parents=True, exist_ok=True)
    for x in results:
        (out / f"{x['page_id']}.md").write_text(x["markdown"], encoding="utf-8")
    if mode == "final":
        (here / "outputs/_runs").mkdir(parents=True, exist_ok=True)
        (here / "outputs/_runs/pulpie.jsonl").write_text("".join(
            json.dumps({"page_id": x["page_id"], "gpu_ms": round(x["ms"], 2), "error": x["error"],
                        "empty": not x["markdown"].strip()}) + "\n" for x in results))
    (here / "outputs/_runs" / f"pulpie_{mode}_summary.json").write_text(json.dumps(s, indent=1))
    print(json.dumps(s, indent=1))
