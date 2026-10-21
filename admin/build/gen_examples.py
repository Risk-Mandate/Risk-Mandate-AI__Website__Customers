# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Examples
# Writes everything under examples/ from data/examples.json: a page per example
# (the session in a chat frame with play, pause and step controls, the three
# acts drawn, the prompts to try it with, what to look for, and the questions
# that ask whether it worked), the index, and the tabs wherever a page carries
# a <!-- rm-customers:examples-tabs:start --> block (the home page, start here).
# Everything runs in Claude or ChatGPT in the browser: nothing is installed.
# `--check` fails on drift.
# Usage: python3 admin/build/gen_examples.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import re
import sys

from chrome import ROOT, METER, AGENT_ADDRESS
from pages  import Site__Pages


DATA   = ROOT / 'data' / 'examples.json'
OUT    = ROOT / 'examples'
KINDS  = ('act', 'new', 'user', 'assistant', 'tool')
PRICE  = {k['kind']: k['price'] for k in METER['kinds']}
esc    = html.escape


class Gen__Examples:

    def __init__(self, check=False):
        self.check    = check
        self.pages    = Site__Pages()
        self.data     = json.loads(DATA.read_text(encoding='utf-8'))
        self.examples = self.data['examples']
        self.validate()

    def validate(self):
        problems = []
        seen     = set()
        for ex in self.examples:
            slug = ex['slug']
            if slug in seen or not re.fullmatch(r'[a-z0-9-]+', slug):
                problems.append(f'{slug}: a slug is unique and lower-case')
            seen.add(slug)
            if not re.fullmatch(r'\d+\.\d+\.\d+', ex['version']) or ex['versions'][-1][0] != ex['version']:
                problems.append(f'{slug}: version {ex["version"]} must be X.Y.Z and the last entry of its versions')
            for kind, text in ex['transcript']:
                if kind not in KINDS:
                    problems.append(f'{slug}: transcript kind "{kind}" is not one of {KINDS}')
                if '{setup}' in text and not ex['setup']:
                    problems.append(f'{slug}: the transcript uses {{setup}} and there is none')
            acts = [t for k, t in ex['transcript'] if k == 'act']
            if len(acts) not in (3, 4) or not all(a.startswith(f'{n} · ') for n, a in zip((1, 2, 3, 4), acts)):
                problems.append(f'{slug}: three acts, numbered 1, 2 and 3, and an optional act 4')
            if ex['ask'] not in ''.join(self.fill(ex, t) for k, t in ex['transcript'] if k == 'user'):
                problems.append(f'{slug}: the ask is never asked in the transcript')
        if problems:
            raise SystemExit('data/examples.json is invalid:\n  ' + '\n  '.join(problems))

    def by_slug(self, slug):
        found = next((ex for ex in self.examples if ex['slug'] == slug), None)
        if found is None:
            raise SystemExit(f'example block names unknown example "{slug}"')
        return found

    def fill(self, ex, text):
        return text.replace('{line}', ex['line']).replace('{setup}', ex['setup'] or '')

    def money(self, pence):
        return 'free' if pence == 0 else f'{pence}p' if pence < 100 else f'£{pence / 100:.2f}'

    # ── pieces ─────────────────────────────────────────────────────────────────

    def player(self, ex, prefix=''):                                              # the session in a chat frame; assets/demo.js adds the controls and plays it
        items = []
        for kind, text in ex['transcript']:
            body  = self.fill(ex, text)
            extra = ' k-line' if kind == 'user' and ex['line'] in body else ''
            items.append(f'<li class="k-{kind}{extra}" data-kind="{kind}">{esc(body)}</li>')
        return '\n'.join([
            f'      <figure class="demo chat-frame look-claude" data-demo="{prefix}{ex["slug"]}" data-example="{ex["slug"]}">',
            '        <div class="chat-window">',
            f'          <div class="chat-top"><span class="chat-title">{esc(ex["tab"])}</span>'
            '<span class="chat-looks" role="group" aria-label="Look"><button type="button" data-look="claude" aria-pressed="true">Claude</button><button type="button" data-look="chatgpt" aria-pressed="false">ChatGPT</button></span></div>',
            f'          <ol class="demo-lines chat-lines verbatim">{"".join(items)}</ol>',
            '          <div class="chat-input" aria-hidden="true"><span class="chat-typed"></span><span class="chat-ph ph-claude">Reply to Claude…</span><span class="chat-ph ph-chatgpt">Ask anything</span><span class="chat-send"></span></div>',
            '        </div>',
            '        <figcaption>An illustration of what to expect, written by us, not a recording; the look is an approximation. Your assistant may answer differently: try it, and tell us below.</figcaption>',
            '      </figure>'])

    def acts_strip(self):                                                          # the three acts, drawn: the same for every example
        cards = ''.join(f'<li><span class="act-n">{a["n"]}</span><b>{esc(a["short"])}</b><span>{esc(a["what"])}</span></li>' for a in self.data['acts'])
        return f'<ol class="acts-strip" aria-label="Every example, in three acts">{cards}</ol>'

    def snippet(self, ident, text):
        return (f'<div class="snippet"><pre id="{ident}"><code>{esc(text)}</code></pre>'
                f'<button type="button" class="copy" data-copy="{ident}">Copy</button></div>')

    def open_links(self):
        o = self.data['open']
        return ('<p class="open-links">' + ' '.join(f'<a class="btn btn-ghost-dark" href="{o[k]["href"]}" target="_blank" rel="noopener">{esc(o[k]["label"])} in a new tab &#8599;</a>' for k in ('claude', 'chatgpt')) + '</p>'
                '<p class="open-note">If your browser opens a window instead, it may be behind this one.</p>')

    def user_lines(self, ex, act):                                                 # what the person types in one act, filled in
        t, at, out = ex['transcript'], 0, []
        for kind, text in t:
            if kind == 'act':
                at += 1
            elif at == act and kind == 'user':
                out.append(self.fill(ex, text))
        return out

    def try_box(self, ex, prefix=''):                                              # every act's messages, from the transcript, each in a box to copy (run C1: act 3 was ambiguous)
        sid   = f'{prefix}{ex["slug"]}'
        box   = lambda name, n, text: self.snippet(f'{name}-{n}-{sid}', text)
        one   = self.user_lines(ex, 1)
        two   = [x for x in self.user_lines(ex, 2) if x != ex['line']]
        three = self.user_lines(ex, 3)
        four  = self.user_lines(ex, 4)
        steps = [f'<li><b>Ask.</b> ' + ('Set the scene, then ask, and watch it do it:' if len(one) > 1 else 'Watch it do it.') + ''.join(box('a1', i, x) for i, x in enumerate(one)) + '</li>',
                 f'<li><b>Paste the line, the behaviour policy,</b> then ' + ('ask:' if two else 'ask again.') + box('line', 0, ex['line']) + ''.join(box('a2', i, x) for i, x in enumerate(two)) + '</li>',
                 f'<li><b>Start a new chat</b> and paste this, all of it, as the first message:' + box('a3', 0, three[0]) + (' Then:' + ''.join(box('a3', i + 1, x) for i, x in enumerate(three[1:])) if len(three) > 1 else '') + '</li>']
        if four:
            steps.append(f'<li><b>Now try to talk it out of the line:</b>' + ''.join(box('a4', i, x) for i, x in enumerate(four)) + '</li>')
        return '\n'.join(['        <div class="try-box">',
                          '          <h3>Try it yourself</h3>',
                          f'          {self.open_links()}',
                          f'          <ol class="try-steps">{"".join(steps)}</ol>',
                          '        </div>'])

    def quiz(self, ex, prefix=''):                                                  # the questions under an example; assets/examples.js turns the answers into an email the reader sends
        sid  = f'{prefix}{ex["slug"]}'
        qs   = (('got',      'Did you get it?',                            (('yes', 'Yes'), ('partly', 'Partly'), ('no', 'No'))),
                ('learned',  'Did you learn something new?',               (('yes', 'Yes'), ('a-little', 'A little'), ('no', 'No'))),
                ('surprised','Were you surprised?',                         (('yes', 'Yes'), ('a-little', 'A little'), ('no', 'No'))),
                ('worked',   'When you tried it, did it go as shown?',      (('yes', 'Yes'), ('differently', 'Differently'), ('no', 'No'), ('not-tried', 'Not tried yet'))),
                ('good',     'How good was this example?',                  (('1', '1 · weak'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5 · excellent'))))
        sets = []
        for key, label, options in qs:
            opts = ''.join(f'<label><input type="radio" name="{sid}-{key}" value="{v}"><span>{esc(t)}</span></label>' for v, t in options)
            sets.append(f'<fieldset data-q="{key}"><legend>{esc(label)}</legend><div class="chips">{opts}</div></fieldset>')
        subject = f'Example {ex["slug"]} v{ex["version"]}'
        return '\n'.join([
            f'        <section class="quiz" data-quiz="{ex["slug"]}" data-example-version="{ex["version"]}" data-to="{AGENT_ADDRESS}" aria-labelledby="quiz-{sid}">',
            f'          <h3 id="quiz-{sid}">Tell us about this example</h3>',
            '          <p class="dim">Five taps and a line, if you have one. The point is for you to be surprised, so tell us if you were not. Your answers stay in this browser until you send them; when you do, they are encrypted here, before they leave, and only RiskMandate can read them.</p>',
            *[f'          {s}' for s in sets],
            f'          <label class="quiz-free"><span>Anything else: what it did when you tried it, what was unclear?</span><textarea name="{sid}-note" rows="3"></textarea></label>',
            '          <details class="send-preview"><summary>Exactly what will be sent</summary><pre><code></code></pre></details>',
            f'          <p class="quiz-actions"><button type="button" class="btn btn-green send-encrypted">Encrypt and send to the agent</button>'
            '<button type="button" class="btn quiz-copy">Copy my answers</button><a href="/feedback/how-sending-works/">How this works</a></p>',
            f'          <p class="quiz-after"><span class="quiz-status" aria-live="polite"></span> <a class="quiz-mail" hidden href="mailto:{AGENT_ADDRESS}?subject={esc(subject.replace(" ", "%20"))}">Send it by email instead</a></p>',
            '        </section>'])

    def panel(self, ex, prefix, selected, tab=True):
        sid = f'{prefix}{ex["slug"]}'
        return '\n'.join([
            f'    <section class="ex-panel" id="ex-{sid}"' + (f' role="tabpanel" aria-labelledby="tab-{sid}"' if tab else '') + ('' if selected else ' data-hidden') + '>',
            f'      <p class="kicker">{esc(ex["level"])} · {ex["minutes"]} minutes · version {ex["version"]}</p>',
            f'      <h3 class="ex-title">{esc(ex["title"])}</h3>',
            f'      <p class="ex-teaches">{esc(ex["teaches"])}</p>',
            '      <div class="ex-grid">',
            self.player(ex, prefix),
            self.try_box(ex, prefix),
            '      </div>',
            f'      <p class="look-for"><strong>Look for:</strong> {esc(ex["look_for"])} <a href="/examples/{ex["slug"]}/">The whole example &#8594;</a></p>',
            self.quiz(ex, prefix),
            '    </section>'])

    def tabs(self, prefix='home-'):
        tabs = ''.join(f'<a class="ex-tab" role="tab" id="tab-{prefix}{ex["slug"]}" href="#ex-{prefix}{ex["slug"]}" aria-controls="ex-{prefix}{ex["slug"]}" aria-selected="{"true" if i == 0 else "false"}">'
                       f'<span class="n">{i + 1}</span>{esc(ex["tab"])}</a>' for i, ex in enumerate(self.examples))
        return '\n'.join([f'  <div class="ex-tabs" data-tabs>',
                          f'    <nav class="ex-tablist" role="tablist" aria-label="Examples">{tabs}</nav>',
                          *[self.panel(ex, prefix, i == 0) for i, ex in enumerate(self.examples)],
                          '  </div>'])

    # ── pages ──────────────────────────────────────────────────────────────────

    def example_page(self, ex, n):
        price    = self.money(PRICE['example'])
        versions = ''.join(f'<tr><td>{esc(v)}</td><td>{esc(d)}</td><td>{esc(w)}</td></tr>' for v, d, w in reversed(ex['versions']))
        nxt      = self.examples[n + 1] if n + 1 < len(self.examples) else None
        main = '\n'.join([
            f'    <p class="kicker">Example {n + 1} of {len(self.examples)} · {esc(ex["level"])} · {ex["minutes"]} minutes · version {ex["version"]} · this page costs {price} read to the end</p>',
            f'    <h1>{esc(ex["title"])}</h1>',
            f'    <p class="lead">{esc(ex["teaches"])}</p>',
            f'    <p><strong>You need:</strong> {esc(ex["needs"])}</p>',
            f'    {self.acts_strip()}',
            '    <div class="ex-grid">',
            self.player(ex),
            self.try_box(ex),
            '    </div>',
            '    <h2>What to look for</h2>',
            f'    <p>{esc(ex["look_for"])}</p>',
            '    <h2>Keep it</h2>',
            '    <p>The line lasts as long as the chat. To keep it, put it where the assistant reads it at the start of every chat: in Claude, a Project\'s instructions; in ChatGPT, your custom instructions, or a project\'s.</p>',
            '    <h2>What a line is, and what it is not</h2>',
            '    <p>The assistant follows the line because it chooses to. That is an <em>expectation</em>, the first of four barriers, and for most of what you will try here it is enough to change what happens. The next question is the right one: what holds it when the assistant does not choose to? <a href="/what-is-an-abp/">What an Agent Behaviour Policy is</a> takes it from there.</p>',
            self.quiz(ex),
            f'    <h2>Versions of this example</h2>',
            f'    <table class="versions"><thead><tr><th>Version</th><th>Date</th><th>What changed</th></tr></thead><tbody>{versions}</tbody></table>',
            '    <p>' + (f'Next: <a href="/examples/{nxt["slug"]}/">{esc(nxt["title"])}</a>. ' if nxt else '') + 'All of them: <a href="/examples/">the examples</a>.</p>'])
        return self.pages.shell(f'{ex["title"]}: an example',
                                f'{ex["teaches"]} Try it in Claude or ChatGPT in your browser, in {ex["minutes"]} minutes: ask, paste one line, ask again, then a new chat with the line first.',
                                main, 'wrap policy')

    def index_page(self):
        cards = ''.join(f'<a class="card" href="/examples/{ex["slug"]}/"><span class="n">{i + 1} · {esc(ex["level"])} · {ex["minutes"]} min</span><b>{esc(ex["title"])}</b><p>{esc(ex["teaches"])}</p></a>'
                        for i, ex in enumerate(self.examples))
        nxt   = ''.join(f'<li><strong>{esc(x["title"])}.</strong> {esc(x["what"])}</li>' for x in self.data['next'])
        main = '\n'.join([
            '    <h1>Six examples, <span class="g">simplest first.</span></h1>',
            '    <p class="lead">Each one runs in Claude or ChatGPT in your browser, with nothing to install. Each goes the same way: ask for something and watch the assistant do it; paste one line and ask again; then a new chat with the line first. Keep a secret has a fourth act: try to talk it out of the line.</p>',
            '    <p>Every example has been tried in real Claude by an agent playing an invented user: <a href="/feedback/runs/C1/">run C1, replayed</a>, with what the page said beside what Claude wrote.</p>',
            f'    {self.acts_strip()}',
            f'    {self.open_links()}',
            f'    <div class="cards">{cards}</div>',
            '    <h2>Next, from what we have mapped</h2>',
            '    <p>Things your assistant can do that most people do not know about. Each becomes an example once we have checked what Claude and ChatGPT do today.</p>',
            f'    <ul class="plist">{nxt}</ul>',
            '    <p>Using Claude Code? Its behaviour policies install a script on your machine, so they are for later: <a href="/policies/">the behaviour policies, for Claude Code too</a>.</p>'])
        return self.pages.shell('Examples: six behaviour policies to try in Claude or ChatGPT, simplest first',
                                'Six examples of an Agent Behaviour Policy to try in Claude or ChatGPT in your browser, from hello world to refunds: ask, paste one line, ask again, and a new chat with the line first. Nothing to install.',
                                main, 'wrap policy')

    # ── run ────────────────────────────────────────────────────────────────────

    def put(self, target, text, changed, page=True):
        if page:
            text = self.pages.keep_chrome(target, text)
        if self.pages.write_if_changed(target, text, self.check):
            changed.append(target.relative_to(ROOT).as_posix())

    def run(self):
        changed = []
        wanted  = {OUT / ex['slug'] / 'index.html' for ex in self.examples} | {OUT / 'index.html'}
        for stale in OUT.glob('*/index.html'):
            if stale not in wanted:
                raise SystemExit(f'{stale.relative_to(ROOT)}: no example in data/examples.json; remove the folder or add the example')
        for n, ex in enumerate(self.examples):
            self.put(OUT / ex['slug'] / 'index.html', self.example_page(ex, n), changed)
        self.put(OUT / 'index.html', self.index_page(), changed)
        index = {'_comment': 'The examples, for the account page (assets/account.js): generated from data/examples.json by admin/build/gen_examples.py.',
                 'examples': [{'slug': ex['slug'], 'title': ex['title'], 'tab': ex['tab'], 'version': ex['version'], 'steps': len(ex['transcript'])} for ex in self.examples]}
        self.put(OUT / 'index.json', json.dumps(index, indent=2, ensure_ascii=False) + '\n', changed, page=False)
        for path in self.pages.html_files():
            text = path.read_text(encoding='utf-8')
            if self.pages.has_block(text, 'examples-tabs') or self.pages.has_block(text, 'acts-strip') or self.pages.has_block(text, 'example'):
                text, _ = self.pages.replace_blocks(text, 'example', lambda attrs: self.panel(self.by_slug(attrs['slug']), attrs.get('prefix', 'one-'), True, tab=False))
                text, _ = self.pages.replace_blocks(text, 'examples-tabs', lambda attrs: self.tabs(attrs.get('prefix', 'home-')))
                text, _ = self.pages.replace_block(text, 'acts-strip', '    ' + self.acts_strip())
                self.put(path, text, changed, page=False)
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Examples(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  examples {verb}: {name}')
    if check and changed:
        print(f'gen_examples --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_examples.py')
        sys.exit(1)
    print(f'gen_examples: {len(changed)} file(s) {verb}')
