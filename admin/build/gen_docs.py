# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Docs
# Renders every markdown document under docs/ and team/ to an HTML page beside
# it (docs/brief/x.md -> docs/brief/x.html) and writes an index page per
# folder. The markdown stays the source and the twin; the HTML page names it
# in <meta name="rm-customers:source">. Runs before gen_chrome, which fills the
# chrome; only the document block and the head metas are this generator's.
# Usage: python3 admin/build/gen_docs.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import re
import sys

from chrome     import ROOT, Chrome
from md_to_html import Markdown__To__Html
from pages      import Site__Pages


DOCS_ROOT     = ROOT / 'docs'
TEAM_ROOT     = ROOT / 'team'
REVIEW_ROOT   = ROOT / 'review'
RE_H1         = re.compile(r'^#\s+(.+?)\s*$', re.M)
RE_PARAGRAPH  = re.compile(r'^(?!#|\||>|-|\*|\d+\.|```|<|\s*$)(.+?)$', re.M)
RE_TITLE      = re.compile(r'<title>.*?</title>', re.S)
RE_DESC       = re.compile(r'<meta name="description" content=".*?">', re.S)
FOLDERS       = {'brief' : (DOCS_ROOT / 'brief', 'The brief',
                            'The article this site was built from, published in full and never edited; the voice memo that followed it, '
                            'byte for byte; and the corrections file, which is where the brief is told it was wrong.'),
                 'ops'   : (DOCS_ROOT / 'ops', 'Operations',
                            'How a release works, and what only a human can do, as commands where a command exists.'),
                 'team'  : (TEAM_ROOT, 'The team',
                            'Who does what, as one file per role with the rules it enforces and the mistake behind each, and the board of work.'),
                 'review': (REVIEW_ROOT, 'The review folder',
                            'The brief read as intent, the corrections to the review brief, and what is not derived yet.')}
DESCRIPTIONS  = {'our-first-customers.md'                     : 'The brief: the newsroom article of 20 October 2026, published in full as written, with its status and date. Never edited here; corrections go beside it.',
                 'memo-2026-10-20-user-onboarding-plan.md'    : 'The voice memo of 20 October 2026 that followed the brief: the first users are the two founders and the agents they run; the first work is the agent-side and hook-side behaviour policies, for Claude and ChatGPT.',
                 'BRIEF-CORRECTIONS.md'                       : 'Where the brief and the memo were wrong, open, or decided differently while building, dated, beside them.',
                 'reality.md'                                 : 'What exists on this site and in the programme, by status, generated from data/reality.json. If it is not listed, it does not exist.',
                 'release.md'                                 : 'The version, the commit subject, the gate, the four CI jobs, and why green does not mean live.',
                 'themes.md'                                  : 'The six themes: how one attribute picks them, what the gate checks, and how to add a seventh.',
                 'needs.md'                                   : 'Exactly what only a human can do, who, and which step waits on it.',
                 'README.md'                                  : 'The team page: two roles today, one person and one agent, and where the board lives.',
                 'board.md'                                   : 'The board: the work as files with a status line each.',
                 'project-lead.md'                            : 'The project lead: what the person decides, and the rules the role enforces.',
                 'build-agent.md'                             : 'The build agent: the session that builds the site from the brief, under rules with a mistake behind each.',
                 'customer-follow-up.md'                      : 'The follow-up role: the daily contact with each customer, the three questions, and what is recorded where.'}


