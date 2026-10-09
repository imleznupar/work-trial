import argparse
import json
from pathlib import Path
from .common import WORK, benchmark_pages, read_jsonl, write_json, write_jsonl


def main():
    p = argparse.ArgumentParser(description='Independent block labeling pipeline (WCXB dev only)')
    p.add_argument('command',choices=['discover','fetch','label','evaluate','run'])
    p.add_argument('--dataset',choices=['wcxb'])
    p.add_argument('--split',choices=['dev'],default='dev')
    p.add_argument('--input',default=str(WORK/'data/discovered_pages.jsonl'))
    p.add_argument('--output',default=str(WORK/'data/discovered_pages.jsonl'))
    p.add_argument('--labels')
    p.add_argument('--reports',default=str(WORK/'results/wcxb_dev'))
    p.add_argument('--cache',default=str(WORK/'data/cache'))
    p.add_argument('--snapshots',default=str(WORK/'data/snapshots'))
    p.add_argument('--per-type',type=int,default=20)
    p.add_argument('--max-domain',type=int,default=3)
    p.add_argument('--manual',help='JSONL rows containing url and optional page_type')
    p.add_argument('--url-dataset',help='CSV or JSONL URL dataset; default existing candidates_verified.csv')
    p.add_argument('--sitemaps',action='store_true')
    p.add_argument('--delay',type=float,default=1)
    p.add_argument('--seed',type=int,default=0)
    p.add_argument('--limit',type=int)
    p.add_argument('--sample-by-type',action='store_true')
    p.add_argument('--max-chars',type=int,default=24000)
    p.add_argument('--max-blocks',type=int,default=80)
    args = p.parse_args()
    if args.command=='discover':
        from .discovery import discover
        rows, report = discover(args.per_type,args.max_domain,args.manual,args.url_dataset,args.sitemaps,args.delay,args.seed)
        write_jsonl(args.output,rows)
        write_json(Path(args.output).with_suffix('.report.json'),report)
        print(json.dumps(report,indent=2))
        return
    if args.command=='fetch':
        from .discovery import fetch
        fetch(args.input,args.snapshots,args.delay)
        return
    if args.command in ('run','evaluate') and args.dataset!='wcxb':
        p.error('Evaluation requires --dataset wcxb')
    labels = Path(args.labels or WORK/('data/wcxb_dev_labels.jsonl' if args.dataset else 'data/discovered_labels.jsonl'))
    if args.command in ('label','run'):
        from .llm import Client, label_page
        client = Client()
        pages = benchmark_pages(args.split) if args.dataset else read_jsonl(args.input)
        if args.sample_by_type:
            # Round robin across all known types, deterministic page IDs.
            groups = {}
            for page in pages:
                groups.setdefault(page.get('page_type','unknown'),[]).append(page)
            pages = [group[i] for i in range(max(map(len,groups.values()),default=0)) for group in groups.values() if i<len(group)]
        if args.limit is not None:
            pages = pages[:args.limit]
        # Retain earlier completed pages; replace retried pages, never duplicate them.
        old = {r['page']['page_id']:r for r in read_jsonl(labels)}
        failures = 0
        for i,page in enumerate(pages):
            print(f"label {i+1}/{len(pages)} {page['page_id']} {page.get('page_type')} {page['url']}",flush=True)
            try:
                result = label_page(page,args.cache,client,args.max_chars,args.max_blocks)
                old[page['page_id']] = result
                write_jsonl(labels,old.values())
                n = sum(r['status']=='unresolved' for r in result['blocks'])
                failures += bool(n)
                print(f"  {len(result['blocks'])} blocks; {n} unresolved",flush=True)
            except Exception as exc:
                failures += 1
                print('  FAILED '+type(exc).__name__+': '+str(exc)[:300],flush=True)
        write_json(labels.with_suffix('.run.json'),{'provider':client.provider,'model':client.model,'seed':args.seed,
                  'requested_pages':len(pages),'failed_or_unresolved_pages':failures,'labels_path':str(labels)})
        if failures:
            print(f'{failures} pages need attention; rerun resumes successful chunks',flush=True)
    if args.command in ('run','evaluate'):
        from .evaluation import evaluate
        report = evaluate(labels,args.reports,args.split)
        print(json.dumps({'pages':report['pages'],'extraction':report['extraction'],'blocks':report['blocks']},indent=2))

if __name__=='__main__':
    main()
