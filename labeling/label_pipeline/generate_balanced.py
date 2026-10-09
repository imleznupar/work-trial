"""Fetch and label a resumable, balanced sample of discovered (non-WCXB) pages."""
import csv
import argparse
import random
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from .common import ROOT, WORK, benchmark_pages, digest, now, read_jsonl, write_json, write_jsonl
from .discovery import TYPES, PoliteHTTP, domain, normalize_url
from .split_guard import SplitGuard

OUT = WORK / 'data/dev'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--max-chars', type=int, default=96000)
    parser.add_argument('--max-blocks', type=int, default=80)
    parser.add_argument('--output', type=Path, default=OUT)
    parser.add_argument('--per-type', type=int, default=20)
    parser.add_argument('--split', choices=('dev', 'test'), default='dev')
    parser.add_argument('--candidates', type=Path)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--exclude', type=Path, action='append', default=[])
    parser.add_argument('--retry-fetches', action='store_true', help='Retry URLs that failed on an earlier run')
    parser.add_argument('--min-content-chars', type=int, default=0, help='Reject newly labeled pages with insufficient primary content')
    args = parser.parse_args()
    if args.workers < 1 or args.max_chars < 2000 or args.max_blocks < 1 or args.per_type < 1:
        parser.error('Invalid worker count or batch limits')
    output = args.output.resolve()
    args.candidates = args.candidates or (output / 'candidates.jsonl' if (output / 'candidates.jsonl').is_file()
                                          else ROOT / 'data/final/candidates_more.csv')
    if args.split == 'test':
        if output == (WORK / 'data/dev').resolve():
            parser.error('Test output must not overwrite data/dev; use --output data/test')
        args.exclude.extend([WORK / 'data/dev/pages.jsonl', WORK / 'data/dev/labels.jsonl'])
        if not (WORK / 'data/dev/pages.jsonl').is_file():
            parser.error('Training metadata is required to exclude dev pages')
    guard = SplitGuard(args.exclude)
    if not args.candidates.is_file():
        parser.error('Candidate pool is missing: ' + str(args.candidates))
    from .llm import Client, label_page

    class RetryingClient(Client):
        def call(self, payload):
            for attempt in range(7):
                try:
                    return super().call(payload)
                except RuntimeError as exc:
                    if 'HTTP status 429' not in str(exc) or attempt == 6:
                        raise
                    time.sleep(min(120, 15 * 2 ** attempt))

    output.mkdir(parents=True, exist_ok=True)
    labels_path = output / 'labels.jsonl'
    pages_path = output / 'pages.jsonl'
    attempts_path = output / 'fetch_attempts.jsonl'
    labels = {r['page']['page_id']: r for r in read_jsonl(labels_path)}
    pages = {r['page_id']: r for r in read_jsonl(pages_path)}
    attempts = read_jsonl(attempts_path)
    bench = benchmark_pages() if (ROOT / 'data/wcxb_blocks/dev_pages.csv').is_file() else []
    excluded = set()
    for p in bench:
        try:
            excluded.add(normalize_url(p['url']))
        except ValueError:
            pass
    bench_domains = {p['domain'] for p in bench}
    with args.candidates.open() as f:
        candidates = list(csv.DictReader(f)) if args.candidates.suffix == '.csv' else read_jsonl(args.candidates)
    random.Random(args.seed).shuffle(candidates)
    client = RetryingClient()
    http = PoliteHTTP(delay=1)
    inflight = {}
    counts = Counter()
    hosts = Counter()
    seen = set()
    if not args.retry_fetches:
        seen.update(r['url'] for r in attempts if r.get('error'))
    for p in pages.values():
        guard.check(p['url'], p.get('final_url'), p.get('snapshot_id'))
        counts[p['page_type']] += 1
        hosts[p['domain']] += 1
        seen.add(p['url'])

    def status(state):
        complete = Counter(r['page']['page_type'] for r in labels.values()
                           if r['blocks'] and all(b['status'] != 'unresolved' for b in r['blocks']))
        write_json(output / 'status.json', dict(timestamp=now(), status=state, target_per_type=args.per_type,
                   selected=dict(counts), completed={k: complete[k] for k in TYPES},
                   provider=client.provider, model=client.model, fetch_attempts=len(attempts),
                   workers=args.workers, max_chars=args.max_chars, max_blocks=args.max_blocks,
                   split=args.split, seed=args.seed, excluded_inputs=[str(p) for p in args.exclude]))

    def collect(wait=False):
        ready = as_completed(list(inflight)) if wait else [f for f in inflight if f.done()]
        for future in ready:
            p = inflight[future]
            try:
                result = future.result()
                if sum(len(b['text']) for b in result['blocks'] if b['label']=='content') < args.min_content_chars:
                    p = dict(p, error='Insufficient labeled primary content')
                    attempts.append(p)
                    write_jsonl(attempts_path, attempts)
                    pages.pop(p['page_id'], None)
                    labels.pop(p['page_id'], None)
                    counts[p['page_type']] -= 1
                    hosts[p['domain']] -= 1
                    write_jsonl(pages_path, pages.values())
                    write_jsonl(labels_path, labels.values())
                    print('REJECTED insufficient content ' + p['url'], flush=True)
                    del inflight[future]
                    status('running')
                    continue
                labels[p['page_id']] = result
                write_jsonl(labels_path, labels.values())
                unresolved = sum(b['status'] == 'unresolved' for b in result['blocks'])
                print(f"LABELED {p['page_type']} {p['url']} blocks={len(result['blocks'])} unresolved={unresolved}", flush=True)
            except Exception as exc:
                print(f"LABEL ERROR {p['url']} {type(exc).__name__}: {str(exc)[:200]}", flush=True)
            del inflight[future]
            status('running')

    def submit(pool, p):
        return pool.submit(label_page, p, output / 'cache', client, args.max_chars, args.max_blocks)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for p in pages.values():
            result = labels.get(p['page_id'])
            if not result or any(b['status'] == 'unresolved' for b in result['blocks']):
                inflight[submit(pool, p)] = p
        for r in candidates:
            collect()
            kind = r['page_type']
            url = normalize_url(r['url'])
            host = domain(url)
            if kind not in TYPES or counts[kind] >= args.per_type or hosts[host] >= 3 or url in seen or url in excluded or url in guard.urls:
                continue
            seen.add(url)
            p = dict(page_id=digest(url)[:20], url=url, domain=host, page_type=kind,
                     page_type_source=r.get('page_type_source', 'provided'),
                     discovery_source=r.get('discovery_source') or 'dataset:' + str(args.candidates.resolve()),
                     discovered_at=now(), dataset='discovered', split=args.split, seed=args.seed,
                     training_url_overlap=False, training_snapshot_overlap=False,
                     training_domain_overlap=host in guard.domains,
                     benchmark_dev_url_overlap=False, benchmark_dev_domain_overlap=host in bench_domains)
            try:
                code, headers, body, final = http.get(url)
                p.update(http_status=code, final_url=final, fetch_timestamp=now())
                if code != 200:
                    raise ValueError('HTTP ' + str(code))
                if 'html' not in headers.get('Content-Type', '').lower():
                    raise ValueError('Response is not HTML')
                if normalize_url(final) in excluded:
                    raise ValueError('Redirect overlaps WCXB dev URL')
                encoding = __import__('requests').utils.get_encoding_from_headers(headers) or 'utf-8'
                body = body.decode(encoding, errors='replace').encode('utf-8')
                snapshot = digest(body)
                guard.check(url, final, snapshot)
                if any(p.get('final_url') == final or p.get('snapshot_id') == snapshot for p in pages.values()):
                    raise ValueError('Duplicate redirect or snapshot within this split')
                path = output / 'snapshots' / (snapshot + '.html')
                path.parent.mkdir(parents=True, exist_ok=True)
                if not path.exists():
                    path.write_bytes(body)
                p.update(snapshot_id=snapshot, snapshot_path=str(path), error=None)
                # Reject empty/error-shell snapshots before using a quota slot.
                from .llm import block_records
                _, blocks = block_records(body.decode('utf-8'), snapshot)
                if not blocks or sum(len(b['text']) for b in blocks) < 200:
                    raise ValueError('Insufficient HTML text')
                pages[p['page_id']] = p
                counts[kind] += 1
                hosts[host] += 1
                write_jsonl(pages_path, pages.values())
                inflight[submit(pool, p)] = p
                print(f"FETCHED {kind} {counts[kind]}/{args.per_type} {url}", flush=True)
            except Exception as exc:
                p.update(error=str(exc)[:300], fetch_timestamp=now())
                print(f"FETCH ERROR {kind} {url}: {p['error']}", flush=True)
            attempts.append(p)
            write_jsonl(attempts_path, attempts)
            status('running')
            if all(counts[k] == args.per_type for k in TYPES):
                break
        collect(wait=True)
        # Retry transient failures after the first pass, retaining successful batches.
        for result in list(labels.values()):
            if any(b['status'] == 'unresolved' for b in result['blocks']):
                p = result['page']
                inflight[submit(pool, p)] = p
        collect(wait=True)
    status('complete' if all(counts[k] == args.per_type for k in TYPES) and len(labels) == args.per_type * len(TYPES)
           and all(r['blocks'] and all(b['status'] != 'unresolved' for b in r['blocks']) for r in labels.values())
           else 'incomplete')
    print((output / 'status.json').read_text(), flush=True)


if __name__ == '__main__':
    main()
