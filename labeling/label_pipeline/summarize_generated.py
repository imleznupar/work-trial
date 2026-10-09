"""Validate and summarize the balanced discovered-page labels."""
import csv
import argparse
from pathlib import Path
from collections import Counter

from .common import WORK, digest, read_jsonl, write_json, write_jsonl

OUT = WORK / 'data/dev'
TYPES = ('article', 'documentation', 'forum', 'product', 'listing', 'collection', 'service')


def main():
    global OUT
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=OUT)
    parser.add_argument('--per-type', type=int)
    args = parser.parse_args()
    OUT = args.input.resolve()
    status = __import__('json').loads((OUT / 'status.json').read_text()) if (OUT / 'status.json').exists() else {}
    target = args.per_type or status.get('target_per_type', 20)
    rows = read_jsonl(OUT / 'labels.jsonl')
    from .split_guard import SplitGuard
    guard = SplitGuard([WORK / 'data/dev/pages.jsonl', WORK / 'data/dev/labels.jsonl']) if status.get('split') == 'test' else None
    ids = [r['page']['page_id'] for r in rows]
    assert len(ids) == len(set(ids)), 'Duplicate pages'
    counts = Counter()
    blocks = Counter()
    labels = Counter()
    flat = []
    inventory = []
    for r in rows:
        page = r['page']
        if guard:
            guard.check(page['url'], page.get('final_url'), r['snapshot_id'])
        assert page['dataset'] == 'discovered'
        assert not page['benchmark_dev_url_overlap']
        assert digest(open(page['snapshot_path'], 'rb').read()) == r['snapshot_id']
        kind = page['page_type']
        counts[kind] += 1
        blocks[kind] += len(r['blocks'])
        page_counts = Counter(b['label'] or 'unresolved' for b in r['blocks'])
        labels.update(page_counts)
        inventory.append(dict(page_id=page['page_id'], page_type=kind, url=page['url'],
                              blocks=len(r['blocks']), **{k: page_counts[k] for k in
                              ('content', 'boilerplate', 'uncertain', 'unresolved')}))
        flat.extend(dict(b, provider=r['provider'], prompt_version=r['prompt_version'],
                         segmentation_version=r['segmentation_version']) for b in r['blocks'])
    write_jsonl(OUT / 'blocks.jsonl', flat)
    with (OUT / 'inventory.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=['page_id', 'page_type', 'url', 'blocks',
                                             'content', 'boilerplate', 'uncertain', 'unresolved'])
        writer.writeheader()
        writer.writerows(inventory)
    summary = dict(pages=len(rows), blocks=len(flat), page_counts={k: counts[k] for k in TYPES},
                   block_counts={k: blocks[k] for k in TYPES}, labels=dict(labels),
                   complete=all(counts[k] == target for k in TYPES) and labels['unresolved'] == 0,
                   target_per_type=target, split=status.get('split', 'dev'),
                   training_overlap_checked=guard is not None,
                   models=sorted({r['model'] for r in rows}),
                   note='Model-generated labels; new discovered pages have no gold annotations or agreement scores.')
    write_json(OUT / 'summary.json', summary)
    text = '# Discovered-page labels\n\n' + summary['note'] + '\n\n'
    text += '| Page type | Labeled pages | Blocks |\n|---|---:|---:|\n'
    text += ''.join(f'| {k} | {counts[k]} | {blocks[k]} |\n' for k in TYPES)
    text += f'\nTotal: {len(rows)} pages, {len(flat):,} blocks.\n\n'
    text += 'Label counts: ' + ', '.join(f'{k}: {n:,}' for k, n in labels.items()) + '.\n\n'
    text += '`labels.jsonl` preserves complete page envelopes; `blocks.jsonl` contains one row per block. '
    text += '`inventory.csv` lists page URLs and label counts. `pages.jsonl`, `snapshots/`, and `fetch_attempts.jsonl` preserve discovery and fetch provenance. '
    text += 'Uncertain labels are abstentions and should be reviewed or excluded from binary training.\n'
    (OUT / 'report.md').write_text(text)
    print(summary)


if __name__ == '__main__':
    main()
