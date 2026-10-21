# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Storyboards
# The storyboards and the demos. Validates every storyboard in storyboards/ against
# the kit's vocabulary (api.storyboards.sgit.ai v0.1.0) and the delay limits this
# site's content security policy allows by hash; writes each bundle.json; fills
# every <!-- rm-customers:storyboard:start slug=... --> block with the viewer (a
# template the loader fills, so the kit never wires an empty viewer) and the
# storyboard as text; writes a page per storyboard and the index; and fills every
# <!-- rm-customers:demo:start id=... --> block from data/demos.json.
# The viewer's markup is storyboards.sgit.ai's, in admin/build/templates/.
# Usage: python3 admin/build/gen_storyboards.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import sys

from chrome import ROOT, KIT
from pages  import Site__Pages


BOARDS    = ROOT / 'storyboards'
DEMOS     = ROOT / 'data' / 'demos.json'
VIEWER    = (ROOT / 'admin' / 'build' / 'templates' / 'storyboard-viewer.tpl').read_text(encoding='utf-8').strip()
CUSTOM    = {'what-is-an-abp': '/what-is-an-abp/', 'one-sentence': '/feedback/runs/C1/storyboard/'}                             # a storyboard whose page is written by hand
ORDER     = ('what-is-an-abp', 'one-sentence', 'your-first-policy', 'the-first-batch')
VOCAB     = {'kinds'   : {'cover', 'scene', 'evidence', 'punchline', 'spectrum', 'map', 'graph'},
             'poses'   : {'stand', 'point', 'wave', 'arms-up', 'shrug', 'think', 'sit'},
             'moods'   : {'neutral', 'happy', 'excited', 'calm', 'worried', 'sad', 'surprised', 'thinking', 'confused', 'determined'},
             'settings': {'none', 'office', 'interview', 'street', 'night', 'classroom'},
             'props'   : {'laptop', 'desk', 'book', 'board', 'phone', 'sign',
                          'key', 'vault', 'qr', 'envelope', 'record', 'server', 'arrow', 'mark', 'calendar', 'terminal', 'phoneqr', 'padlock'}}
LOOKS     = {'hair': {'short', 'long', 'curly', 'bun', 'beanie', 'bald'}, 'accessory': {'glasses', 'headphones', 'lanyard'}}
esc       = html.escape


