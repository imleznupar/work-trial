"""WCXB dev-only evaluation. This is the sole annotation-reading module."""
import json
import csv
from collections import Counter, defaultdict
from pathlib import Path
from .common import ROOT, digest, read_jsonl, write_json, write_jsonl
import blocks as B
import merge as M
import label_alignment as LA
import wcxb_dataset as WD
from block_clf_dev_pages import page_metrics
from score_outputs import md_to_text, norm, snippet_key
from .llm import block_records, segmentation_version


def block_metrics(rows, weighted=False):
    cm = Counter()
    unresolved = uncertain = total = correct = decided = 0
    for r in rows:
        weight = len(r['text']) if weighted else 1
        total += weight
        pred = r.get('label') or 'unresolved'
        truth = r['wcxb_label']
        cm[truth+'->'+pred] += weight
        if pred=='uncertain':
            uncertain += weight
        elif pred=='unresolved':
            unresolved += weight
        else:
            decided += weight
            correct += weight*(truth==pred)
    tp = cm['content->content']
    fp = cm['boilerplate->content']
    # Abstentions never count as correct; content abstentions cost recall.
    fn = sum(v for k,v in cm.items() if k.startswith('content->') and k!='content->content')
    p = tp/(tp+fp) if tp+fp else 0
    rec = tp/(tp+fn) if tp+fn else 0
    return dict(precision=p,recall=rec,f1=2*p*rec/(p+rec) if p+rec else 0,
                confusion=dict(cm),coverage=decided/total if total else 0,
                uncertain_rate=uncertain/total if total else 0,unresolved_rate=unresolved/total if total else 0,
                agreement=correct/total if total else 0,agreement_on_decided=correct/decided if decided else None)


def average(rows):
    keys = ('word_P','word_R','word_F1','include','leak','title_present','author_present','publication_date_present')
    return {k:sum(vals)/len(vals) if vals else None for k in keys
            for vals in [[r[k] for r in rows if r.get(k) is not None]]}


