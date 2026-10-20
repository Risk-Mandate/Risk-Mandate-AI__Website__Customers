# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Converters
# The two converters on the constructs the site uses: html_to_md for the twins
# and md_to_html for the documents; and the real documents render every
# heading with no raw markdown table rows left behind.
# ═══════════════════════════════════════════════════════════════════════════════

import re
import sys

from pathlib  import Path
from unittest import TestCase

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'admin' / 'build'))

from html_to_md import Html__To__Markdown                                          # noqa: E402
from md_to_html import Markdown__To__Html                                          # noqa: E402


class Test__Html__To__Md(TestCase):

    def convert(self, fragment):
        return Html__To__Markdown.convert(fragment)

    def test_headings_and_paragraphs(self):
        md = self.convert('<h1>Title</h1><p>One <strong>bold</strong> and <em>soft</em>.</p><h2>Next</h2>')
        self.assertEqual(md, '# Title\n\nOne **bold** and *soft*.\n\n## Next\n')

    def test_links_point_at_twins(self):
        md = self.convert('<p><a href="/admin/versions.html">v</a> <a href="/admin/">a</a> <a href="https://riskmandate.ai/x.html">x</a> <a href="/llms.txt">l</a></p>')
        self.assertEqual(md, '[v](/admin/versions.md) [a](/admin/index.md) [x](https://riskmandate.ai/x.html) [l](/llms.txt)\n')

    def test_table(self):
        md = self.convert('<table><thead><tr><th>A</th><th>B</th></tr></thead><tbody><tr><td>1</td><td>x | y</td></tr></tbody></table>')
        self.assertEqual(md, '| A | B |\n|---|---|\n| 1 | x \\| y |\n')

    def test_definition_list(self):
        md = self.convert('<dl class="kv"><dt>Started</dt><dd>2026-10-20</dd></dl>')
        self.assertIn('**Started**', md)
        self.assertIn('2026-10-20', md)


class Test__Md__To__Html(TestCase):

    def render(self, markdown):
        return Markdown__To__Html().render(markdown)

    def test_headings_get_github_ids(self):
        out = self.render('# A title\n\n## Customers, not beta users')
        self.assertIn('<h1 id="a-title">A title</h1>', out)
        self.assertIn('<h2 id="customers-not-beta-users">', out)

    def test_table(self):
        out = self.render('| A | B |\n|---|---|\n| 1 | `x` |')
        self.assertIn('<thead><tr><th>A</th><th>B</th></tr></thead>', out)
        self.assertIn('<tr><td>1</td><td><code>x</code></td></tr>', out)

    def test_html_is_escaped(self):
        out = self.render('a <script>alert(1)</script>')
        self.assertNotIn('<script>', out)

    def test_real_documents_render_every_heading_and_table(self):
        for path in sorted(list((ROOT / 'docs').rglob('*.md')) + list((ROOT / 'team').rglob('*.md'))):
            if 'memos' in path.parts:
                continue
            text = path.read_text(encoding='utf-8')
            out  = self.render(text)
            with self.subTest(document=path.relative_to(ROOT).as_posix()):
                headings = len(re.findall(r'^#{1,6}\s', re.sub(r'```[\s\S]*?```', '', text), re.M))   # a fenced block is not a heading
                self.assertEqual(len(re.findall(r'<h[1-6] id=', out)), headings)
                self.assertNotRegex(out, r'^\|.*\|$', 'a markdown table row survived unrendered')
