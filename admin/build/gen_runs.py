# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Runs
# Writes everything under feedback/runs/ from data/feedback/runs/: the runs of
# browser agents playing invented users on the live site in real Claude. For
# each run, an article (data/feedback/runs/<id>/article.html, with markers this
# generator fills: replays, the scorecard, the findings, what was kept), the
# replays themselves (the real screenshots, step by step, beside a flow chart
# and what each step means, with what the page said the assistant would write
# beside what it wrote), the storyboard experiment, and copies of the run's
# report and record for agents and people to read. Also the brief a browser
# agent is given, and the personas it may play. `--check` fails on drift.
# Usage: python3 admin/build/gen_runs.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import re
import sys

from chrome import ROOT, AGENT_ADDRESS
from pages  import Site__Pages
from gen_feedback    import webp_size
from gen_storyboards import Gen__Storyboards


DATA    = ROOT / 'data' / 'feedback' / 'runs'
OUT     = ROOT / 'feedback' / 'runs'
SHOTS   = ROOT / 'assets' / 'feedback'
RUNS    = ('C1',)
MATCH   = {'yes': ('matched', 'verdict-confirmed'), 'partly': ('in part', 'verdict-partly'), 'no': ('did not match', 'verdict-artefact'), 'extra': ('not on the page', 'decision-question')}
ACTS    = {1: 'Ask', 2: 'Add the line', 3: 'New chat', 4: 'Talk it out of it'}
PLACES  = {'site': 'customers.riskmandate.ai', 'claude': 'claude.ai · incognito chat', 'chatgpt': 'chatgpt.com · logged out'}
WHO     = {'claude': 'Claude wrote', 'chatgpt': 'ChatGPT wrote'}
esc     = html.escape


