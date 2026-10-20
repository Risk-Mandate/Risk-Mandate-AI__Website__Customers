# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Render
# Renders the intent files into review/index.html between the review markers:
# every story with its rules and examples, each linked to its section of the
# brief and to the page it lands on, and the counts. Static HTML, no script;
# the navigator as web components is proposed, not built.
# Usage: python3 review/tools/render.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import sys

from pathlib import Path

ROOT   = Path(__file__).resolve().parents[2]
REVIEW = ROOT / 'review'
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from pages import Site__Pages                                                     # noqa: E402


class Render:

    def __init__(self, check=False):
        self.check    = check
        self.pages    = Site__Pages()
        self.sections = json.loads((REVIEW / 'intent' / 'sections.json').read_text(encoding='utf-8'))
        self.stories  = json.loads((REVIEW / 'intent' / 'stories.json').read_text(encoding='utf-8'))
        self.page_of  = {d['doc']: d['page'] for d in self.sections['docs']}
        self.title_of = {(d['doc'], a): s['title'] for d in self.sections['docs'] for a, s in d['sections'].items()}

    def source_link(self, source):
        page = self.page_of[source['doc']]
        return f'<a href="{page}#{source["section"]}">{html.escape(self.title_of[(source["doc"], source["section"])])}</a>'

    def surface_link(self, surface):
        return f' · lands on <a href="{surface}"><code>{html.escape(surface)}</code></a>' if surface else ''

    def body(self):
        stories  = self.stories['stories']
        rules    = sum(len(s['rules']) for s in stories)
        examples = sum(len(r.get('examples', [])) for s in stories for r in s['rules'])
        prov     = self.stories['provenance']
        parts    = ['  <div class="counts" data-generated-from="review/intent/stories.json">',
                    f'    <div class="c"><b>{len(stories)}</b><span>stories</span></div>',
                    f'    <div class="c"><b>{rules}</b><span>rules</span></div>',
                    f'    <div class="c"><b>{examples}</b><span>examples</span></div>',
                    f'    <div class="c"><b>{sum(len(d["sections"]) for d in self.sections["docs"])}</b><span>headings anchored</span></div>',
                    '  </div>',
                    f'  <p>Written by {html.escape(prov["written_by"]["who"])} on {prov["written_by"]["date"]}: {html.escape(prov["written_by"]["note"])}. '
                    f'Accepted by: {html.escape(prov["accepted_by"] or "nobody yet; the lead accepts by a release")}.</p>']
        for story in stories:
            parts.append(f'  <h3 id="{story["id"]}">{html.escape(story["name"])}</h3>')
            parts.append(f'  <p>As {html.escape(story["as_a"])}, I want {html.escape(story["i_want"])}. '
                         f'From {self.source_link(story["source"])}{self.surface_link(story.get("surface"))}.</p>')
            parts.append('  <ul>')
            for rule in story['rules']:
                items = ''.join(f'<li id="{e["id"]}">{html.escape(e["text"])}{self.surface_link(e.get("surface"))}</li>' for e in rule.get('examples', []))
                parts.append(f'    <li id="{rule["id"]}"><strong>{html.escape(rule["text"])}</strong> From {self.source_link(rule["source"])}.'
                             + (f'<ul>{items}</ul>' if items else '') + '</li>')
            parts.append('  </ul>')
        return '\n'.join(parts)

    def run(self):
        page        = REVIEW / 'index.html'
        text        = page.read_text(encoding='utf-8')
        text, found = self.pages.replace_block(text, 'review', self.body())
        if not found:
            raise SystemExit('review/index.html has no rm-customers:review block')
        changed = self.pages.write_if_changed(page, text, self.check)
        if self.check and changed:
            print('render --check: review/index.html is out of date; run python3 review/tools/render.py')
            return 1
        print(f'render: review/index.html {"updated" if changed else "current"}')
        return 0


if __name__ == '__main__':
    sys.exit(Render(check='--check' in sys.argv).run())
