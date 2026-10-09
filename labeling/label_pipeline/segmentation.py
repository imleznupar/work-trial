"""Shared preprocessing: segment raw HTML into blocks, in DOM order. Used by all three classifiers.

A block is:
  - p, li, h1-h6, dd, dt, figcaption, blockquote: the element's *own inline content* (text plus inline
    children such as <a>, <span>, <b>); nested structural children (lists, paragraphs, divs, ...) become
    their own blocks;
  - table, pre: the whole element as one block (not descended into);
  - any other element (div, section, article, td, nav, ...): its own inline content, only if that direct
    text is substantial (>= MIN_DIRECT_CHARS characters).
script/style/noscript/template/svg and comments are dropped first. If malformed HTML leaves page content
nested inside one of the dropped tags (other than svg), the tag is unwrapped instead (its own text dropped).

This is the segmentation the 140 LLM-labeled pages in labeling/data/dev were produced with (verified
block-for-block by models/build_dataset.py), so those labels attach to these blocks by index.
"""
import re
from dataclasses import dataclass, field

from lxml import html as lxml_html

BLOCK_TAGS = {"p", "li", "h1", "h2", "h3", "h4", "h5", "h6", "dd", "dt", "figcaption", "blockquote"}
WHOLE_TAGS = {"table", "pre"}
INLINE_TAGS = {"a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "del", "dfn", "em", "font", "i",
               "img", "ins", "kbd", "label", "mark", "q", "s", "samp", "small", "span", "strong", "sub", "sup",
               "time", "tt", "u", "var", "wbr", "big", "strike", "nobr"}
DROP_TAGS = ("script", "style", "noscript", "template", "svg")
MIN_DIRECT_CHARS = 20
KINDS = ["paragraph", "heading", "list_item", "table", "code", "quote", "caption", "term", "container"]


@dataclass
class Block:
    index: int
    tag: str
    kind: str          # one of KINDS
    el: object = field(repr=False)
    whole: bool        # True: the whole element (table/pre); False: the element's own inline content
    text: str = ""     # whitespace-normalized


def kind_of(tag: str) -> str:
    if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        return "heading"
    return {"p": "paragraph", "li": "list_item", "table": "table", "pre": "code", "blockquote": "quote",
            "figcaption": "caption", "dt": "term", "dd": "term"}.get(tag, "container")


def is_inline(el) -> bool:
    return isinstance(el.tag, str) and el.tag.lower() in INLINE_TAGS


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s or "").strip()


def inline_text(el) -> str:
    """Text of an inline element and its inline descendants."""
    if el.tag == "img":
        return ""
    parts = [el.text or ""]
    for child in el:
        if isinstance(child.tag, str) and is_inline(child):
            parts.append(inline_text(child))
        parts.append(child.tail or "")
    return "".join(parts)


def own_inline_text(el) -> str:
    """Text of el excluding descendant non-inline elements (their tails are el's own text)."""
    parts = [el.text or ""]
    for child in el:
        if not isinstance(child.tag, str):  # comments / processing instructions
            parts.append(child.tail or "")
            continue
        if is_inline(child):
            parts.append(inline_text(child))
        parts.append(child.tail or "")
    return "".join(parts)


def table_text(el) -> str:
    return norm_ws(" ".join(el.itertext()))


def clean(doc):
    """Drop script/style/noscript/template/svg and comments in place (see module docstring)."""
    for bad in doc.xpath("|".join(f"//{t}" for t in DROP_TAGS)):
        if bad.getparent() is None:
            continue
        if bad.tag != "svg" and any(isinstance(c.tag, str) for c in bad):
            bad.text = None
            bad.drop_tag()
        else:
            bad.drop_tree()
    for c in doc.xpath("//comment()"):
        parent = c.getparent()
        if parent is None:
            continue
        if c.tail:
            prev = c.getprevious()
            if prev is not None:
                prev.tail = (prev.tail or "") + c.tail
            else:
                parent.text = (parent.text or "") + c.tail
        parent.remove(c)
    return doc


def parse(html: str):
    return clean(lxml_html.fromstring(html))


def _between(top, el):
    """Ancestors of el strictly below top."""
    out, node = [], el.getparent()
    while node is not None and node is not top:
        out.append(node)
        node = node.getparent()
    return out


def segment(html: str, min_direct_chars: int = MIN_DIRECT_CHARS, doc=None):
    """Return (doc, [Block, ...]) in DOM order. If doc (an already-parsed lxml.html tree) is given, it is
    cleaned in place and segmented instead of parsing html again. Unparseable input -> (None, [])."""
    try:
        doc = parse(html) if doc is None else clean(doc)
    except Exception:  # noqa: BLE001  (empty or unparseable document)
        return None, []
    body = doc.find("body")
    root = body if body is not None else doc
    blocks = []

    def emit(el, whole, text):
        blocks.append(Block(len(blocks), el.tag, kind_of(el.tag), el, whole, text))

    def visit(el):
        tag = el.tag.lower() if isinstance(el.tag, str) else None
        if tag is None:
            return
        if tag in WHOLE_TAGS:
            t = table_text(el) if tag == "table" else norm_ws(el.text_content())
            if t:
                emit(el, True, t)
            return
        if tag in INLINE_TAGS:
            return
        own = norm_ws(own_inline_text(el))
        if tag in BLOCK_TAGS:
            if own:
                emit(el, False, own)
        elif el is not root and len(own) >= min_direct_chars:
            emit(el, False, own)
        for child in el:
            if isinstance(child.tag, str) and not is_inline(child):
                visit(child)
                continue
            if not isinstance(child.tag, str) or not is_inline(child):
                continue
            # structural elements nested inside inline wrappers (e.g. <a><div>..</div></a>)
            for sub in child.iter():
                if sub is child or not isinstance(sub.tag, str) or is_inline(sub):
                    continue
                if any(is_inline(a) is False for a in _between(child, sub)):
                    continue
                visit(sub)

    visit(root)
    for i, b in enumerate(blocks):
        b.index = i
    return doc, blocks