class Gen__Docs:

    def __init__(self, check=False):
        self.check  = check
        self.chrome = Chrome()
        self.pages  = Site__Pages()

    def sources(self):
        found = []
        for _, (base, _, _) in FOLDERS.items():
            for path in sorted(base.rglob('*.md')):
                if path.name == 'index.md' or 'tools' in path.parts or 'memos' in path.parts:
                    continue
                html_twin = path.with_suffix('.html')
                if html_twin.exists() and not self.pages.meta_source(html_twin):  # a hand-written page whose twin this is
                    continue
                found.append(path)
        found.append(DOCS_ROOT / 'reality.md')
        return found

    def rewrite_link(self, href):                                                 # .md links become .html where a rendering exists
        if re.match(r'^[a-z][a-z0-9+.-]*:', href) and not href.startswith('/'):
            return href
        base, _, fragment = href.partition('#')
        if base.endswith('.md') and not base.endswith('/memos/' + base.rsplit('/', 1)[-1]):
            base = base[:-3] + '.html'
        return base + ('#' + fragment if fragment else '')

    def description_of(self, path, text):
        if path.name in DESCRIPTIONS:
            return DESCRIPTIONS[path.name]
        for match in RE_PARAGRAPH.finditer(text):
            plain = re.sub(r'[*_`\[\]]|\(http[^)]*\)', '', match.group(1)).strip()
            if plain and not plain.startswith('Status:'):
                return plain if len(plain) <= 200 else plain[:197].rstrip() + '…'
        return path.stem

    def skeleton(self, title, description, rel_md, body):
        return '\n'.join(['<!doctype html>'                                                                                  ,
                          '<html lang="en-GB">'                                                                              ,
                          '<head>'                                                                                           ,
                          '  <meta charset="utf-8">'                                                                         ,
                          '  <meta name="viewport" content="width=device-width, initial-scale=1">'                           ,
                          f'  <title>{html.escape(title)}</title>'                                             ,
                          f'  <meta name="description" content="{html.escape(description)}">'                               ,
                          f'  <meta name="rm-customers:source" content="{rel_md}">'                                          ,
                          '  <!-- rm-customers:head:start -->'                                                               ,
                          '  <!-- rm-customers:head:end -->'                                                                 ,
                          '</head>'                                                                                          ,
                          '<body>'                                                                                           ,
                          '  <!-- rm-customers:nav:start -->'                                                                ,
                          '  <!-- rm-customers:nav:end -->'                                                                  ,
                          '  <main class="wrap document">'                                                                   ,
                          '    <!-- rm-customers:docs:start -->'                                                             ,
                          body                                                                                               ,
                          '    <!-- rm-customers:docs:end -->'                                                               ,
                          '  </main>'                                                                                        ,
                          '  <!-- rm-customers:footer:start -->'                                                             ,
                          '  <!-- rm-customers:footer:end -->'                                                               ,
                          '</body>'                                                                                          ,
                          '</html>'                                                                                          ,
                          ''                                                                                                 ])

    def render_document(self, path):
        text   = path.read_text(encoding='utf-8')
        rel_md = '/' + path.relative_to(ROOT).as_posix()
        h1     = RE_H1.search(text)
        title  = re.sub(r'[*_`]', '', h1.group(1)) if h1 else path.stem
        body   = Markdown__To__Html(self.rewrite_link).render(text).rstrip()
        note   = (f'<p class="doc-source">Rendered from <a href="{rel_md}">{rel_md[1:]}</a>, which is the source of truth and the '
                  f'markdown twin of this page. Rendered at site v{self.chrome.version}.</p>')
        return title, self.description_of(path, text), rel_md, f'{note}\n{body}'

    def render_index(self, folder):
        base, label, description = FOLDERS[folder]
        items = []
        for path in sorted(base.rglob('*.md')):
            if path.name == 'index.md' or 'tools' in path.parts or 'memos' in path.parts:
                continue
            text  = path.read_text(encoding='utf-8')
            h1    = RE_H1.search(text)
            title = re.sub(r'[*_`]', '', h1.group(1)) if h1 else path.stem
            url   = '/' + path.relative_to(ROOT).as_posix()
            items.append(f'<li><a href="{url[:-3]}.html">{html.escape(title)}</a>: {html.escape(self.description_of(path, text))} '
                         f'<a href="{url}">(markdown)</a></li>')
        body = '\n'.join([f'<h1>{html.escape(label)}</h1>', f'<p class="lead">{html.escape(description)}</p>', '<ul>', *items, '</ul>'])
        return label, description, body

    def update(self, target, title, description, body, source=None):
        if target.exists():
            text = target.read_text(encoding='utf-8')
            text = RE_TITLE.sub(f'<title>{html.escape(title)}</title>', text, count=1)
            text = RE_DESC.sub(f'<meta name="description" content="{html.escape(description)}">', text, count=1)
            text, found = self.pages.replace_block(text, 'docs', body)
            if not found:
                raise SystemExit(f'{target.relative_to(ROOT)}: exists but has no rm-customers:docs block')
        else:
            text = self.skeleton(title, description, source or '', body)
            if source is None:
                text = text.replace('  <meta name="rm-customers:source" content="">\n', '')
        return self.pages.write_if_changed(target, text, self.check)

    def run(self):
        changed = []
        for path in self.sources():
            title, description, rel_md, body = self.render_document(path)
            if self.update(path.with_suffix('.html'), title, description, body, source=rel_md):
                changed.append(path.with_suffix('.html').relative_to(ROOT).as_posix())
        for folder, (base, _, _) in FOLDERS.items():
            target = base / 'index.html'
            if target.exists() and not self.pages.has_block(target.read_text(encoding='utf-8'), 'docs'):
                continue                                                          # a hand-written index page owns itself
            title, description, body = self.render_index(folder)
            if self.update(target, title, description, body):
                changed.append(target.relative_to(ROOT).as_posix())
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Docs(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  docs {verb}: {name}')
    if check and changed:
        print(f'gen_docs --check: {len(changed)} page(s) out of date; run python3 admin/build/gen_docs.py')
        sys.exit(1)
    print(f'gen_docs: {len(changed)} page(s) {verb}')
