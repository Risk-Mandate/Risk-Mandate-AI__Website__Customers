# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Runs
# The runs of browser agents hold together: every step has its screenshot and
# its section, every answer says whether it matched, every finding leads to a
# proposal in the register, the pages are current, and the brief asks for the
# fields the replays read.
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from gen_runs import Gen__Runs, RUNS                                              # noqa: E402


class Test__Runs(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gen      = Gen__Runs(check=True)
        cls.register = {p['id'] for p in json.loads((ROOT / 'data' / 'feedback' / 'proposals.json').read_text(encoding='utf-8'))['proposals']}

    def test_the_pages_are_current(self):
        self.assertEqual(self.gen.run(), [])

    def test_every_finding_leads_to_a_proposal_in_the_register(self):
        for rid, run in self.gen.runs.items():
            for f in run['findings']:
                with self.subTest(run=rid, finding=f['n']):
                    self.assertTrue(f['proposals'])
                    self.assertLessEqual(set(f['proposals']), self.register)

    def test_every_answer_has_what_the_page_said_or_says_it_was_not_on_the_page(self):
        for rid, run in self.gen.runs.items():
            for s in run['steps']:
                if s['real']:
                    with self.subTest(run=rid, step=s['n']):
                        self.assertIn(s['matched'], ('yes', 'partly', 'no', 'extra'))
                        self.assertTrue(s['expected'])

    def test_the_replay_has_a_screenshot_and_a_note_for_every_step(self):
        page = (ROOT / 'feedback' / 'runs' / 'C1' / 'index.html').read_text(encoding='utf-8')
        full = re.search(r'<figure class="replay" id="rp-full".*?</figure>', page, re.S).group(0)
        n    = len(self.gen.runs['C1']['steps'])
        self.assertEqual(full.count('<li data-n='), 2 * n)                       # a screenshot and a note each

    def test_the_brief_asks_for_the_fields_the_replays_read(self):
        brief = (ROOT / 'feedback' / 'runs' / 'brief.txt').read_text(encoding='utf-8')
        for field in ('"shot"', '"section"', '"place"', '"where"', '"title"', '"saw"', '"expected"', '"real"', '"matched"', '"findings"', '"expect"', '"thought"'):
            with self.subTest(field=field):
                self.assertIn(field, brief)

    def test_every_run_is_marked_invented(self):
        for rid in RUNS:
            page = (ROOT / 'feedback' / 'runs' / rid / 'index.html').read_text(encoding='utf-8')
            self.assertIn('An invented user, a real run.', page)
