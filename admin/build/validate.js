#!/usr/bin/env node
// ── validate.js — the eight-check release gate for customers.riskmandate.ai ───
//
// No dependencies beyond Node's standard library. Run from anywhere:
//     node admin/build/validate.js
// Exit code 0 means every check passed. Each check returns a list of problems;
// the run prints every problem of every check before failing, so one run shows
// everything. The helpers are exported for tests/unit/validate.test.js and the
// script only runs when invoked directly. Copied from secrets.sgit.ai's gate
// and cut to what this site has; the house words are riskmandate.ai's.
//
// Checks:
//   1 version agreement          5 code from another origin only from the two pinned releases, with their integrity; every script parses
//   2 internal links and orphans 6 the data holds together (customers, milestones, versions, reality)
//   3 canonical host             7 docs/reality.md regenerates identically
//   4 leak tripwire              8 the house words: never ADP, never "the policy" alone, no score, steps not rungs, British spelling
// Plus one advisory that never fails the build: em-dashes in prose we write.

'use strict'

const fs            = require('node:fs')
const path          = require('node:path')
const { spawnSync } = require('node:child_process')

const ROOT          = path.resolve(__dirname, '..', '..')
const SKIP_DIRS     = new Set(['.git', 'node_modules', '__pycache__', '.pytest_cache', '_site', 'credentials'])
const TEXT_PROBE    = 8000                                                       // bytes inspected for a NUL to decide binary
const SELF          = 'admin/build/validate.js'
const MARK          = 'rm-customers:head:start'

// ── leak tripwire patterns ────────────────────────────────────────────────────
// The fix for a trip is always a redaction, never a wider pattern.

const LEAK_PATTERNS = Object.freeze([
    { name : 'sgit vault key'               , re : /sgit_private_vault_[A-Za-z0-9]{6,}/                                                     },
    { name : 'sgit read key'                , re : /sgit_private_read_[A-Za-z0-9]{6,}/                                                      },
    { name : 'sgit write token'             , re : /sgit_write_[A-Za-z0-9]{6,}/                                                             },
    { name : 'sgit passphrase:vault_id'     , re : /\b[a-z]+(?:-[a-z]+){2,}:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b/ },
    { name : 'AWS access key id'            , re : /\b(?:AKIA|ASIA)[A-Z0-9]{16}\b/                                                          },
    { name : 'GitHub token'                 , re : /\bgh[pousr]_[A-Za-z0-9]{30,}\b/                                                         },
    { name : 'sk- API key'                  , re : /\bsk-(?:ant-|or-)?[A-Za-z0-9_-]{20,}\b/                                                 },
    { name : 'PEM private key block'        , re : /-----BEGIN [A-Z ]*PRIVATE KEY-----/                                                     },
    { name : 'Slack token'                  , re : /\bxox[bpa]-[A-Za-z0-9-]{10,}\b/                                                         },
    { name : 'Google OAuth client secret'   , re : /\bGOCSPX-[A-Za-z0-9_-]{10,}\b/                                                          },
    { name : 'service-account JSON'         , re : /"private_key_id"\s*:/                                                                   },
    { name : 'append token (64 hex)'        , re : /\bappend_token"?\s*[:=]\s*"?[0-9a-f]{64}\b/                                             },
    { name : 'bare 12-digit number'         , re : /(?<![\w.\-])\d{12}(?![\w.\-])/                                                          },
])

const LEAK_ALLOW_FILES = Object.freeze([SELF])                                    // validate.js names every pattern, so it is exempt
const LEAK_PUBLIC      = Object.freeze({ 'feedback/lane.json': ['append token (64 hex)'] })   // public by design (R003): a lane token can only append, and the browser must have it

// ── runtime-origin rules (check 5) ────────────────────────────────────────────

