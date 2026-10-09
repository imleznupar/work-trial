"""Prevent URL, redirect, and exact-snapshot leakage between discovered splits."""
from .common import read_jsonl
from .discovery import normalize_url


class SplitGuard:
    def __init__(self, paths):
        self.urls = set()
        self.snapshots = set()
        self.domains = set()
        for path in paths:
            for row in read_jsonl(path):
                page = row.get('page', row)
                for key in ('url', 'final_url'):
                    if page.get(key):
                        self.urls.add(normalize_url(page[key]))
                snapshot = page.get('snapshot_id') or row.get('snapshot_id')
                if snapshot:
                    self.snapshots.add(snapshot)
                if page.get('domain'):
                    self.domains.add(page['domain'])

    def check(self, url, final_url=None, snapshot_id=None):
        if normalize_url(url) in self.urls or (final_url and normalize_url(final_url) in self.urls):
            raise ValueError('URL or redirect overlaps an excluded split')
        if snapshot_id and snapshot_id in self.snapshots:
            raise ValueError('Snapshot duplicates an excluded split')
