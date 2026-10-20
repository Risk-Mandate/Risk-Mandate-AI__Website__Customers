# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Customers__Data
# The customer records: the shape the generator demands, the example marked as
# such, no contact details anywhere, every step of the ladder on every record,
# and the counts on the home page equal to what the data says.
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from gen_customers import Gen__Customers, RE_CONTACT                             # noqa: E402


class Test__Customers__Data(TestCase):

    def setUp(self):
        self.gen = Gen__Customers(check=True)                                     # validates on construction

    def test_the_example_is_marked(self):
        examples = [c for c in self.gen.customers if c['kind'] == 'example']
        self.assertEqual(len(examples), 1)
        self.assertEqual(examples[0]['status'], 'example')
        self.assertIn('not a customer', examples[0]['handle'])

    def test_no_contact_details(self):
        text = (ROOT / 'data' / 'customers.json').read_text(encoding='utf-8')
        self.assertIsNone(RE_CONTACT.search(text))
        self.assertIsNotNone(RE_CONTACT.search('write to someone@example.com'))  # the pattern itself works
        self.assertIsNotNone(RE_CONTACT.search('call +44 20 7946 0000 now'))

    def test_every_record_carries_every_step(self):
        for customer in self.gen.customers:
            self.assertEqual(sorted(customer['milestones']), sorted(self.gen.step_ids))

    def test_counts_on_the_home_page_are_the_data(self):
        counts = self.gen.counts()
        home   = (ROOT / 'index.html').read_text(encoding='utf-8')
        self.assertIn(f'<b>{counts["customers"]}</b><span>customers in the first batch</span>', home)
        self.assertIn(f'<b>{counts["steps_done"]} of {counts["steps_total"]}</b>', home)

    def test_every_record_has_a_page_and_no_page_lacks_a_record(self):
        ids     = {c['id'] for c in self.gen.customers}
        folders = {p.parent.name for p in (ROOT / 'customers').glob('*/index.html')}
        self.assertEqual(ids, folders)

    def test_validation_rejects_a_bad_record(self):
        gen   = Gen__Customers(check=True)
        bad   = json.loads(json.dumps(gen.customers[0]))
        bad['handle'] = 'Someone, reach them at someone@example.com'
        gen.customers = [bad]
        with self.assertRaises(SystemExit):
            gen.validate()
