# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Feedback
# The reviews, the synthetic study and the register hold together: a reviewer's
# quote is word for word in the memo, every proposal has a decision and a reason
# and something that led to it, every invented user's finding is checked once,
# and the words kept as given are the only words the house check leaves alone.
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re
import subprocess
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from gen_feedback import Gen__Feedback, webp_size, squash                        # noqa: E402


class Test__Feedback(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gen = Gen__Feedback(check=True)

    def test_the_pages_are_current(self):
        self.assertEqual(self.gen.run(), [])

    def test_every_quote_is_word_for_word_in_its_memo(self):
        for review in self.gen.reviews:
            memo = squash(review['memo_text'])
            for point in review['points']:
                with self.subTest(point=point['id']):
                    self.assertIn(squash(point['quote']), memo)

    def test_every_proposal_has_a_reason_and_a_source(self):
        for p in self.gen.register['proposals']:
            with self.subTest(proposal=p['id']):
                self.assertTrue(p['reason'].strip())
                self.assertTrue(self.gen.sources_of(p['id']))
                if p['decision'] in ('done', 'reversed'):
                    self.assertRegex(p['version'], r'^\d+\.\d+\.\d+$')

    def test_a_done_proposal_is_not_from_the_future(self):
        version = (ROOT / 'admin' / 'build' / 'version.txt').read_text().strip()
        released = [r['version'] for r in json.loads((ROOT / 'data' / 'versions.json').read_text())['releases']]
        for p in self.gen.register['proposals']:
            if p['decision'] in ('done', 'reversed'):
                with self.subTest(proposal=p['id']):
                    self.assertTrue(p['version'] in released or p['version'] == version)

    def test_every_finding_is_checked_once(self):
        for who, run in self.gen.runs.items():
            with self.subTest(run=who):
                found = sorted(c['finding'] for c in self.gen.checks['checks'] if c['run'] == who)
                self.assertEqual(found, list(range(len(run['findings']))))

    def test_every_journey_was_written_for_a_persona(self):
        self.assertEqual(set(self.gen.journeys), {p['id'] for p in self.gen.personas['personas']})

    def test_every_persona_is_marked_invented(self):
        for p in self.gen.personas['personas']:
            self.assertIs(p['invented'], True)

    def test_every_study_page_says_invented(self):
        for page in (ROOT / 'feedback' / 'synthetic').rglob('index.html'):
            with self.subTest(page=page.relative_to(ROOT).as_posix()):
                self.assertIn('Invented, not user research.', page.read_text(encoding='utf-8'))

    def test_webp_sizes_are_read_from_the_header(self):
        for shot in (ROOT / 'assets' / 'feedback').rglob('*.webp'):
            w, h = webp_size(shot)
            self.assertTrue(100 < w < 4000 and 20 < h < 4000, shot)                     # a header strip is short

    def test_the_house_check_leaves_only_kept_words_alone(self):
        script = ("const v = require('./admin/build/validate.js');"
                  "const kept = '<blockquote class=\"verbatim\"><p>what the policy is doing</p></blockquote>';"
                  "const ours = '<p>what the policy is doing</p>';"
                  "console.log(JSON.stringify([v.wordProblems('a.html', kept).length, v.wordProblems('a.html', ours).length]))")
        out = subprocess.run(['node', '-e', script], cwd=ROOT, capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(out.stdout.strip().splitlines()[-1]), [0, 1])

    def test_no_contact_details_in_the_feedback_data(self):
        contact = re.compile(r'[\w.+-]+@[\w-]+\.[\w.-]+|https?://(?:www\.)?linkedin\.com')
        for path in (ROOT / 'data' / 'feedback').rglob('*'):
            if path.is_file() and path.suffix in ('.json', '.txt'):
                with self.subTest(path=path.relative_to(ROOT).as_posix()):
                    self.assertEqual([m for m in contact.findall(path.read_text(encoding='utf-8')) if m != 'agent@riskmandate.ai'], [])
