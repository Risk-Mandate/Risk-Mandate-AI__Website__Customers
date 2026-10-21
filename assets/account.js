// ── account.js — your account: the balance, and the history of what you read and what it cost ──
//
// The meter (SG Meter, from api.newsroom.sgit.ai) keeps its state in this browser's local
// storage under the key in window.SG_METER_CONFIG. This file reads that state, at the
// meter's pinned version (v1.4.1, state v3), and draws this site's own account page from it:
// no newsroom, no personas, which are the newsroom's and not this site's (R002). It writes
// nothing to the meter's state; it can only export it. Text is only ever set with
// textContent.

(function () {
    'use strict'
    const host = document.getElementById('account-live')
    if (!host) return
    const cfg    = window.SG_METER_CONFIG || {}
    const key    = cfg.storageKey || 'sg.meter.v1'
    const symbol = cfg.symbol || '£'
    const start  = typeof cfg.start === 'number' ? cfg.start : 5000

    const money = (p) => `${p < -0.004 ? '−' : ''}${symbol}${(Math.abs(p) / 100).toFixed(2)}`
    const pence = (p) => { p = Math.round(p * 10) / 10; return p === 0 ? 'nothing' : `${p % 1 ? p.toFixed(1) : p}p` }
    const when  = (iso) => String(iso || '').slice(0, 16).replace('T', ' ')

    function el(tag, attrs, ...kids) {
        const node = document.createElement(tag)
        for (const [k, v] of Object.entries(attrs || {})) if (v != null) node.setAttribute(k, v)
        for (const kid of kids.flat()) if (kid != null) node.append(kid instanceof Node ? kid : String(kid))
        return node
    }

    function read() {
        try {
            const raw = window.localStorage.getItem(key)
            const s   = raw ? JSON.parse(raw) : {}
            return { balance: start, spent: 0, reads: 0, declined: 0, log: [], topups: [], ...s }
        } catch (e) {
            return null
        }
    }

    function exportState(s) {
        const blob = new Blob([JSON.stringify(s, null, 2)], { type: 'application/json' })
        const a    = el('a', { href: URL.createObjectURL(blob), download: `riskmandate-account-${new Date().toISOString().slice(0, 10)}.json` })
        document.body.append(a)
        a.click()
        a.remove()
    }

    function draw() {
        const s = read()
        if (!s) {
            host.replaceChildren(el('p', { class: 'note warn' }, 'This browser is not letting the site keep a balance (its storage is blocked), so every page starts again at ', money(start), '.'))
            return
        }
        const neg   = s.balance < 0
        const log   = Array.isArray(s.log) ? s.log : []
        const kinds = {}
        for (const e of log) {
            const k = kinds[e.kind] || (kinds[e.kind] = { pages: 0, cost: 0 })
            k.pages++
            k.cost += e.declined ? 0 : (e.cost || 0)
        }
        const exp = el('button', { type: 'button', class: 'btn' }, 'Export as JSON')
        exp.addEventListener('click', () => exportState(s))
        const card = el('div', { class: 'account-card' },
            el('div', {},
                el('span', { class: 'dim' }, neg ? 'Read beyond your credit' : 'Your balance'),
                el('b', { class: `account-balance${neg ? ' neg' : ''}` }, money(s.balance)),
                el('span', { class: 'dim' }, `${s.reads} page${s.reads === 1 ? '' : 's'} opened · ${money(s.spent)} spent of the ${money(start)} you started with`
                    + (s.declined ? ` · ${money(s.declined)} not charged at your request` : ''))),
            el('div', { class: 'account-actions' }, el('a', { class: 'btn btn-green', href: '/account/top-up.html' }, 'Top up'), exp))
        const byKind = Object.keys(kinds).length
            ? el('table', { class: 'account-kinds' },
                el('thead', {}, el('tr', {}, ['Kind of page', 'Pages', 'Spent'].map((h) => el('th', {}, h)))),
                el('tbody', {}, Object.entries(kinds).sort((a, b) => b[1].cost - a[1].cost).map(([k, v]) => el('tr', {}, el('td', {}, k), el('td', {}, String(v.pages)), el('td', {}, money(v.cost))))))
            : el('p', { class: 'dim' }, 'Nothing yet.')
        const rows = log.slice(0, 200).map((e) => el('tr', {},
            el('td', {}, when(e.at)),
            el('td', {}, el('a', { href: e.path }, String(e.title || e.path))),
            el('td', {}, e.kind || ''),
            el('td', {}, e.declined ? `not charged (${e.declined.reason || 'at your request'})` : `${pence(e.cost || 0)} (${Math.round((e.depth == null ? 1 : e.depth) * 100)}% read)`)))
        const history = rows.length
            ? el('div', { class: 'tablewrap' }, el('table', { class: 'account-history' }, el('thead', {}, el('tr', {}, ['When', 'Page', 'Kind', 'Cost'].map((h) => el('th', {}, h)))), el('tbody', {}, rows)))
            : el('p', { class: 'dim' }, 'No pages read yet in this browser.')
        const tops = (s.topups || []).map((t) => el('li', {}, el('b', {}, t.ref || 'top-up'), ` ${when(t.at)}: ${money(t.credit || 0)} of credit, ${t.source === 'link' ? 'from the payment page' : 'simulated, nothing charged'}`))
        host.replaceChildren(
            card,
            el('h2', { id: 'spent' }, 'Where it went, by kind of page'), byKind,
            el('h2', { id: 'history' }, 'Everything you have read'), history,
            el('h2', { id: 'top-ups' }, 'Top-ups'), tops.length ? el('ul', { class: 'plist' }, tops) : el('p', { class: 'dim' }, `None yet. You started with ${money(start)} of credit.`))
    }

    draw()
    window.addEventListener('storage', (e) => { if (e.key === key) draw() })
    document.addEventListener('visibilitychange', () => { if (!document.hidden) draw() })
    window.setTimeout(draw, 1500)                                                     // after the meter has opened this page
}())
