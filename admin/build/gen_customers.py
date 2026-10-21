# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Gen__Customers
# Reads data/customers.json and data/milestones.json, validates them, and
# generates (1) one page per customer under customers/<id>/index.html, (2) the
# batch table in customers/index.html, (3) the steps on milestones/index.html,
# and (4) the counts block on the programme page. Every number on those pages is
# counted here, from the data, never typed. `--check` fails on drift.
# Usage: python3 admin/build/gen_customers.py [--check]
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json
import re
import sys

from chrome import ROOT, Chrome
from pages  import Site__Pages


CUSTOMERS_FILE  = ROOT / 'data' / 'customers.json'
MILESTONES_FILE = ROOT / 'data' / 'milestones.json'
CUSTOMERS_DIR   = ROOT / 'customers'
STEP_STATES     = ('open', 'in-progress', 'done')
RE_ID           = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
RE_DATE         = re.compile(r'^\d{4}-\d{2}-\d{2}$')
RE_CONTACT      = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+|\+?(?:\d[\s().-]*){9,}\d|https?://(?:www\.)?linkedin\.com', re.I)   # no contact details, ever: an address, a run of ten or more digits (a date has eight), a profile link


class Gen__Customers:

    def __init__(self, check=False):
        self.check      = check
        self.chrome     = Chrome()
        self.pages      = Site__Pages()
        self.data       = json.loads(CUSTOMERS_FILE.read_text(encoding='utf-8'))
        self.customers  = self.data['customers']
        self.steps      = json.loads(MILESTONES_FILE.read_text(encoding='utf-8'))['steps']
        self.step_ids   = [step['id'] for step in self.steps]
        self.validate()

    # ── validation: the shape, the states, and no contact details ──────────────

    def validate(self):
        problems = []
        seen     = set()
        for customer in self.customers:
            cid = customer.get('id', '?')
            for key in ('id', 'handle', 'kind', 'status', 'started', 'agent', 'credit', 'first_policy', 'objectives', 'milestones', 'follow_ups'):
                if key not in customer:
                    problems.append(f'{cid}: missing "{key}"')
            if not RE_ID.match(cid):
                problems.append(f'{cid}: id must be lower-case words joined by hyphens')
            if cid in seen:
                problems.append(f'{cid}: duplicate id')
            seen.add(cid)
            if customer.get('kind') not in self.data['kinds']:
                problems.append(f'{cid}: kind "{customer.get("kind")}" is not in kinds')
            if customer.get('status') not in self.data['statuses']:
                problems.append(f'{cid}: status "{customer.get("status")}" is not in statuses')
            if (customer.get('kind') == 'example') != (customer.get('status') == 'example'):
                problems.append(f'{cid}: an example is an example in both kind and status')
            if customer.get('started') is not None and not RE_DATE.match(str(customer['started'])):
                problems.append(f'{cid}: started must be YYYY-MM-DD or null')
            credit = customer.get('credit') or {}
            for key in ('granted', 'currency', 'used', 'topped_up'):
                if key not in credit:
                    problems.append(f'{cid}: credit is missing "{key}"')
            if credit.get('used', 0) > credit.get('granted', 0) and not credit.get('topped_up'):
                problems.append(f'{cid}: credit used exceeds credit granted without a top-up')
            policy = customer.get('first_policy')
            if policy is not None:
                for key in ('date', 'rows', 'gaps'):
                    if key not in policy:
                        problems.append(f'{cid}: first_policy is missing "{key}"')
                if policy.get('gaps', 0) > policy.get('rows', 0):
                    problems.append(f'{cid}: first_policy has more gaps than rows')
            milestones = customer.get('milestones') or {}
            if sorted(milestones) != sorted(self.step_ids):
                problems.append(f'{cid}: milestones must name exactly {self.step_ids}')
            for step_id, state in milestones.items():
                if state.get('state') not in STEP_STATES:
                    problems.append(f'{cid}: {step_id} state must be one of {STEP_STATES}')
                if state.get('state') == 'done' and not RE_DATE.match(str(state.get('date', ''))):
                    problems.append(f'{cid}: {step_id} is done and needs a date')
            for entry in customer.get('follow_ups') or []:
                for key in ('date', 'did', 'blocked', 'next'):
                    if key not in entry:
                        problems.append(f'{cid}: a follow-up is missing "{key}"')
                if not RE_DATE.match(str(entry.get('date', ''))):
                    problems.append(f'{cid}: follow-up date must be YYYY-MM-DD')
            found = RE_CONTACT.search(json.dumps(customer))
            if found:
                problems.append(f'{cid}: looks like contact details ({found.group(0)[:12]}…); the record carries none')
        if problems:
            raise SystemExit('data/customers.json is invalid:\n  ' + '\n  '.join(problems))

    # ── counting ───────────────────────────────────────────────────────────────

    def real(self):
        return [c for c in self.customers if c['kind'] != 'example']

    def done_steps(self, customer):
        return sum(1 for state in customer['milestones'].values() if state['state'] == 'done')

    def counts(self):
        real = self.real()
        return {'customers'      : len(real)                                                                  ,
                'started'        : sum(1 for c in real if c['started'])                                       ,
                'first_policies' : sum(1 for c in real if c['first_policy'])                                  ,
                'steps_done'     : sum(self.done_steps(c) for c in real)                                      ,
                'steps_total'    : len(self.step_ids) * len(real)                                             ,
                'credit_granted' : sum(c['credit']['granted'] for c in real)                                  ,
                'credit_used'    : sum(c['credit']['used'] for c in real)                                     ,
                'topped_up'      : sum(1 for c in real if c['credit']['topped_up'])                            ,
                'follow_ups'     : sum(len(c['follow_ups']) for c in real)                                    }

    # ── fragments ──────────────────────────────────────────────────────────────

    def esc(self, text):
        return html.escape(str(text))

    def step_chip(self, state):
        label = state['state'] + (f' {state["date"]}' if state.get('date') else '')
        return f'<span class="step-state {state["state"]}">{self.esc(label)}</span>'

    def credit_text(self, customer):
        credit = customer['credit']
        if credit['granted'] == 0 and credit['used'] == 0:
            return 'none (' + self.esc(credit.get('note', 'no credit for this record')) + ')'
        symbol = {'GBP': '£'}.get(credit['currency'], credit['currency'] + ' ')
        return (f'{symbol}{credit["used"]} used of {symbol}{credit["granted"]} granted; '
                f'{"topped up" if credit["topped_up"] else "not topped up"}'
                + (f' ({self.esc(credit["note"])})' if credit.get('note') else ''))

    def policy_text(self, customer):
        policy = customer['first_policy']
        if not policy:
            return 'not yet'
        return f'{policy["date"]}: {policy["rows"]} rows, {policy["gaps"]} gaps'

    def counts_html(self):
        counts = self.counts()
        tiles  = [(counts['customers'], 'customers in the first batch'),
                  (counts['started'], 'started'),
                  (counts['first_policies'], 'first behaviour policies written'),
                  (f'{counts["steps_done"]} of {counts["steps_total"]}', 'milestone steps done'),
                  (f'£{counts["credit_used"]} of £{counts["credit_granted"]}', 'credit used'),
                  (counts['topped_up'], 'topped up'),
                  (counts['follow_ups'], 'follow-ups recorded')]
        parts  = ['  <div class="counts" data-generated-from="data/customers.json">']
        for value, label in tiles:
            parts.append(f'    <div class="c"><b>{self.esc(value)}</b><span>{self.esc(label)}</span></div>')
        parts.append('  </div>')
        return '\n'.join(parts)

    def batch_table_html(self):
        rows = []
        for customer in self.customers:
            rows.append('      <tr>'
                        f'<td><a href="/customers/{customer["id"]}/">{self.esc(customer["handle"])}</a></td>'
                        f'<td>{self.esc(customer["kind"])}</td>'
                        f'<td>{self.esc(customer["status"])}</td>'
                        f'<td>{self.esc(customer["started"] or "not yet")}</td>'
                        f'<td>{self.policy_text(customer)}</td>'
                        f'<td>{self.done_steps(customer)} of {len(self.step_ids)}</td>'
                        f'<td>{self.credit_text(customer)}</td>'
                        f'<td>{len(customer["follow_ups"])}</td>'
                        '</tr>')
        return '\n'.join(['  <table class="batch" data-generated-from="data/customers.json">'                                                                              ,
                          '    <thead><tr><th>Customer</th><th>Kind</th><th>Status</th><th>Started</th><th>First behaviour policy</th><th>Steps done</th><th>Credit</th><th>Follow-ups</th></tr></thead>',
                          '    <tbody>'                                                                                                                                      ,
                          *rows                                                                                                                                              ,
                          '    </tbody>'                                                                                                                                     ,
                          '  </table>'                                                                                                                                       ])

    def steps_html(self):
        parts = ['  <ol class="steps" data-generated-from="data/milestones.json">']
        for step in self.steps:
            parts.append(f'    <li id="{step["id"]}"><b>{step["id"]} · {self.esc(step["title"])}</b>'
                         f'<p>{self.esc(step["objective"])}</p>'
                         f'<p><strong>Done when:</strong> {self.esc(step["done_when"])}</p>'
                         f'<p><strong>Who:</strong> {self.esc(step["who"])}</p></li>')
        parts.append('  </ol>')
        return '\n'.join(parts)

    def customer_page(self, customer):
        cid      = customer['id']
        title    = f'{customer["handle"]}: where they are'
        if customer['kind'] == 'example':
            description = 'A worked example of a customer page, with invented numbers, so the shape can be seen before the first customer fills it. Not a customer.'
        else:
            description = (f'{customer["handle"]}: {customer["status"]}; started {customer["started"] or "not yet"}; '
                           f'first behaviour policy {self.policy_text(customer)}; {self.done_steps(customer)} of {len(self.step_ids)} steps done. '
                           f'No contact details on this page.')
        objectives = ''.join(f'<li>{self.esc(o)}</li>' for o in customer['objectives']) or '<li>None agreed yet.</li>'
        steps      = []
        for step in self.steps:
            state = customer['milestones'][step['id']]
            steps.append(f'      <tr><td><a href="/milestones/#{step["id"]}">{step["id"]}</a></td><td>{self.esc(step["title"])}</td><td>{self.step_chip(state)}</td></tr>')
        follow_ups = []
        for entry in reversed(customer['follow_ups']):
            follow_ups.append(f'      <tr><td>{entry["date"]}</td><td>{self.esc(entry["did"])}</td><td>{self.esc(entry["blocked"])}</td><td>{self.esc(entry["next"])}</td></tr>')
        follow_table = ('\n'.join(['    <table class="follow-ups">'                                                                      ,
                                   '      <thead><tr><th>Date</th><th>What they did</th><th>What got in the way</th><th>What is next</th></tr></thead>',
                                   '      <tbody>', *follow_ups, '      </tbody>', '    </table>'])
                        if follow_ups else '    <p>No follow-up recorded yet.</p>')
        example_note = ('    <div class="note warn"><p><strong>A worked example.</strong> The numbers on this page are invented to show the shape of a customer page. '
                        'Nothing here describes a real person or organisation.</p></div>\n') if customer['kind'] == 'example' else ''
        return '\n'.join(['<!doctype html>'                                                                                                   ,
                          '<html lang="en-GB">'                                                                                               ,
                          '<head>'                                                                                                            ,
                          '  <meta charset="utf-8">'                                                                                          ,
                          '  <meta name="viewport" content="width=device-width, initial-scale=1">'                                            ,
                          f'  <title>{self.esc(title)}</title>'                                                                  ,
                          f'  <meta name="description" content="{self.esc(description)}">'                                                    ,
                          '  <!-- rm-customers:head:start -->'                                                                                ,
                          '  <!-- rm-customers:head:end -->'                                                                                  ,
                          '</head>'                                                                                                           ,
                          '<body>'                                                                                                            ,
                          '  <!-- rm-customers:nav:start -->'                                                                                 ,
                          '  <!-- rm-customers:nav:end -->'                                                                                   ,
                          '  <main class="wrap" data-generated-from="data/customers.json">'                                                   ,
                          f'    <h1>{self.esc(customer["handle"])}</h1>'                                                                      ,
                          f'    <p class="lead">{self.esc(self.data["kinds"][customer["kind"]][:1].upper() + self.data["kinds"][customer["kind"]][1:])}. Status: <strong>{self.esc(customer["status"])}</strong>, '
                          f'{self.esc(self.data["statuses"][customer["status"]])}.</p>'                                                      ,
                          example_note.rstrip('\n')                                                                                           ,
                          '    <h2>What the brief asks us to track</h2>'                                                                      ,
                          '    <dl class="kv">'                                                                                               ,
                          f'      <dt>Started</dt><dd>{self.esc(customer["started"] or "not yet")}</dd>'                                      ,
                          f'      <dt>The agent</dt><dd>{self.esc(customer["agent"])}</dd>'                                                   ,
                          f'      <dt>First behaviour policy</dt><dd>{self.policy_text(customer)}</dd>'                                       ,
                          f'      <dt>Milestone steps done</dt><dd>{self.done_steps(customer)} of {len(self.step_ids)}</dd>'                  ,
                          f'      <dt>Credit</dt><dd>{self.credit_text(customer)}</dd>'                                                       ,
                          f'      <dt>Follow-ups recorded</dt><dd>{len(customer["follow_ups"])}</dd>'                                         ,
                          '    </dl>'                                                                                                         ,
                          '    <h2>Objectives agreed with them</h2>'                                                                          ,
                          f'    <ul>{objectives}</ul>'                                                                                         ,
                          '    <h2>The steps</h2>'                                                                                            ,
                          '    <p>The shared ladder is on <a href="/milestones/">the milestones page</a>; the state of each step for this customer is here.</p>',
                          '    <table class="steps-table">'                                                                                   ,
                          '      <thead><tr><th>Step</th><th>Milestone</th><th>State</th></tr></thead>'                                       ,
                          '      <tbody>'                                                                                                     ,
                          *steps                                                                                                              ,
                          '      </tbody>'                                                                                                    ,
                          '    </table>'                                                                                                      ,
                          '    <h2>The follow-up log</h2>'                                                                                    ,
                          '    <p>Each follow-up asks three things: what they did, what got in the way, and what is next. Newest first. '
                          'The record here is the summary; anything private stays with the lead.</p>'                                        ,
                          follow_table                                                                                                        ,
                          '    <p class="note"><strong>What is not on this page.</strong> No contact details, no private notes, nothing the customer did not agree to show. '
                          'The source is <code>data/customers.json</code>; a change to it is a release, so the history of this page is the history of the repository.</p>',
                          '  </main>'                                                                                                         ,
                          '  <!-- rm-customers:footer:start -->'                                                                              ,
                          '  <!-- rm-customers:footer:end -->'                                                                                ,
                          '</body>'                                                                                                           ,
                          '</html>'                                                                                                           ,
                          ''                                                                                                                  ])

    # ── run ────────────────────────────────────────────────────────────────────

    def write_page(self, customer, changed):
        target = CUSTOMERS_DIR / customer['id'] / 'index.html'
        text   = self.customer_page(customer)
        text   = self.pages.keep_chrome(target, text)
        if self.pages.write_if_changed(target, text, self.check):
            changed.append(target.relative_to(ROOT).as_posix())

    def run(self):
        changed = []
        wanted  = {CUSTOMERS_DIR / c['id'] / 'index.html' for c in self.customers}
        for stale in CUSTOMERS_DIR.glob('*/index.html'):
            if stale not in wanted:
                raise SystemExit(f'{stale.relative_to(ROOT)}: no record in data/customers.json; remove the folder or add the record')
        for customer in self.customers:
            self.write_page(customer, changed)
        for page, block, body in ((CUSTOMERS_DIR / 'index.html', 'customers' , self.batch_table_html()),
                                  (ROOT / 'milestones' / 'index.html', 'milestones', self.steps_html()),
                                  (ROOT / 'programme' / 'index.html', 'counts', self.counts_html())):
            text        = page.read_text(encoding='utf-8')
            text, found = self.pages.replace_block(text, block, body)
            if not found:
                raise SystemExit(f'{page.relative_to(ROOT)} has no rm-customers:{block} block')
            if self.pages.write_if_changed(page, text, self.check):
                changed.append(page.relative_to(ROOT).as_posix())
        return changed


if __name__ == '__main__':
    check   = '--check' in sys.argv
    changed = Gen__Customers(check=check).run()
    verb    = 'stale' if check else 'updated'
    for name in changed:
        print(f'  customers {verb}: {name}')
    if check and changed:
        print(f'gen_customers --check: {len(changed)} file(s) out of date; run python3 admin/build/gen_customers.py')
        sys.exit(1)
    print(f'gen_customers: {len(changed)} file(s) {verb}')
