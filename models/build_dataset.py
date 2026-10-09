"""Build the block-level training table from both sources (shared by all three classifiers).

Sources:
  wcxb      WCXB dev split (models/data/wcxb, github.com/Murrough-Foley/web-content-extraction-benchmark, dev/ only;
            the test split is never checked out or read). Labels from ground-truth main_content (labels.py).
  labeling  the 140 LLM-labeled pages in labeling/data/dev (snapshots + block labels).

Per page: blocking.segment -> labels -> features (features.py, incl. trafilatura agreement).
Writes models/data/dataset/{blocks.pkl.gz, pages.csv, build_report.json}.
Usage: python models/build_dataset.py
"""
import glob
import hashlib
import json
import pathlib
import subprocess
import sys
import time
from collections import defaultdict
from multiprocessing import Pool
from urllib.parse import urlparse

import pandas as pd

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import blocking as B  # noqa: E402
import features as F  # noqa: E402
import labels as L  # noqa: E402

WCXB = HERE / "data/wcxb/dev"
LAB = ROOT / "labeling/data/dev"
OUT = HERE / "data/dataset"
TWO_LEVEL = {"co.uk", "org.uk", "ac.uk", "gov.uk", "me.uk", "com.au", "net.au", "org.au", "co.nz", "co.jp", "co.in",
             "com.br", "com.cn", "com.mx", "co.za", "com.sg", "com.tr", "co.kr", "com.hk", "com.tw"}
SHARED_HOSTS = {"github.io", "readthedocs.io", "blogspot.com", "wordpress.com", "substack.com", "medium.com",
                "netlify.app", "vercel.app", "gitlab.io", "pages.dev", "tumblr.com"}


def reg_domain(url: str) -> str:
    """Registrable domain (eTLD+1, one level deeper on shared hosting) used to group CV folds."""
    host = urlparse(url or "").netloc.lower().split(":")[0]
    parts = [p for p in host.split(".") if p]
    if parts[:1] == ["www"]:
        parts = parts[1:]
    if len(parts) < 2:
        return host
    n = 3 if ".".join(parts[-2:]) in TWO_LEVEL else 2
    if ".".join(parts[-2:]) in SHARED_HOSTS:
        n = 3
    return ".".join(parts[-n:])


def wcxb_pages():
    out = []
    for f in sorted(glob.glob(str(WCXB / "ground-truth/*.json"))):
        d, fid = json.load(open(f)), pathlib.Path(f).stem  # file name = HTML file name (file_id is not always set)
        out.append({"source": "wcxb", "page_id": f"wcxb_{fid}", "file_id": fid, "url": d.get("url") or "",
                    "page_type": d["_internal"]["page_type"]["primary"], "html_path": str(WCXB / "html" / f"{fid}.html.gz"),
                    "gt_path": f})
    return out


def labeling_pages():
    pages = [json.loads(l) for l in open(LAB / "pages.jsonl")]
    return [{"source": "labeling", "page_id": f"lab_{p['page_id']}", "lab_id": p["page_id"],
             "url": p.get("final_url") or p["url"], "page_type": p["page_type"], "html_path": p["snapshot_path"]}
            for p in pages]


LAB_ROWS = {}


def read_html(path) -> str:
    """WCXB ships gzipped HTML; labeling snapshots are plain UTF-8."""
    raw = pathlib.Path(path).read_bytes()
    if str(path).endswith(".gz"):
        import gzip
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", errors="replace")


def init(lab_rows):
    LAB_ROWS.update(lab_rows)


