"""HTML-only block features, kept local to the labeling pipeline."""
import re
from . import segmentation as B


def _ancestors(el):
    out, node = [], el.getparent()
    while node is not None and isinstance(node.tag, str):
        out.append(node)
        node = node.getparent()
    return out


def _links(b):
    if b.whole:
        anchors = list(b.el.iter('a'))
    else:
        anchors = []
        stack = [c for c in b.el if isinstance(c.tag, str) and B.is_inline(c)]
        while stack:
            c = stack.pop()
            if c.tag == 'a':
                anchors.append(c)
            else:
                stack.extend(x for x in c if isinstance(x.tag, str) and B.is_inline(x))
    chars = sum(len(B.norm_ws(' '.join(a.itertext()) if b.whole else B.inline_text(a))) for a in anchors)
    return chars, len(anchors)


def block_hidden_kind(b):
    nodes = [b.el] + _ancestors(b.el)
    stack = list(b.el) if b.whole else [c for c in b.el if isinstance(c.tag, str) and B.is_inline(c)]
    while stack:
        el = stack.pop()
        nodes.append(el)
        stack.extend(c for c in el if isinstance(c.tag, str) and (b.whole or B.is_inline(c)))
    for el in nodes:
        style = re.sub(r'\s+', '', el.get('style', '').lower())
        classes = el.get('class', '').lower()
        if 'hidden' in el.attrib or 'display:none' in style or 'visibility:hidden' in style:
            return 'hidden'
        if el.get('aria-hidden', '').lower() == 'true':
            return 'aria'
        if re.search(r'sr-only|screen-reader|visually-hidden|visuallyhidden', classes):
            return 'sr_only'
    return ''
