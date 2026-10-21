# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Chrome
# The one definition of the site chrome: head block, the RiskMandate header
# (mark, wordmark, the sub-site name, the nav, the version chip, the parent
# link), breadcrumbs, footer, CSP and canonical URL. Every HTML page gets it
# injected between markers by gen_chrome.py, so the chrome cannot drift between
# pages. The look is riskmandate.ai's (paper surfaces, the green, the dark
# canvas); every colour lives in assets/site.css as a token and nowhere else.
# ═══════════════════════════════════════════════════════════════════════════════

import base64
import hashlib
import html
import json

from pathlib import Path


ROOT           = Path(__file__).resolve().parents[2]
VERSION_FILE   = ROOT / 'admin' / 'build' / 'version.txt'
CNAME_FILE     = ROOT / 'CNAME'
VERSIONS_FILE  = ROOT / 'data' / 'versions.json'
THEMES_FILE    = ROOT / 'data' / 'themes.json'
METER_FILE     = ROOT / 'data' / 'meter.json'
KIT_FILE       = ROOT / 'data' / 'storyboards.json'
PINS_DIR       = ROOT / 'admin' / 'build' / 'pins'

MARKER_PREFIX  = 'rm-customers'                                                  # <!-- rm-customers:<block>:start -->

SITE_NAME      = 'customers.riskmandate.ai'
SITE_ONE_LINER = ('The first customers of the Agent Behaviour Policy: an early access programme run as a site, '
                  'with a start-here page, a page per customer, credit to spend, the milestones agreed with each one, '
                  'and a daily follow-up. Part of riskmandate.ai.')
PARENT_URL     = 'https://riskmandate.ai'
PARENT_TITLE   = 'riskmandate.ai: the company and the product this programme is for'
LICENCE_URL    = 'https://creativecommons.org/licenses/by/4.0/'
LICENCE_NAME   = 'CC BY 4.0'
REPO_URL       = 'https://github.com/Risk-Mandate/Risk-Mandate-AI__Website__Customers'
AGENT_ADDRESS  = 'agent@riskmandate.ai'

METER          = json.loads(METER_FILE.read_text(encoding='utf-8'))
KIT            = json.loads(KIT_FILE.read_text(encoding='utf-8'))


class Pins:                                                                      # the two APIs this site loads code from, each pinned to one release and checked against a copy of its manifest

    @staticmethod
    def manifest(host, release):
        return json.loads((PINS_DIR / host.replace('https://', '') / release / 'manifest.json').read_text(encoding='utf-8'))

    @staticmethod
    def meter_url():
        return f"{METER['api']['host']}/{METER['api']['release']}/{METER['api']['component']}"

    @staticmethod
    def meter_integrity():                                                       # the manifest gives sha256 in hex; the integrity attribute wants base64
        files = {f['path']: f for f in Pins.manifest(METER['api']['host'], METER['api']['release'])['files']}
        return 'sha256-' + base64.b64encode(bytes.fromhex(files[METER['api']['component']]['sha256'])).decode()

    @staticmethod
    def kit(path):                                                               # (url, integrity) for one file of the storyboard kit
        files = {f['path']: f for f in Pins.manifest(KIT['api']['host'], KIT['api']['release'])['files']}
        return f"{KIT['api']['host']}/{KIT['api']['release']}/{path}", files[path]['integrity']

    @staticmethod
    def js_number(x):                                                            # a number as JavaScript prints it: the shortest repr, and no ".0" on a whole number
        return str(int(x)) if float(x).is_integer() else repr(float(x))

    @staticmethod
    def style_delays():                                                          # the exact inline style values the kit writes, computed with the same float arithmetic
        d      = KIT['style_delays']
        values = list(d['fixed'])
        for start, step in d['families']:
            for i in range(d['count']):
                value = f"--d:{Pins.js_number(start + i * step)}s"
                if value not in values:
                    values.append(value)
        return values

    @staticmethod
    def style_hashes():
        return ["'sha256-" + base64.b64encode(hashlib.sha256(v.encode()).digest()).decode() + "'" for v in Pins.style_delays()]


