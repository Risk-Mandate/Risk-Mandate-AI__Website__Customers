# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Feedback
# Writes everything under feedback/ from data/feedback/: the page where a
# customer gives feedback (with the two prompts in feedback/prompts/), the
# consolidated reviews document (every review verbatim, our reading point by
# point with screenshots, every synthetic finding with its check, and the one
# register of proposals, each with a decision and a reason), a page per review,
# and the synthetic study with a page per run. `--check` fails on drift.
# A reviewer's words and an invented user's words are kept as given, marked
# class="verbatim", and the house-word check leaves them alone.
# Usage: python3 admin/build/gen_feedback.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import re
import struct
import sys

from chrome import ROOT, AGENT_ADDRESS, FEEDBACK_LANE
from pages  import Site__Pages


DATA       = ROOT / 'data' / 'feedback'
OUT        = ROOT / 'feedback'
SHOTS      = ROOT / 'assets' / 'feedback'
PROMPTS    = OUT / 'prompts'
STANCES    = {'agree': 'agreed', 'agree-in-part': 'agreed in part', 'disagree': 'we disagree', 'question': 'a question', 'asked': 'asked of us'}
DECISIONS  = ('done', 'reversed', 'accepted', 'proposed', 'question', 'declined')
VERDICTS   = ('confirmed', 'partly', 'artefact', 'not-confirmed')
esc        = html.escape


def webp_size(path):                                                              # (width, height) from a WebP header, so the build needs nothing outside the standard library
    data = path.read_bytes()[:30]
    if data[:4] != b'RIFF' or data[8:12] != b'WEBP':
        raise SystemExit(f'{path.relative_to(ROOT)}: not a WebP file')
    kind = data[12:16]
    if kind == b'VP8 ':
        w, h = struct.unpack('<HH', data[26:30])
        return w & 0x3fff, h & 0x3fff
    if kind == b'VP8L':
        b = int.from_bytes(data[21:25], 'little')
        return (b & 0x3fff) + 1, ((b >> 14) & 0x3fff) + 1
    if kind == b'VP8X':
        return int.from_bytes(data[24:27], 'little') + 1, int.from_bytes(data[27:30], 'little') + 1
    raise SystemExit(f'{path.relative_to(ROOT)}: unknown WebP kind {kind!r}')


def squash(text):
    return re.sub(r'\s+', ' ', text).strip()