const RUNTIME_RE            = Object.freeze([
    { name : '<script src="http…">'      , re : /<script\b[^>]*\bsrc\s*=\s*["']https?:/i       },
    { name : "import from 'http…'"       , re : /\bfrom\s+["']https?:/                          },
    { name : "import 'http…'"            , re : /\bimport\s*\(?\s*["']https?:/                  },
    { name : '@import url(http…)'        , re : /@import\s+(?:url\()?\s*["']?https?:/i          },
])
const LINK_RELS_THAT_LOAD    = Object.freeze(['stylesheet', 'preload', 'modulepreload', 'prefetch', 'icon', 'manifest'])  // canonical, alternate, license are pointers, not loads
const LINK_TAG_RE            = /<link\b[^>]*>/gi

// ── the house words (check 8) ─────────────────────────────────────────────────
// riskmandate.ai's rules, which this sub-site inherits. Verbatim documents are
// exempt: the brief and the memo are published as they were said.

const WORD_RULES = Object.freeze([
    { name : 'ADP: the acronym is ABP'                                    , re : /\bADP\b/                                           },
    { name : '"the policy" alone: say the ABP or the behaviour policy'    , re : /\bthe polic(?:y|ies)\b(?! beside)/i                },
    { name : 'rung: the ladder has steps'                                 , re : /\brungs?\b/i                                       },
    { name : 'a behaviour policy carries no score'                        , re : /\b(?:scored|rated|out of 100)\b|\b\d+\s*\/\s*100\b/i },
    { name : 'British English: behaviour, authorise, licence'             , re : /\b(?:behavior|behaviors|authorize[ds]?|authorizing|a license\b)/ },
    { name : 'beta users: the brief says customers'                       , re : /(?<!\bnot )\bbeta users?\b/i                        },
])
const WORD_EXEMPT = Object.freeze(['docs/brief/our-first-customers.md', 'docs/brief/memos/', 'data/feedback/memos/', 'data/feedback/synthetic/runs/', SELF, 'tests/unit/validate.test.js', 'LICENSE'])

// ── helpers ───────────────────────────────────────────────────────────────────

function walkTree(root = ROOT, dir = root, out = []) {
    for (const entry of fs.readdirSync(dir, { withFileTypes : true })) {
        if (entry.isDirectory()) {
            if (!SKIP_DIRS.has(entry.name)) walkTree(root, path.join(dir, entry.name), out)
        } else if (entry.isFile()) {
            out.push(path.relative(root, path.join(dir, entry.name)).split(path.sep).join('/'))
        }
    }
    return out.sort()
}

function read(rel, root = ROOT) {
    return fs.readFileSync(path.join(root, rel), 'utf8')
}

function exists(rel, root = ROOT) {
    return fs.existsSync(path.join(root, rel))
}

function isBinary(rel, root = ROOT) {
    const fd  = fs.openSync(path.join(root, rel), 'r')
    const buf = Buffer.alloc(TEXT_PROBE)
    const n   = fs.readSync(fd, buf, 0, TEXT_PROBE, 0)
    fs.closeSync(fd)
    return buf.subarray(0, n).includes(0)
}

function lineOf(text, index) {
    return text.slice(0, index).split('\n').length
}

function headingSlug(heading) {                                                   // GitHub-style anchors for markdown headings
    return heading.toLowerCase().trim()
        .replace(/<[^>]+>/g, '')
        .replace(/[`*~]/g, '')
        .replace(/[^\p{L}\p{N}\s_-]/gu, '')                                      // GitHub keeps _ and -
        .replace(/\s+/g, '-')
}

function stripCode(markdown) {                                                    // fenced blocks and inline code are not links
    return markdown.replace(/```[\s\S]*?```/g, '').replace(/`[^`\n]*`/g, '')
}

function isInternalLink(href) {
    if (!href) return false
    if (/^[a-z][a-z0-9+.-]*:/i.test(href) && !href.startsWith('/')) return false // http:, https:, mailto:, data:, javascript:
    if (href.startsWith('//')) return false
    return true
}

function resolveLink(fromRel, href, root = ROOT) {                                // → { rel, fragment }
    const [withoutQuery]        = href.split('?')
    const [target, fragment]    = withoutQuery.split('#')
    let rel
    if (target === '')       rel = fromRel
    else if (target.startsWith('/')) rel = target.slice(1)
    else                     rel = path.posix.normalize(path.posix.join(path.posix.dirname(fromRel), target))
    if (rel === '.' || rel === '') rel = ''
    const abs = path.join(root, rel)
    if (rel === '' || (fs.existsSync(abs) && fs.statSync(abs).isDirectory())) {
        rel = path.posix.join(rel, 'index.html')
    }
    return { rel, fragment : fragment || null }
}

function anchorsIn(rel, root = ROOT) {
    const text  = read(rel, root)
    const found = new Set()
    for (const match of text.matchAll(/\b(?:id|name)\s*=\s*["']([^"']+)["']/g)) found.add(match[1])
    if (rel.endsWith('.md')) {
        for (const match of text.matchAll(/^#{1,6}\s+(.+?)\s*#*\s*$/gm)) found.add(headingSlug(match[1]))
    }
    return found
}

function linksIn(rel, root = ROOT) {                                              // → [{ href, line }]
    const text  = read(rel, root)
    const links = []
    if (rel.endsWith('.html')) {
        for (const match of text.matchAll(/\b(?:href|src)\s*=\s*["']([^"']+)["']/g)) {
            links.push({ href : match[1], line : lineOf(text, match.index) })
        }
    } else if (rel.endsWith('.md')) {
        const scan = stripCode(text)
        for (const match of scan.matchAll(/\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
            links.push({ href : match[1], line : lineOf(scan, match.index) })
        }
    }
    return links
}

function readVersion(root = ROOT) {
    return read('admin/build/version.txt', root).trim()
}

function nextVersionOk(previous, next) {                                           // next minor, a patch, or a deliberate major .0.0
    if (!previous) return true
    const [pM, pm, pp] = previous.split('.').map(Number)
    const [nM, nm, np] = next.split('.').map(Number)
    if (nM === pM && nm === pm + 1 && np === 0) return true
    if (nM === pM && nm === pm && np === pp + 1) return true
    if (nM === pM + 1 && nm === 0 && np === 0) return true
    return false
}

function proseOf(rel, root = ROOT) {                                              // the part of a file we write: <main> of a page, the whole of a markdown or JSON file
    const text = read(rel, root)
    if (rel.endsWith('.html')) {
        if (/<meta name="rm-customers:source" content="([^"]+)">/.test(text)) {
            const source = text.match(/<meta name="rm-customers:source" content="\/([^"]+)">/)[1]
            if (WORD_EXEMPT.some(e => source === e || source.startsWith(e))) return null   // rendered from a verbatim document
        }
        return (text.match(/<main\b[^>]*>([\s\S]*?)<\/main>/) || ['', ''])[1]
    }
    return text
}

const MENTION_RE = [/<(blockquote|q|dl|p)\b[^>]*\bclass="[^"]*\bverbatim\b[^"]*"[^>]*>[\s\S]*?<\/\1>/gi, /"quote"\s*:\s*"(?:[^"\\]|\\.)*"/g,   // a reviewer's or an invented user's own words, kept as given
                    /```[\s\S]*?```/g, /<pre\b[\s\S]*?<\/pre>/gi, /<code\b[^>]*>[\s\S]*?<\/code>/gi, /`[^`\n]*`/g,
                    /"[^"\n]{1,80}"/g, /&quot;[^&\n]{1,80}&quot;/g, /(?<![\w])'[^'\n]{1,80}'(?![\w])/g, /&#x27;[^&\n]{1,80}&#x27;/g, /\*[^*\n]{1,60}\*/g, /<em>[^<\n]{1,60}<\/em>/gi, /<i>[^<\n]{1,60}<\/i>/gi]

function withoutMentions(text) {                                                  // naming a word in quotes, emphasis or code is not using it; the replacement keeps every index
    let out = text
    for (const re of MENTION_RE) out = out.replace(re, m => m.replace(/[^\n]/g, ' '))
    return out
}

function wordProblems(rel, text) {                                                // check 8 on one file's prose
    const problems = []
    const scan     = withoutMentions(text)
    for (const rule of WORD_RULES) {
        const match = rule.re.exec(scan)
        if (match) problems.push(`${rel}:${lineOf(text, match.index)}: ${rule.name} ("…${text.slice(Math.max(0, match.index - 20), match.index + match[0].length + 20).replace(/\s+/g, ' ')}…")`)
    }
    return problems
}

// ── the checks ────────────────────────────────────────────────────────────────

function checkVersionAgreement(root = ROOT) {
    const problems = []
    const version  = readVersion(root)
    if (!/^\d+\.\d+\.\d+$/.test(version)) problems.push(`admin/build/version.txt: '${version}' is not X.Y.Z`)

    for (const rel of walkTree(root).filter(f => f.endsWith('.html'))) {
        const text   = read(rel, root)
        const badges = [...text.matchAll(/data-version="([^"]+)"/g)].map(m => m[1])
        if (!text.includes(MARK)) continue
        if (badges.length === 0) problems.push(`${rel}: no version badge (data-version)`)
        for (const badge of badges) if (badge !== version) problems.push(`${rel}: badge says ${badge}, version.txt says ${version}`)
    }

    const releases = JSON.parse(read('data/versions.json', root)).releases
    const seen     = new Set()
    for (const release of releases) {
        if (seen.has(release.version)) problems.push(`data/versions.json: ${release.version} listed twice`)
        seen.add(release.version)
    }
    if (!releases.length || releases[0].version !== version) problems.push(`data/versions.json: newest row is ${releases[0] && releases[0].version}, version.txt says ${version}`)
    const versionsPage = read('admin/versions.html', root)
    if (!versionsPage.includes(`<code>v${version}</code>`)) problems.push(`admin/versions.html: no row for v${version}`)

    for (const rel of ['llms.txt', 'llms-full.txt']) {
        const match = read(rel, root).match(/^Site version: v(\d+\.\d+\.\d+)/m)
        if (!match) problems.push(`${rel}: no 'Site version: vX.Y.Z' line`)
        else if (match[1] !== version) problems.push(`${rel}: says ${match[1]}, version.txt says ${version}`)
    }
    const twin = read('index.md', root).match(/· site v(\d+\.\d+\.\d+)/)
    if (!twin) problems.push('index.md: no "site vX.Y.Z" in the source line')
    else if (twin[1] !== version) problems.push(`index.md: says ${twin[1]}, version.txt says ${version}`)
    return problems
}

function checkInternalLinks(root = ROOT) {
    const problems = []
    const anchors  = new Map()
    const reached  = new Set(['index.html'])                                      // orphan rule: a page nothing links to is unpublished
    const anchorsOf = (rel) => {
        if (!anchors.has(rel)) anchors.set(rel, anchorsIn(rel, root))
        return anchors.get(rel)
    }
    for (const rel of walkTree(root).filter(f => f.endsWith('.html') || f.endsWith('.md'))) {
        for (const { href, line } of linksIn(rel, root)) {
            if (!isInternalLink(href)) continue
            const { rel : target, fragment } = resolveLink(rel, href, root)
            if (!exists(target, root) || fs.statSync(path.join(root, target)).isDirectory()) {
                problems.push(`${rel}:${line}: link '${href}' → ${target} does not exist`)
                continue
            }
            if (rel.endsWith('.html')) reached.add(target)
            if (fragment && (target.endsWith('.html') || target.endsWith('.md')) && !anchorsOf(target).has(decodeURIComponent(fragment))) {
                problems.push(`${rel}:${line}: fragment '#${fragment}' not found in ${target}`)
            }
        }
    }
    for (const rel of walkTree(root).filter(f => f.endsWith('.html') && read(f, root).includes(MARK))) {
        if (!reached.has(rel) && rel !== '404.html') problems.push(`${rel}: no page links to it (an orphan page is unpublished)`)
    }
    return problems
}

function checkCanonicalHost(root = ROOT) {
    const problems = []
    const host     = read('CNAME', root).trim()
    const base     = `https://${host}/`
    for (const rel of walkTree(root).filter(f => f.endsWith('.html'))) {
        const text = read(rel, root)
        if (!text.includes(MARK)) continue
        const canonical = text.match(/<link rel="canonical" href="([^"]+)">/)
        const og        = text.match(/<meta property="og:url" content="([^"]+)">/)
        if (!canonical)                              problems.push(`${rel}: no rel=canonical`)
        else if (!canonical[1].startsWith(base))     problems.push(`${rel}: canonical ${canonical[1]} is not on ${base}`)
        if (!og)                                     problems.push(`${rel}: no og:url`)
        else if (!og[1].startsWith(base))            problems.push(`${rel}: og:url ${og[1]} is not on ${base}`)
        if (canonical && og && canonical[1] !== og[1]) problems.push(`${rel}: canonical and og:url differ`)
    }
    return problems
}

function checkLeakTripwire(root = ROOT) {
    const problems = []
    for (const rel of walkTree(root)) {
        if (LEAK_ALLOW_FILES.includes(rel)) continue
        if (isBinary(rel, root)) continue
        const text = read(rel, root)
        for (const pattern of LEAK_PATTERNS) {
            if ((LEAK_PUBLIC[rel] || []).includes(pattern.name)) continue
            const match = pattern.re.exec(text)
            if (match) problems.push(`${rel}:${lineOf(text, match.index)}: looks like a ${pattern.name} (${match[0].slice(0, 6)}…). Redact it.`)
        }
    }
    return problems
}

function loadPins(root = ROOT) {                                                 // the two APIs this site may load code from: host, release, and the manifest's files with their integrity
    const meter = JSON.parse(read('data/meter.json', root)).api
    const kit   = JSON.parse(read('data/storyboards.json', root)).api
    const pin   = (api, integrityOf) => {
        const manifest = JSON.parse(read(`admin/build/pins/${api.host.replace('https://', '')}/${api.release}/manifest.json`, root))
        const files    = new Map(manifest.files.map(f => [f.path, integrityOf(f)]))
        return { base : `${api.host}/${api.release}/`, files, release : manifest.release }
    }
    return [pin(meter, f => 'sha256-' + Buffer.from(f.sha256, 'hex').toString('base64')),
            pin(kit  , f => f.integrity)]
}

function pinnedProblem(url, tag, pins) {                                            // null when the URL is a pinned file loaded with its manifest's integrity
    const pin = pins.find(p => url.startsWith(p.base))
    if (!pin) return 'loads from another origin, outside the two pinned releases in data/meter.json and data/storyboards.json'
    const path = url.slice(pin.base.length)
    if (!pin.files.has(path)) return `names ${path}, which is not in the pinned manifest of ${pin.base}`
    const integrity = (tag.match(/\bintegrity\s*=\s*["']([^"']+)["']/i) || [])[1]
    if (integrity !== pin.files.get(path)) return `carries integrity ${integrity || '(none)'}, the manifest says ${pin.files.get(path)}`
    if (!/\bcrossorigin\s*=\s*["']anonymous["']/i.test(tag)) return 'needs crossorigin="anonymous" for its integrity to be checked'
    return null
}

function checkRuntimeOrigin(root = ROOT) {
    const problems = checkScriptsParse(root)
    const pins     = loadPins(root)
    for (const rel of walkTree(root).filter(f => /\.(html|js|mjs|css)$/.test(f) && !f.startsWith('admin/build/pins/'))) {
        const text    = read(rel, root)
        const foreign = (index, why) => problems.push(`${rel}:${lineOf(text, index)}: ${why}`)
        for (const match of text.matchAll(/<script\b[^>]*\bsrc\s*=\s*["'](https?:[^"']+)["'][^>]*>/gi)) {
            const why = pinnedProblem(match[1], match[0], pins)
            if (why) foreign(match.index, `<script src="${match[1]}"> ${why}`)
        }
        for (const match of text.matchAll(LINK_TAG_RE)) {
            const relAttr = match[0].match(/\brel\s*=\s*["']([^"']+)["']/i)
            const href    = match[0].match(/\bhref\s*=\s*["'](https?:[^"']*)["']/i)
            if (!relAttr || !href || !LINK_RELS_THAT_LOAD.includes(relAttr[1].toLowerCase())) continue
            const why = pinnedProblem(href[1], match[0], pins)
            if (why) foreign(match.index, `<link rel="${relAttr[1]}" href="${href[1]}"> ${why}`)
        }
        for (const rule of RUNTIME_RE.filter(r => !r.name.startsWith('<script'))) {
            for (const match of text.matchAll(new RegExp(rule.re.source, rule.re.flags + 'g'))) foreign(match.index, `${rule.name} loads from another origin. Vendor it, or do without.`)
        }
        if (rel.endsWith('.html') && text.includes(MARK)) {
            if (/<script\b(?![^>]*\bsrc=)/.test(text)) problems.push(`${rel}: an inline script; the CSP forbids it`)
            if (/<style\b/.test(text) || /\sstyle\s*=/.test(text)) problems.push(`${rel}: an inline style; the CSP forbids it`)
        }
    }
    return problems
}

function checkScriptsParse(root = ROOT) {                                        // every script the site serves parses (node --check)
    const problems = []
    for (const rel of walkTree(root).filter(f => /\.(js|mjs)$/.test(f))) {
        const run = spawnSync('node', ['--check', path.join(root, rel)], { encoding : 'utf8' })
        if (run.status !== 0) problems.push(`${rel}: does not parse: ${(run.stderr || '').trim().split('\n').slice(-1)[0]}`)
    }
    return problems
}

function checkData(root = ROOT) {                                                 // check 6: the generators validate the shape; this re-runs them in check mode and asks about the pages they wrote
    const problems = []
    for (const name of ['gen_customers', 'gen_versions']) {
        const run = spawnSync('python3', [`admin/build/${name}.py`, '--check'], { cwd : root, encoding : 'utf8' })
        if (run.error) problems.push(`could not run ${name}.py --check: ${run.error.message}`)
        else if (run.status !== 0) problems.push(`${name}.py --check failed:\n${(run.stdout + run.stderr).trim()}`)
    }
    const customers = JSON.parse(read('data/customers.json', root)).customers
    for (const customer of customers) {
        const page = `customers/${customer.id}/index.html`
        if (!exists(page, root)) problems.push(`${page}: no page for the record ${customer.id}`)
    }
    for (const folder of fs.readdirSync(path.join(root, 'customers'), { withFileTypes : true }).filter(d => d.isDirectory()).map(d => d.name)) {
        if (!customers.some(c => c.id === folder)) problems.push(`customers/${folder}/: no record in data/customers.json`)
    }
    return problems
}

function checkReality(root = ROOT) {
    const run = spawnSync('python3', ['admin/build/gen_reality.py', '--check'], { cwd : root, encoding : 'utf8' })
    if (run.error) return [`could not run gen_reality.py --check: ${run.error.message}`]
    if (run.status !== 0) return [`gen_reality.py --check failed:\n${(run.stdout + run.stderr).trim()}`]
    return []
}

function checkHouseWords(root = ROOT) {
    const problems = []
    for (const rel of walkTree(root).filter(f => /\.(html|md|json|txt)$/.test(f) && !f.endsWith('llms-full.txt'))) {
        if (WORD_EXEMPT.some(e => rel === e || rel.startsWith(e))) continue
        if (rel.endsWith('.md') && exists(rel.slice(0, -3) + '.html', root) && !read(rel.slice(0, -3) + '.html', root).includes('rm-customers:source')) continue   // a twin repeats its page
        const prose = proseOf(rel, root)
        if (prose === null) continue
        problems.push(...wordProblems(rel, prose))
    }
    return problems
}

const EM_DASH_PROSE = Object.freeze(['*.html', '*/index.html', '*/*/index.html', 'admin/*.html', 'docs/ops/*.md', 'docs/reality.md', 'docs/brief/BRIEF-CORRECTIONS.md', 'docs/brief/memo-*.md', 'review/*.md', 'team/**/*.md', 'README.md', 'data/*.json'])

function adviseEmDashes(root = ROOT) {                                            // advisory: the house writes without em-dashes; verbatim documents are exempt
    const notes = []
    const globs = EM_DASH_PROSE.map(g => new RegExp('^' + g.replace(/\./g, '\\.').replace(/\*\*\//g, '(.+/)?').replace(/\*/g, '[^/]+') + '$'))
    for (const rel of walkTree(root).filter(f => globs.some(g => g.test(f)))) {
        const body = proseOf(rel, root)
        if (body === null) continue
        const count = (body.match(/—/g) || []).length
        if (count) notes.push(`${rel}: ${count} em-dash(es) in prose we write; the house uses commas, colons or full stops`)
    }
    return notes
}

const CHECKS = Object.freeze([
    { n : 1, name : 'version agreement'                          , run : checkVersionAgreement },
    { n : 2, name : 'internal links, fragments and no orphans'   , run : checkInternalLinks    },
    { n : 3, name : 'canonical host'                             , run : checkCanonicalHost    },
    { n : 4, name : 'leak tripwire'                              , run : checkLeakTripwire     },
    { n : 5, name : 'code from another origin only from the two pinned releases, with integrity; scripts parse; no inline script or style', run : checkRuntimeOrigin },
    { n : 6, name : 'the data holds together'                    , run : checkData             },
    { n : 7, name : 'reality regenerates identically'            , run : checkReality          },
    { n : 8, name : 'the house words'                            , run : checkHouseWords       },
])
const N = CHECKS.length

function main() {
    let failed = 0
    for (const check of CHECKS) {
        let problems
        try { problems = check.run(ROOT) } catch (error) { problems = [`threw: ${error.message}`] }
        if (problems.length === 0) {
            console.log(`  ✓ ${check.n}/${N} ${check.name}`)
        } else {
            failed += 1
            console.log(`  ✗ ${check.n}/${N} ${check.name}`)
            for (const problem of problems) console.log(`      ${problem}`)
        }
    }
    const notes = adviseEmDashes(ROOT)
    for (const note of notes) console.log(`  · advisory: ${note}`)
    if (failed) {
        console.log(`validate: ${failed} of ${N} checks failed (site v${readVersion()})`)
        process.exit(1)
    }
    console.log(`validate: ${N}/${N} checks passed (site v${readVersion()})${notes.length ? `, ${notes.length} advisory note(s)` : ''}`)
}

module.exports = {
    ROOT, LEAK_PATTERNS, LEAK_ALLOW_FILES, RUNTIME_RE, LINK_RELS_THAT_LOAD, WORD_RULES, WORD_EXEMPT, CHECKS,
    walkTree, isBinary, headingSlug, stripCode, isInternalLink, resolveLink, anchorsIn, linksIn, nextVersionOk, wordProblems, withoutMentions, proseOf,
    checkVersionAgreement, checkInternalLinks, checkCanonicalHost, checkLeakTripwire, checkRuntimeOrigin, checkScriptsParse, loadPins, pinnedProblem,
    checkData, checkReality, checkHouseWords, adviseEmDashes,
}

if (require.main === module) main()
