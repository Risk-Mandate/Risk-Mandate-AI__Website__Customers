# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Policies
# Writes everything under policies/ from data/policies.json, the rules copied
# from riskmandate.ai (data/rules/) and the hooks in policies/hooks/: a page per
# policy (the line, the hook, the settings that wire it, the prompt to try it),
# the settings.json beside each hooked policy, the starter pack (its page, its
# CLAUDE.md block, its merged settings.json and the INSTALL.md an agent follows),
# and the index with all of riskmandate.ai's rules. `--check` fails on drift.
# Usage: python3 admin/build/gen_policies.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import sys

from chrome import ROOT, METER, SITE_NAME, AGENT_ADDRESS
from pages  import Site__Pages
from gen_storyboards import Gen__Storyboards


POLICIES_FILE = ROOT / 'data' / 'policies.json'
RULES_DIR     = ROOT / 'data' / 'rules'
OUT           = ROOT / 'policies'
HOOKS         = OUT / 'hooks'
BASE          = 'https://' + SITE_NAME
PACK_VERSION  = 'v1'
PRICE         = {k['kind']: k['price'] for k in METER['kinds']}
esc           = html.escape


class Gen__Policies:

    def __init__(self, check=False):
        self.check    = check
        self.pages    = Site__Pages()
        self.data     = json.loads(POLICIES_FILE.read_text(encoding='utf-8'))
        self.rules    = {r['slug']: r for r in (json.loads(p.read_text(encoding='utf-8')) for p in sorted(RULES_DIR.glob('*.json')) if p.name != 'SOURCE.json')}
        self.source   = json.loads((RULES_DIR / 'SOURCE.json').read_text(encoding='utf-8'))
        self.policies = self.data['policies']
        self.demos    = Gen__Storyboards(check=True)                                     # the demo markup comes from one place, so the two generators agree on the block
        self.validate()

    def validate(self):
        problems = []
        for p in self.policies:
            rule = self.rules.get(p['slug'])
            if not rule:
                problems.append(f'{p["slug"]}: no rule of that slug in data/rules/')
            elif rule['id'] != p['rule']:
                problems.append(f'{p["slug"]}: names {p["rule"]}, the rule is {rule["id"]}')
            if p['hook'] and not (HOOKS / p['hook']['file']).exists():
                problems.append(f'{p["slug"]}: hook {p["hook"]["file"]} is not in policies/hooks/')
            if not p['hook'] and not p.get('where'):
                problems.append(f'{p["slug"]}: a policy with no hook says where its line goes')
        for slug in self.data['starter']:
            policy = next((p for p in self.policies if p['slug'] == slug), None)
            if not policy or not policy['hook']:
                problems.append(f'starter: {slug} is not a policy with a hook')
        if len(self.rules) != self.source['count']:
            problems.append(f'data/rules/ holds {len(self.rules)} rules, SOURCE.json says {self.source["count"]}')
        if problems:
            raise SystemExit('data/policies.json is invalid:\n  ' + '\n  '.join(problems))

    # ── the files a customer installs ──────────────────────────────────────────

    def hook_entry(self, p):
        return {'matcher': p['hook']['matcher'],
                'hooks'  : [{'type': 'command', 'command': f'python3 "${{CLAUDE_PROJECT_DIR}}/.claude/hooks/{p["hook"]["file"]}"', 'timeout': 10}]}

    def permissions_of(self, rule):                                               # the deny and ask rules riskmandate.ai published as the rule's setting, read as JSON
        out = {}
        for s in rule.get('stronger') or []:
            if s['kind'] != 'setting' or not s['how'].lstrip().startswith('{'):
                continue
            for key, values in json.loads(s['how']).get('permissions', {}).items():
                out.setdefault(key, [])
                out[key] += [v for v in values if v not in out[key]]
        return out

    def settings(self, policies):
        perms = {}
        for p in policies:
            for key, values in self.permissions_of(self.rules[p['slug']]).items():
                perms.setdefault(key, [])
                perms[key] += [v for v in values if v not in perms[key]]
        out = {'hooks': {'PreToolUse': [self.hook_entry(p) for p in policies]}}
        if perms:
            out = {'permissions': perms, **out}
        return json.dumps(out, indent=2) + '\n'

    def claude_md(self, policies):
        lines = [f'## Behaviour policy (customers.riskmandate.ai starter pack, {PACK_VERSION})', '',
                 'These lines are rules for you, the agent. Hooks in .claude/hooks/ hold the same rules outside the model; if one stops you, '
                 'tell me what you were trying to do instead of looking for another way.', '']
        for p in policies:
            rule = self.rules[p['slug']]
            lines.append(f'- {rule["line"]} ({rule["id"]}, {BASE}/policies/{p["slug"]}/)')
        return '\n'.join(lines) + '\n'

    def install_md(self, policies):
        hooks = '\n'.join(f'   - {BASE}/policies/hooks/{p["hook"]["file"]} to `.claude/hooks/{p["hook"]["file"]}`' for p in policies if p['slug'] != 'change-its-own-permissions')
        last  = next(p for p in policies if p['slug'] == 'change-its-own-permissions')
        return '\n'.join([
            f'# Install the starter pack ({PACK_VERSION}) from customers.riskmandate.ai',
            '',
            'For the agent the person is talking to. Four Agent Behaviour Policies, each a line for CLAUDE.md and a Claude Code hook. '
            'Follow these steps in order. Show the person every file before you write it, and wait for a yes for each one. '
            'Do not change anything this file does not name, and do not remove anything already in their settings.',
            '',
            '1. Tell the person what is about to be installed: the four lines in ' + f'{BASE}/policies/starter/CLAUDE.md' + ', and that each comes with a hook that stops or asks before the thing the line rules out.',
            '2. Fetch and show each hook, then save it, keeping its name:',
            hooks,
            f'3. Merge {BASE}/policies/starter/settings.json into the project\'s `.claude/settings.json`: add its `permissions` entries and its `hooks.PreToolUse` entries to any already there, keep everything else, and show the person the result before saving it. Create the file if there is none.',
            f'4. Add the block in {BASE}/policies/starter/CLAUDE.md to the end of the project\'s CLAUDE.md, creating it if there is none.',
            f'5. Last, because from then on any change to your own settings asks the person: save {BASE}/policies/hooks/{last["hook"]["file"]} to `.claude/hooks/{last["hook"]["file"]}`.',
            '6. Tell the person that Claude Code picks up the hooks on its own and that /hooks lists them, and give them the four prompts on ' + f'{BASE}/policies/starter/' + ' to try.',
            '',
            'The hooks need Python 3 and nothing else. Each is under eighty lines; the person may want to read them, and should.',
            ''])

    # ── the pages ──────────────────────────────────────────────────────────────

    def snippet(self, ident, text, label='Copy'):
        return (f'<div class="snippet"><pre id="{ident}"><code>{esc(text)}</code></pre>'
                f'<button type="button" class="copy" data-copy="{ident}">{label}</button></div>')

    def money(self, pence):
        return 'free' if pence == 0 else f'{pence}p' if pence < 100 else f'£{pence / 100:.2f}'

    def install_prompt(self, p):
        return (f'Install the behaviour policy at {BASE}/policies/{p["slug"]}/ in this project: add its line to CLAUDE.md, '
                f'save {BASE}/policies/hooks/{p["hook"]["file"]} as .claude/hooks/{p["hook"]["file"]}, and merge '
                f'{BASE}/policies/{p["slug"]}/settings.json into .claude/settings.json. Show me each change before you make it, and wait for my yes.')

    def stronger_html(self, rule):
        items = []
        for s in rule.get('stronger') or []:
            how = (f'<pre><code>{esc(s["how"])}</code></pre>' if s['how'].lstrip().startswith('{') else f'<p>{esc(s["how"])}</p>')
            items.append(f'<li><span class="status status-{"shipped" if s["kind"] == "boundary" else "proposed"}">{esc(s["kind"])}</span> '
                         f'<strong>{esc(s["what"])}.</strong> {how}<p class="src">Source: <a href="{esc(s["source"])}">{esc(s["source"])}</a>, read {esc(s["read"])}, as riskmandate.ai quotes it.</p></li>')
        return '<ul class="plist stronger">' + ''.join(items) + '</ul>' if items else '<p>riskmandate.ai lists no stronger control for this rule yet.</p>'

    def plain_html(self, p):                                                      # the hook in plain words, written from its own rules (P12 of the feedback register)
        w    = p['plain']
        rows = ''.join(f'<tr><td>{label}</td><td>{esc(w[key])}</td></tr>' for key, label in (('looks_at', 'Looks at'), ('stops', 'Stops'), ('asks', 'Asks you first'), ('lets_through', 'Lets through'), ('misses', 'Does not see')))
        return (f'<p><strong>What the hook does, in plain words:</strong></p><table class="plain"><tbody>{rows}</tbody></table>'
                f'<p><strong>To turn it off:</strong> remove its entry under <code>hooks.PreToolUse</code> in <code>.claude/settings.json</code>; Claude Code stops running it straight away.</p>')

    def did_it_work_html(self, p):                                                # what a customer does when the try does not go as the page says (P11)
        return (f'<div class="note did-it-work"><p><strong>Did it work?</strong> If Claude Code stopped it, or asked you, the hook is running. '
                f'If the prompt went through as if nothing were installed, the hook did not run, and Claude Code does not wait for a hook that cannot run: '
                f'the action goes ahead (on Windows without Git Bash it may be blocked instead). The hook fails open, one more reason it is a setting and not a boundary. Check three things: '
                f'that <code>/hooks</code> lists it; that <code>python3 --version</code> works where Claude Code runs (on Windows, Claude Code runs hooks in Git Bash, or in PowerShell if Git Bash is not installed, '
                f'and <code>python3</code> may not exist there: install Python, or put <code>py</code> in place of <code>python3</code> in the settings); and that <code>.claude/hooks/{p["hook"]["file"]}</code> is there. '
                f'Still stuck? <a href="mailto:{AGENT_ADDRESS}?subject={p["rule"]}%20did%20not%20work">Tell us</a>.</p>'
                f'<p>The tests for this hook feed it the JSON Claude Code would send, every refusal with an allowed twin beside it; they do not drive a live Claude Code session. Your try is the live test.</p></div>')

    def policy_page(self, p):
        rule  = self.rules[p['slug']]
        price = self.money(PRICE['policy'])
        slug  = p['slug']
        where = 'CLAUDE.md, at the top of your project (create it if there is none)' if p['hook'] else p['where']
        steps = [f'      <li><b>Tell the agent.</b><p>Paste this line into {esc(where)}. It is the rule in the agent\'s own words; on its own it is an <em>expectation</em>, which the agent follows when it can.</p>{self.snippet(f"line-{slug}", rule["line"])}</li>']
        if p['hook']:
            hook_src = (HOOKS / p['hook']['file']).read_text(encoding='utf-8')
            steps.append(f'      <li><b>Make Claude Code hold it.</b><p>The hook runs outside the model, before every matching tool call, and stops or asks before the thing the line rules out. The quickest way is to ask Claude Code to install it, and to read each change before you say yes:</p>'
                         f'{self.snippet(f"install-{slug}", self.install_prompt(p))}'
                         f'<p>Or by hand: save <a href="/policies/hooks/{p["hook"]["file"]}"><code>{p["hook"]["file"]}</code></a> as <code>.claude/hooks/{p["hook"]["file"]}</code> and merge <a href="/policies/{slug}/settings.json"><code>settings.json</code></a> into <code>.claude/settings.json</code>. Claude Code picks up the change on its own; <code>/hooks</code> lists the hooks it is running.</p>'
                         f'{self.snippet(f"settings-{slug}", self.settings([p]))}'
                         f'{self.plain_html(p)}'
                         f'<details class="hook-source"><summary>Read the hook before you install it ({len(hook_src.splitlines())} lines of Python, standard library only; the box scrolls)</summary><pre><code>{esc(hook_src)}</code></pre></details></li>')
        else:
            steps.append(f'      <li><b>There is no hook here, and that matters.</b><p>{" and ".join(esc(f) for f in p["for"])} take the line and nothing else, so this behaviour policy is an expectation and the page says so. The stronger controls riskmandate.ai lists are below; in Claude Code, the same line goes in CLAUDE.md.</p></li>')
        steps.append(f'      <li><b>Try it.</b><p>Paste this, as you would, and watch what happens.</p>{self.snippet(f"try-{slug}", p["try"]["prompt"])}'
                     f'<p><strong>With the behaviour policy:</strong> {esc(p["try"]["with"])}</p><p><strong>Without it:</strong> {esc(p["try"]["without"])}</p>'
                     + (self.did_it_work_html(p) if p['hook'] else '')
                     + (f'\n    <!-- rm-customers:demo:start id="{p["demo"]}" -->\n{self.demos.demo(p["demo"])}\n    <!-- rm-customers:demo:end -->\n' if p.get('demo') else '')
                     + '</li>')
        halves = [f'<tr><td>The line</td><td>expectation</td><td>the agent reads it and follows it when it can</td></tr>']
        if p['hook']:
            halves.append('<tr><td>The hook</td><td>setting</td><td>Claude Code runs it before the tool call, outside the model; it lives in a file the agent could edit, which <a href="/policies/change-its-own-permissions/">RM-R0015</a> guards</td></tr>')
        main = '\n'.join([
            f'    <p class="kicker">{rule["id"]} · {" · ".join(esc(f) for f in p["for"])} · {p["minutes"]} minute{"s" if p["minutes"] != 1 else ""} · this page costs {price} read to the end</p>',
            f'    <h1>{esc(p["title"])}</h1>',
            f'    <p class="lead">{esc(rule["worry"])}</p>',
            f'    <p class="you-get"><strong>What you get:</strong> {esc(rule["you_get"])}</p>',
            '    <ol class="steps install">', *steps, '    </ol>',
            '    <h2>What this is, and what it is not</h2>',
            f'    <table><thead><tr><th>{"Half" if p["hook"] else "Part"}</th><th>Barrier</th><th>What holds it</th></tr></thead><tbody>' + ''.join(halves) + '</tbody></table>',
            ('    <p>Neither half is a <em>boundary</em>, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:</p>' if p['hook'] else
             '    <p>The line is an <em>expectation</em>, not a <em>boundary</em>, the only barrier that holds when the agent does not cooperate. The stronger controls for this rule, from riskmandate.ai:</p>'),
            f'    {self.stronger_html(rule)}',
            '    <h2>Tell us what happened</h2>',
            f'    <p>Did it stop what it should, and nothing else? What did it get in the way of? <a href="mailto:{AGENT_ADDRESS}?subject={rule["id"]}%20tried">Write to {AGENT_ADDRESS}</a>; it goes on your follow-up, and a person reads it within a working day. Or record a voice memo and let your Claude turn it into a review: <a href="/feedback/">tell us what you think</a>.</p>',
            f'    <p class="src">The rule is <a href="https://riskmandate.ai/rules/{slug}.html">{rule["id"]} on riskmandate.ai</a>, version {esc(rule["version"])}, CC BY 4.0; copied here on {self.source["copied"]}. The hook and this page are this site\'s, CC BY 4.0 and Apache-2.0.</p>'])
        title = f'{p["title"]}: behaviour policy {rule["id"]}'
        desc  = f'{rule["question"]} The line for your agent, ' + ('the Claude Code hook that holds it, ' if p['hook'] else '') + f'and a prompt to try it with, in {p["minutes"]} minute{"s" if p["minutes"] != 1 else ""}. From riskmandate.ai\'s {rule["id"]}.'
        return self.pages.shell(title, desc, main, 'wrap policy')

    def card(self, p):
        rule = self.rules[p['slug']]
        tags = ' · '.join(p['for']) + (' · line and hook' if p['hook'] else ' · line only')
        return (f'      <a class="card policy-card" href="/policies/{p["slug"]}/"><span class="n">{rule["id"]} · {esc(tags)}</span>'
                f'<b>{esc(p["title"])}</b><p>{esc(rule["question"])}</p><p class="price">{p["minutes"]} min · {self.money(PRICE["policy"])}</p></a>')

    def starter_page(self, starters):
        tries = ''.join(f'<li><b>{esc(p["title"])}</b>{self.snippet(f"try-pack-{p["slug"]}", p["try"]["prompt"])}<p>{esc(p["try"]["with"])}</p></li>' for p in starters)
        main = '\n'.join([
            f'    <p class="kicker">Starter pack {PACK_VERSION} · Claude Code · 5 minutes · this page costs {self.money(PRICE["pack"])} read to the end</p>',
            '    <h1>Four behaviour policies, <span class="g">one install.</span></h1>',
            '    <p class="lead">The four things most people do not want a coding agent to do without asking: read a secret, push to main, delete their files, and change its own permissions. Each comes as a line for CLAUDE.md and a hook Claude Code runs before the tool call. The fourth keeps the other three in place.</p>',
            '    <h2>Install it: ask Claude Code</h2>',
            '    <p>Paste this into Claude Code, in the project you want covered. It shows you every file before it writes it.</p>',
            f'    {self.snippet("install-pack", f"Install the behaviour policies in {BASE}/policies/starter/INSTALL.md in this project. Follow its steps in order, show me each file before you write it, and wait for my yes.")}',
            '    <h2>Or by hand</h2>',
            '    <ol class="plist-n">',
            '      <li>Save the four hooks into <code>.claude/hooks/</code>: ' + ', '.join(f'<a href="/policies/hooks/{p["hook"]["file"]}"><code>{p["hook"]["file"]}</code></a>' for p in starters) + '.</li>',
            '      <li>Merge <a href="/policies/starter/settings.json"><code>settings.json</code></a> into <code>.claude/settings.json</code>.</li>',
            '      <li>Add <a href="/policies/starter/CLAUDE.md">the CLAUDE.md block</a> to your project\'s CLAUDE.md.</li>',
            '      <li>Claude Code picks them up on its own; <code>/hooks</code> lists them.</li>',
            '    </ol>',
            f'    {self.snippet("pack-settings", self.settings(starters))}',
            f'    {self.snippet("pack-claude-md", self.claude_md(starters))}',
            '    <h2>Then try each one</h2>',
            f'    <ol class="steps">{tries}</ol>',
            '    <p>Each policy has its own page, with what it is and what it is not: ' + ', '.join(f'<a href="/policies/{p["slug"]}/">{esc(p["title"])}</a>' for p in starters) + '.</p>'])
        return self.pages.shell('The starter pack: four behaviour policies for Claude Code, one install, five minutes',
                                'Four Agent Behaviour Policies for Claude Code in one install: keep away from secrets, push only to your branch, nothing deleted without a yes, and only you change its permissions. Each is a line for CLAUDE.md and a hook; ask Claude Code to install them, or copy four files.',
                                main, 'wrap policy')

    def index_page(self, starters):
        rows = []
        for rule in sorted(self.rules.values(), key=lambda r: r['id']):
            here = next((p for p in self.policies if p['slug'] == rule['slug']), None)
            link = f'<a href="/policies/{rule["slug"]}/">here, with a hook</a>' if here and here['hook'] else f'<a href="/policies/{rule["slug"]}/">here</a>' if here else f'<a href="https://riskmandate.ai/rules/{rule["slug"]}.html">riskmandate.ai</a>'
            rows.append(f'      <tr><td><code>{rule["id"]}</code></td><td>{esc(rule["question"])}</td><td>{esc(rule["answer"])}</td><td>{esc(rule["line"])}</td><td>{link}</td></tr>')
        main = '\n'.join([
            '    <h1>Pick one thing <span class="g">you do not want your agent to do.</span></h1>',
            '    <p class="lead">Each behaviour policy here starts from one worry and ends with the agent stopping, or asking you, before it does that thing. If you are new to this, start with <a href="/examples/">the six examples</a>, in Claude or ChatGPT in your browser.</p>',
            '    <h2>In Claude or ChatGPT, in your browser: a line</h2>',
            '    <div class="cards">', *[self.card(p) for p in self.policies if not p['hook']], '    </div>',
            '    <h2>For Claude Code, later: a line and a hook</h2>',
            '    <div class="note warn"><p><strong>These install a script on your machine.</strong> A hook is a small Python program Claude Code runs before the agent acts; it runs as you, with everything you can reach. Read every hook before you install it, as each page asks, and start with the examples above if you have not tried a line yet.</p></div>',
            f'    <a class="card pack-card" href="/policies/starter/"><span class="n">Starter pack {PACK_VERSION} · Claude Code · 5 minutes</span><b>All four Claude Code policies in one install</b><p>Secrets, pushes, deletes, and the agent\'s own permissions. Paste one prompt; Claude Code shows you every file before it writes it.</p><p class="price">{self.money(PRICE["pack"])}</p></a>',
            '    <div class="cards">', *[self.card(p) for p in self.policies if p['hook']], '    </div>',
            f'    <h2>All {len(self.rules)} of riskmandate.ai\'s rules</h2>',
            f'    <p>The behaviour policies above are built from these, copied on {self.source["copied"]} from <a href="{self.source["page"]}">riskmandate.ai\'s rules</a>, CC BY 4.0. Each rule\'s page there has the stronger settings and, for some, a run with and without the line.</p>',
            '    <table class="rules"><thead><tr><th>Rule</th><th>The question</th><th>Answer</th><th>The line</th><th>Where</th></tr></thead><tbody>', *rows, '    </tbody></table>'])
        return self.pages.shell('Behaviour policies: pick one worry, paste one line, add one hook, try it',
                                'The behaviour policies a customer installs first: four for Claude Code, each a line and a hook, two for ChatGPT and Claude, each a line; a starter pack that installs the four in one go; and all 24 of riskmandate.ai\'s rules they come from.',
                                main, 'wrap policy')

    # ── run ────────────────────────────────────────────────────────────────────

    def put(self, target, text, changed, page=False):
        if page:
            text = self.pages.keep_chrome(target, text)
        if self.pages.write_if_changed(target, text, self.check):
            changed.append(target.relative_to(ROOT).as_posix())

    def run(self):
        changed  = []
        starters = [next(p for p in self.policies if p['slug'] == s) for s in self.data['starter']]
        wanted   = {OUT / p['slug'] / 'index.html' for p in self.policies} | {OUT / 'starter' / 'index.html', OUT / 'index.html'}
        for stale in OUT.glob('*/index.html'):
            if stale not in wanted:
                raise SystemExit(f'{stale.relative_to(ROOT)}: no policy in data/policies.json; remove the folder or add the policy')
        for p in self.policies:
            self.put(OUT / p['slug'] / 'index.html', self.policy_page(p), changed, page=True)
            if p['hook']:
                self.put(OUT / p['slug'] / 'settings.json', self.settings([p]), changed)
        self.put(OUT / 'starter' / 'index.html', self.starter_page(starters), changed, page=True)
        self.put(OUT / 'starter' / 'settings.json', self.settings(starters), changed)
        self.put(OUT / 'starter' / 'CLAUDE.md', self.claude_md(starters), changed)
        self.put(OUT / 'starter' / 'INSTALL.md', self.install_md(starters), changed)
        self.put(OUT / 'index.html', self.index_page(starters), changed, page=True)
        for path in self.pages.html_files():                                          # the policy cards wherever a page asks for them (the home page)
            text = path.read_text(encoding='utf-8')
            if self.pages.has_block(text, 'policy-cards'):
                text, _ = self.pages.replace_block(text, 'policy-cards', '\n'.join(['    <div class="cards">', *[self.card(p) for p in self.policies], '    </div>']))
                self.put(path, text, changed)
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Policies(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  policies {verb}: {name}')
    if check and changed:
        print(f'gen_policies --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_policies.py')
        sys.exit(1)
    print(f'gen_policies: {len(changed)} file(s) {verb}')
