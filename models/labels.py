"""Block labels (1 = main content, 0 = noise) for the two training sources.

WCXB dev (models/data/wcxb/dev): WCXB has no block labels, only the page's ground-truth `main_content` text
(plus with/without snippets, used for evaluation only). A block is labelled content if its text is present in
`main_content`:
  - text is compared after lowercasing and removing all whitespace;
  - blocks <= 300 chars: exact substring, or rapidfuzz partial_ratio >= 85;
  - longer blocks: 120-char chunks; content if >= 50% of chunks are present (substring or partial_ratio >= 85);
  - tables: content if >= 60% of their cells (>= 3 chars) occur in the ground truth;
  - short-block guard: a non-table block under 20 chars (e.g. "Home", "News", "3") matches almost any long
    ground truth by accident, so it is content only if it occurs inside a single ground-truth line at most 3x
    its length (WCXB puts headings on their own lines).
Pages with empty main_content are skipped.

labeling/data/dev: block labels from the LLM labeler (labeling/, Gemini 3.5 Flash-Lite, rubric block-rubric-v1),
joined by block index after checking that the block text/tag match this segmentation. content -> 1,
boilerplate -> 0; uncertain or unresolved -> None (excluded from training and scoring, kept as sequence context).
"""
import re

from rapidfuzz import fuzz

import blocking as B

DUP_THRESHOLD = 85
LONG_BLOCK_CHARS = 300
CHUNK_CHARS = 120
LONG_BLOCK_COVERAGE = 0.5
TABLE_CELL_COVERAGE = 0.6
TABLE_MIN_CELL_CHARS = 3
SHORT_CHARS = 20
SHORT_LINE_RATIO = 3


def fuzzy_norm(s: str) -> str:
    return re.sub(r"\s+", "", s or "").lower()


def presence(text_norm: str, ref_norm: str) -> float:
    """Score in [0, 100]: how much of text_norm appears in ref_norm."""
    if not text_norm or not ref_norm:
        return 0.0
    if text_norm in ref_norm:
        return 100.0
    if len(text_norm) <= LONG_BLOCK_CHARS:
        return fuzz.partial_ratio(text_norm, ref_norm)
    chunks = [text_norm[i:i + CHUNK_CHARS] for i in range(0, len(text_norm), CHUNK_CHARS)]
    chunks = [c for c in chunks if len(c) >= CHUNK_CHARS // 3] or chunks
    hits = sum(c in ref_norm or fuzz.partial_ratio(c, ref_norm) >= DUP_THRESHOLD for c in chunks)
    cov = hits / len(chunks)
    return 100.0 * cov if cov < LONG_BLOCK_COVERAGE else max(DUP_THRESHOLD, 100.0 * cov)


def table_coverage(block, ref_norm: str) -> float:
    cells = set()
    for cell in block.el.xpath(".//td|.//th"):
        c = fuzzy_norm(B.norm_ws(" ".join(cell.itertext())))
        if len(c) >= TABLE_MIN_CELL_CHARS:
            cells.add(c)
    return sum(c in ref_norm for c in cells) / len(cells) if cells else 0.0


def wcxb_labels(blocks, main_content: str):
    """[(label, score)] per block against the ground-truth main_content."""
    ref = fuzzy_norm(main_content)
    lines = [fuzzy_norm(l) for l in main_content.split("\n") if l.strip()]
    out = []
    for b in blocks:
        if b.kind == "table":
            cov = table_coverage(b, ref)
            out.append((int(cov >= TABLE_CELL_COVERAGE), round(100 * cov, 1)))
            continue
        t = fuzzy_norm(b.text)
        score = presence(t, ref)
        hit = score >= DUP_THRESHOLD
        if hit and len(t) < SHORT_CHARS:
            hit = any(t in L and len(L) <= SHORT_LINE_RATIO * len(t) for L in lines)
        out.append((int(hit), round(score, 1)))
    return out


def llm_labels(blocks, labeled_rows):
    """Labels for one labeling/data/dev page; raises if the segmentation does not match the labeled blocks."""
    rows = sorted(labeled_rows, key=lambda r: r["block_index"])
    if len(rows) != len(blocks) or any((b.text, b.tag) != (r["text"], r["tag"]) for b, r in zip(blocks, rows)):
        raise ValueError("segmentation does not match the labeled blocks")
    m = {"content": 1, "boilerplate": 0}
    return [(m.get(r["label"]) if r["status"] == "resolved" else None, r.get("confidence")) for r in rows]
