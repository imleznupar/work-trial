import csv
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(os.environ.get('LABELING_PROJECT_ROOT', Path(__file__).resolve().parents[2]))
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'eval'))
WORK = Path(__file__).resolve().parents[1]

def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()

def now():
    return datetime.now(timezone.utc).isoformat()

def read_jsonl(path):
    if not Path(path).exists():
        return []
    return [json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]

def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2))
    tmp.replace(path)

def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
    tmp.replace(path)

def benchmark_pages(split='dev'):
    if split != 'dev':
        raise ValueError('Only WCXB dev is enabled. Final test evaluation requires a future explicit change.')
    # Read metadata index, NEVER annotation files in the labeling/discovery path.
    with (ROOT / 'data/wcxb_blocks/dev_pages.csv').open() as f:
        return [dict(page_id=r['page_id'], url=r['url'], page_type=r['page_type'], domain=r['domain'],
                     dataset='wcxb', split='dev', snapshot_path=str(ROOT / 'data/wcxb/dev/html' / (r['page_id'] + '.html')))
                for r in csv.DictReader(f)]
