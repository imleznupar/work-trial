"""Generate outputs on the 210 test pages for the CPU systems; no scoring here.

  gbm / logreg / seq   frozen block classifiers (models/frozen), via models/classify (segment -> features incl.
                       trafilatura agreement -> probabilities -> frozen threshold); kept blocks rendered to markdown
  trafilatura          trafilatura.extract(markdown, tables, links) - the baseline

Runtime: one process, pages sequential, single-threaded inference, one untimed warm-up page per system; wall and
CPU ms per page include everything from raw HTML to markdown (for the classifiers: segmentation, trafilatura run
for the agreement features, features, inference, rendering).
Writes eval/outputs/{system}/{page_id}.md, eval/outputs/_runs/{system}.jsonl and, for the classifiers,
eval/outputs/_blocks/{system}.jsonl (per-block probability and decision, for block-level scoring).
"""
import json
import re
import sys
import time

import common as E

import blocking as B  # noqa: E402  (models/)
import classify as CL  # noqa: E402
import features as F  # noqa: E402


def render_block(b) -> str:
    """Markdown for one block: headings, list items, quotes, code fences and tables keep their structure."""
    if b.kind == "table":
        from markdownify import markdownify
        from lxml import etree
        try:
            return markdownify(etree.tostring(b.el, encoding="unicode", with_tail=False), bullets="-").strip()
        except Exception:  # noqa: BLE001  (malformed tags)
            return b.text
    if b.kind == "code":
        code = b.el.text_content().strip("\n")
        return f"```\n{code}\n```" if code.strip() else ""
    if b.kind == "heading":
        return "#" * int(b.tag[1]) + " " + b.text
    if b.kind == "list_item":
        return b.text if re.match(r"^([-*+]|\d+[.)])\s", b.text) else "- " + b.text
    if b.kind == "quote":
        return "> " + b.text
    return b.text


def classifier_system(name):
    clf = CL.load(name)

    def run(html, url):
        _, blocks = B.segment(html)
        X = F.page_features(blocks, F.trafilatura_text(html, url))
        p = CL.predict_proba(clf, X)
        keep = p >= clf["threshold"]
        md = "\n\n".join(m for m in (render_block(b) for b, k in zip(blocks, keep) if k) if m)
        return md, [{"block_index": b.index, "prob": float(pr), "keep": bool(k)} for b, pr, k in zip(blocks, p, keep)]
    return run


def trafilatura_system(html, url):
    import trafilatura
    return (trafilatura.extract(html, url=url, output_format="markdown", include_tables=True, include_links=True,
                                include_comments=False) or ""), None


def main():
    import torch
    torch.set_num_threads(1)
    only = sys.argv[1].split(",") if len(sys.argv) > 1 else ["gbm", "logreg", "seq", "trafilatura"]
    pages = E.pages()
    warm = E.read(pages[0]["snapshot"])
    for s in only:
        fn = trafilatura_system if s == "trafilatura" else classifier_system(s)
        fn(warm, pages[0]["url"])  # warm-up, not timed
        (E.OUT / s).mkdir(parents=True, exist_ok=True)
        (E.OUT / "_runs").mkdir(parents=True, exist_ok=True)
        (E.OUT / "_blocks").mkdir(parents=True, exist_ok=True)
        runs, blocks_out = [], []
        t_sys = time.time()
        for p in pages:
            html = E.read(p["snapshot"])
            err = ""
            w0, c0 = time.perf_counter(), time.process_time()
            try:
                md, bl = fn(html, p["url"])
            except Exception as e:  # noqa: BLE001  (counted as empty output)
                md, bl, err = "", None, f"{type(e).__name__}: {e}"[:300]
            w, c = (time.perf_counter() - w0) * 1000, (time.process_time() - c0) * 1000
            (E.OUT / s / f"{p['page_id']}.md").write_text(md or "", encoding="utf-8")
            runs.append({"page_id": p["page_id"], "wall_ms": round(w, 2), "cpu_ms": round(c, 2), "error": err,
                         "empty": not (md or "").strip()})
            if bl is not None:
                blocks_out.append({"page_id": p["page_id"], "blocks": bl})
        (E.OUT / "_runs" / f"{s}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in runs))
        if blocks_out:
            (E.OUT / "_blocks" / f"{s}.jsonl").write_text("".join(json.dumps(r) + "\n" for r in blocks_out))
        print(f"{s}: {len(pages)} pages in {time.time() - t_sys:.0f}s; errors {sum(bool(r['error']) for r in runs)}, "
              f"empty {sum(r['empty'] for r in runs)}", flush=True)


if __name__ == "__main__":
    main()
