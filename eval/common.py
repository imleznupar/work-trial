"""Shared paths and helpers for the final evaluation on labeling/data/test (210 pages)."""
import html as htmllib
import json
import pathlib
import re
import sys
import unicodedata

EVAL = pathlib.Path(__file__).resolve().parent
ROOT = EVAL.parent
# the labeling project folder was renamed during this work ("labeling" -> "labeling loop"); accept either,
# or set EVAL_TEST_DIR explicitly
import os
TEST = pathlib.Path(os.environ["EVAL_TEST_DIR"]) if os.environ.get("EVAL_TEST_DIR") else next(
    (d for d in (ROOT / "labeling loop/data/test", ROOT / "labeling/data/test") if d.exists()), ROOT / "labeling/data/test")
OUT = EVAL / "outputs"
RESULTS = EVAL / "results"
sys.path.insert(0, str(ROOT / "models"))

SYSTEMS = ["gbm", "logreg", "seq", "trafilatura", "pulpie"]
LABELS = {"gbm": "Gradient booster", "logreg": "Logistic regression", "seq": "Sequence model (BiGRU)",
          "trafilatura": "trafilatura", "pulpie": "Pulpie (L4 GPU)"}


def annotations():
    return [json.loads(l) for l in open(TEST / "annotations.jsonl")]


def pages():
    """Test pages in annotation order, with snapshot path and URL."""
    meta = {p["page_id"]: p for p in map(json.loads, open(TEST / "pages.jsonl"))}
    out = []
    for a in annotations():
        p = meta[a["page_id"]]
        path = TEST / "snapshots" / f"{a['snapshot_id']}.html"
        out.append({"page_id": a["page_id"], "url": p.get("final_url") or a["url"], "page_type": a["page_type"],
                    "domain": p.get("domain"), "snapshot": path})
    return out


def read(path) -> str:
    return pathlib.Path(path).read_bytes().decode("utf-8", errors="replace")


# ---------------------------------------------------------------- markdown -> text, snippet matching
LINK = re.compile(r"!?\[([^\]]*)\]\((?:<[^>]*>|(?:[^()\s]|\([^()]*\))*)(?:\s+\"[^\"]*\")?\)")
FENCE = re.compile(r"^\s*(```|~~~)")


def md_to_text(md: str) -> str:
    s = LINK.sub(r"\1", md or "")
    s = re.sub(r"<((?:https?|mailto):[^>\s]+)>", r"\1", s)
    s = re.sub(r"<[^>\n]+>", "", s)
    s = htmllib.unescape(s)
    s = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|>~<])", r"\1", s)
    return re.sub(r"[*_`#|>~]", " ", s)


def alnum_key(s: str) -> str:
    """Case-folded Unicode alphanumerics only (the test README's snippet normalization)."""
    s = unicodedata.normalize("NFKC", s).casefold()
    return "".join(ch for ch in s if ch.isalnum())


def snippet_in(snippet: str, text_key: str) -> bool:
    k = alnum_key(md_to_text(snippet))
    return bool(k) and k in text_key


def words(s: str):
    return re.findall(r"\w+", unicodedata.normalize("NFKC", s).lower())


def word_prf(pred: str, ref: str):
    from collections import Counter
    p, r = Counter(words(pred)), Counter(words(ref))
    if not r:
        return (1.0, 1.0, 1.0) if not p else (0.0, 0.0, 0.0)
    if not p:
        return 0.0, 0.0, 0.0
    o = sum((p & r).values())
    P, R = o / sum(p.values()), o / sum(r.values())
    return P, R, (2 * P * R / (P + R) if P + R else 0.0)


# ---------------------------------------------------------------- markdown structure
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+\S")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+\S")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")


def md_structure(md: str) -> dict:
    """Counts of headings, tables, lists, list items and fenced code blocks (outside code fences)."""
    h = t = lists = items = code = 0
    in_fence, prev_item, prev_row = False, False, False
    rows_in_table = 0
    for line in (md or "").splitlines():
        if FENCE.match(line):
            if not in_fence:
                code += 1
            in_fence = not in_fence
            prev_item = prev_row = False
            continue
        if in_fence:
            continue
        if HEADING.match(line):
            h += 1
        is_item = bool(LIST_ITEM.match(line))
        if is_item:
            items += 1
            if not prev_item:
                lists += 1
        if line.strip():
            prev_item = is_item or (prev_item and line.startswith((" ", "\t")))
        is_row = bool(TABLE_ROW.match(line))
        if is_row:
            rows_in_table += 1
            if rows_in_table == 2:
                t += 1
        else:
            rows_in_table = 0
        prev_row = is_row
    return {"headings": h, "tables": t, "lists": lists, "list_items": items, "code": code}


STRUCT_KEYS = ["headings", "tables", "list_items", "code"]


def structure_score(expected: dict, md: str):
    """Mean over structure types the golden page has (count > 0) of min(observed / expected, 1); None if none."""
    obs = md_structure(md)
    parts = {k: min(obs[k] / expected[k], 1.0) for k in STRUCT_KEYS if expected.get(k, 0) > 0}
    return (sum(parts.values()) / len(parts) if parts else None), parts, obs
