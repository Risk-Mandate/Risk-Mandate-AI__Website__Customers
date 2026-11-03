# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Present
# The talk holds together: every slide beat has its slide, every embed and live
# frame is on a host the content security policy frames, the 20-minute version
# names only real beats, the pages are current, and only the pages that frame
# something are allowed to.
# ═══════════════════════════════════════════════════════════════════════════════

import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from chrome      import FRAME_HOSTS                                               # noqa: E402
from gen_present import Gen__Present, CORE20                                      # noqa: E402


class Test__Present(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.gen   = Gen__Present(check=True)
        cls.beats = cls.gen.talk['beats']

    def test_the_pages_are_current(self):
        self.assertEqual(self.gen.run(), [])

    def test_every_slide_beat_has_its_slide(self):
        for b in self.beats:
            if b['kind'] == 'slide':
                with self.subTest(beat=b['id']):
                    self.assertIn(b['id'], self.gen.slides)

    def test_every_frame_is_on_a_framed_host(self):
        srcs  = [b['embed']['src'] for b in self.beats if b['kind'] == 'embed']
        srcs += [b['frame']['src'] for b in self.beats if b.get('frame')]
        srcs += [a['src'] for a in self.gen.anims['extra']]
        self.assertTrue(srcs)
        for s in srcs:
            with self.subTest(src=s):
                self.assertTrue(s.startswith(FRAME_HOSTS))

    def test_the_twenty_minute_version_names_real_beats_in_order(self):
        ids = [b['id'] for b in self.beats]
        self.assertTrue(set(CORE20) <= set(ids))
        self.assertEqual(list(CORE20), [i for i in ids if i in CORE20])

    def test_the_counts_on_the_evidence_slide_are_filled(self):
        self.assertNotIn('{{', self.gen.slides['evidence'])

    def test_only_pages_that_frame_something_allow_frames(self):
        for page in ROOT.glob('**/index.html'):
            if '.git' in page.parts or 'node_modules' in page.parts:
                continue
            text   = page.read_text(encoding='utf-8')
            allows = 'frame-src' in text
            needs  = 'data-frame=' in text or 'data-boot=' in text
            with self.subTest(page=str(page.relative_to(ROOT))):
                self.assertEqual(allows, needs)
