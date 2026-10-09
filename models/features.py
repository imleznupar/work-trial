"""Per-block features shared by the three classifiers (computed from the HTML and trafilatura only; never from
labels or ground truth).

Groups:
  text       length, words, punctuation/stopword/digit/uppercase ratios, sentence end, currency
  links      share of the block's characters inside <a>, link count
  structure  tag and kind (categorical codes), heading level, flags, DOM depth, position on the page
  repetition identical-text blocks on the page, same-signature siblings
  ancestors  nav/header/footer/aside/main/article/form ancestors; class/id/role keyword hits; hidden
  phrases    common boilerplate phrases (cookie notices, copyright, sign-up, ...)
  trafilatura how much of the block appears in trafilatura's extraction of the page
"""
import math
import re
from collections import Counter

import numpy as np
import pandas as pd

import blocking as B
import labels as L

TAGS = ["p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "dd", "dt", "figcaption", "blockquote", "table", "pre",
        "div", "section", "article", "main", "header", "footer", "aside", "nav", "form", "td", "th", "span", "ul",
        "button", "label", "other"]
TAG_CODE = {t: i for i, t in enumerate(TAGS)}
KIND_CODE = {k: i for i, k in enumerate(B.KINDS)}
ANCESTOR_TAGS = ["nav", "header", "footer", "aside", "main", "article", "form", "button", "li", "table"]
CLASS_TERMS = {  # keyword -> regex over class/id/role tokens of the block element and its ancestors
    "nav": r"nav|menu|breadcrumb|toolbar|tabs?\b",
    "footer": r"footer|copyright|legal",
    "header": r"header|masthead|topbar|top-bar",
    "sidebar": r"sidebar|aside|widget|rail",
    "related": r"related|recommend|more-from|also|popular|trending|suggest",
    "social": r"share|social|follow|twitter|facebook",
    "comment": r"comment|reply|discuss",
    "cookie": r"cookie|consent|gdpr|privacy",
    "promo": r"\bad\b|ads\b|advert|sponsor|promo|banner",
    "signup": r"newsletter|subscribe|signup|sign-up|login|register",
    "modal": r"modal|popup|dialog|overlay|drawer",
    "cart": r"cart|checkout|basket|bag",
    "content": r"content|article|post|entry|story|body|main|text|prose|markdown",
    "product": r"product|price|sku|variant|review",
}
NOISE_TERMS = ["nav", "footer", "header", "sidebar", "related", "social", "comment", "cookie", "promo", "signup",
               "modal", "cart"]
CLASS_RE = {k: re.compile(v) for k, v in CLASS_TERMS.items()}
PHRASES = re.compile(r"all rights reserved|©|copyright|privacy policy|terms of (use|service)|cookie|sign up|sign in|"
                     r"log in|subscribe|newsletter|follow us|share this|read more|skip to|back to top|"
                     r"add to (cart|bag)|related (posts|articles)|you may also like|advertisement", re.I)
STOPWORDS = set("the a an and or but of to in on at for with by from as is are was were be been it this that "
                "these those he she they we you i his her their our your its not no so if then than there here "
                "what which who when where how all any can will would should could has have had do does did".split())
CURRENCY = re.compile(r"[$€£¥]\s?\d|\d\s?(usd|eur|gbp)\b", re.I)

FEATURES = (["n_chars", "log_chars", "n_words", "avg_word_len", "punct_ratio", "stopword_ratio", "digit_ratio",
             "upper_ratio", "ends_sentence", "n_sentences", "has_currency", "link_density", "link_count",
             "tag_code", "kind_code", "heading_level", "is_table", "is_list_item", "is_heading", "is_code",
             "is_whole", "dom_depth", "rel_pos", "rel_char_pos", "dup_count", "similar_siblings", "n_siblings",
             "is_hidden", "phrase_hit", "page_log_blocks"]
            + [f"anc_{t}" for t in ANCESTOR_TAGS] + [f"cls_{k}" for k in CLASS_TERMS]
            + ["cls_noise_hits", "traf_score", "in_traf"])
CATEGORICAL = ["tag_code", "kind_code"]
NUMERIC = [f for f in FEATURES if f not in CATEGORICAL]


def _tokens(el):
    if not isinstance(el.tag, str):
        return ""
    return " ".join(filter(None, (el.get("class"), el.get("id"), el.get("role"), el.get("aria-label")))).lower()


def _hidden(el):
    style = (el.get("style") or "").replace(" ", "").lower()
    return (el.get("hidden") is not None or el.get("aria-hidden") == "true" or "display:none" in style
            or "visibility:hidden" in style)


