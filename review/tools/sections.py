# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Sections
# Writes review/intent/sections.json: every heading of the brief with the anchor
# the rendered page gives it, so an intent node's {doc, section} source can link
# to the exact place in the brief. Derived from the brief's markdown with the
# same slug rule the renderer uses. The brief's headings are not numbered, so
# the key is the slug itself.
# Usage: python3 review/tools/sections.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re
import sys

from pathlib import Path

ROOT   = Path(__file__).resolve().parents[2]
REVIEW = ROOT / 'review'
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from md_to_html import Markdown__To__Html                                        # noqa: E402


DOCS = (('docs/brief/our-first-customers.md'                  , '/docs/brief/our-first-customers.html'                 ),
        ('docs/brief/memo-2026-10-20-user-onboarding-plan.md' , '/docs/brief/memo-2026-10-20-user-onboarding-plan.html'))


class Sections:

    def __init__(self, check=False, target=REVIEW / 'intent' / 'sections.json'):
        self.check  = check
        self.target = Path(target)

    def collect(self, doc):
        renderer = Markdown__To__Html()
        sections = {}
        in_fence = False
        for line in (ROOT / doc).read_text(encoding='utf-8').splitlines():
            if line.startswith('```'):
                in_fence = not in_fence
            if in_fence or not line.startswith('#'):
                continue
            heading = re.sub(r'^#+\s+', '', line).strip()
            level   = len(line) - len(line.lstrip('#'))
            anchor  = renderer.slug(heading)                                      # keeps the renderer's duplicate counting in step
            sections[anchor] = {'anchor': anchor, 'title': heading, 'level': level}
        return sections

    def run(self):
        data = {'docs': [{'doc': doc, 'page': page, 'sections': self.collect(doc)} for doc, page in DOCS]}
        text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + '\n'
        current = self.target.read_text(encoding='utf-8') if self.target.exists() else None
        changed = current != text
        if changed and not self.check:
            self.target.write_text(text, encoding='utf-8')
        if self.check and changed:
            print(f'sections --check: {self.target.relative_to(ROOT)} is out of date; run python3 review/tools/sections.py')
            return 1
        total = sum(len(d['sections']) for d in data['docs'])
        print(f'sections: {total} headings across {len(DOCS)} document(s){" (updated)" if changed else " (current)"}')
        return 0


if __name__ == '__main__':
    sys.exit(Sections(check='--check' in sys.argv).run())