def evaluate(labels_path, output, split='dev'):
    if split!='dev':
        raise ValueError('Only dev evaluation is enabled')
    if not Path(labels_path).is_file():
        raise ValueError('Label file does not exist: '+str(labels_path))
    pages, all_blocks, disagreements, failures = [], [], [], []
    provenance = []
    cached_v1 = {}
    scores = ROOT/'data/wcxb_blocks/dev_page_scores.csv'
    if scores.exists():
        with scores.open() as f:
            cached_v1 = {r['page_id']:{k:float(r[k]) if r.get(k) else None
                         for k in ('word_P','word_R','word_F1','include','leak')}
                         for r in csv.DictReader(f) if r['system']=='block_clf'}
    for result in read_jsonl(labels_path):
        page = result['page']
        if page.get('dataset')!='wcxb' or page.get('split')!='dev':
            continue
        provenance.append({'page_id':page['page_id'],'snapshot_id':result['snapshot_id'],
                           'model':result['model'],'provider':result['provider'],
                           'prompt_version':result['prompt_version'],
                           'segmentation_version':result['segmentation_version']})
        pid = page['page_id']
        if not pid.isdigit():
            raise ValueError('Invalid benchmark page ID')
        raw = (ROOT/'data/wcxb/dev/html'/f'{pid}.html').read_bytes()
        if digest(raw)!=result['snapshot_id'] or result['segmentation_version']!=segmentation_version():
            raise ValueError('Snapshot or segmentation changed: '+pid)
        blocks, records = block_records(raw.decode('utf-8',errors='replace'),result['snapshot_id'])
        saved = result['blocks']
        if [r['block_id'] for r in saved]!=[r['block_id'] for r in records] or [r['text'] for r in saved]!=[b.text for b in blocks]:
            raise ValueError('Block identity mismatch: '+pid)
        # Load full annotations without any length cutoff.
        gt = json.loads((ROOT/'data/wcxb/dev/ground-truth'/f'{pid}.json').read_text())['ground_truth']
        main = gt.get('main_content') or ''
        if not main.strip():
            failures.append({'page_id':pid,'reason':'empty main_content; excluded from metrics'})
            continue
        gt_norm = M.fuzzy_norm(main)
        gt_lines = [M.fuzzy_norm(s) for s in main.splitlines() if s.strip()]
        alignment = LA.GT(main)
        rows = []
        for b,r in zip(blocks,saved):
            label, _, score = WD.label_block(b,gt_norm,gt_lines)
            cov, short = LA.block_coverage(LA.tokens(b.text),alignment)
            row = dict(r,wcxb_label='content' if label else 'boilerplate',wcxb_score=score,
                       alignment_coverage=cov,alignment_short=short)
            rows.append(row)
        keep = {r['block_index'] for r in rows if r['label']=='content'}
        md = B.assemble(blocks,lambda b:b.index in keep)
        md_path = Path(output)/'markdown'/f'{pid}.md'
        md_path.parent.mkdir(parents=True,exist_ok=True)
        md_path.write_text(md)
        metrics = page_metrics(md,gt)
        text = norm(md_to_text(md))
        metadata = {key+'_present':snippet_key(str(gt[key])) in text if gt.get(key) else None
                    for key in ('title','author','publication_date')}
        report = dict(page_id=pid,url=page['url'],page_type=page['page_type'],**metrics,**metadata,
                      blocks=block_metrics(rows),characters=block_metrics(rows,True),baselines={})
        if pid in cached_v1:
            report['baselines']['v1_dev_out_of_fold'] = cached_v1[pid]
        for name, path in [('trafilatura',ROOT/'data/wcxb_cache/trafilatura/dev'/f'{pid}.md'),
                           ('v1',ROOT/'outputs/block_clf'/f'{pid}.md')]:
            if path.exists():
                report['baselines'][name] = page_metrics(path.read_text(),gt)
        pages.append(report)
        all_blocks.extend(rows)
        for category, predicate in [
            ('content_vs_boilerplate',lambda r:r['label']=='content' and r['wcxb_label']=='boilerplate'),
            ('boilerplate_vs_content',lambda r:r['label']=='boilerplate' and r['wcxb_label']=='content'),
            ('uncertain',lambda r:r['label']=='uncertain'),('unresolved',lambda r:r['label'] is None)]:
            examples = [r for r in rows if predicate(r)]
            examples.sort(key=lambda r:len(r['text']),reverse=True)
            for r in examples[:3]:
                disagreements.append(dict(category=category,page_id=pid,url=page['url'],page_type=page['page_type'],
                    block_id=r['block_id'],text=r['text'][:600],reason=r['reason'],wcxb_label=r['wcxb_label'],
                    alignment_coverage=r['alignment_coverage'],word_F1=metrics['word_F1']))
    by_type = {}
    for kind in sorted({p['page_type'] for p in pages}):
        prs = [p for p in pages if p['page_type']==kind]
        brs = [r for r in all_blocks if r['page_type']==kind]
        by_type[kind] = {'pages':len(prs),'extraction':average(prs),'blocks':block_metrics(brs),'characters':block_metrics(brs,True)}
    baseline_names = {name for p in pages for name in p['baselines']}
    report = {'pages':len(pages),'extraction':average(pages),'blocks':block_metrics(all_blocks),
              'synthetic':any(p['provider']=='mock' for p in provenance),'provenance':provenance,
              'characters':block_metrics(all_blocks,True),'by_page_type':by_type,
              'baselines':{name:{'pages':len(rs),'extraction':average(rs)} for name in baseline_names
                           for rs in [[p['baselines'][name] for p in pages if name in p['baselines']]]},
              'poor_pages':sorted(pages,key=lambda p:p['word_F1'])[:10], 'excluded':failures,
              'policy':'WCXB-derived fuzzy alignment labels with existing short-block guard; imperfect page-text proxy, not human block annotations. 5-gram coverage is diagnostic. Uncertain/unresolved abstain, are excluded from Markdown and count as misses for content recall; coverage and agreement reported separately. Extraction scores are macro means; metadata is separate.'}
    write_json(Path(output)/'aggregate.json',report)
    write_jsonl(Path(output)/'pages.jsonl',pages)
    write_jsonl(Path(output)/'disagreements.jsonl',disagreements)
    write_jsonl(Path(output)/'aligned_blocks.jsonl',all_blocks)
    summary = '# WCXB dev labeling evaluation\n\n'+report['policy']+'\n\n'+json.dumps({k:report[k] for k in ('pages','extraction','blocks','characters','by_page_type','baselines')},indent=2)
    if report['synthetic']:
        summary = '**SYNTHETIC MOCK RESPONSES: plumbing validation only, not LLM accuracy.**\n\n'+summary
    summary += '\n\nPoor extraction pages: '+json.dumps([{'url':p['url'],'page_type':p['page_type'],'word_F1':p['word_F1']} for p in report['poor_pages']],indent=2)
    (Path(output)/'report.md').write_text(summary)
    return report
