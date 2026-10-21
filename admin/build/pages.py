# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Site__Pages
# Finds every HTML page that carries the chrome markers and reads what the
# generators need from it: url path, title, description, main content.
# ═══════════════════════════════════════════════════════════════════════════════

import html
import re

from pathlib import Path

from chrome import ROOT, MARKER_PREFIX


SKIP_DIRS      = {'.git', 'node_modules', '__pycache__', '.pytest_cache', 'vendor', '_site'}
RE_TITLE       = re.compile(r'<title>(.*?)</title>'                                        , re.S)
RE_DESCRIPTION = re.compile(r'<meta\s+name="description"\s+content="(.*?)"'                , re.S)
RE_MAIN        = re.compile(r'<main\b[^>]*>(.*?)</main>'                                   , re.S)
RE_H1          = re.compile(r'<h1\b[^>]*>(.*?)</h1>'                                       , re.S)
RE_SOURCE      = re.compile(r'<meta\s+name="rm-customers:source"\s+content="(.*?)"'         , re.S)


class Site__Pages:

    def __init__(self, root=ROOT):
        self.root = Path(root)

    def html_files(self):
        found = []
        for path in sorted(self.root.rglob('*.html')):
            if SKIP_DIRS & set(path.relative_to(self.root).parts):
                continue
            if self.has_block(path.read_text(encoding='utf-8'), 'head'):         # with or without attributes on the marker
                found.append(path)
        return found

    def marker(self, block, edge):
        return f'<!-- {MARKER_PREFIX}:{block}:{edge} -->'

    def url_path(self, path):
        relative = path.relative_to(self.root).as_posix()
        if relative == 'index.html':
            return '/'
        if relative.endswith('/index.html'):
            return '/' + relative[:-len('index.html')]
        return '/' + relative

    def twin_file(self, path):
        return path.with_suffix('.md')

    def meta(self, path):
        text        = path.read_text(encoding='utf-8')
        title       = RE_TITLE.search(text)
        description = RE_DESCRIPTION.search(text)
        main        = RE_MAIN.search(text)
        if not title or not description or not main:
            raise SystemExit(f'{path.relative_to(self.root)}: needs <title>, <meta name="description"> and <main>')
        source      = RE_SOURCE.search(text)
        return {'path'        : path                                            ,
                'url'         : self.url_path(path)                             ,
                'title'       : html.unescape(title.group(1).strip())           ,
                'description' : html.unescape(description.group(1).strip())     ,
                'main'        : main.group(1)                                   ,
                'source'      : source.group(1) if source else None             }   # the markdown a rendered page came from; it is the twin

    def meta_source(self, path):                                                # the markdown a rendered page came from, or None
        found = RE_SOURCE.search(path.read_text(encoding='utf-8'))
        return found.group(1) if found else None

    def replace_block(self, text, block, body):                                  # one block, no attributes: returns (new_text, found)
        return self.replace_blocks(text, block, lambda attrs: body)

    def replace_blocks(self, text, block, render):                               # every block of this kind; render(attrs) -> body
        pattern = re.compile(rf'(<!-- {MARKER_PREFIX}:{block}:start((?:\s+\w+="[^"]*")*)\s*-->)\n?.*?(?:\n([ \t]*))?(<!-- {MARKER_PREFIX}:{block}:end -->)', re.S)
        found   = [False]

        def swap(match):                                                          # keeps the end marker's own indentation
            found[0] = True
            attrs    = dict(re.findall(r'(\w+)="([^"]*)"', match.group(2)))
            return f'{match.group(1)}\n{render(attrs)}\n{match.group(3) or ""}{match.group(4)}'

        return pattern.sub(swap, text), found[0]

    def keep_chrome(self, target, text):                                         # a generator that writes a whole page keeps the chrome gen_chrome already filled, so a rerun is idempotent
        if not target.exists():
            return text
        current = target.read_text(encoding='utf-8')
        for block in ('head', 'nav', 'footer'):
            found = re.search(rf'<!-- {MARKER_PREFIX}:{block}:start -->\n?(.*?)\n?[ \t]*<!-- {MARKER_PREFIX}:{block}:end -->', current, re.S)
            if found:
                text = text.replace(f'  <!-- {MARKER_PREFIX}:{block}:start -->\n  <!-- {MARKER_PREFIX}:{block}:end -->',
                                    f'  <!-- {MARKER_PREFIX}:{block}:start -->\n{found.group(1)}\n<!-- {MARKER_PREFIX}:{block}:end -->')
        return text

    def shell(self, title, description, main, main_class='wrap'):               # a page a generator writes whole: the chrome markers empty, the content given
        return '\n'.join(['<!doctype html>', '<html lang="en-GB">', '<head>', '  <meta charset="utf-8">',
                          '  <meta name="viewport" content="width=device-width, initial-scale=1">',
                          f'  <title>{html.escape(title)}</title>', f'  <meta name="description" content="{html.escape(description)}">',
                          f'  <!-- {MARKER_PREFIX}:head:start -->', f'  <!-- {MARKER_PREFIX}:head:end -->', '</head>', '<body>',
                          f'  <!-- {MARKER_PREFIX}:nav:start -->', f'  <!-- {MARKER_PREFIX}:nav:end -->',
                          f'  <main class="{main_class}">', main.rstrip('\n'), '  </main>',
                          f'  <!-- {MARKER_PREFIX}:footer:start -->', f'  <!-- {MARKER_PREFIX}:footer:end -->', '</body>', '</html>', ''])

    def has_block(self, text, block):
        return re.search(rf'<!-- {MARKER_PREFIX}:{block}:start', text) is not None

    def write_if_changed(self, path, text, check):                               # returns True when the file is (or would be) changed
        current = path.read_text(encoding='utf-8') if path.exists() else None
        if current == text:
            return False
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding='utf-8')
        return True
