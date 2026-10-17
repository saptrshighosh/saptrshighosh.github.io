"""Validate generated portfolio pages, local links, anchors, and content invariants."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.links, self.ids, self.images, self.h1s = path, [], set(), [], 0
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate id in {self.path.name}: {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'h1': self.h1s += 1
        if tag == 'a': self.links.append(a.get('href',''))
        if tag in ['link','script','img']:
            asset=a.get('src',a.get('href',''))
            if asset: self.links.append(asset)
        if tag == 'img':
            assert a.get('alt'), f'Missing image alternative in {self.path.name}'
            self.images.append(a['src'])

pages={p.name:Page(p) for p in ROOT.glob('*.html')}
assert len(pages)==5
for name,p in pages.items():
    assert p.h1s==1, f'{name}: expected one H1'
    for href in p.links:
        u=urlsplit(href)
        if u.scheme or u.netloc: continue
        target=ROOT/unquote(u.path) if u.path else p.path
        assert target.exists(), f'{name}: broken local link {href}'
        if u.fragment and target.suffix=='.html':
            assert u.fragment in pages[target.name].ids, f'{name}: missing anchor {href}'
    assert all(i=='profile.jpg' for i in p.images)
assert sum(len(p.images) for p in pages.values())==1
data=json.loads((ROOT/'assets/content.json').read_text())
assert len(data['projects'])==len({p['id'] for p in data['projects']})==20
combined='\n'.join(p.path.read_text() for p in pages.values())
for old in ['PhD candidate','PhD Candidate','patent pending','GPA 3.5','cdn-cgi/l/email-protection']:
    assert old not in combined, f'Stale claim or broken URL: {old}'
for fact in ['biological sample-level','training-only','8.57 / 10','Aug 2023 – May 2025','Under revision']:
    assert fact in combined, f'Missing verified detail: {fact}'
print(f'PASS: {len(pages)} pages, all local links/anchors, one profile image, 20 projects, and verified content invariants.')
