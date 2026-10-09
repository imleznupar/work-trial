"""Dataset and sitemap discovery with conservative robots-aware HTTP access."""
import csv
import json
import time
from collections import Counter
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit
from urllib.robotparser import RobotFileParser
import requests
from lxml import etree
from .common import ROOT, benchmark_pages, digest, now, read_jsonl, write_jsonl

TYPES = ('article','documentation','forum','product','listing','collection','service')
AGENT = 'HTMLBlockLabeling/1.0'
SEEDS = {'article':['https://www.theguardian.com','https://www.sciencedaily.com'],
         'documentation':['https://docs.python.org','https://developer.mozilla.org'],
         'forum':['https://discuss.python.org','https://forum.inaturalist.org'],
         'product':['https://www.ikea.com','https://www.adafruit.com'],
         'listing':['https://www.eventbrite.com','https://www.allrecipes.com'],
         'collection':['https://www.gutenberg.org','https://www.nasa.gov'],
         'service':['https://www.digitalocean.com','https://www.cloudflare.com']}

def normalize_url(url):
    p = urlsplit(url.strip())
    if p.scheme.lower() not in ('http','https') or not p.hostname or p.username or p.password:
        raise ValueError('Expected public HTTP(S) URL')
    host = p.hostname.lower().encode('idna').decode()
    port = p.port
    netloc = ('['+host+']' if ':' in host else host)
    if port and not (p.scheme.lower()=='http' and port==80 or p.scheme.lower()=='https' and port==443):
        netloc += ':'+str(port)
    query = urlencode(sorted((k,v) for k,v in parse_qsl(p.query,keep_blank_values=True)
                             if not k.lower().startswith('utm_') and k.lower() not in ('fbclid','gclid')))
    return urlunsplit((p.scheme.lower(),netloc,p.path or '/',query,''))

def domain(url):
    host = urlsplit(url).hostname or ''
    return host.removeprefix('www.').lower()

def classify(url, hint=None):
    if hint in TYPES:
        return hint
    p = urlsplit(url)
    s = (p.hostname or '') + p.path.lower()
    for kind, words in [('forum',('forum','discuss','/questions/','/topic/')),
                         ('documentation',('docs.','/docs/','/documentation/','/reference/')),
                         ('product',('/product/','/products/','/shop/')),
                         ('article',('/news/','/blog/','/article/','/essays/')),
                         ('collection',('/category/','/collections/','/tags/')),
                         ('listing',('/search','/events/','/jobs/'))]:
        if any(w in s for w in words):
            return kind
    return 'service'

class PoliteHTTP:
    def __init__(self, delay=1.0, max_bytes=10_000_000):
        self.delay, self.max_bytes = delay, max_bytes
        self.robots, self.last = {}, {}
        self.session = requests.Session()
        self.session.headers['User-Agent'] = AGENT

    def wait(self, origin, delay):
        time.sleep(max(0,delay-(time.monotonic()-self.last.get(origin,0))))
        self.last[origin] = time.monotonic()

    def raw(self, url):
        # Redirects are checked separately against the destination robots policy.
        with self.session.get(url, timeout=30, allow_redirects=False, stream=True) as r:
            body = bytearray()
            for chunk in r.iter_content(65536):
                body.extend(chunk)
                if len(body) > self.max_bytes:
                    raise ValueError('Response exceeds maximum snapshot size')
            return r.status_code, dict(r.headers), bytes(body)

    def policy(self, url):
        p = urlsplit(url)
        origin = urlunsplit((p.scheme,p.netloc,'','',''))
        if origin not in self.robots:
            self.wait(origin,self.delay)
            status, _, body = self.raw(origin+'/robots.txt')
            if status in (404,410):
                body = b'User-agent: *\nDisallow:\n'
            elif status != 200:
                raise ValueError('Cannot establish robots policy: HTTP '+str(status))
            rp = RobotFileParser()
            rp.parse(body.decode('utf-8',errors='replace').splitlines())
            self.robots[origin] = rp
        return origin, self.robots[origin]

    def get(self, url):
        url = normalize_url(url)
        for _ in range(6):
            origin, rp = self.policy(url)
            if not rp.can_fetch(AGENT,url):
                raise PermissionError('robots.txt disallows this URL')
            rate = rp.request_rate(AGENT) or rp.request_rate('*')
            delay = max(self.delay,rp.crawl_delay(AGENT) or rp.crawl_delay('*') or 0,
                        rate.seconds/rate.requests if rate and rate.requests else 0)
            self.wait(origin,delay)
            status, headers, body = self.raw(url)
            if status in (301,302,303,307,308) and headers.get('Location'):
                url = normalize_url(urljoin(url,headers['Location']))
                continue
            return status, headers, body, url
        raise ValueError('Too many redirects')

    def sitemap_urls(self, seed, limit=400):
        _, rp = self.policy(seed)
        todo = list(rp.site_maps() or [urljoin(seed,'/sitemap.xml')])
        visited, out = set(), []
        while todo and len(visited)<8 and len(out)<limit:
            sm = todo.pop(0)
            if sm in visited:
                continue
            visited.add(sm)
            status, _, body, _ = self.get(sm)
            if status != 200:
                continue
            root = etree.fromstring(body,parser=etree.XMLParser(resolve_entities=False,no_network=True))
            locs = root.xpath('//*[local-name()="loc"]/text()')
            if etree.QName(root).localname == 'sitemapindex':
                todo.extend(locs[:8])
            else:
                out.extend(locs[:limit-len(out)])
        return out

