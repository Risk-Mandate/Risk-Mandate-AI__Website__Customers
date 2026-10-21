# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Storyboards
# The storyboard kit's delay attributes, the only inline styles the content
# security policy allows, are exactly what JavaScript prints (checked against
# node itself); every storyboard page loads the kit with its integrity and
# carries the viewer as a template and the panels as text; every bundle is
# the storyboard, its cast and the security pack; every demo is on a page.
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re
import subprocess
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from chrome import KIT, Pins, CSP, CSP_STORYBOARD                               # noqa: E402
from pages  import Site__Pages                                                  # noqa: E402


class Test__Storyboards(TestCase):

    def test_delays_are_what_javascript_prints(self):
        d      = KIT['style_delays']
        script = ('const out = ' + json.dumps(d['fixed']) + ';'
                  f'for (const [a, b] of {json.dumps(d["families"])}) for (let i = 0; i < {d["count"]}; i++) {{ const v = "--d:" + (a + i * b) + "s"; if (!out.includes(v)) out.push(v) }}'
                  'console.log(JSON.stringify(out))')
        node   = json.loads(subprocess.run(['node', '-e', script], capture_output=True, text=True, check=True).stdout)
        self.assertEqual(Pins.style_delays(), node)

    def test_only_storyboard_pages_allow_the_kit(self):
        self.assertNotIn('unsafe-hashes', CSP)
        self.assertNotIn(KIT['api']['host'], CSP)
        self.assertIn("'unsafe-hashes'", CSP_STORYBOARD)
        self.assertNotIn("'unsafe-inline'", CSP_STORYBOARD)

    def test_storyboard_pages(self):
        pages = [p for p in Site__Pages().html_files() if 'data-sb-bundle=' in p.read_text(encoding='utf-8')]
        self.assertGreaterEqual(len(pages), 3)
        for path in pages:
            text = path.read_text(encoding='utf-8')
            with self.subTest(page=path.relative_to(ROOT).as_posix()):
                for script in KIT['api']['scripts']:
                    url, sri = Pins.kit(script)
                    self.assertIn(f'<script src="{url}" integrity="{sri}" crossorigin="anonymous"></script>', text)
                self.assertIn('<template class="sb-template"><div class="sb-viewer">', text)
                self.assertIn('<details class="sb-text">', text)
                bundle = re.search(r'data-sb-bundle="([^"]+)"', text).group(1)
                self.assertTrue((ROOT / bundle.lstrip('/')).exists(), bundle)

    def test_bundles(self):
        cast = json.loads((ROOT / 'storyboards' / 'cast.json').read_text(encoding='utf-8'))
        for path in sorted((ROOT / 'storyboards').glob('*/bundle.json')):
            bundle = json.loads(path.read_text(encoding='utf-8'))
            board  = json.loads((path.parent / 'storyboard.json').read_text(encoding='utf-8'))
            with self.subTest(bundle=path.parent.name):
                self.assertEqual(bundle['storyboard'], board)
                self.assertEqual(bundle['cast'], cast)
                self.assertEqual(bundle['packs'], ['security'])

    def test_every_demo_is_on_a_page(self):
        demos = {d['id'] for d in json.loads((ROOT / 'data' / 'demos.json').read_text(encoding='utf-8'))['demos']}
        used  = set()
        for path in Site__Pages().html_files():
            used |= set(re.findall(r'data-demo="([^"]+)"', path.read_text(encoding='utf-8')))
        self.assertEqual(demos - used, set(), 'a demo nobody can see')