def _link_chars(b):
    """Characters of the block's own text that sit inside <a> elements."""
    if b.whole:
        links = list(b.el.iter("a"))
    else:
        links, stack = [], [c for c in b.el if B.is_inline(c)]
        while stack:
            c = stack.pop()
            if c.tag == "a":
                links.append(c)
            else:
                stack.extend(x for x in c if B.is_inline(x))
    text = sum(len(B.norm_ws(B.inline_text(a) if not b.whole else a.text_content())) for a in links)
    return text, len(links)


def trafilatura_text(html: str, url: str = None) -> str:
    import trafilatura
    try:
        return trafilatura.extract(html, url=url, output_format="txt", include_tables=True, include_comments=False,
                                   favor_precision=False) or ""
    except Exception:  # noqa: BLE001
        return ""


def page_features(blocks, traf_text: str) -> pd.DataFrame:
    n = len(blocks)
    if not n:
        return pd.DataFrame(columns=FEATURES)
    total_chars = sum(len(b.text) for b in blocks) or 1
    dup = Counter(b.text for b in blocks)
    traf_norm = L.fuzzy_norm(traf_text)
    rows, cum = [], 0
    for b in blocks:
        t = b.text
        nc = len(t)
        words = re.findall(r"\w+", t)
        nw = len(words)
        letters = [c for c in t if c.isalpha()]
        lc, lk = _link_chars(b)
        ancestors = list(b.el.iterancestors())
        anc_tags = {a.tag for a in ancestors if isinstance(a.tag, str)}
        toks = " ".join([_tokens(b.el)] + [_tokens(a) for a in ancestors])
        cls = {k: int(bool(rx.search(toks))) for k, rx in CLASS_RE.items()}
        parent = b.el.getparent()
        sig = (b.el.tag, b.el.get("class"))
        sibs = [s for s in parent if isinstance(s.tag, str)] if parent is not None else []
        if b.kind == "table":
            ts = 100.0 * L.table_coverage(b, traf_norm)
        else:
            ts = L.presence(L.fuzzy_norm(t), traf_norm)
        r = {
            "n_chars": nc, "log_chars": math.log1p(nc), "n_words": nw,
            "avg_word_len": (sum(map(len, words)) / nw) if nw else 0.0,
            "punct_ratio": sum(c in ".,;:!?\"'()" for c in t) / max(nc, 1),
            "stopword_ratio": sum(w.lower() in STOPWORDS for w in words) / max(nw, 1),
            "digit_ratio": sum(c.isdigit() for c in t) / max(nc, 1),
            "upper_ratio": sum(c.isupper() for c in letters) / max(len(letters), 1),
            "ends_sentence": int(t.rstrip().endswith((".", "!", "?", "”", '"'))),
            "n_sentences": len(re.findall(r"[.!?](\s|$)", t)),
            "has_currency": int(bool(CURRENCY.search(t))),
            "link_density": min(lc / max(nc, 1), 1.0), "link_count": lk,
            "tag_code": TAG_CODE.get(str(b.tag).lower(), TAG_CODE["other"]), "kind_code": KIND_CODE[b.kind],
            "heading_level": int(b.tag[1]) if b.kind == "heading" else 0,
            "is_table": int(b.kind == "table"), "is_list_item": int(b.kind == "list_item"),
            "is_heading": int(b.kind == "heading"), "is_code": int(b.kind == "code"), "is_whole": int(b.whole),
            "dom_depth": len(ancestors), "rel_pos": b.index / max(n - 1, 1), "rel_char_pos": cum / total_chars,
            "dup_count": dup[t] - 1,
            "similar_siblings": sum((s.tag, s.get("class")) == sig for s in sibs) - 1 if sibs else 0,
            "n_siblings": len(sibs), "is_hidden": int(_hidden(b.el) or any(_hidden(a) for a in ancestors)),
            "phrase_hit": int(bool(PHRASES.search(t))), "page_log_blocks": math.log1p(n),
            **{f"anc_{a}": int(a in anc_tags) for a in ANCESTOR_TAGS},
            **{f"cls_{k}": v for k, v in cls.items()},
            "cls_noise_hits": sum(cls[k] for k in NOISE_TERMS),
            "traf_score": ts / 100.0, "in_traf": int(ts >= L.DUP_THRESHOLD),
        }
        cum += nc
        rows.append(r)
    return pd.DataFrame(rows, columns=FEATURES).astype(np.float64)