def discover(per_type=20, max_domain=3, manual=None, dataset=None, sitemaps=False, delay=1, seed=0):
    if per_type<1 or max_domain<1:
        raise ValueError('Counts must be positive')
    bench = benchmark_pages()
    known_urls = {normalize_url(r['url']) for r in bench if r.get('url')}
    known_domains = {r['domain'] for r in bench}
    candidates = []
    if manual:
        candidates.extend((r,'manual') for r in read_jsonl(manual))
    source = Path(dataset) if dataset else ROOT/'data/final/candidates_verified.csv'
    if source.exists():
        with source.open() as f:
            data = list(csv.DictReader(f)) if source.suffix=='.csv' else read_jsonl(source)
        candidates.extend((r,'dataset:'+str(source)) for r in data)
    counts, domains, seen, out = Counter(), Counter(), set(), []
    def add(r, source):
        try:
            url = normalize_url(r['url'])
        except (KeyError,ValueError):
            return
        kind = classify(url,r.get('page_type'))
        host = domain(url)
        if url in seen or counts[kind]>=per_type or domains[host]>=max_domain:
            return
        seen.add(url)
        counts[kind]+=1
        domains[host]+=1
        out.append({'page_id':digest(url)[:20],'url':url,'domain':host,'page_type':kind,
                    'page_type_source':'provided' if r.get('page_type') in TYPES else 'url_heuristic',
                    'discovery_source':source,'discovered_at':now(),'dataset':'discovered','seed':seed,
                    'benchmark_dev_url_overlap':url in known_urls,'benchmark_dev_domain_overlap':host in known_domains,
                    'fetch_timestamp':None,'http_status':None,'error':None})
    import random
    rng = random.Random(seed)
    # Manual rows have priority; randomize only dataset rows.
    manual_rows = [r for r in candidates if r[1]=='manual']
    rest = [r for r in candidates if r[1]!='manual']
    rng.shuffle(rest)
    for r, src in manual_rows+rest:
        add(r,src)
    errors = []
    if sitemaps or any(counts[k]<per_type for k in TYPES):
        http = PoliteHTTP(delay)
        for kind, seeds in SEEDS.items():
            for seed_url in seeds:
                if counts[kind]>=per_type:
                    break
                try:
                    for url in http.sitemap_urls(seed_url):
                        add({'url':url,'page_type':kind},'sitemap:'+seed_url)
                except Exception as exc:
                    errors.append({'source':seed_url,'error':str(exc)[:200]})
    return out, {'counts':dict(counts),'shortfalls':{k:max(0,per_type-counts[k]) for k in TYPES},'errors':errors,'seed':seed}

def fetch(input_path, snapshots, delay=1):
    rows = read_jsonl(input_path)
    http = PoliteHTTP(delay)
    for i,r in enumerate(rows):
        # Benchmark fetching is forbidden; never overwrite a saved snapshot.
        if r.get('dataset')=='wcxb':
            raise ValueError('WCXB must use existing snapshots')
        path = Path(r.get('snapshot_path',''))
        if r.get('snapshot_id') and path.is_file() and digest(path.read_bytes())==r['snapshot_id']:
            continue
        try:
            status, headers, body, final_url = http.get(r['url'])
            r.update(http_status=status,fetch_timestamp=now(),final_url=final_url,error=None)
            if status!=200:
                raise ValueError('HTTP '+str(status))
            if 'html' not in headers.get('Content-Type','').lower():
                raise ValueError('Response is not HTML')
            # Store Unicode HTML so all downstream tools share the same decoding.
            encoding = requests.utils.get_encoding_from_headers(headers) or 'utf-8'
            body = body.decode(encoding,errors='replace').encode('utf-8')
            sid = digest(body)
            path = Path(snapshots)/f'{sid}.html'
            path.parent.mkdir(parents=True,exist_ok=True)
            if not path.exists():
                path.write_bytes(body)
            r.update(snapshot_path=str(path.resolve()),snapshot_id=sid)
        except Exception as exc:
            r.update(error=str(exc)[:300],fetch_timestamp=now())
        write_jsonl(input_path,rows)
        print(f"fetch {i+1}/{len(rows)} {r['url']} status={r.get('http_status')} error={r.get('error')}",flush=True)
    return rows