def csp(storyboard=False):                                                       # one policy; a page with a storyboard also allows the kit's stylesheets, fonts and delay attributes
    style = f"style-src 'self' {KIT['api']['host']} 'unsafe-hashes' {' '.join(Pins.style_hashes())}; font-src {KIT['api']['host']}; " if storyboard else "style-src 'self'; "
    kit   = f" {KIT['api']['host']}" if storyboard else ''
    return ("default-src 'self'; "
            f"connect-src 'self' {METER['api']['host']}; "                         # the meter fetches its markup and styles from beside itself
            "img-src 'self' data:; "
            + style +
            f"script-src 'self' {METER['api']['host']}{kit}; "
            "object-src 'none'; "
            "base-uri 'none'; "
            "form-action 'none'")                                                 # no form on this site yet; the next-batch page says where the form is


CSP            = csp()
CSP_STORYBOARD = csp(storyboard=True)

# Each group: (label, the group's own page, [(href, label), ...]). A group label is a
# plain link to its first page, so the nav works with no JavaScript at all.
NAV_GROUPS     = (('Start here'   , '/start-here/' , (('/start-here/'                                   , 'Your first five minutes'          ),
                                                      ('/account/'                                      , 'Your account: £50 to spend'       ),
                                                      ('/credit/'                                       , 'What each page costs'             ))),
                  ('Policies'     , '/policies/'   , (('/policies/'                                     , 'Pick one worry: every policy'     ),
                                                      ('/policies/starter/'                             , 'The starter pack: four in one go' ),
                                                      ('/policies/touch-your-secrets/'                  , 'Keep it away from your secrets'   ),
                                                      ('/policies/push-anywhere/'                       , 'Only push to your branch'         ),
                                                      ('/policies/send-as-you/'                         , 'ChatGPT: nothing sent without a yes'))),
                  ('Learn'        , '/what-is-an-abp/', (('/what-is-an-abp/'                            , 'What an ABP is'                   ),
                                                      ('/storyboards/'                                  , 'Storyboards'                      ),
                                                      ('/storyboards/your-first-policy/'                , 'Your first policy, drawn'         ))),
                  ('The programme', '/programme/'  , (('/programme/'                                    , 'Customers, not beta users'        ),
                                                      ('/customers/'                                    , 'The first batch'                  ),
                                                      ('/milestones/'                                   , 'The milestones: seven steps'      ),
                                                      ('/follow-up/'                                    , 'The daily follow-up'              ),
                                                      ('/learning/'                                     , 'What we want to discover'         ),
                                                      ('/next-batch/'                                   , 'The next batch'                   ),
                                                      ('/storyboards/the-first-batch/'                  , 'The first batch, drawn'           ))),
                  ('Docs'         , '/docs/'       , (('/docs/'                                         , 'All documents'                    ),
                                                      ('/docs/brief/our-first-customers.html'           , 'The brief, in full'               ),
                                                      ('/docs/brief/memo-2026-10-20-user-onboarding-plan.html', 'The memo of 20 October'    ),
                                                      ('/docs/brief/BRIEF-CORRECTIONS.html'             , 'Brief corrections'                ),
                                                      ('/docs/reality.html'                             , 'Reality: what exists'             ),
                                                      ('/docs/ops/'                                     , 'Operations'                       ),
                                                      ('/team/'                                         , 'The team'                         ),
                                                      ('/admin/'                                        , 'How the site is built'            ),
                                                      ('/admin/versions.html'                           , 'Release history'                  ),
                                                      ('/review/'                                       , 'The review folder'                ),
                                                      ('/llms.txt'                                      , 'llms.txt, for agents'             ))))