class Gen__Runs:

    def __init__(self, check=False):
        self.check    = check
        self.pages    = Site__Pages()
        self.runs     = {rid: json.loads((DATA / rid / 'run.json').read_text(encoding='utf-8')) for rid in RUNS}
        self.personas = json.loads((DATA / 'personas.json').read_text(encoding='utf-8'))
        self.boards   = Gen__Storyboards(check=True)
        self.validate()

    def validate(self):
        problems = []
        for rid, run in self.runs.items():
            sections = {s['id'] for s in run['sections']}
            for i, s in enumerate(run['steps'], 1):
                if s['n'] != i:
                    problems.append(f'{rid} step {i}: numbered {s["n"]}')
                if s['section'] not in sections:
                    problems.append(f'{rid} step {i}: section {s["section"]} is not one of the run\'s sections')
                if not (SHOTS / rid / f'{s["shot"]}.webp').exists():
                    problems.append(f'{rid} step {i}: assets/feedback/{rid}/{s["shot"]}.webp is missing')
                if s['matched'] and s['matched'] not in MATCH:
                    problems.append(f'{rid} step {i}: matched must be one of {tuple(MATCH)}')
                if s['real'] and not s['matched']:
                    problems.append(f'{rid} step {i}: an answer says whether it matched')
                for f in s['findings']:
                    if not any(x['n'] == f for x in run['findings']):
                        problems.append(f'{rid} step {i}: no finding {f}')
            for f in run['findings']:
                if not f.get('proposals'):
                    problems.append(f'{rid} finding {f["n"]}: every finding leads to a proposal')
            if run['persona']['name'].split()[0].lower() not in {p['id'] for p in self.personas['personas']}:
                problems.append(f'{rid}: persona {run["persona"]["name"]} is not on the personas page')
        if problems:
            raise SystemExit('data/feedback/runs/ is invalid:\n  ' + '\n  '.join(problems))

    # ── the replay ─────────────────────────────────────────────────────────────

    def sections(self, run):
        return {s['id']: s for s in run['sections']}

    def act_label(self, act, example):                                             # act 4 is Talk it out of it where the example has one; elsewhere, the agent pushing on it
        return ACTS[act] if act <= 3 or example == 'keep-a-secret' else 'Pushing on it'

    def node(self, steps, label, cls=''):
        return f'<span class="rp-node{cls}" data-steps="{" ".join(str(s["n"]) for s in steps)}">{esc(label)}</span>'

    def flow_full(self, run, steps):                                                # one row per section; an example's row has a node per act
        rows, secs = [], self.sections(run)
        for sec in run['sections']:
            mine = [s for s in steps if s['section'] == sec['id']]
            if not mine:
                continue
            if sec.get('example'):
                acts = []
                for a in sorted({s['act'] for s in mine if s['act']}):
                    at  = [s for s in mine if s['act'] == a]
                    m   = next((s['matched'] for s in at if s['matched']), None)
                    acts.append(self.node(at, self.act_label(a, sec['example']), f' m-{m}' if m else ''))
                page = [s for s in mine if not s['act']]
                if page:
                    acts.insert(0, self.node(page, 'The page'))
                rows.append(f'<div class="rp-row"><span class="rp-label">{esc(sec["title"])}</span><span class="rp-nodes">{"".join(acts)}</span></div>')
            else:
                rows.append(f'<div class="rp-row"><span class="rp-label">{esc(sec["title"])}</span><span class="rp-nodes">{self.node(mine, f"{len(mine)} step" + ("s" if len(mine) != 1 else ""))}</span></div>')
        return '<div class="rp-flow rp-flow-full" aria-label="The run, as a flow chart">' + ''.join(rows) + '</div>'

    def flow_line(self, steps):                                                     # one row: the page, then each act, with arrows
        nodes = []
        page  = [s for s in steps if not s['act']]
        if page:
            nodes.append(self.node(page, 'The page'))
        for a in sorted({s['act'] for s in steps if s['act']}):
            at = [s for s in steps if s['act'] == a]
            m  = next((s['matched'] for s in at if s['matched']), None)
            nodes.append(self.node(at, self.act_label(a, at[0]['example']), f' m-{m}' if m else ''))
        return '<div class="rp-flow rp-flow-line" aria-label="The steps, as a flow chart">' + '<span class="rp-arrow" aria-hidden="true">&#8594;</span>'.join(nodes) + '</div>'

    def note(self, run, s):
        secs = self.sections(run)
        vs   = ''
        if s['real']:
            label, cls = MATCH[s['matched']]
            said = f'<div><span class="rp-k">The page said</span><q class="verbatim">{esc(s["expected"])}</q></div>' if s['expected'] else ''
            vs   = (f'<div class="rp-vs">{said}<div><span class="rp-k">{WHO.get(s["place"], "It wrote")}</span><q class="verbatim">{esc(s["real"])}</q></div>'
                    f'<span class="decision {cls}">{label}</span></div>')
        meaning = f'<p class="rp-meaning">{esc(s["meaning"])}</p>' if s['meaning'] else ''
        return (f'<li data-n="{s["n"]}"><p class="rp-step">Step {s["n"]} · {esc(secs[s["section"]]["title"])}</p><b>{esc(s["title"])}</b>'
                f'<p class="verbatim">{esc(s["saw"])}</p>{meaning}{vs}</li>')

    def replay(self, rid, steps, ident, flow, caption, sync=None, panels=None):
        run, secs = self.runs[rid], self.sections(self.runs[rid])
        shots = []
        for s in steps:
            w, h  = webp_size(SHOTS / rid / f'{s["shot"]}.webp')
            panel = f' data-panel="{panels[s["n"]]}"' if panels and s['n'] in panels else ''
            shots.append(f'<li data-n="{s["n"]}" data-section="{s["section"]}" data-section-title="{esc(secs[s["section"]]["title"], quote=True)}" data-place="{s["place"]}" '
                         f'data-where="{esc(PLACES[s["place"]] if s["place"] != "site" else "customers.riskmandate.ai" + (s["where"] if s["where"].startswith("/") else ""), quote=True)}" data-title="{esc(s["title"], quote=True)}"{panel}>'
                         f'<img src="/assets/feedback/{rid}/{s["shot"]}.webp" width="{w}" height="{h}" loading="lazy" alt="Step {s["n"]}: {esc(s["title"], quote=True)}"></li>')
        return '\n'.join([
            f'    <figure class="replay" id="{ident}"' + (f' data-sync="{sync}"' if sync else '') + '>',
            '      <div class="rp-grid">',
            f'        <div class="rp-screen"><div class="rp-chrome"><span class="rp-dots" aria-hidden="true"></span><span class="rp-place">{esc(PLACES[steps[0]["place"]])}</span></div><ol class="rp-shots">{"".join(shots)}</ol></div>',
            f'        <div class="rp-side">{flow}<ol class="rp-notes">{"".join(self.note(run, s) for s in steps)}</ol></div>',
            '      </div>',
            f'      <figcaption>{caption}</figcaption>',
            '    </figure>'])

    # ── the article's parts ────────────────────────────────────────────────────

    def scorecard(self, rid):
        run, secs = self.runs[rid], self.sections(self.runs[rid])
        rows = []
        for sec in run['sections']:
            if not sec.get('example'):
                continue
            cells = []
            for a in (1, 2, 3, 4):
                at = [s for s in run['steps'] if s['section'] == sec['id'] and s['act'] == a and s['matched']]
                if not at:
                    cells.append('<td class="dim">·</td>')
                    continue
                label, cls = MATCH[at[0]['matched']]
                cells.append(f'<td><a class="decision {cls}" href="#replay" data-replay-jump="rp-full:{at[0]["n"]}">{label}</a><q class="sc-real verbatim">{esc((at[0]["real"] or "")[:90])}{"…" if len(at[0]["real"] or "") > 90 else ""}</q></td>')
            rows.append(f'<tr><th scope="row">{esc(sec["title"])}</th>{"".join(cells)}</tr>')
        return '<table class="scorecard"><thead><tr><th>Example</th><th>Act 1 · ask</th><th>Act 2 · add the line</th><th>Act 3 · new chat</th><th>Beyond the page</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table>'

    def findings(self, rid):
        run, items = self.runs[rid], []
        for f in run['findings']:
            steps = [s['n'] for s in run['steps'] if f['n'] in s['findings']]
            links = ', '.join(f'<a href="#replay" data-replay-jump="rp-full:{n}">{n}</a>' for n in steps)
            props = ', '.join(f'<a href="/feedback/reviews/#{p.lower()}">{p}</a>' for p in f['proposals'])
            items.append(f'<li><p><b>{f["n"]}.</b> <q class="verbatim">{esc(f["title"])}</q> <span class="decision verdict-{f["verdict"]}">{esc(f["verdict"])}</span> <span class="decision decision-done">{esc(f["status"])}</span></p>'
                         f'<p>{esc(f["note"])}</p><p class="dim">Steps {links or "none"} · leads to {props}.</p></li>')
        return '<ol class="run-findings">' + ''.join(items) + '</ol>'

    def kept(self, rid):
        return '<ul class="plist">' + ''.join(f'<li class="verbatim">{esc(k)}</li>' for k in self.runs[rid]['kept']) + '</ul>'

    def example_replays(self, rid):
        run, out = self.runs[rid], []
        for sec in run['sections']:
            if not sec.get('example'):
                continue
            steps = [s for s in run['steps'] if s['section'] == sec['id']]
            out.append(f'    <h3 id="ex-{sec["example"]}">{esc(sec["title"])}</h3>')
            out.append(self.replay(rid, steps, f'rp-{sec["id"]}', self.flow_line(steps),
                                   f'Run C1, {esc(sec["title"])}: steps {steps[0]["n"]} to {steps[-1]["n"]}, real screenshots. <a href="/examples/{sec["example"]}/">The example</a>.'))
        return '\n'.join(out)

    def article(self, rid):
        run  = self.runs[rid]
        text = (DATA / rid / 'article.html').read_text(encoding='utf-8')
        ex4  = [s for s in run['steps'] if s['section'] == 'ex4']
        text = text.replace('    <!-- replay:full -->', self.replay(rid, run['steps'], 'rp-full', self.flow_full(run, run['steps']),
                            f'Run C1, all {len(run["steps"])} steps: the real screenshots, as the agent took them, in Chrome on an iMac, 21 October 2026.'))
        text = text.replace('    <!-- replay:ex4 -->', self.replay(rid, ex4, 'rp-one-sentence', self.flow_line(ex4),
                            'Keep a secret in real Claude, steps 23 to 27: the page, act 1, act 2, act 3, and one sentence. <a href="/feedback/runs/C1/storyboard/">The same, beside a storyboard</a>.'))
        text = text.replace('    <!-- replay:examples -->', self.example_replays(rid))
        text = text.replace('    <!-- scorecard -->', '    ' + self.scorecard(rid))
        text = text.replace('    <!-- findings -->', '    ' + self.findings(rid))
        text = text.replace('    <!-- kept -->', '    ' + self.kept(rid))
        if '<!--' in text:
            raise SystemExit(f'data/feedback/runs/{rid}/article.html: a marker was not filled: {re.search(r"<!--.*?-->", text).group(0)}')
        return self.pages.shell(f'Run C1: {run["title"]}; what worked, what did not, and what we changed',
                                'An agent played Priya, an invented operations lead, through all six examples in real Claude, in Chrome, and sent back forty screenshots and a report. The run replayed step by step beside a flow chart, the scorecard, what worked, what did not, the one sentence that switched a line off, and what we changed.',
                                text, 'wrap document-wide run-article')

    def storyboard_page(self, rid):
        run   = self.runs[rid]
        steps = [s for s in run['steps'] if s['section'] == 'ex4']
        panels = {23: 1, 24: 2, 25: 3, 26: 4, 27: 5}
        main = '\n'.join([
            '    <p class="kicker">Run C1 · an experiment · the real run beside a drawn one</p>',
            '    <h1>One sentence, <span class="g">real and drawn.</span></h1>',
            '    <p class="lead">Five steps of a real run, Keep a secret in real Claude, beside a storyboard drawn from them. Press Play on the replay and the storyboard turns with it: the screenshot says what happened, the panel says what it means.</p>',
            '    <p class="banner-invented"><b>An invented user, a real run.</b> Priya does not exist; the chats with Claude and their answers were real. The storyboard\'s words are shortened from them.</p>',
            '    <div class="sb-beside">',
            '      <div class="sb-beside-board" id="sb-one-sentence">',
            self.boards.viewer('one-sentence').replace('<div class="sb-host"', '<div class="sb-host" id="sb-one-sentence-host"', 1),
            '      </div>',
            '      <div class="sb-beside-run">',
            self.replay(rid, steps, 'rp-sb', self.flow_line(steps), 'Run C1, steps 23 to 27. The storyboard turns with each step, and to its last panel at the end.', sync='sb-one-sentence-host', panels=panels).replace('data-sync=', 'data-panel-end="6" data-sync=', 1),
            '      </div>',
            '    </div>',
            '    <h2>Why try this</h2>',
            '    <p>A screenshot is evidence: it is what really happened, and it is dense. A storyboard is the story: one idea a panel, with faces. Shown together, a newcomer gets both at once, and the sixth panel says the thing no screenshot can: <em>whoever can talk to it can talk it out of the line</em>. Tell us whether it helped: <a href="/feedback/">tell us what you think</a>.</p>',
            '    <p>The whole run: <a href="/feedback/runs/C1/">Priya tries the six examples in real Claude</a>. The storyboard alone, as data: <a href="/storyboards/one-sentence/bundle.json">bundle.json</a>.</p>'])
        return self.pages.shell('One sentence, real and drawn: a run beside its storyboard',
                                'An experiment: five steps of a real run of Keep a secret in Claude, played beside a storyboard drawn from them, turning together. The line holds, and then one sentence switches it off.',
                                main, 'wrap document-wide run-article run-wide')

    def index_page(self):
        cards = ''.join(f'<a class="card card-thumb" href="/feedback/runs/{rid}/"><img src="/assets/feedback/{rid}/27.webp" alt="The step that matters in run {rid}" width="640" height="400" loading="lazy">'
                        f'<span class="n">Run {rid} · {esc(r["persona"]["name"])} · site v{esc(r["site_version"])}</span><b>{esc(r["title"])}</b><p>{len(r["steps"])} steps, {len(r["findings"])} findings, each checked, and replayed.</p></a>'
                        for rid, r in self.runs.items())
        main = '\n'.join([
            '    <h1>Runs: invented users, <span class="g">in a real browser, in real Claude.</span></h1>',
            '    <p class="lead">An agent plays one invented person, drives a real browser on the live site, tries every example in real Claude, and sends back its screenshots, its report and a record of every step. Each run is replayed here, step by step, with what we found and what we changed.</p>',
            '    <p class="banner-invented"><b>Invented users, real runs.</b> The people are invented and a model plays them; the browser, the site and the assistant\'s answers are real. This is not user research.</p>',
            f'    <div class="cards thumbs">{cards}</div>',
            '    <h2>Run one yourself</h2>',
            '    <ul class="plist">',
            '      <li><strong><a href="/feedback/runs/brief/">The brief for browser agents</a>:</strong> what to give an agent that can drive a browser, such as Claude in Chrome: who to be, the rules, what to capture at every step, and the record to send back.</li>',
            '      <li><strong><a href="/feedback/runs/personas/">The personas</a>:</strong> the invented people it may play, and which have been played.</li>',
            '      <li><strong><a href="/feedback/synthetic/">Study S1</a>:</strong> the first study, in a headless browser on a copy of the site, before any run in a real one.</li>',
            '    </ul>'])
        return self.pages.shell('Runs: invented users in a real browser, in real Claude, replayed',
                                'Runs of browser agents playing invented users on customers.riskmandate.ai, in real Claude: each replayed step by step from its screenshots, with its findings checked and what we changed. Plus the brief to run one, and the personas.',
                                main, 'wrap document-wide')

    def brief_page(self):
        brief = (OUT / 'brief.txt').read_text(encoding='utf-8')
        main = '\n'.join([
            '    <p class="kicker">Runs · for the person who starts the agent</p>',
            '    <h1>The brief for <span class="g">browser agents.</span></h1>',
            '    <p class="lead">Paste this into an agent that can drive a real browser, signed in to Claude, such as Claude in Chrome. It plays one invented person from <a href="/feedback/runs/personas/">the personas</a>, tries every example in real Claude, captures each step the same way, and sends back a record this site turns into a replay, like <a href="/feedback/runs/C1/">run C1</a>.</p>',
            '    <h2>What it asks for, that C1 did not have</h2>',
            '    <ul class="plist">',
            '      <li><strong>A named persona</strong>, from a page, instead of one the agent makes up; so runs can be compared, and a persona run twice shows what a release changed.</li>',
            '      <li><strong>What it expects before each step, and what it thinks after</strong>, so a surprise shows as the gap between the two.</li>',
            '      <li><strong>The assistant\'s text, copied exactly</strong>, beside the line the page showed, with whether they match.</li>',
            '      <li><strong>Screenshots taken one way</strong>: one a step, numbered, the whole answer visible, nothing of the account.</li>',
            '      <li><strong>The record as data</strong>, run.json, in the shape the replay reads; and a summary sent with Encrypt and send.</li>',
            '    </ul>',
            '    <h2>The brief</h2>',
            '    <div class="snippet prompt"><pre id="agent-brief"><code>' + esc(brief) + '</code></pre><button type="button" class="copy" data-copy="agent-brief">Copy</button></div>',
            '    <p>As a file: <a href="/feedback/runs/brief.txt">brief.txt</a>. To ask for one persona, add a line before it: <code>Play the persona with id marcus.</code></p>',
            f'    <p>What comes back goes to the person who started the agent, and its summary to us with Encrypt and send. Questions about running one: <a href="mailto:{AGENT_ADDRESS}">{AGENT_ADDRESS}</a>.</p>'])
        return self.pages.shell('The brief for browser agents: run an invented user on customers.riskmandate.ai in real Claude',
                                'The instructions to give a browser agent, such as Claude in Chrome, to play one invented user on customers.riskmandate.ai: who to be, the rules, what to capture at every step, the ten questions, and the run record to send back, which the site turns into a replay.',
                                main, 'wrap policy')

    def personas_page(self):
        cards = []
        for p in self.personas['personas']:
            runs = ', '.join(f'<a href="/feedback/runs/{r}/">{r}</a>' for r in p['runs']) or 'not yet'
            lis  = lambda xs: ''.join(f'<li>{esc(x)}</li>' for x in xs)
            cards.append(f'<section class="persona" id="{p["id"]}"><h2>{esc(p["name"])} <code>{p["id"]}</code></h2><p>{esc(p["who"])}</p>'
                         f'<dl class="meta"><dt>Uses</dt><dd>{esc(p["assistant"])}</dd><dt>Arrives</dt><dd>{esc(p["arrives"])}</dd><dt>Asks</dt><dd>{esc(p["question"])}</dd>'
                         f'<dt>Knows</dt><dd><ul>{lis(p["knows"])}</ul></dd><dt>Does not know</dt><dd><ul>{lis(p["does_not_know"])}</ul></dd><dt>Leaves if</dt><dd><ul>{lis(p["leaves_if"])}</ul></dd>'
                         f'<dt>Pushes</dt><dd>{esc(p["pushes"])}</dd><dt>Runs</dt><dd>{runs}</dd></dl></section>')
        main = '\n'.join([
            '    <p class="kicker">Runs · invented, every one</p>',
            '    <h1>The personas a browser agent may play</h1>',
            '    <p class="lead">Each is a situation and a question, not a real person. An agent reads them from <a href="/feedback/runs/personas.json">personas.json</a>, plays the one it is given, and records which. Five are study S1\'s, adapted for a real browser and Claude; Priya was made up by the agent of run C1.</p>',
            *cards])
        return self.pages.shell('Personas: the invented users a browser agent may play on customers.riskmandate.ai',
                                'The invented users a browser agent may play on customers.riskmandate.ai: who they are, what they ask, what they do not know, what makes them leave, how they push, and which runs they have been in.',
                                main, 'wrap policy')

    # ── run ────────────────────────────────────────────────────────────────────

    def put(self, target, text, changed, page=True):
        if page:
            text = self.pages.keep_chrome(target, text)
        if self.pages.write_if_changed(target, text, self.check):
            changed.append(target.relative_to(ROOT).as_posix())

    def run(self):
        changed = []
        wanted  = {OUT / 'index.html', OUT / 'brief' / 'index.html', OUT / 'personas' / 'index.html'} | {OUT / r / 'index.html' for r in RUNS} | {OUT / r / 'storyboard' / 'index.html' for r in RUNS}
        for stale in OUT.rglob('index.html'):
            if stale not in wanted:
                raise SystemExit(f'{stale.relative_to(ROOT)}: nothing in data/feedback/runs/ makes this page')
        self.put(OUT / 'index.html', self.index_page(), changed)
        self.put(OUT / 'brief' / 'index.html', self.brief_page(), changed)
        self.put(OUT / 'personas' / 'index.html', self.personas_page(), changed)
        self.put(OUT / 'personas.json', (DATA / 'personas.json').read_text(encoding='utf-8'), changed, page=False)
        for rid in RUNS:
            self.put(OUT / rid / 'index.html', self.article(rid), changed)
            self.put(OUT / rid / 'storyboard' / 'index.html', self.storyboard_page(rid), changed)
            self.put(OUT / rid / 'run.json', (DATA / rid / 'run.json').read_text(encoding='utf-8'), changed, page=False)
            self.put(OUT / rid / 'report.md', re.sub(r'\]\(screenshots/(\d+)-[^)]*\.jpg\)', lambda m: f'](/assets/feedback/{rid}/{m.group(1)}.webp)', (DATA / rid / 'report.md').read_text(encoding='utf-8')), changed, page=False)
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Runs(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  runs {verb}: {name}')
    if check and changed:
        print(f'gen_runs --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_runs.py')
        sys.exit(1)
    print(f'gen_runs: {len(changed)} file(s) {verb}')
