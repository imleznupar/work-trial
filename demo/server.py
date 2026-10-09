"""Local HTML block comparison demo. Run with ../.venv/bin/python server.py."""
import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'models'))
import blocking as B
import classify as C
import features as F
import torch

torch.set_num_threads(1)
MODELS = {name: C.load(name) for name in ('logreg', 'gbm', 'seq')}


def analyze(html, url=None):
    start = time.perf_counter()
    _, blocks = B.segment(html)
    baseline = F.trafilatura_text(html, url)
    features = F.page_features(blocks, baseline)
    systems = {}
    for name, model in MODELS.items():
        scores = C.predict_proba(model, features)
        systems[name] = {'threshold': model['threshold'], 'decisions': [
            {'keep': bool(p >= model['threshold']), 'prob': float(p)} for p in scores]}
    systems['heuristic'] = {'threshold': None, 'decisions': [
        {'keep': bool(row.in_traf), 'prob': None} for row in features.itertuples()]}
    for system in systems.values():
        system['text'] = '\n\n'.join(b.text for b, d in zip(blocks, system['decisions']) if d['keep'])
    systems['heuristic']['original_text'] = baseline
    return {'blocks': [{'index': b.index, 'tag': b.tag, 'kind': b.kind, 'text': b.text} for b in blocks],
            'systems': systems, 'elapsed_ms': round((time.perf_counter() - start) * 1000)}


class Handler(BaseHTTPRequestHandler):
    def respond(self, status, body, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self.respond(200, (HERE / 'index.html').read_bytes(), 'text/html; charset=utf-8')
        else:
            self.respond(404, b'{"error":"Not found"}')

    def do_POST(self):
        if self.path != '/api/analyze':
            self.respond(404, b'{"error":"Not found"}')
            return
        try:
            size = int(self.headers.get('Content-Length', 0))
            if not 0 < size <= 5_000_000:
                self.respond(413, b'{"error":"Submit HTML smaller than 5 MB."}')
                return
            data = json.loads(self.rfile.read(size))
            html = data.get('html')
            url = data.get('url') or None
            if not isinstance(html, str) or not html.strip() or (url is not None and not isinstance(url, str)):
                raise ValueError('Enter HTML and an optional URL as text.')
            result = analyze(html, url)
            self.respond(200, json.dumps(result).encode())
        except (ValueError, TypeError, AttributeError) as exc:
            self.respond(400, json.dumps({'error': str(exc)}).encode())
        except Exception:
            self.respond(500, b'{"error":"Inference failed. See the server terminal for details."}')
            import traceback
            traceback.print_exc()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    print(f'Block demo: http://127.0.0.1:{args.port}', flush=True)
    HTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