class Gen__Storyboards:

    def __init__(self, check=False):
        self.check  = check
        self.pages  = Site__Pages()
        self.cast   = json.loads((BOARDS / 'cast.json').read_text(encoding='utf-8'))
        self.boards = {slug: json.loads((BOARDS / slug / 'storyboard.json').read_text(encoding='utf-8')) for slug in ORDER}
        self.demos  = {d['id']: d for d in json.loads(DEMOS.read_text(encoding='utf-8'))['demos']}
        self.kinds  = json.loads(DEMOS.read_text(encoding='utf-8'))['kinds']
        self.validate()

    # ── validation: the kit's words, and no list longer than the delays the CSP allows ─

    def validate(self):
        problems = []
        limit    = KIT['style_delays']['count']
        people   = {c['id']: c for c in self.cast['characters']}
        for c in self.cast['characters']:
            for field, allowed in LOOKS.items():
                value = (c.get('look') or {}).get(field)
                if value is not None and value not in allowed:
                    problems.append(f'cast {c["id"]}: look.{field} "{value}" is not one the kit draws ({", ".join(sorted(allowed))})')
        for slug, board in self.boards.items():
            if board['slug'] != slug:
                problems.append(f'{slug}: its slug says {board["slug"]}')
            for n, scene in enumerate(board['scenes'], 1):
                where = f'{slug} panel {n}'
                kind  = scene.get('kind', 'scene')
                for field, value in (('kinds', kind), ('settings', scene.get('setting', 'none'))):
                    if value not in VOCAB[field]:
                        problems.append(f'{where}: {field[:-1]} "{value}" is not in the kit\'s vocabulary')
                for entry in scene.get('cast', []):
                    if entry['who'] not in people:
                        problems.append(f'{where}: "{entry["who"]}" is not in storyboards/cast.json')
                    if entry.get('pose', 'stand') not in VOCAB['poses'] or entry.get('mood', 'neutral') not in VOCAB['moods']:
                        problems.append(f'{where}: {entry["who"]} has a pose or mood the kit does not draw')
                for prop in scene.get('props', []):
                    if prop['kind'] not in VOCAB['props']:
                        problems.append(f'{where}: prop "{prop["kind"]}" is not in the kit or its security pack')
                for name in ('cast', 'stops', 'props'):
                    if len(scene.get(name, [])) > limit:
                        problems.append(f'{where}: {len(scene[name])} {name}, more than the {limit} delays the content security policy allows')
                if kind == 'graph' and len((scene.get('graph') or {}).get('nodes', [])) > limit:
                    problems.append(f'{where}: more graph nodes than the {limit} delays allowed')
        for demo in self.demos.values():
            for kind, _ in demo['lines']:
                if kind not in self.kinds:
                    problems.append(f'demo {demo["id"]}: line kind "{kind}" is not in data/demos.json kinds')
        if problems:
            raise SystemExit('a storyboard or demo is invalid:\n  ' + '\n  '.join(problems))

    # ── fragments ──────────────────────────────────────────────────────────────

    def bundle(self, slug):
        return json.dumps({'storyboard': self.boards[slug], 'cast': self.cast, 'packs': ['security']}, indent=1, ensure_ascii=False) + '\n'

    def scene_text(self, scene):
        head  = scene.get('title') or scene.get('punchline') or scene.get('caption') or ''
        names = {c['id']: c['name'] for c in self.cast['characters']}
        said  = [f'{names[e["who"]]}: “{e["says"]}”' for e in scene.get('cast', []) if e.get('says')]
        extra = [f'{s["label"]}: {s["note"]}' for s in scene.get('stops', [])] + [l for p in scene.get('props', []) for l in (p.get('lines') or [])]
        parts = [f'<b>{esc(head)}</b>'] + [esc(x) for x in said] + ([esc('; '.join(extra))] if extra else []) + ([f'<span class="dim">{esc(scene["note"])}</span>'] if scene.get('note') else [])
        return '<li>' + ' '.join(parts) + '</li>'

    def viewer(self, slug):
        board = self.boards[slug]
        text  = ''.join(self.scene_text(s) for s in board['scenes'])
        return '\n'.join([f'  <div class="sb-host" data-sb-bundle="/storyboards/{slug}/bundle.json">',
                          f'    <template class="sb-template">{VIEWER}</template>',
                          f'    <p class="sb-wait">The storyboard draws here, in your browser, with the kit from <a href="https://api.storyboards.sgit.ai/">api.storyboards.sgit.ai</a>. Without JavaScript, the same panels are below as text.</p>',
                          '  </div>',
                          f'  <details class="sb-text"><summary>{esc(board["title"])}, as text ({len(board["scenes"])} panels)</summary><ol>{text}</ol>'
                          f'<p class="src">The data: <a href="/storyboards/{slug}/bundle.json">bundle.json</a>, the storyboard with its cast. {esc(board.get("rule", ""))}</p></details>'])

    def demo(self, demo_id):
        demo  = self.demos[demo_id]
        lines = ''.join(f'<li class="k-{kind}" data-kind="{kind}">{esc(text)}</li>' for kind, text in demo['lines'])
        frame = (f'<div class="demo-laptop"><div class="demo-screen"><div class="demo-bar"><span></span><span></span><span></span><b>{esc(demo["title"])}</b></div><ol class="demo-lines">{lines}</ol></div><div class="demo-base"></div></div>'
                 if demo['frame'] == 'laptop' else
                 f'<div class="demo-browser"><div class="demo-bar"><span></span><span></span><span></span><b>{esc(demo["title"])}</b></div><ol class="demo-lines chat">{lines}</ol></div>')
        return '\n'.join([f'  <figure class="demo demo-{demo["frame"]}-frame" data-demo="{demo_id}">',
                          f'    {frame}',
                          f'    <figcaption>{esc(demo["caption"])}</figcaption>',
                          '  </figure>'])

    def board_page(self, slug):
        board = self.boards[slug]
        main  = '\n'.join([f'    <p class="kicker">A storyboard · {len(board["scenes"])} panels · {esc(board.get("by", ""))}</p>',
                           f'    <h1>{esc(board["title"])}</h1>',
                           f'    <p class="lead">{esc(board["subtitle"])}</p>',
                           f'    <!-- rm-customers:storyboard:start slug="{slug}" -->', self.viewer(slug), '    <!-- rm-customers:storyboard:end -->',
                           '    <p>More: <a href="/storyboards/">every storyboard on this site</a> · <a href="/policies/">pick your first behaviour policy</a>.</p>'])
        return self.pages.shell(f'{board["title"]}: a storyboard', board['subtitle'] + ' Drawn in your browser by the storyboard kit.', main)

    def index_page(self):
        cards = []
        for slug in ORDER:
            board = self.boards[slug]
            href  = CUSTOM.get(slug, f'/storyboards/{slug}/')
            cards.append(f'      <a class="card" href="{href}"><span class="n">{len(board["scenes"])} panels</span><b>{esc(board["title"])}</b><p>{esc(board["subtitle"])}</p></a>')
        main = '\n'.join(['    <h1>Storyboards</h1>',
                          '    <p class="lead">What an Agent Behaviour Policy is, what you do on this site, and what the first batch is for, drawn as storyboards: data, drawn in your browser by the kit from <a href="https://api.storyboards.sgit.ai/">api.storyboards.sgit.ai</a>, pinned to its release and checked by its hashes. Every storyboard has its panels as text too.</p>',
                          '    <div class="cards">', *cards, '    </div>',
                          '    <p>The cast reuses <a href="https://riskmandate.ai/stories/">riskmandate.ai\'s</a> people, Maya, Dev and Imani, with the agent and the hook as things with faces; it is in <a href="/storyboards/cast.json">storyboards/cast.json</a>. More storyboards, from the rest of the estate, are on <a href="https://storyboards.sgit.ai/">storyboards.sgit.ai</a>.</p>'])
        return self.pages.shell('Storyboards: what an ABP is, your first policy, and the first batch',
                                'Three storyboards drawn in your browser: what an Agent Behaviour Policy is, the five minutes a customer spends installing their first one, and what the first batch is for and what comes next.', main)

    # ── run ────────────────────────────────────────────────────────────────────

    def run(self):
        changed = []
        def put(target, text, page=False):
            if page:
                text = self.pages.keep_chrome(target, text)
            if self.pages.write_if_changed(target, text, self.check):
                changed.append(target.relative_to(ROOT).as_posix())
        for slug in ORDER:
            put(BOARDS / slug / 'bundle.json', self.bundle(slug))
            if slug not in CUSTOM:
                put(BOARDS / slug / 'index.html', self.board_page(slug), page=True)
        put(BOARDS / 'index.html', self.index_page(), page=True)
        for path in self.pages.html_files():
            text = path.read_text(encoding='utf-8')
            if not (self.pages.has_block(text, 'storyboard') or self.pages.has_block(text, 'demo')):
                continue
            text, _ = self.pages.replace_blocks(text, 'storyboard', lambda attrs: self.viewer(attrs['slug']))
            text, _ = self.pages.replace_blocks(text, 'demo'      , lambda attrs: self.demo(attrs['id']))
            put(path, text)
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Storyboards(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  storyboards {verb}: {name}')
    if check and changed:
        print(f'gen_storyboards --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_storyboards.py')
        sys.exit(1)
    print(f'gen_storyboards: {len(changed)} file(s) {verb}')
