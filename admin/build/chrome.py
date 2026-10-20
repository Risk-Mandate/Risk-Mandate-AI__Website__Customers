# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Chrome
# The one definition of the site chrome: head block, the RiskMandate header
# (mark, wordmark, the sub-site name, the nav, the version chip, the parent
# link), breadcrumbs, footer, CSP and canonical URL. Every HTML page gets it
# injected between markers by gen_chrome.py, so the chrome cannot drift between
# pages. The look is riskmandate.ai's (paper surfaces, the green, the dark
# canvas); every colour lives in assets/site.css as a token and nowhere else.
# ═══════════════════════════════════════════════════════════════════════════════

import html
import json

from pathlib import Path


ROOT           = Path(__file__).resolve().parents[2]
VERSION_FILE   = ROOT / 'admin' / 'build' / 'version.txt'
CNAME_FILE     = ROOT / 'CNAME'
VERSIONS_FILE  = ROOT / 'data' / 'versions.json'

MARKER_PREFIX  = 'rm-customers'                                                  # <!-- rm-customers:<block>:start -->

SITE_NAME      = 'customers.riskmandate.ai'
SITE_ONE_LINER = ('The first customers of the Agent Behaviour Policy: an early access programme run as a site, '
                  'with a start-here page, a page per customer, credit to spend, the milestones agreed with each one, '
                  'and a daily follow-up. Part of riskmandate.ai.')
STAGE          = 'first batch, being set up'                                     # the stage pill; changes when the first customer reaches the usage moment
PARENT_URL     = 'https://riskmandate.ai'
PARENT_TITLE   = 'riskmandate.ai: the company and the product this programme is for'
LICENCE_URL    = 'https://creativecommons.org/licenses/by/4.0/'
LICENCE_NAME   = 'CC BY 4.0'
REPO_URL       = 'https://github.com/SGit-AI/SGit-AI__Website__Customers'
AGENT_ADDRESS  = 'agent@riskmandate.ai'

CSP            = ("default-src 'self'; "
                  "connect-src 'self'; "
                  "img-src 'self' data:; "
                  "style-src 'self'; "
                  "script-src 'self'; "
                  "object-src 'none'; "
                  "base-uri 'none'; "
                  "form-action 'none'")                                           # no form on this site yet; the next-batch page says where the form is

# Each group: (label, the group's own page, [(href, label), ...]). A group label is a
# plain link to its first page, so the nav works with no JavaScript at all.
NAV_GROUPS     = (('Start here'   , '/start-here/' , (('/start-here/'                                   , 'What to do first, in order'       ),)),
                  ('The programme', '/programme/'  , (('/programme/'                                    , 'Customers, not beta users'        ),
                                                      ('/credit/'                                       , 'Credit, and the meter'            ),
                                                      ('/milestones/'                                   , 'The milestones: seven steps'      ),
                                                      ('/follow-up/'                                    , 'The daily follow-up'              ),
                                                      ('/learning/'                                     , 'What we want to discover'         ),
                                                      ('/next-batch/'                                   , 'The next batch'                   ))),
                  ('Customers'    , '/customers/'  , (('/customers/'                                    , 'The first batch, and where each is'),)),
                  ('Docs'         , '/docs/'       , (('/docs/'                                         , 'All documents'                    ),
                                                      ('/docs/brief/our-first-customers.html'           , 'The brief, in full'               ),
                                                      ('/docs/brief/memo-2026-10-20-user-onboarding-plan.html', 'The memo of 20 October'    ),
                                                      ('/docs/brief/BRIEF-CORRECTIONS.html'             , 'Brief corrections'                ),
                                                      ('/docs/reality.html'                             , 'Reality: what exists'             ),
                                                      ('/docs/ops/'                                     , 'Operations'                       ),
                                                      ('/team/'                                         , 'The team'                         ))),
                  ('Admin'        , '/admin/'      , (('/admin/'                                        , 'How the site is built'            ),
                                                      ('/admin/versions.html'                           , 'Release history'                  ),
                                                      ('/docs/ops/needs.html'                           , 'What needs a human'               ),
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
                  '/admin/'       : ('Admin'      , '/admin/'      )}


class Chrome:

    def __init__(self):
        self.version  = VERSION_FILE.read_text(encoding='utf-8').strip()
        self.host     = CNAME_FILE.read_text(encoding='utf-8').strip()
        self.base_url = f'https://{self.host}'
        self.released = self.release_date()
        self.labels   = {href: label for _, _, items in NAV_GROUPS for href, label in items}

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

    def head(self, url_path, title, description, connect=''):
        canonical = self.canonical_url(url_path)
        twin      = self.twin_path(url_path)
        esc       = html.escape
        lines     = [f'<meta http-equiv="Content-Security-Policy" content="{CSP}">'                      ,
                     f'<link rel="canonical" href="{canonical}">'                                         ,
                     f'<link rel="alternate" type="text/markdown" href="{twin}">'                        ,
                     f'<link rel="license" href="{LICENCE_URL}">'                                         ,
                     f'<link rel="icon" href="/assets/brand/riskmandate-favicon-32.png" sizes="32x32">'  ,
                     f'<link rel="icon" href="/assets/brand/riskmandate-mark.svg" type="image/svg+xml">' ,
                     f'<link rel="stylesheet" href="/assets/site.css">'                                   ,
                     f'<script src="/assets/nav.js" defer></script>'                                      ,
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
                          'RiskMandate<span class="sub">customers</span></a>'                                                                                ,
                          f'      <a class="parent" href="{PARENT_URL}" title="{html.escape(PARENT_TITLE)}">&#8599; riskmandate.ai</a>'                       ,
                          f'      <span class="stage-pill">{STAGE}</span>'                                                                                     ,
                          '      <button class="navtoggle" type="button" aria-expanded="false" aria-label="Menu"><span></span><span></span><span></span></button>',
                          '      <nav class="navlinks" aria-label="Site">'                                                                                   ,
                          *groups                                                                                                                            ,
                          '      </nav>'                                                                                                                     ,
                          f'      {self.version_badge()}'                                                                                                     ,
                          '    </div>'                                                                                                                       ,
                          self.crumbs(url_path, title)                                                                                                       ,
                          '  </header>'                                                                                                                      ])

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

    def footer(self, url_path):
        twin = self.twin_path(url_path)
        return '\n'.join(['  <footer class="foot">'                                                                                                ,
                          '    <div class="wrap">'                                                                                                 ,
                          f'      <p>{SITE_NAME} · site {self.version_badge()} · released {self.released} · '
                          f'<a href="/admin/versions.html">releases</a> · <a href="{twin}">this page as markdown</a> · <a href="/llms.txt">llms.txt</a> · '
                          f'<a href="{REPO_URL}">source</a> · <a href="{PARENT_URL}">part of riskmandate.ai</a> · <a href="/about/participant.html">who publishes this</a></p>',
                          f'      <p>Code Apache-2.0. Pages <a href="{LICENCE_URL}">{LICENCE_NAME}</a>. '
                          f'What exists, is proposed or is deliberately absent is listed in <a href="/docs/reality.html">docs/reality.md</a>; '
                          f'if it is not listed there, it does not exist. Nothing in this repository is secret, and no customer\'s contact details are in it. '
                          f'Write to <a href="mailto:{AGENT_ADDRESS}">{AGENT_ADDRESS}</a>.</p>'                                                   ,
                          '    </div>'                                                                                                             ,
                          '  </footer>'                                                                                                            ])
