# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Themes
# The six themes: data/themes.json, assets/theme.js and assets/themes.css name
# the same ones; every theme block defines every token the default defines; no
# colour is written outside assets/themes.css; every swatch exists; and the
# pairs a reader reads hold their contrast in every theme (WCAG 2: 4.5:1 for
# text, 3:1 for large text and for the controls and chips).
# ═══════════════════════════════════════════════════════════════════════════════

import json
import re

from pathlib  import Path
from unittest import TestCase

ROOT      = Path(__file__).resolve().parents[2]
THEMES    = json.loads((ROOT / 'data' / 'themes.json').read_text(encoding='utf-8'))
CSS       = (ROOT / 'assets' / 'themes.css').read_text(encoding='utf-8')
JS        = (ROOT / 'assets' / 'theme.js').read_text(encoding='utf-8')
RE_BLOCK  = re.compile(r':root\[data-theme="([a-z]+)"\]\s*\{(.*?)\}', re.S)
RE_TOKEN  = re.compile(r'(--rm-[a-z0-9-]+)\s*:\s*([^;]+);')
RE_COLOUR = re.compile(r'(?<!&)#[0-9A-Fa-f]{3,8}\b|\brgba?\(|\bhsla?\(')      # &#9662; is a character, not a colour

TEXT      = 4.5
LARGE     = 3.0
PAIRS     = (('--rm-chat-c-text', '--rm-chat-c-bg', TEXT),                          # the Claude-style and ChatGPT-style chat frames, the same in every theme
             ('--rm-chat-c-text', '--rm-chat-c-user', TEXT),
             ('--rm-chat-c-muted', '--rm-chat-c-bg', TEXT),
             ('--rm-chat-g-text', '--rm-chat-g-bg', TEXT),
             ('--rm-chat-g-text', '--rm-chat-g-user', TEXT),
             ('--rm-chat-g-muted', '--rm-chat-g-bg', TEXT),
             ('--rm-chat-policy', '--rm-chat-policy-bg', TEXT),
             ('--rm-chat-tool', '--rm-chat-tool-bg', TEXT),
             ('--rm-chat-on-send', '--rm-chat-c-send', LARGE),
             ('--rm-text'      , '--rm-bg'      , TEXT ),                          # body text and headings
             ('--rm-text'      , '--rm-card'    , TEXT ),
             ('--rm-text'      , '--rm-bg-2'    , TEXT ),
             ('--rm-muted'     , '--rm-bg'      , TEXT ),                          # secondary text, the crumbs
             ('--rm-muted'     , '--rm-card'    , TEXT ),
             ('--rm-muted'     , '--rm-bg-2'    , TEXT ),
             ('--rm-faint'     , '--rm-bg'      , LARGE),                          # labels only, never a sentence
             ('--rm-accent'    , '--rm-bg'      , TEXT ),                          # links
             ('--rm-accent'    , '--rm-card'    , TEXT ),
             ('--rm-accent'    , '--rm-bg-2'    , TEXT ),
             ('--rm-accent'    , '--rm-accent-bg', TEXT),                          # the current entry in a menu
             ('--rm-on-accent' , '--rm-accent'  , TEXT ),                          # a button
             ('--rm-warn'      , '--rm-warn-bg' , TEXT ),
             ('--rm-fg'        , '--rm-canvas'  , TEXT ),                          # the hero and the footer
             ('--rm-fg-2'      , '--rm-canvas'  , TEXT ),
             ('--rm-band-accent', '--rm-canvas' , LARGE),                          # the hero's accent words, 34px and up
             ('--rm-on-status' , '--rm-status-shipped' , TEXT),                    # the reality chips
             ('--rm-on-status' , '--rm-status-proposed', TEXT),
             ('--rm-on-status' , '--rm-status-absent'  , TEXT),
             ('--rm-step-done' , '--rm-bg'      , TEXT ),                          # the step states, as text
             ('--rm-step-progress', '--rm-bg'   , TEXT ),
             ('--rm-term-fg'   , '--rm-term-bg' , TEXT ),                          # the demo's terminal
             ('--rm-term-dim'  , '--rm-term-bg' , TEXT ),
             ('--rm-term-green', '--rm-term-bg' , TEXT ),
             ('--rm-term-red'  , '--rm-term-bg' , TEXT ),
             ('--rm-term-amber', '--rm-term-bg' , TEXT ),
             ('--rm-term-blue' , '--rm-term-bg' , TEXT ))


def blocks():
    found = {name: dict(RE_TOKEN.findall(body)) for name, body in RE_BLOCK.findall(CSS)}
    return found


