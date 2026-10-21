// ── account.js — your account: everything you have done here, and everything this browser keeps ──
//
// Drawn from this browser alone; nothing here is fetched from us except the list of examples
// (/examples/index.json). What it reads, all under the prefix riskmandate.customers.:
//   meter.v1        the reading meter's state (SG Meter v1.4.1, state v3): balance, history, top-ups
//   progress        how far you got in each example's player (assets/demo.js)
//   quiz.<example>  your answers to an example's questions (assets/examples.js)
//   sent            what you sent with Encrypt and send, and whether it went; not the text (assets/envelope.js)
//   theme, look     the theme you picked, and the Claude or ChatGPT look
//   storyboards.v1  the storyboard viewer's preferences
// and, in this tab only (session storage), meter.v1.seen: the pages already charged in this visit.
// It writes nothing, except when you ask: Export everything downloads all of it as one file;
// Delete everything removes all of it, and the meter starts again at £50.00. Text is only ever set
// with textContent.

(function () {
    'use strict'
    const host = document.getElementById('account-live')
    if (!host) return
    const PREFIX = 'riskmandate.customers.'
    const cfg    = window.SG_METER_CONFIG || {}
    const mkey   = cfg.storageKey || PREFIX + 'meter.v1'
    const symbol = cfg.symbol || '£'
    const start  = typeof cfg.start === 'number' ? cfg.start : 5000
    const WHAT   = {
        'meter.v1': 'Your reading account: balance, every page read and what it cost, top-ups',
        'meter.v1.seen': 'The pages already charged in this visit, so a page is charged once per visit (this tab only)',
        'progress': 'How far you got in each example',
        'sent': 'What you sent us with Encrypt and send, and whether it went (not the text)',
        'theme': 'The theme you picked',
        'look': 'Claude or ChatGPT, for the chat frames',
        'storyboards.v1': 'The storyboard viewer’s settings',
    }

    const money = (p) => `${p < -0.004 ? '−' : ''}${symbol}${(Math.abs(p) / 100).toFixed(2)}`
    const pence = (p) => { p = Math.round(p * 10) / 10; return p === 0 ? 'nothing' : `${p % 1 ? p.toFixed(1) : p}p` }
    const when  = (iso) => String(iso || '').slice(0, 16).replace('T', ' ')
    const json  = (k, d) => { try { const v = window.localStorage.getItem(PREFIX + k); return v ? JSON.parse(v) : d } catch (e) { return d } }

    function el(tag, attrs, ...kids) {
        const node = document.createElement(tag)
        for (const [k, v] of Object.entries(attrs || {})) if (v != null) node.setAttribute(k, v)
        for (const kid of kids.flat()) if (kid != null) node.append(kid instanceof Node ? kid : String(kid))
        return node
    }
    const table = (heads, rows, cls) => el('div', { class: 'tablewrap' }, el('table', { class: cls }, el('thead', {}, el('tr', {}, heads.map((h) => el('th', {}, h)))), el('tbody', {}, rows)))

    function stored() {                                                                // every key of ours, in both stores
        const out = []
        for (const [area, store] of [['this browser', window.localStorage], ['this tab', window.sessionStorage]]) {
            try {
                for (let i = 0; i < store.length; i++) {
                    const k = store.key(i)
                    if (k && k.startsWith(PREFIX)) out.push({ area, key: k, value: store.getItem(k) })
                }
            } catch (e) { /* blocked */ }
        }
        return out.sort((a, b) => a.key.localeCompare(b.key))
    }
    const whatIs = (k) => { const short = k.slice(PREFIX.length); return WHAT[short] || (short.startsWith('quiz.') ? `Your answers to the questions under example ${short.slice(5)}` : 'Kept by this site') }

    function download(name, data) {
        const a = el('a', { href: URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })), download: name })
        document.body.append(a); a.click(); a.remove()
    }

    let examples = []
    function draw() {
        let s
        try { s = { balance: start, spent: 0, reads: 0, declined: 0, log: [], topups: [], ...(JSON.parse(window.localStorage.getItem(mkey) || '{}')) } }
        catch (e) { host.replaceChildren(el('p', { class: 'note warn' }, 'This browser is not letting the site keep anything (its storage is blocked), so every page starts again at ', money(start), '.')); return }
        const log      = Array.isArray(s.log) ? s.log : []
        const progress = json('progress', {})
        const sent     = json('sent', [])
        const answered = examples.filter((x) => json('quiz.' + x.slug, null))
        const finished = examples.filter((x) => progress[x.slug] && progress[x.slug].finished)
        const watched  = examples.filter((x) => progress[x.slug] && progress[x.slug].furthest > 0)
        const neg      = s.balance < 0

        // the summary
        const exporter = () => {
            const b = el('button', { type: 'button', class: 'btn' }, 'Export everything')
            b.addEventListener('click', () => download(`riskmandate-account-${new Date().toISOString().slice(0, 10)}.json`, Object.fromEntries(stored().map((x) => [x.key, (() => { try { return JSON.parse(x.value) } catch (e) { return x.value } })()]))))
            return b
        }
        const tile = (n, label, href) => el('a', { class: 'account-tile', href }, el('b', {}, String(n)), el('span', {}, label))
        const summary = el('div', { class: 'account-card' },
            el('div', {},
                el('span', { class: 'dim' }, neg ? 'Read beyond your credit' : 'Your balance'),
                el('b', { class: `account-balance${neg ? ' neg' : ''}` }, money(s.balance)),
                el('span', { class: 'dim' }, `${money(s.spent)} spent of the ${money(start)} you started with` + (s.declined ? ` · ${money(s.declined)} not charged at your request` : ''))),
            el('div', { class: 'account-actions' }, el('a', { class: 'btn btn-green', href: '/account/top-up.html', title: 'A simulation: no money moves yet' }, 'Top up (a simulation)'), exporter()))
        const tiles = el('div', { class: 'account-tiles' },
            tile(`${watched.length} of ${examples.length}`, 'examples watched', '#examples'),
            tile(`${finished.length}`, 'played to the end', '#examples'),
            tile(`${answered.length}`, 'with your answers', '#examples'),
            tile(`${sent.filter((x) => x.ok).length}`, 'sent to us, encrypted', '#sent'),
            tile(`${s.reads}`, 'pages opened', '#history'))

        // the examples
        const exRows = examples.map((x) => {
            const pr = progress[x.slug], q = json('quiz.' + x.slug, null)
            const tried = q && q.worked ? q.worked : ''
            const mine  = q ? ['got', 'learned', 'surprised', 'good'].filter((k) => q[k]).map((k) => `${{ got: 'got it', learned: 'learned', surprised: 'surprised', good: 'how good' }[k]}: ${q[k]}`).join(' · ') : ''
            const went  = sent.find((e) => e.ok && e.about && e.about.startsWith(`example ${x.slug} `))
            return el('tr', {},
                el('td', {}, el('a', { href: `/examples/${x.slug}/` }, x.tab), el('span', { class: 'dim' }, ` v${x.version}`)),
                el('td', {}, pr ? (pr.finished ? 'to the end' : `step ${pr.furthest} of ${pr.of}`) : 'not yet'),
                el('td', {}, tried || (q ? 'not said' : '')),
                el('td', {}, mine || el('a', { href: `/examples/${x.slug}/#quiz-${x.slug}` }, 'answer the questions')),
                el('td', {}, went ? `sent ${when(went.at)}` : q ? 'not sent' : ''))
        })

        // where the credit went
        const kinds = {}
        for (const e of log) { const k = kinds[e.kind] || (kinds[e.kind] = { pages: 0, cost: 0 }); k.pages++; k.cost += e.declined ? 0 : (e.cost || 0) }
        const byKind = Object.keys(kinds).length
            ? table(['Kind of page', 'Pages', 'Spent'], Object.entries(kinds).sort((a, b) => b[1].cost - a[1].cost).map(([k, v]) => el('tr', {}, el('td', {}, k), el('td', {}, String(v.pages)), el('td', {}, money(v.cost)))), 'account-kinds')
            : el('p', { class: 'dim' }, 'Nothing yet.')
        const history = log.length
            ? table(['When', 'Page', 'Kind', 'Cost'], log.slice(0, 200).map((e) => el('tr', {}, el('td', {}, when(e.at)), el('td', {}, el('a', { href: e.path }, String(e.title || e.path))), el('td', {}, e.kind || ''),
                el('td', {}, e.declined ? `not charged (${e.declined.reason || 'at your request'})` : `${pence(e.cost || 0)} (${Math.round((e.depth == null ? 1 : e.depth) * 100)}% read)`))), 'account-history')
            : el('p', { class: 'dim' }, 'No pages read yet in this browser.')

        // what was sent
        const sentList = sent.length
            ? table(['When', 'What', 'Result'], sent.map((e) => el('tr', {}, el('td', {}, when(e.at)), el('td', {}, e.about || e.form), el('td', {}, e.ok ? `sent, encrypted to ${e.to || 'the lane key'}` : `did not go: ${e.why || ''}`))), 'account-sent')
            : el('p', { class: 'dim' }, 'Nothing yet. Every example has questions under it, and ', el('a', { href: '/feedback/' }, 'you can write to us'), '.')

        // everything this browser keeps
        const keep = stored()
        const del  = el('button', { type: 'button', class: 'btn btn-danger' }, 'Delete everything this site keeps here')
        del.addEventListener('click', () => {
            if (!window.confirm('Delete your balance, history, answers, progress and settings from this browser? The meter starts again at ' + money(start) + '. What you already sent us is not affected.')) return
            for (const x of stored()) { try { (x.area === 'this tab' ? window.sessionStorage : window.localStorage).removeItem(x.key) } catch (e) { /* fine */ } }
            draw()
        })
        const keyRows = keep.map((x) => {
            const show = el('details', {}, el('summary', {}, `${(x.value || '').length.toLocaleString()} characters`), el('pre', {}, el('code', {}, (() => { try { return JSON.stringify(JSON.parse(x.value), null, 2) } catch (e) { return x.value } })())))
            return el('tr', {}, el('td', {}, el('code', {}, x.key)), el('td', {}, whatIs(x.key)), el('td', {}, x.area), el('td', {}, show))
        })
        const prefs = `Theme: ${json('theme', null) || (window.localStorage.getItem(PREFIX + 'theme') || 'the default')} · Chat look: ${window.localStorage.getItem(PREFIX + 'look') || 'Claude'}`

        host.replaceChildren(
            summary, tiles,
            el('h2', { id: 'examples' }, 'Your examples'),
            el('p', {}, 'How far you got in each, what you said when you tried it, and whether you sent it.'),
            table(['Example', 'Watched', 'Tried it?', 'Your answers', 'Sent'], exRows, 'account-examples'),
            el('h2', { id: 'sent' }, 'What you sent us'), sentList,
            el('h2', { id: 'spent' }, 'Where your credit went, by kind of page'), byKind,
            el('h2', { id: 'history' }, 'Everything you have read'), history,
            el('h2', { id: 'top-ups' }, 'Top-ups'),
            (s.topups || []).length ? el('ul', { class: 'plist' }, s.topups.map((t) => el('li', {}, el('b', {}, t.ref || 'top-up'), ` ${when(t.at)}: ${money(t.credit || 0)} of credit, ${t.source === 'link' ? 'from the payment page' : 'simulated, nothing charged'}`))) : el('p', { class: 'dim' }, `None yet. You started with ${money(start)} of credit.`),
            el('h2', { id: 'browser' }, 'Everything this site keeps in this browser'),
            el('p', {}, `${keep.length} item${keep.length === 1 ? '' : 's'}, all of it here and nowhere else: we cannot see any of it unless you send it. ${prefs}.`),
            keep.length ? table(['Key', 'What it is', 'Where', 'What is in it'], keyRows, 'account-keys') : el('p', { class: 'dim' }, 'Nothing.'),
            el('p', { class: 'account-actions' }, exporter(), del))
    }

    fetch('/examples/index.json').then((r) => r.json()).then((d) => { examples = d.examples || []; draw() }).catch(() => draw())
    draw()
    window.addEventListener('storage', (e) => { if (e.key && e.key.startsWith(PREFIX)) draw() })
    document.addEventListener('visibilitychange', () => { if (!document.hidden) draw() })
    window.setTimeout(draw, 1500)                                                     // after the meter has opened this page
}())
