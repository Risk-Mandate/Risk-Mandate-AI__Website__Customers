# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Chrome__In__Every__Page
# Every HTML page on the real tree carries the generated chrome: the CSP, the
# canonical URL on the CNAME host, the version badge equal to version.txt, the
# header, the footer and a <main>; and no inline script or style.
# ═══════════════════════════════════════════════════════════════════════════════

import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from chrome import Chrome, CSP, CSP_STORYBOARD, NAV_GROUPS                                        # noqa: E402
from pages  import Site__Pages                                                    # noqa: E402


class Test__Chrome__In__Every__Page(TestCase):

    def setUp(self):
        self.chrome = Chrome()
        self.pages  = Site__Pages()
        self.files  = self.pages.html_files()

    def test_there_are_pages(self):
        self.assertGreaterEqual(len(self.files), 12)
        self.assertIn(ROOT / 'index.html', self.files)

    def test_every_page_has_the_chrome(self):
        dropdowns = sum(1 for _, _, items in NAV_GROUPS if len(items) > 1)
        for path in self.files:
            text = path.read_text(encoding='utf-8')
            with self.subTest(page=path.relative_to(ROOT).as_posix()):
                policy = CSP_STORYBOARD if 'data-sb-bundle=' in text else CSP                                    # a page with a storyboard also allows the kit
                self.assertIn(f'<meta http-equiv="Content-Security-Policy" content="{policy}">', text)
                self.assertIn('<sg-meter class="meter-nav" view="balance"></sg-meter>', text)                     # the balance in every header
                self.assertRegex(text, r'<sg-meter view="page" kind="[a-z]+" title=')                             # and the page's charge under every page
                self.assertIn(f'<link rel="canonical" href="{self.chrome.base_url}', text)
                self.assertIn('<header class="top">', text)
                self.assertIn('<footer class="foot">', text)
                self.assertRegex(text, r'<main\b')
                self.assertIn('<link rel="stylesheet" href="/assets/site.css">', text)
                self.assertIn('<script src="/assets/nav.js" defer></script>', text)
                self.assertLess(text.index('<script src="/assets/theme.js"></script>'), text.index('<link rel="stylesheet" href="/assets/themes.css">'))   # the theme is set before the first paint
                self.assertLess(text.index('<link rel="stylesheet" href="/assets/themes.css">'), text.index('<link rel="stylesheet" href="/assets/site.css">'))
                self.assertIn('<div class="theme-pick">', text)
                self.assertNotIn('stage-pill', text)
                self.assertIn('<nav class="navlinks" aria-label="Site">', text)
                self.assertIn('<button class="navtoggle"', text)
                self.assertEqual(len(re.findall(r'<span class="navgroup( active)?">', text)), dropdowns)

    def test_every_badge_equals_version_txt(self):
        for path in self.files:
            badges = re.findall(r'data-version="([^"]+)"', path.read_text(encoding='utf-8'))
            with self.subTest(page=path.relative_to(ROOT).as_posix()):
                self.assertTrue(badges)
                self.assertEqual(set(badges), {self.chrome.version})

    def test_canonical_matches_the_page_location(self):
        for path in self.files:
            page = self.pages.meta(path)
            text = path.read_text(encoding='utf-8')
            with self.subTest(page=page['url']):
                self.assertIn(f'<link rel="canonical" href="{self.chrome.canonical_url(page["url"])}">', text)
                self.assertIn(f'<meta property="og:url" content="{self.chrome.canonical_url(page["url"])}">', text)

    def test_no_inline_script_or_style(self):                                     # the CSP forbids both; a page must not depend on them
        for path in self.files:
            text = path.read_text(encoding='utf-8')
            with self.subTest(page=path.relative_to(ROOT).as_posix()):
                self.assertNotRegex(text, r'<script\b(?![^>]*\bsrc=)')
                self.assertNotIn('<style', text)
                self.assertNotRegex(text, r'\sstyle\s*=')