def rgb(value):
    value = value.strip()
    match = re.fullmatch(r'#([0-9A-Fa-f]{6})', value)
    if not match:
        raise ValueError(f'not a six-digit hex colour: {value}')
    return tuple(int(match.group(1)[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(colour):
    channel = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in colour)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    la, lb = sorted((luminance(rgb(a)), luminance(rgb(b))), reverse=True)
    return (la + 0.05) / (lb + 0.05)


class Test__Themes(TestCase):

    def test_the_three_lists_agree(self):
        ids = [t['id'] for t in THEMES['themes']]
        self.assertEqual(ids, list(blocks()))                                       # the CSS blocks, in the same order
        js  = re.findall(r'^\s+([a-z]+)\s*:\s*\'', JS.split('Object.freeze({', 1)[1].split('})', 1)[0], re.M)
        self.assertEqual(ids, js)
        self.assertIn(f"const KEY     = '{THEMES['storageKey']}'", JS)
        self.assertIn(f"const LIGHT   = '{THEMES['default']}'", JS)
        self.assertIn(f"const DARK    = '{THEMES['whenPreferringDark']}'", JS)
        self.assertEqual(ids[0], THEMES['default'])

    def test_the_default_is_also_the_unthemed_root(self):
        self.assertIn(f':root,\n:root[data-theme="{THEMES["default"]}"]', CSS)

    def test_every_theme_defines_every_token(self):
        found   = blocks()
        default = set(found[THEMES['default']])
        for name, tokens in found.items():
            with self.subTest(theme=name):
                self.assertEqual(set(tokens), default, f'{name} is missing {sorted(default - set(tokens))} or adds {sorted(set(tokens) - default)}')

    def test_every_token_the_stylesheet_reads_is_defined(self):
        site    = (ROOT / 'assets' / 'site.css').read_text(encoding='utf-8')
        used    = set(re.findall(r'var\((--rm-[a-z0-9-]+)', site))
        local   = set(re.findall(r'(--rm-[a-z0-9-]+)\s*:', site))
        default = set(blocks()[THEMES['default']])
        self.assertEqual(used - local - default, set())

    def test_no_colour_outside_themes_css(self):
        for path in [ROOT / 'assets' / 'site.css', ROOT / 'assets' / 'theme.js', ROOT / 'assets' / 'nav.js', *ROOT.rglob('*.html')]:
            if '_site' in path.parts:
                continue
            with self.subTest(file=path.relative_to(ROOT).as_posix()):
                text = re.sub(r'\b(?:href|id)="[^"]*"', '', path.read_text(encoding='utf-8'))   # a #fragment is a link, not a colour
                text = re.sub(r'<code\b[^>]*>.*?</code>', '', text, flags=re.S)               # a colour named in a code span is documentation, not styling
                self.assertIsNone(RE_COLOUR.search(text))

    def test_every_theme_has_a_swatch_equal_to_its_token(self):
        found = blocks()
        for theme in THEMES['themes']:
            with self.subTest(theme=theme['id']):
                swatch = re.search(rf'\.sw-{theme["id"]}\s*\{{\s*--sw:\s*(#[0-9A-Fa-f]{{6}});', CSS)
                self.assertIsNotNone(swatch)
                self.assertEqual(swatch.group(1).upper(), found[theme['id']]['--rm-swatch'].upper())

    def test_mode_matches_color_scheme(self):
        bodies = dict(RE_BLOCK.findall(CSS))
        for theme in THEMES['themes']:
            with self.subTest(theme=theme['id']):
                self.assertIn(f'color-scheme:          {theme["mode"]};', bodies[theme['id']])

    def test_contrast_in_every_theme(self):
        failures = []
        for name, tokens in blocks().items():
            for fg, bg, minimum in PAIRS:
                ratio = contrast(tokens[fg], tokens[bg])
                if ratio < minimum:
                    failures.append(f'{name}: {fg} {tokens[fg]} on {bg} {tokens[bg]} is {ratio:.2f}:1, needs {minimum}:1')
        self.assertEqual(failures, [], '\n' + '\n'.join(failures))

    def test_stylesheets_are_balanced(self):                                      # a stray brace turns the next rule into one that applies everywhere
        for path in (ROOT / 'assets').glob('*.css'):
            depth = 0
            with self.subTest(file=path.name):
                for ch in re.sub(r'/\*.*?\*/', '', path.read_text(encoding='utf-8'), flags=re.S):
                    depth += (ch == '{') - (ch == '}')
                    self.assertGreaterEqual(depth, 0)
                self.assertEqual(depth, 0)