CRUMB_FOLDERS  = {'/docs/'        : ('Docs'       , '/docs/'       ),
                  '/docs/brief/'  : ('The brief'  , '/docs/brief/' ),
                  '/docs/ops/'    : ('Operations' , '/docs/ops/'   ),
                  '/team/'        : ('The team'   , '/team/'       ),
                  '/team/roles/'  : ('Roles'      , '/team/'       ),
                  '/customers/'   : ('Customers'  , '/customers/'  ),
                  '/about/'       : ('About'      , '/about/participant.html'),
                  '/review/'      : ('Review'     , '/review/'     ),
                  '/admin/'       : ('Admin'      , '/admin/'      ),
                  '/policies/'    : ('Policies'   , '/policies/'   ),
                  '/storyboards/' : ('Storyboards', '/storyboards/'),
                  '/account/'     : ('Your account', '/account/'   )}


class Chrome:

    def __init__(self):
        self.version  = VERSION_FILE.read_text(encoding='utf-8').strip()
        self.host     = CNAME_FILE.read_text(encoding='utf-8').strip()
        self.base_url = f'https://{self.host}'
        self.released = self.release_date()
        self.labels   = {href: label for _, _, items in NAV_GROUPS for href, label in items}
        self.themes   = json.loads(THEMES_FILE.read_text(encoding='utf-8'))

    def release_date(self):
        releases = json.loads(VERSIONS_FILE.read_text(encoding='utf-8'))['releases']
        for release in releases:
            if release['version'] == self.version:
                return release['date']
        raise SystemExit(f'data/versions.json has no entry for version {self.version}')

    def marker(self, block, edge):
        return f'<!-- {MARKER_PREFIX}:{block}:{edge} -->'

    def canonical_url(self, url_path):
        return self.base_url + url_path

    def twin_path(self, url_path):
        if url_path.endswith('/'):
            return url_path + 'index.md'
        return url_path[:-len('.html')] + '.md'

    # ── head ──────────────────────────────────────────────────────────────────

    def kind_of(self, url_path):                                                 # the meter's price class for a page, from data/meter.json's path rules, longest first
        path = url_path if not url_path.endswith('/') else url_path + 'index.html'
        for prefix, kind in sorted(METER['paths'], key=lambda rule: -len(rule[0])):
            if path == prefix or path.startswith(prefix if prefix.endswith('/') else prefix + '\0'):
                return kind
        return 'page'

    def head(self, url_path, title, description, storyboard=False):
        canonical = self.canonical_url(url_path)
        twin      = self.twin_path(url_path)
        esc       = html.escape
        kit_css   = [Pins.kit(path) for path in KIT['api']['styles']] if storyboard else []
        lines     = [f'<meta http-equiv="Content-Security-Policy" content="{CSP_STORYBOARD if storyboard else CSP}">',
                     f'<link rel="canonical" href="{canonical}">'                                         ,
                     f'<link rel="alternate" type="text/markdown" href="{twin}">'                        ,
                     f'<link rel="license" href="{LICENCE_URL}">'                                         ,
                     f'<link rel="icon" href="/assets/brand/riskmandate-favicon-32.png" sizes="32x32">'  ,
                     f'<link rel="icon" href="/assets/brand/riskmandate-mark.svg" type="image/svg+xml">' ,
                     f'<script src="/assets/site-config.js"></script>'                                   ,   # the meter's config and the storyboard viewer's key, before anything reads them
                     f'<script src="/assets/theme.js"></script>'                                         ,   # before the stylesheets, so the theme is set before the first paint
                     f'<link rel="stylesheet" href="/assets/themes.css">'                                 ,
                     f'<link rel="stylesheet" href="/assets/site.css">'                                   ,
                     *[f'<link rel="stylesheet" href="{url}" integrity="{sri}" crossorigin="anonymous">' for url, sri in kit_css],
                     f'<script src="/assets/nav.js" defer></script>'                                      ,
                     f'<script src="/assets/copy.js" defer></script>'                                     ,
                     f'<script src="/assets/demo.js" defer></script>'                                     ,
                     f'<script type="module" src="{Pins.meter_url()}" integrity="{Pins.meter_integrity()}" crossorigin="anonymous"></script>',
                     f'<meta property="og:type" content="website">'                                       ,
                     f'<meta property="og:site_name" content="RiskMandate">'                             ,
                     f'<meta property="og:url" content="{canonical}">'                                    ,
                     f'<meta property="og:title" content="{esc(title)}">'                                 ,
                     f'<meta property="og:description" content="{esc(description)}">'                     ,
                     f'<meta name="{MARKER_PREFIX}:version" content="{self.version}">'                    ,
                     f'<meta name="{MARKER_PREFIX}:released" content="{self.released}">'                  ]
        return '\n'.join('  ' + line for line in lines)

    # ── nav ───────────────────────────────────────────────────────────────────

    def version_badge(self):
        return (f'<a class="version" href="/admin/versions.html" '
                f'data-version="{self.version}" title="released {self.released}; what shipped in v{self.version}">v{self.version}</a>')

    def group_is_here(self, group, url_path):                                   # the group's own folder, or any page it lists
        _, own, items = group
        return url_path.startswith(own) or any(href == url_path for href, _ in items)

    def nav(self, url_path, title=''):
        groups = []
        for group in NAV_GROUPS:
            label, own, items = group
            here = ' active' if self.group_is_here(group, url_path) else ''
            if len(items) == 1:                                                   # one page: a flat link, no dropdown
                current = ' aria-current="page"' if own == url_path else ''
                groups.append(f'        <a class="pagelink{here}" href="{own}"{current}>{html.escape(label)}</a>')
                continue
            links = []
            for href, text in items:
                current = ' aria-current="page"' if href == url_path else ''
                links.append(f'            <a class="pagelink navchild{" active" if href == url_path else ""}" href="{href}"{current}>{html.escape(text)}</a>')
            groups.append('\n'.join([f'        <span class="navgroup{here}">'                                                                      ,
                                     f'          <a class="navgroup-btn" href="{own}">{html.escape(label)}<span class="navgroup-car" aria-hidden="true">&#9662;</span></a>',
                                     f'          <div class="navmenu">'                                                                           ,
                                     *links                                                                                                        ,
                                     f'          </div>'                                                                                           ,
                                     f'        </span>'                                                                                            ]))
        return '\n'.join(['  <header class="top">'                                                                                                           ,
                          '    <div class="wrap">'                                                                                                           ,
                          '      <a class="brand" href="/"><img class="rm" src="/assets/brand/riskmandate-mark.svg" alt="" width="26" height="26">'
                          '<span class="word">RiskMandate</span><span class="sub">customers</span></a>'                                                                                ,
                          f'      <a class="parent" href="{PARENT_URL}" title="{html.escape(PARENT_TITLE)}">&#8599; riskmandate.ai</a>'                       ,
                          '      <button class="navtoggle" type="button" aria-expanded="false" aria-label="Menu"><span></span><span></span><span></span></button>',
                          '      <nav class="navlinks" aria-label="Site">'                                                                                   ,
                          *groups                                                                                                                            ,
                          '      </nav>'                                                                                                                     ,
                          '      <div class="tools">'                                                                                                        ,
                          '        <sg-meter class="meter-nav" view="balance"></sg-meter>'                                                                    ,
                          self.theme_picker()                                                                                                                ,
                          f'        {self.version_badge()}'                                                                                                   ,
                          '      </div>'                                                                                                                     ,
                          '    </div>'                                                                                                                       ,
                          self.crumbs(url_path, title)                                                                                                       ,
                          '  </header>'                                                                                                                      ])

    def theme_picker(self):                                                     # the list is drawn here from data/themes.json; assets/theme.js wires it and marks the current one
        default = next(t for t in self.themes['themes'] if t['id'] == self.themes['default'])
        picks   = [f'            <li><button type="button" data-theme-pick="{t["id"]}" aria-pressed="false">'
                   f'<span class="sw sw-{t["id"]}" aria-hidden="true"></span><span>{html.escape(t["name"])}<small>{html.escape(t["note"])}</small></span></button></li>'
                   for t in self.themes['themes']]
        return '\n'.join(['        <div class="theme-pick">'                                                                                                ,
                          '          <button type="button" aria-haspopup="true" aria-expanded="false" title="The theme: six to choose from, kept in this browser">'
                          f'<span class="sw sw-{default["id"]}" aria-hidden="true"></span><span class="name">{html.escape(default["name"])}</span>'
                          '<span class="caret" aria-hidden="true">&#9662;</span></button>'                                                                  ,
                          '          <ul aria-label="Theme" hidden>'                                                                                       ,
                          *picks                                                                                                                             ,
                          f'            <li class="sub-note">Kept in this browser only, as <code>{self.themes["storageKey"]}</code>; nothing else is stored.</li>',
                          '          </ul>'                                                                                                                  ,
                          '        </div>'                                                                                                                   ])

    def crumbs(self, url_path, title):
        if url_path == '/':
            return ''
        parts  = ['<a href="/">Home</a>']
        folder = '/'
        for segment in url_path.strip('/').split('/')[:-1]:                     # every folder above the page
            folder += segment + '/'
            name, href = CRUMB_FOLDERS.get(folder, (segment, folder))
            parts.append(f'<a href="{href}">{html.escape(name)}</a>')
        leaf = self.labels.get(url_path) or CRUMB_FOLDERS.get(url_path, (None, None))[0] or title.split(': ')[0]
        parts.append(f'<span aria-current="page">{html.escape(leaf)}</span>')
        return '    <div class="crumbs wrap" aria-label="Breadcrumb">' + ' <span class="sep">/</span> '.join(parts) + '</div>'

    # ── footer ────────────────────────────────────────────────────────────────

    def meter_card(self, url_path, title):
        kind = self.kind_of(url_path)
        return (f'  <div class="wrap meter-card"><sg-meter view="page" kind="{kind}" title="{html.escape(title, quote=True)}"'
                + (' quiet' if kind == 'free' else '') + '></sg-meter></div>')

    def kit_scripts(self):
        return [f'  <script src="{url}" integrity="{sri}" crossorigin="anonymous"></script>'
                for url, sri in (Pins.kit(path) for path in KIT['api']['scripts'])] + ['  <script src="/assets/storyboards.js" defer></script>']

    def footer(self, url_path, title='', storyboard=False):
        twin = self.twin_path(url_path)
        return '\n'.join([self.meter_card(url_path, title)                                                                                    ,
                          '  <footer class="foot">'                                                                                                ,
                          '    <div class="wrap">'                                                                                                 ,
                          f'      <p>{SITE_NAME} · site {self.version_badge()} · released {self.released} · '
                          f'<a href="/admin/versions.html">releases</a> · <a href="{twin}">this page as markdown</a> · <a href="/llms.txt">llms.txt</a> · '
                          f'<a href="{REPO_URL}">source</a> · <a href="{PARENT_URL}">part of riskmandate.ai</a> · <a href="/about/participant.html">who publishes this</a></p>',
                          f'      <p>Code Apache-2.0. Pages <a href="{LICENCE_URL}">{LICENCE_NAME}</a>. '
                          f'What exists, is proposed or is deliberately absent is listed in <a href="/docs/reality.html">docs/reality.md</a>; '
                          f'if it is not listed there, it does not exist. Nothing in this repository is secret, and no customer\'s contact details are in it. '
                          f'Write to <a href="mailto:{AGENT_ADDRESS}">{AGENT_ADDRESS}</a>.</p>'                                                   ,
                          '    </div>'                                                                                                             ,
                          '  </footer>'                                                                                                            ,
                          *(self.kit_scripts() if storyboard else [])                                                                              ])
