# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Validate__Review
# The intent files against their shape: every story has an id, a name, an
# as_a and an i_want; every rule and example an id and a text; every id is
# unique; every source names a document and a section that sections.json
# knows; every surface is a page that exists. Standard library only.
# Usage: python3 review/tools/validate_review.py
# ═══════════════════════════════════════════════════════════════════════════════

import json
import sys

from pathlib import Path

ROOT   = Path(__file__).resolve().parents[2]
REVIEW = ROOT / 'review'


class Validate__Review:

    def __init__(self):
        self.sections = json.loads((REVIEW / 'intent' / 'sections.json').read_text(encoding='utf-8'))
        self.stories  = json.loads((REVIEW / 'intent' / 'stories.json').read_text(encoding='utf-8'))
        self.known    = {(d['doc'], anchor) for d in self.sections['docs'] for anchor in d['sections']}

    def check_source(self, where, source, problems):
        if not isinstance(source, dict) or 'doc' not in source or 'section' not in source:
            problems.append(f'{where}: source must be {{doc, section}}')
            return
        if (source['doc'], source['section']) not in self.known:
            problems.append(f'{where}: source {source["doc"]}#{source["section"]} is not a heading sections.json knows')

    def check_surface(self, where, surface, problems):
        if surface is None:
            return
        path = surface.split('#')[0]
        rel  = path.lstrip('/')
        if rel.endswith('/'):
            rel += 'index.html'
        if not (ROOT / rel).exists():
            problems.append(f'{where}: surface {surface} is not a page in the tree')

    def run(self):
        problems = []
        ids      = []
        prov     = self.stories.get('provenance', {})
        for key in ('kind', 'source_doc', 'written_by', 'accepted_by', 'brief_corrections'):
            if key not in prov:
                problems.append(f'stories.json: provenance is missing "{key}"')
        for story in self.stories.get('stories', []):
            sid = story.get('id', '?')
            for key in ('id', 'name', 'as_a', 'i_want', 'source', 'rules'):
                if key not in story:
                    problems.append(f'story {sid}: missing "{key}"')
            ids.append(sid)
            self.check_source(f'story {sid}', story.get('source'), problems)
            self.check_surface(f'story {sid}', story.get('surface'), problems)
            for rule in story.get('rules', []):
                rid = rule.get('id', '?')
                for key in ('id', 'text', 'source'):
                    if key not in rule:
                        problems.append(f'rule {rid}: missing "{key}"')
                ids.append(rid)
                self.check_source(f'rule {rid}', rule.get('source'), problems)
                for example in rule.get('examples', []):
                    eid = example.get('id', '?')
                    for key in ('id', 'text'):
                        if key not in example:
                            problems.append(f'example {eid}: missing "{key}"')
                    ids.append(eid)
                    self.check_surface(f'example {eid}', example.get('surface'), problems)
        seen = set()
        for node_id in ids:
            if node_id in seen:
                problems.append(f'duplicate node id {node_id}')
            seen.add(node_id)
        if problems:
            print(f'validate_review: {len(problems)} problem(s)')
            for problem in problems:
                print(f'  {problem}')
            return 1
        print(f'validate_review: {len(self.stories["stories"])} stories, {len(ids)} nodes; every source resolves to a heading and every surface to a page')
        return 0


if __name__ == '__main__':
    sys.exit(Validate__Review().run())