def process(page):
    t0 = time.perf_counter()
    meta = {k: page[k] for k in ("source", "page_id", "url", "page_type")}
    meta["domain"] = reg_domain(page["url"])
    html = read_html(page["html_path"])
    gt = None
    if page["source"] == "wcxb":
        gt = json.load(open(page["gt_path"]))["ground_truth"]
        if not (gt.get("main_content") or "").strip():
            return {**meta, "skipped": "empty main_content", "n_blocks": 0}, None
    _, blocks = B.segment(html)
    if not blocks:
        return {**meta, "skipped": "no blocks", "n_blocks": 0}, None
    if page["source"] == "wcxb":
        lab = L.wcxb_labels(blocks, gt["main_content"])
    else:
        lab = L.llm_labels(blocks, LAB_ROWS[page["lab_id"]])
    X = F.page_features(blocks, F.trafilatura_text(html, page["url"] or None))
    X.insert(0, "block_index", range(len(blocks)))
    for k, v in meta.items():
        X.insert(0, k, v)
    X["tag"] = [str(b.tag) for b in blocks]
    X["kind"] = [b.kind for b in blocks]
    X["text"] = [b.text for b in blocks]
    X["label"] = [l for l, _ in lab]
    X["label_score"] = [s for _, s in lab]
    return {**meta, "skipped": "", "n_blocks": len(blocks), "seconds": round(time.perf_counter() - t0, 2)}, X


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def main():
    t0 = time.time()
    lab_rows = defaultdict(list)
    for l in open(LAB / "blocks.jsonl"):
        r = json.loads(l)
        lab_rows[r["page_id"]].append({k: r[k] for k in ("block_index", "text", "tag", "label", "status", "confidence")})
    pages = wcxb_pages() + labeling_pages()
    with Pool(8, initializer=init, initargs=(dict(lab_rows),)) as pool:
        res = pool.map(process, pages, chunksize=4)
    pinfo = pd.DataFrame([m for m, _ in res])
    blocks = pd.concat([x for _, x in res if x is not None], ignore_index=True)
    blocks["label"] = blocks["label"].astype("Float64")
    OUT.mkdir(parents=True, exist_ok=True)
    blocks.to_pickle(OUT / "blocks.pkl.gz")
    pinfo.to_csv(OUT / "pages.csv", index=False)
    lab = blocks.dropna(subset=["label"])
    rep = {
        "built_at": time.strftime("%Y-%m-%d %H:%M"),
        "wcxb_git_commit": subprocess.run(["git", "-C", str(HERE / "data/wcxb"), "rev-parse", "HEAD"],
                                          capture_output=True, text=True).stdout.strip(),
        "labeling_sha256": {f: sha(LAB / f) for f in ("pages.jsonl", "blocks.jsonl")},
        "code_sha256": {f: sha(HERE / f) for f in ("blocking.py", "labels.py", "features.py", "build_dataset.py")},
        "pages": pinfo.groupby("source").size().to_dict(),
        "pages_used": pinfo[pinfo.skipped == ""].groupby("source").size().to_dict(),
        "skipped": pinfo[pinfo.skipped != ""].groupby(["source", "skipped"]).size().rename("n").reset_index().to_dict("records"),
        "domains": blocks.groupby("source").domain.nunique().to_dict(),
        "domain_overlap_between_sources": len(set(blocks[blocks.source == "wcxb"].domain) & set(blocks[blocks.source == "labeling"].domain)),
        "blocks": blocks.groupby("source").size().to_dict(),
        "labeled_blocks": lab.groupby("source").size().to_dict(),
        "excluded_unlabeled_blocks": int(blocks.label.isna().sum()),
        "content_share_blocks": lab.groupby("source").label.mean().round(4).to_dict(),
        "content_share_chars": (lab.assign(c=lab.n_chars * lab.label).groupby("source").c.sum()
                                / lab.groupby("source").n_chars.sum()).round(4).to_dict(),
        "by_type": lab.groupby(["source", "page_type"]).agg(pages=("page_id", "nunique"), blocks=("label", "size"),
                                                             content=("label", "mean")).round(4).reset_index().to_dict("records"),
        "seconds": round(time.time() - t0, 1),
    }
    (OUT / "build_report.json").write_text(json.dumps(rep, indent=1, default=str))
    print(json.dumps({k: rep[k] for k in ("pages_used", "domains", "domain_overlap_between_sources", "blocks",
                                          "labeled_blocks", "content_share_blocks", "content_share_chars", "seconds")}, indent=1))


if __name__ == "__main__":
    main()