class Gen__Feedback:

    def __init__(self, check=False):
        self.check     = check
        self.pages     = Site__Pages()
        self.register  = json.loads((DATA / 'proposals.json').read_text(encoding='utf-8'))
        self.proposals = {p['id']: p for p in self.register['proposals']}
        self.reviews   = [json.loads(p.read_text(encoding='utf-8')) for p in sorted((DATA / 'reviews').glob('*.json'))]
        for review in self.reviews:
            review['memo_text'] = (ROOT / review['memo']).read_text(encoding='utf-8')
        study          = DATA / 'synthetic'
        self.personas  = json.loads((study / 'personas.json').read_text(encoding='utf-8'))
        self.journeys  = {j['persona']: j for j in json.loads((study / 'journeys.json').read_text(encoding='utf-8'))['journeys']}
        self.protocol  = json.loads((study / 'protocol.json').read_text(encoding='utf-8'))
        self.checks    = json.loads((study / 'checks.json').read_text(encoding='utf-8'))
        self.study     = self.personas['study']
        self.runs      = {p['id']: json.loads((study / 'runs' / p['id'] / 'run.json').read_text(encoding='utf-8')) for p in self.personas['personas']}
        self.captures  = {p['id']: json.loads((study / 'runs' / p['id'] / '_capture.json').read_text(encoding='utf-8')) for p in self.personas['personas']}
        self.questions = {q['id']: q for r in self.reviews for q in r.get('questions', [])} | {q['id']: q for q in self.register.get('questions', [])}
        self.validate()

    # ── validation ─────────────────────────────────────────────────────────────

    def validate(self):
        problems = []
        for p in self.register['proposals']:
            if p['decision'] not in DECISIONS:
                problems.append(f'{p["id"]}: decision must be one of {DECISIONS}')
            if p['decision'] in ('done', 'reversed') and not p.get('version'):
                problems.append(f'{p["id"]}: a {p["decision"]} proposal names its version')
            for version, decision in p.get('history', []):
                if decision not in DECISIONS:
                    problems.append(f'{p["id"]}: history decision "{decision}" is not one of {DECISIONS}')
            if p.get('history') and p['history'][-1][1] != p['decision']:
                problems.append(f'{p["id"]}: the last entry of its history is its decision')
            if not p.get('reason'):
                problems.append(f'{p["id"]}: every decision has a reason')
            if not self.sources_of(p['id']):
                problems.append(f'{p["id"]}: no review point or finding leads to it')
        for review in self.reviews:
            memo = squash(review['memo_text'])
            for point in review['points']:
                if squash(point['quote']) not in memo:
                    problems.append(f'{point["id"]}: the quote is not in {review["memo"]}, word for word')
                if point['stance'] not in STANCES:
                    problems.append(f'{point["id"]}: stance must be one of {tuple(STANCES)}')
                for ident in point['proposals']:
                    if ident not in self.proposals:
                        problems.append(f'{point["id"]}: no proposal {ident}')
                for ident in point.get('questions', []):
                    if ident not in self.questions:
                        problems.append(f'{point["id"]}: no question {ident}')
                for shot in point['shots']:
                    if shot not in review['screens']:
                        problems.append(f'{point["id"]}: no screen {shot}')
            for shot in review['screens']:
                if not (SHOTS / review['id'] / f'{shot}.webp').exists():
                    problems.append(f'{review["id"]}: assets/feedback/{review["id"]}/{shot}.webp is missing')
        for who, run in self.runs.items():
            if who not in self.journeys:
                problems.append(f'{who}: no expected journey, written before the run')
            found = sorted(c['finding'] for c in self.checks['checks'] if c['run'] == who)
            if found != list(range(len(run['findings']))):
                problems.append(f'{who}: every finding is checked once (checked {found} of {len(run["findings"])})')
            for step in run['steps']:
                if not (SHOTS / self.study / who / f'{step["n"]:02d}.webp').exists():
                    problems.append(f'{who}: step {step["n"]} has no screenshot')
        for c in self.checks['checks']:
            if c['verdict'] not in VERDICTS:
                problems.append(f'{c["run"]} finding {c["finding"]}: verdict must be one of {VERDICTS}')
            for ident in c['proposals']:
                if ident not in self.proposals:
                    problems.append(f'{c["run"]} finding {c["finding"]}: no proposal {ident}')
        if problems:
            raise SystemExit('data/feedback/ is invalid:\n  ' + '\n  '.join(problems))

    # ── links between reviews, findings and proposals ──────────────────────────

    def point_anchor(self, ident):
        return ident.lower().replace('.', '-')

    def finding_anchor(self, who, index):
        return f'{self.study.lower()}-{who}-{index + 1}'

    def sources_of(self, proposal_id):                                             # [(label, href)] for every point and finding that leads to a proposal
        out = []
        for review in self.reviews:
            for point in review['points']:
                if proposal_id in point['proposals']:
                    out.append((point['id'], f'/feedback/reviews/#{self.point_anchor(point["id"])}'))
        for c in self.checks['checks']:
            if proposal_id in c['proposals']:
                name = self.persona(c['run'])['name'].split()[0]
                out.append((f'{self.study} {name} {c["finding"] + 1}', f'/feedback/reviews/#{self.finding_anchor(c["run"], c["finding"])}'))
        return out

    def persona(self, who):
        return next(p for p in self.personas['personas'] if p['id'] == who)

    def source_label(self, url):                                                   # 'Claude Code docs: hooks', from the page a fact was checked against
        name = url.rstrip('/').rsplit('/', 1)[-1]
        return f'Claude Code docs: {name}' if 'code.claude.com' in url else name

    def proposal_links(self, idents):
        return ', '.join(f'<a href="/feedback/reviews/#{i.lower()}">{i}</a>' for i in idents) or 'none'

    def question_links(self, idents):
        return ', '.join(f'<a href="/feedback/reviews/#{i.lower()}">{i}</a>' for i in idents)

    # ── pieces ─────────────────────────────────────────────────────────────────

    def figure(self, folder, name, caption, alt, ident=None):
        path  = SHOTS / folder / f'{name}.webp'
        w, h  = webp_size(path)
        tall  = ' tall' if h > w * 1.4 else ''
        href  = f'/assets/feedback/{folder}/{name}.webp'
        return (f'<figure class="shot{tall}"' + (f' id="{ident}"' if ident else '') + f'><a href="{href}">'
                f'<img src="{href}" width="{w}" height="{h}" loading="lazy" alt="{esc(alt, quote=True)}"></a>'
                f'<figcaption>{caption}</figcaption></figure>')

    def snippet(self, ident, text, label='Copy'):
        return (f'<div class="snippet prompt"><pre id="{ident}"><code>{esc(text)}</code></pre>'
                f'<button type="button" class="copy" data-copy="{ident}">{label}</button></div>')

    def decision_chip(self, p):
        label = f'{p["decision"]} v{p["version"]}' if p['decision'] in ('done', 'reversed') else p['decision']
        chip  = f'<span class="decision decision-{p["decision"]}">{esc(label)}</span>'
        if len(p.get('history', [])) > 1:                                           # a decision that changed keeps its history
            chip += '<span class="history">' + ' &#8594; '.join(f'{esc(d)} at v{esc(v)}' for v, d in p['history']) + '</span>'
        return chip

    def verdict_chip(self, verdict):
        return f'<span class="decision verdict-{verdict}">{esc(verdict)}</span>'

    def counts(self):
        out = []
        for d in DECISIONS:
            n = sum(1 for p in self.register['proposals'] if p['decision'] == d)
            if n:
                out.append(f'{n} {d}')
        return ', '.join(out)

    # ── the register ───────────────────────────────────────────────────────────

    def register_html(self, only=None):
        rows = []
        for p in self.register['proposals']:
            if only is not None and p['id'] not in only:
                continue
            sources = ', '.join(f'<a href="{href}">{esc(label)}</a>' for label, href in self.sources_of(p['id']))
            refs    = ''.join(f' <a class="src" href="{esc(s)}">{esc(self.source_label(s))}</a>' for s in p.get('sources', []))
            rows.append(f'      <tr id="{p["id"].lower()}"><td><b>{p["id"]}</b></td><td><b>{esc(p["title"])}</b><p>{esc(p["what"])}</p></td>'
                        f'<td>{self.decision_chip(p)}<p>{esc(p["reason"])}{refs}</p></td><td>{sources}</td></tr>')
        return '\n'.join(['    <table class="register" data-generated-from="data/feedback/proposals.json">',
                          '      <thead><tr><th>Id</th><th>The proposal</th><th>Decision, and why</th><th>From</th></tr></thead>',
                          '      <tbody>', *rows, '      </tbody>', '    </table>'])

    def questions_html(self):
        items = []
        for q in self.questions.values():
            answer = f' <span class="answered">Answered: {esc(q["answer"])}</span>' if q.get('answer') else ''
            items.append(f'      <li id="{q["id"].lower()}"><b>{q["id"]}, to {esc(q["to"])}.</b> {esc(q["ask"])}{answer}</li>')
        return '\n'.join(['    <ul class="plist">', *items, '    </ul>'])

    # ── a review written by a person ───────────────────────────────────────────

    def review_section(self, review, level='h2'):
        sub    = 'h3' if level == 'h2' else 'h2'
        memo   = ''.join(f'<p>{esc(para)}</p>' for para in review['memo_text'].strip().split('\n\n'))
        points = []
        for point in review['points']:
            figures = ''.join(self.figure(review['id'], s, f'{esc(review["screens"][s]["caption"])} <span class="where">{esc(review["screens"][s]["page"])} · {esc(review["screens"][s]["viewport"])} · v{esc(review["site_version"])}</span>',
                                          review['screens'][s]['caption']) for s in point['shots'])
            qs      = f' Open question: {self.question_links(point["questions"])}.' if point.get('questions') else ''
            sources = ''.join(f' <a class="src" href="{esc(s)}">{esc(self.source_label(s))}</a>' for s in point.get('sources', []))
            points.append(f'    <div class="point" id="{self.point_anchor(point["id"])}">'
                          f'<p class="point-head"><b>{point["id"]}</b> <span class="stance stance-{point["stance"]}">{STANCES[point["stance"]]}</span></p>'
                          f'<blockquote class="verbatim"><p>{esc(point["quote"])}</p></blockquote>'
                          f'<p>{esc(point["reading"])}{sources}</p>{figures}'
                          f'<p class="leads-to">Leads to: {self.proposal_links(point["proposals"])}.{qs}</p></div>')
        notes = ''.join(f'<li>{esc(n)}</li>' for n in review.get('notes', []))
        return '\n'.join([
            f'    <{level} id="{review["id"].lower()}">{review["id"]}: {esc(review["title"])}</{level}>',
            f'    <dl class="meta"><dt>Reviewer</dt><dd>{esc(review["reviewer"])}, {esc(review["role"])}</dd><dt>Given</dt><dd>{esc(review["given"])}</dd>'
            f'<dt>Reviewing</dt><dd>site v{esc(review["site_version"])}</dd><dt>As</dt><dd>{esc(review["medium"])}</dd><dt>Status</dt><dd>{esc(review["status"])}</dd></dl>',
            f'    <ul class="plist">{notes}</ul>' if notes else '',
            f'    <{sub}>The memo, verbatim</{sub}>',
            f'    <blockquote class="verbatim memo">{memo}</blockquote>',
            f'    <{sub}>Our reading, point by point</{sub}>',
            *points])

    # ── the synthetic study ────────────────────────────────────────────────────

    def check_of(self, who, index):
        return next(c for c in self.checks['checks'] if c['run'] == who and c['finding'] == index)

    def findings_by_cost(self):
        order = {c: i for i, c in enumerate(self.protocol['costs'])}
        out   = []
        for who, run in self.runs.items():
            for i, f in enumerate(run['findings']):
                out.append((order.get(f['costs'], len(order)), VERDICTS.index(self.check_of(who, i)['verdict']), who, i, f))
        return sorted(out, key=lambda t: (t[0], t[1], t[2], t[3]))

    def ratings_table(self):
        rows = []
        for p in self.personas['personas']:
            run = self.runs[p['id']]
            one = next((qa['a'] for qa in run['interview'] if qa['q'].startswith('One change')), '')
            rows.append(f'      <tr><td><a href="/feedback/synthetic/{p["id"]}/">{esc(p["name"])}</a><p>{esc(p["who"])}</p></td><td>{esc(p["device"]["kind"])}, {p["device"]["width"]}×{p["device"]["height"]}</td>'
                        f'<td>{esc(run["ended"])}, after {len(run["steps"])} screenshots</td><td><b>{run["rating"]}</b> of 5</td><td><q class="verbatim">{esc(one)}</q></td></tr>')
        return '\n'.join(['    <table class="study">', '      <thead><tr><th>Invented user</th><th>On</th><th>Ended</th><th>Rating</th><th>Their one change</th></tr></thead>',
                          '      <tbody>', *rows, '      </tbody>', '    </table>'])

    def findings_html(self, anchors=True):
        rows = []
        for _, _, who, i, f in self.findings_by_cost():
            c    = self.check_of(who, i)
            name = self.persona(who)['name']
            step = f'<a href="/feedback/synthetic/{who}/#step-{f["step"]}">step {f["step"]}</a>'
            ident = f' id="{self.finding_anchor(who, i)}"' if anchors else ''
            rows.append(f'      <tr{ident}><td>{esc(f["costs"])}</td><td><q class="verbatim">{esc(f["title"])}</q><p>{esc(name)}, {step}, <code>{esc(f["page"])}</code></p></td>'
                        f'<td>{self.verdict_chip(c["verdict"])}<p>{esc(c["note"])}</p></td><td>{self.proposal_links(c["proposals"])}</td></tr>')
        return '\n'.join(['    <table class="register findings">', '      <thead><tr><th>Costs</th><th>The finding, in their words</th><th>Our check</th><th>Leads to</th></tr></thead>',
                          '      <tbody>', *rows, '      </tbody>', '    </table>'])

    def tally(self):
        verdicts = [c['verdict'] for c in self.checks['checks']]
        return ', '.join(f'{verdicts.count(v)} {v}' for v in VERDICTS if verdicts.count(v))

    def study_summary(self):
        ratings = [str(self.runs[p['id']]['rating']) for p in self.personas['personas']]
        steps   = sum(len(r['steps']) for r in self.runs.values())
        return (f'{len(self.runs)} invented users took {steps} screenshots on site v{esc(self.personas["site_version"])}, gave it {", ".join(ratings[:-1])} and {ratings[-1]} out of 5, '
                f'and reported {len(self.checks["checks"])} findings. We checked each one: {self.tally()}.')

    def banner(self):
        return ('    <p class="banner-invented"><b>Invented, not user research.</b> Everybody in this study is invented, and their words were written by a model playing them. '
                'What they saw is real: each screenshot is what the browser showed at that step. They find what a page fails to say; they cannot tell us what a customer wants.</p>')

    # ── pages ──────────────────────────────────────────────────────────────────

    def give_page(self):
        voice     = (PROMPTS / 'voice-memo.txt').read_text(encoding='utf-8')
        interview = (PROMPTS / 'interview.txt').read_text(encoding='utf-8')
        last      = self.reviews[-1]
        main = '\n'.join([
            '    <p class="kicker">Feedback · free to read · a person reads every word</p>',
            '    <h1>Tell us what you think. <span class="g">A voice memo is best.</span></h1>',
            '    <p class="lead">What did you try, what stopped, what got in the way, and where did you have to guess? Criticism first: it is what we can use. Three ways, from one line to fifteen minutes.</p>',
            '    <ol class="steps">',
            f'      <li><b>Write it here, and encrypt and send it.</b><p>A line or a page. It is encrypted in this browser before it leaves, and only RiskMandate can read it. Add your name or an email only if you want a reply. <a href="/feedback/how-sending-works/">How this works</a>.</p>'
            f'<div class="send-box" data-to="{AGENT_ADDRESS}"><label class="quiz-free"><span>What happened, what got in the way, what you would change</span><textarea rows="5" name="message"></textarea></label>'
            '<label class="quiz-free"><span>Your name or email, if you want a reply (optional)</span><input type="text" name="who" autocomplete="off"></label>'
            '<details class="send-preview"><summary>Exactly what will be sent</summary><pre><code></code></pre></details>'
            '<p class="quiz-actions"><button type="button" class="btn btn-green send-encrypted">Encrypt and send to the agent</button><button type="button" class="btn quiz-copy">Copy it</button></p>'
            f'<p class="quiz-after"><span class="quiz-status" aria-live="polite"></span> <a class="quiz-mail" hidden href="mailto:{AGENT_ADDRESS}?subject=Feedback">Send it by email instead</a></p></div></li>',
            f'      <li><b>One line, by email.</b><p>What happened, in a line. <a href="mailto:{AGENT_ADDRESS}?subject=Feedback">Write to {AGENT_ADDRESS}</a>; a person reads it within a working day.</p></li>',
            '      <li><b>Record a voice memo, and give it to your Claude.</b><p>Talk for two to five minutes, on your phone, while it is fresh: walk through what you did and say what you thought. '
            'Transcribe it (your phone, Otter, or the Claude app can), then paste this prompt and the transcript into Claude, or ChatGPT. It turns the memo into a review without softening it, '
            'tells you which screenshots to attach, and asks before anything is published.</p>' + self.snippet('prompt-voice', voice) +
            '<p>The same prompt as a file: <a href="/feedback/prompts/voice-memo.txt">voice-memo.txt</a>.</p></li>',
            '      <li><b>Let Claude interview you.</b><p>Paste this into Claude and switch to voice. It asks one question at a time, about fifteen minutes, criticism first, and writes up what you said, '
            'kept apart from what it thinks you meant. You read it before you send it.</p>' + self.snippet('prompt-interview', interview) +
            '<p>As a file: <a href="/feedback/prompts/interview.txt">interview.txt</a>.</p></li>',
            '    </ol>',
            '    <h2>What happens to it</h2>',
            '    <ul class="plist">',
            '      <li><strong>It becomes a review,</strong> kept in your words, with our reading point by point and screenshots of what you were looking at.</li>',
            '      <li><strong>Every point leads to a proposal with a decision:</strong> done, proposed, a question, or declined. We do not do everything a reviewer asks, but every no has a reason, and you can see it.</li>',
            '      <li><strong>Nothing is published without your yes,</strong> under your name or anonymously, as you choose. No contact details are ever published.</li>',
            '    </ul>',
            f'    <p>Every review so far, and what we did: <a href="/feedback/reviews/">the reviews</a>. The latest is <a href="/feedback/reviews/{last["id"]}/">{last["id"]}, {esc(last["title"])}</a>. '
            f'We also run invented users through the site: <a href="/feedback/synthetic/">study {self.study}</a>.</p>'])
        return self.pages.shell('Tell us what you think: a line, a voice memo for your Claude, or a Claude interview',
                                'Give feedback on customers.riskmandate.ai: one line by email, a voice memo that your Claude turns into a review, or a fifteen-minute interview by Claude. Criticism first; every point gets a decision and a reason; nothing is published without your yes.',
                                main, 'wrap policy')

    def how_page(self):
        lane = FEEDBACK_LANE
        main = '\n'.join([
            '    <p class="kicker">Feedback · free to read</p>',
            '    <h1>How Encrypt and send works</h1>',
            '    <p class="lead">What you send is encrypted in your browser, before it leaves, to a key only RiskMandate holds. It goes to an encrypted vault, not to an inbox, and the host that stores it cannot read it.</p>',
            '    <h2>What happens when you press it</h2>',
            '    <ol class="steps">',
            '      <li><b>Your browser fetches the lane\'s address and key.</b><p>From <a href="/feedback/lane.json">/feedback/lane.json</a>: the vault, the lane, a token that can only add to it, and a public key that can only encrypt. The page checks the key against its fingerprint, <code>' + esc(lane['encrypt_to']) + '</code>, before it uses it.</p></li>',
            '      <li><b>It encrypts what you wrote, there and then.</b><p>A fresh AES-256-GCM key for the message, and that key wrapped with RSA-OAEP (SHA-256) to the public key: sgit\'s hybrid envelope, the one riskmandate.ai\'s contact form uses. The code is <a href="/assets/envelope.js">assets/envelope.js</a>, about seventy lines, and runs nowhere else.</p></li>',
            '      <li><b>It adds the sealed message to the lane.</b><p>The <code>' + esc(lane['lane']) + '</code> append lane of vault <code>' + esc(lane['vault']) + '</code>, on <code>' + esc(lane['endpoint'].replace('https://', '')) + '</code>, sgit.ai\'s vault host. The token lets anybody add to the lane and nobody read it.</p></li>',
            '      <li><b>Only the vault\'s key opens it.</b><p>That key is RiskMandate\'s and is not on this site or in its source. The site\'s agent drains the lane, files each message in the vault, and a person reads it.</p></li>',
            '    </ol>',
            '    <h2>What is sent, and what is not</h2>',
            '    <ul class="plist">',
            '      <li><strong>Sent:</strong> exactly the text under <em>Exactly what will be sent</em>, with the page you sent it from and the time. Your name or email only if you typed them.</li>',
            '      <li><strong>Not sent:</strong> your balance, your history, your other answers, anything else this browser keeps. <a href="/account/">Your account</a> lists all of that, at its foot, and it stays here.</li>',
            '      <li><strong>What the host sees:</strong> that a sealed message arrived, when, how big it is, and the network address it came from, as any server does. Not what it says.</li>',
            '      <li><strong>What your browser keeps:</strong> that you sent something, when, and whether it went, so your account can show it. Not the text.</li>',
            '    </ul>',
            '    <h2>For an agent</h2>',
            '    <p>An agent reviewing this site can send its findings the same way: build the envelope as <a href="/assets/envelope.js">assets/envelope.js</a> does, and POST <code>{"append_token": …, "payload": …}</code> to <code>' + esc(lane['endpoint']) + '/api/vault/append/write/' + esc(lane['vault']) + '</code>, with the token and key from <a href="/feedback/lane.json">lane.json</a>. Put <code>To: agent &lt;' + esc(lane['to']) + '&gt;</code> and a <code>Subject</code> in the message\'s first lines. <code>admin/feedback/lane.mjs send</code> in <a href="https://github.com/Risk-Mandate/Risk-Mandate-AI__Website__Customers">the source</a> does it in Node.</p>',
            '    <p>If anything fails, the page says why and offers the same text as an email to <a href="mailto:' + AGENT_ADDRESS + '">' + AGENT_ADDRESS + '</a>.</p>'])
        return self.pages.shell('How Encrypt and send works: encrypted in your browser, to a key only RiskMandate holds',
                                'What happens when you press Encrypt and send on customers.riskmandate.ai: the message is encrypted in your browser with sgit\'s hybrid envelope, appended to an encrypted vault\'s lane that anybody can add to and nobody can read, and opened only with RiskMandate\'s key.',
                                main, 'wrap policy')

    def reviews_page(self):
        people = [r for r in self.reviews]
        index  = ''.join(f'<li><a href="#{r["id"].lower()}">{r["id"]}</a>, {esc(r["reviewer"])}, {esc(r["given"])}, on site v{esc(r["site_version"])}: {esc(r["title"])} ({len(r["points"])} points; <a href="/feedback/reviews/{r["id"]}/">on its own page</a>)</li>' for r in people)
        main = '\n'.join([
            '    <p class="kicker">Feedback · every review · one document</p>',
            '    <h1>Every review, what we read in it, <span class="g">and what we will do.</span></h1>',
            '    <p class="lead">Each review is kept in the reviewer\'s own words. Our reading follows point by point, with screenshots of what the reviewer was looking at. Every point leads to a proposal, and every proposal has a decision and a reason: we do not do everything a reviewer asks, but every no is explained here.</p>',
            f'    <ul class="plist"><li><strong>Reviews by people:</strong> {len(people)}.</li><li><strong>Synthetic users:</strong> <a href="#{self.study.lower()}">study {self.study}</a>. {self.study_summary()}</li>'
            f'<li><strong>Proposals:</strong> {len(self.register["proposals"])}: {self.counts()}. <a href="#register">The register</a>.</li><li><strong>Questions:</strong> {sum(1 for q in self.questions.values() if not q.get("answer"))} waiting for an answer, {sum(1 for q in self.questions.values() if q.get("answer"))} answered. <a href="#questions">The questions</a>.</li></ul>',
            f'    <p>Give a review of your own: <a href="/feedback/">tell us what you think</a>.</p>',
            '    <h2 id="by-people">Reviews by people</h2>',
            f'    <ul class="plist">{index}</ul>',
            *[self.review_section(r, 'h2') for r in people],
            f'    <h2 id="{self.study.lower()}">Synthetic users: study {self.study}</h2>',
            self.banner(),
            f'    <p>{self.study_summary()} The study, with each run step by step: <a href="/feedback/synthetic/">study {self.study}</a>.</p>',
            self.ratings_table(),
            '    <h3>Every finding, by what it costs, with our check</h3>',
            self.findings_html(),
            '    <h2 id="register">The proposals, with a decision each</h2>',
            '    <p>From every review and every finding above. ' + '; '.join(f'<span class="decision decision-{d}">{d}</span> {esc(t)}' for d, t in self.register['decisions'].items()) + '.</p>',
            self.register_html(),
            '    <h2 id="questions">Questions we need answered</h2>',
            self.questions_html()])
        return self.pages.shell('Every review of customers.riskmandate.ai, what we read in it, and what we will do',
                                f'The consolidated reviews: each review verbatim, our reading point by point with screenshots, the synthetic study\'s findings with our checks, and one register of {len(self.register["proposals"])} proposals, each with a decision and a reason.',
                                main, 'wrap document-wide')

    def review_page(self, review):
        mine = {i for p in review['points'] for i in p['proposals']}
        main = '\n'.join([
            f'    <p class="kicker">Review {review["id"]} · {esc(review["reviewer"])} · site v{esc(review["site_version"])}</p>',
            f'    <h1>{esc(review["title"])}</h1>',
            f'    <p class="lead">{esc(review["reviewer"])}, {esc(review["given"])}. {esc(review["status"]).capitalize()}. The same review is in <a href="/feedback/reviews/#{review["id"].lower()}">the consolidated document</a>, beside every other.</p>',
            self.review_section(review, 'h2').replace(f'<h2 id="{review["id"].lower()}">', '<h2 id="review">', 1),
            '    <h2 id="proposals">What it led to</h2>',
            self.register_html(only=mine).replace(' id="p', ' id="here-p').replace(' id="d', ' id="here-d')])
        return self.pages.shell(f'Review {review["id"]}: {review["title"]}',
                                f'{review["reviewer"]}\'s review of customers.riskmandate.ai v{review["site_version"]}, {review["given"]}: the memo verbatim, our reading point by point with screenshots, and the proposals it led to.',
                                main, 'wrap document-wide')

    def study_page(self):
        rows = []
        for p in self.personas['personas']:
            j, run = self.journeys[p['id']], self.runs[p['id']]
            rows.append(f'      <tr><td><a href="/feedback/synthetic/{p["id"]}/">{esc(p["name"])}</a><p>{esc(p["who"])}</p></td><td>{esc(p["question"])}</td>'
                        f'<td>{esc(j["hypothesis"])}</td><td><q class="verbatim">{esc(run["ended_why"])}</q></td></tr>')
        loop   = ''.join(f'<li>{esc(x)}</li>' for x in self.protocol['loop'])
        rules  = ''.join(f'<li>{esc(x)}</li>' for x in self.protocol['rules'])
        qs     = ''.join(f'<li>{esc(x)}</li>' for x in self.protocol['interview'])
        adapt  = ''.join(f'<li>{esc(x)}</li>' for x in self.protocol['adapted'] + self.checks['helper_changes'])
        main = '\n'.join([
            f'    <p class="kicker">Feedback · synthetic users · study {self.study} · site v{esc(self.personas["site_version"])}</p>',
            f'    <h1>Five people who do not exist, <span class="g">on the site as it was.</span></h1>',
            self.banner(),
            f'    <p class="lead">{self.study_summary()}</p>',
            f'    <p>Why these five: {esc(self.personas["why_these"])}</p>',
            '    <h2>Who, what we expected, and what happened</h2>',
            '    <p>Each expected journey was written before the run, so a run is compared with a hypothesis instead of being explained afterwards.</p>',
            '    <table class="study"><thead><tr><th>Invented user</th><th>Arrived asking</th><th>We expected</th><th>What happened, in their words</th></tr></thead><tbody>', *rows, '    </tbody></table>',
            '    <h2>Ratings, and the one change each asked for</h2>',
            self.ratings_table(),
            '    <h2>Every finding, by what it costs</h2>',
            '    <p>Checked against the browser\'s own record, the screenshots, the site\'s files and, where a finding is about Claude Code, its documentation. Each finding is kept whatever the verdict, so the next study can be compared with this one.</p>',
            self.findings_html(anchors=False),
            '    <h2>How it was run</h2>',
            f'    <p>The method is newsroom.sgit.ai\'s, <a href="https://newsroom.sgit.ai/articles/how-to-run-synthetic-users.html">How to run synthetic users</a>, adapted for this site. Each user was played by Claude Sonnet, driving a real browser one screenshot at a time. {esc(self.protocol["browser"])}</p>',
            f'    <h3>The loop</h3><ol class="plist-n">{loop}</ol>',
            f'    <h3>The rules</h3><ul class="plist">{rules}</ul>',
            f'    <h3>The interview</h3><ol class="plist-n">{qs}</ol>',
            f'    <h3>What we changed from the newsroom\'s method</h3><ul class="plist">{adapt}</ul>',
            '    <h3>The files</h3>',
            '    <pre><code>data/feedback/synthetic/personas.json     the users, and why these ones\n'
            'data/feedback/synthetic/journeys.json     what each was expected to do, written before any run\n'
            'data/feedback/synthetic/protocol.json     the loop, the rules, the interview, the record format\n'
            'data/feedback/synthetic/checks.json       what we checked, finding by finding\n'
            'data/feedback/synthetic/runs/&lt;who&gt;/run.json        the run as the invented user wrote it\n'
            'data/feedback/synthetic/runs/&lt;who&gt;/_capture.json   the browser\'s own record of every step\n'
            'assets/feedback/S1/&lt;who&gt;/NN.webp                    what they were looking at, step by step\n'
            'feedback/synthetic/tools/step.mjs, driver.mjs      the browser helper</code></pre>'])
        return self.pages.shell(f'Synthetic users, study {self.study}: five invented people on customers.riskmandate.ai',
                                f'Study {self.study}: five invented users, with profiles and expected journeys written first, drove a browser through customers.riskmandate.ai v{self.personas["site_version"]} one screenshot at a time. Their runs, interviews, ratings and findings, each checked. Invented, not user research.',
                                main, 'wrap document-wide')

    def run_page(self, who):
        p, run, cap, j = self.persona(who), self.runs[who], self.captures[who], self.journeys[who]
        steps = []
        for s in run['steps']:
            at   = next((c for c in cap['steps'] if c['n'] == s['n']), {})
            fig  = self.figure(f'{self.study}/{who}', f'{s["n"]:02d}', f'Step {s["n"]}: <code>{esc(at.get("url", ""))}</code>, scrolled {at.get("scrollY", 0)} of {at.get("height", 0)} pixels, {esc(cap["viewport"])}',
                               f'What {p["name"]} saw at step {s["n"]}')
            rows = ''.join(f'<dt>{label}</dt><dd>{esc(str(s[key]))}</dd>' for key, label in (('saw', 'Saw'), ('thought', 'Thought'), ('question', 'Question'), ('confusion', 'Confusion'), ('action', 'Did'), ('why', 'Why')) if s.get(key))
            steps.append(f'    <div class="run-step" id="step-{s["n"]}">{fig}<dl class="verbatim">{rows}</dl></div>')
        interview = ''.join(f'<dt>{esc(qa["q"])}</dt><dd>{esc(qa["a"])}</dd>' for qa in run['interview'])
        knows     = lambda items: ''.join(f'<li>{esc(x)}</li>' for x in items)
        main = '\n'.join([
            f'    <p class="kicker">Study {self.study} · invented user · {esc(p["device"]["kind"])} {p["device"]["width"]}×{p["device"]["height"]} · gave it {run["rating"]} out of 5</p>',
            f'    <h1>{esc(p["name"])}: {esc(p["question"])}</h1>',
            self.banner(),
            f'    <p class="lead">{esc(p["who"])} {esc(p["arrives"])}</p>',
            f'    <dl class="meta"><dt>Knows</dt><dd><ul>{knows(p["knows"])}</ul></dd><dt>Does not know</dt><dd><ul>{knows(p["does_not_know"])}</ul></dd>'
            f'<dt>Patience</dt><dd>{esc(p["patience"])}</dd><dt>Leaves if</dt><dd><ul>{knows(p["leaves_if"])}</ul></dd>'
            f'<dt>We expected</dt><dd>{esc(j["hypothesis"])}</dd><dt>Ended</dt><dd>{esc(run["ended"])}: <q class="verbatim">{esc(run["ended_why"])}</q></dd></dl>',
            f'    <h2>The run, {len(run["steps"])} screenshots</h2>',
            *steps,
            '    <h2>The interview</h2>',
            f'    <dl class="verbatim interview">{interview}</dl>',
            '    <h2>Findings, and our check</h2>',
            '    <table class="register findings"><thead><tr><th>Costs</th><th>The finding</th><th>Our check</th><th>Leads to</th></tr></thead><tbody>',
            *[f'      <tr><td>{esc(f["costs"])}</td><td><q class="verbatim">{esc(f["title"])}</q><p class="verbatim">{esc(f["detail"])}</p><p><a href="#step-{f["step"]}">step {f["step"]}</a>, <code>{esc(f["page"])}</code></p></td>'
              f'<td>{self.verdict_chip(self.check_of(who, i)["verdict"])}<p>{esc(self.check_of(who, i)["note"])}</p></td><td>{self.proposal_links(self.check_of(who, i)["proposals"])}</td></tr>' for i, f in enumerate(run['findings'])],
            '    </tbody></table>',
            f'    <p>The whole study: <a href="/feedback/synthetic/">study {self.study}</a>. Every review and proposal: <a href="/feedback/reviews/">the reviews</a>.</p>'])
        return self.pages.shell(f'{p["name"]}, an invented user: study {self.study}, step by step',
                                f'Study {self.study}, invented user {p["name"]} ({p["who"]}) on customers.riskmandate.ai v{self.personas["site_version"]}: the run screenshot by screenshot, the interview, the rating and the findings, each checked. Invented, not user research.',
                                main, 'wrap document-wide')

    # ── run ────────────────────────────────────────────────────────────────────

    def put(self, target, text, changed):
        text = self.pages.keep_chrome(target, text)
        if self.pages.write_if_changed(target, text, self.check):
            changed.append(target.relative_to(ROOT).as_posix())

    def latest_html(self):                                                          # the reviews on the home page, newest first, so they are easy to find (R003)
        cards = []
        for r in sorted(self.reviews, key=lambda r: r['id'], reverse=True):
            mine = {i for p in r['points'] for i in p['proposals']}
            done = sum(1 for i in mine if self.proposals[i]['decision'] in ('done', 'reversed'))
            cards.append(f'      <a class="card" href="/feedback/reviews/{r["id"]}/"><span class="n">{r["id"]} · {esc(r["reviewer"])} · site v{esc(r["site_version"])}</span>'
                         f'<b>{esc(r["title"])}</b><p>{len(r["points"])} points; {len(mine)} proposals, {done} done.</p></a>')
        cards.append(f'      <a class="card" href="/feedback/synthetic/"><span class="n">Study {self.study} · invented users · site v{esc(self.personas["site_version"])}</span>'
                     f'<b>Five people who do not exist, on the site as it was</b><p>{len(self.checks["checks"])} findings, each checked.</p></a>')
        return '\n'.join(['    <div class="cards">', *cards, '    </div>'])

    def run(self):
        changed = []
        for path in self.pages.html_files():
            text = path.read_text(encoding='utf-8')
            if self.pages.has_block(text, 'reviews-latest'):
                text, _ = self.pages.replace_block(text, 'reviews-latest', self.latest_html())
                if self.pages.write_if_changed(path, text, self.check):
                    changed.append(path.relative_to(ROOT).as_posix())
        wanted  = ({OUT / 'index.html', OUT / 'reviews' / 'index.html', OUT / 'synthetic' / 'index.html', OUT / 'how-sending-works' / 'index.html'}
                   | {OUT / 'reviews' / r['id'] / 'index.html' for r in self.reviews}
                   | {OUT / 'synthetic' / who / 'index.html' for who in self.runs})
        for stale in OUT.rglob('index.html'):
            if stale not in wanted:
                raise SystemExit(f'{stale.relative_to(ROOT)}: nothing in data/feedback/ makes this page; remove it or add its record')
        self.put(OUT / 'index.html', self.give_page(), changed)
        self.put(OUT / 'how-sending-works' / 'index.html', self.how_page(), changed)
        self.put(OUT / 'reviews' / 'index.html', self.reviews_page(), changed)
        for review in self.reviews:
            self.put(OUT / 'reviews' / review['id'] / 'index.html', self.review_page(review), changed)
        self.put(OUT / 'synthetic' / 'index.html', self.study_page(), changed)
        for who in self.runs:
            self.put(OUT / 'synthetic' / who / 'index.html', self.run_page(who), changed)
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Feedback(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  feedback {verb}: {name}')
    if check and changed:
        print(f'gen_feedback --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_feedback.py')
        sys.exit(1)
    print(f'gen_feedback: {len(changed)} file(s) {verb}')
