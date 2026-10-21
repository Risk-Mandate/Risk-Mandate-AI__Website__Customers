# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Examples
# The examples a customer tries first: each goes in three acts, asks what it
# says it asks, has a version and the questions under it; and the pages a
# customer reads first install nothing and mention no hook (R002: web first).
# ═══════════════════════════════════════════════════════════════════════════════

import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from gen_examples import Gen__Examples                                            # noqa: E402

FRONT = ('index.html', 'start-here/index.html', 'examples/index.html')


def main_of(path):
    text = (ROOT / path).read_text(encoding='utf-8')
    return re.search(r'<main\b[^>]*>(.*?)</main>', text, re.S).group(1)


class Test__Examples(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gen = Gen__Examples(check=True)

    def test_the_pages_are_current(self):
        self.assertEqual(self.gen.run(), [])

    def test_every_example_has_its_page_its_questions_and_its_version(self):
        for ex in self.gen.examples:
            with self.subTest(example=ex['slug']):
                page = (ROOT / 'examples' / ex['slug'] / 'index.html').read_text(encoding='utf-8')
                self.assertIn(f'data-quiz="{ex["slug"]}"', page)
                self.assertIn(f'version {ex["version"]}', page)
                self.assertIn('class="demo chat-frame', page)

    def test_the_line_is_pasted_in_act_two_and_first_in_act_three(self):
        for ex in self.gen.examples:
            with self.subTest(example=ex['slug']):
                kinds = [k for k, _ in ex['transcript']]
                acts  = [i for i, k in enumerate(kinds) if k == 'act']
                two   = [t for k, t in ex['transcript'][acts[1]:acts[2]] if k == 'user']
                three = [t for k, t in ex['transcript'][acts[2]:] if k == 'user']
                self.assertEqual(two[0], '{line}')
                self.assertIn('{line}', three[0])
                self.assertIn('new', kinds[acts[2]:])

    def test_the_front_pages_mention_no_hook_and_install_nothing(self):
        for path in FRONT:
            with self.subTest(page=path):
                main  = re.sub(r'<section class="[^"]*\breviews-band\b.*?</section>', ' ', main_of(path), flags=re.S)   # the reviews' own titles, which record why the hooks went
                prose = re.sub(r'<[^>]+>', ' ', main)
                self.assertNotRegex(prose, r'(?i)\bhooks?\b')
                self.assertNotIn('.claude/', prose)

    def test_every_tab_has_its_panel(self):
        home = main_of('index.html')
        for ex in self.gen.examples:
            with self.subTest(example=ex['slug']):
                self.assertIn(f'href="#ex-home-{ex["slug"]}"', home)
                self.assertIn(f'id="ex-home-{ex["slug"]}"', home)
