// ── present.js — the presenter for /present/: one beat at a time, with notes, a timer and an audience window ──
//
// The pattern is the Ultimate Insider's player (the-ultimate-insider.presentation.sgit.ai, Apache-2.0), rebuilt for
// this site's content security policy: no inline script or style, nothing loaded from elsewhere but the frames the
// page names. Without this file, /present/ is the whole talk as one page: every slide with what to say under it.
// With it, one beat fills the screen, and the keys are:
//   → / Space   next step (a reveal), then the next beat        ←   back a step, then the previous beat
//   ↓ / PageDown / N   next beat                                  ↑ / PageUp   previous beat
//   P   presenter notes: what to say, the cue, the links, what comes next, and the timers
//   A   an audience window for the projector, kept in step through the browser (no server)
//   G   every beat, by part, to jump to          B   a black screen          F   full screen
//   R   replay an animation                      T   restart the talk timer  X   leave, back to the page
//   ?   these keys                               #b-<id> in the address opens that beat
// An animation from another site loads only when its beat is shown and is dropped two beats later, so nothing
// plays unseen; a live demo, once booted, is kept. Only classes, attributes and text are set. The one thing kept
// in this browser is the talk timer's start, under riskmandate.customers.present.

(function () {
    'use strict'
    const deck = document.getElementById('deck')
    if (!deck) return
    const beats    = [...deck.querySelectorAll('section.beat')]
    const params   = new URLSearchParams(location.search)
    const audience = params.has('audience')
    const channel  = 'BroadcastChannel' in window ? new BroadcastChannel('rm-present') : null
    const KEY      = 'riskmandate.customers.present'
    const store    = { get() { try { return JSON.parse(localStorage.getItem(KEY) || '{}') } catch (e) { return {} } }, set(v) { try { localStorage.setItem(KEY, JSON.stringify(v)) } catch (e) { /* fine */ } } }
    const plan     = beats.reduce((n, b) => n + Number(b.dataset.dur || 0), 0)
    let i = 0, step = 0, black = false, notes = !audience && params.has('notes'), quiet = false
    let started = store.get().started || null, beatAt = Date.now()

    const el = (tag, cls, text, attrs) => { const n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; for (const [k, v] of Object.entries(attrs || {})) n.setAttribute(k, v); return n }
    const mmss = (s) => `${s < 0 ? '−' : ''}${Math.floor(Math.abs(s) / 60)}:${String(Math.floor(Math.abs(s) % 60)).padStart(2, '0')}`
    const stepsOf = (b) => Math.max(0, ...[...b.querySelectorAll('[data-step]')].map((x) => Number(x.dataset.step)))

    document.documentElement.classList.add('deck-on')
    if (audience) document.documentElement.classList.add('deck-audience')

    // ── the bar under the stage, and the panels ─────────────────────────────
    const ui     = el('div', 'deck-ui', null, { role: 'toolbar', 'aria-label': 'Presenter' })
    const prev   = el('button', 'dc', '‹', { type: 'button', 'aria-label': 'Previous' })
    const next   = el('button', 'dc dc-play', '›', { type: 'button', 'aria-label': 'Next' })
    const where  = el('span', 'deck-where')
    const clock  = el('span', 'deck-clock', null, { title: 'Talk time against the plan (T restarts it)' })
    const bNotes = el('button', 'dc', 'Notes · P', { type: 'button' })
    const bAud   = el('button', 'dc', 'Audience · A', { type: 'button' })
    const bAll   = el('button', 'dc', 'All beats · G', { type: 'button' })
    const bFull  = el('button', 'dc', 'Full screen · F', { type: 'button' })
    const bExit  = el('button', 'dc', 'Leave · X', { type: 'button' })
    const bar    = el('div', 'deck-progress'); const fill = el('i'); bar.append(fill)
    ui.append(prev, next, where, clock, bNotes, bAud, bAll, bFull, bExit)
    const side   = el('aside', 'deck-side', null, { 'aria-label': 'Presenter notes' })
    const grid   = el('nav', 'deck-grid', null, { 'aria-label': 'All beats', hidden: '' })
    const help   = el('div', 'deck-help', null, { hidden: '' })
    const curtain = el('div', 'deck-black', null, { hidden: '' })
    help.append(el('b', null, 'Keys'), el('p', null, '→ Space: next step · ←: back · ↓ N PageDown: next beat · ↑ PageUp: previous beat · P: notes · A: audience window · G: all beats · B: black · F: full screen · R: replay the animation · T: restart the timer · X: leave · ?: these keys'))
    deck.after(bar, ui, side, grid, help, curtain)

    let part = null
    beats.forEach((b, n) => {                                                          // the jump grid, by part
        if (b.dataset.partTitle !== part) { part = b.dataset.partTitle; grid.append(el('b', 'deck-grid-part', part)) }
        const a = el('button', 'deck-grid-beat', `${n + 1}. ${b.dataset.title}`, { type: 'button' })
        a.addEventListener('click', () => { go(n, 0); toggleGrid(false) })
        grid.append(a)
    })

    // ── frames: an animation loads when its beat shows, and goes two beats later ─────
    function frameIn(b) {
        const box = b.querySelector('.embed[data-frame]')
        if (!box || box.querySelector('iframe')) return
        const f = el('iframe', null, null, { src: box.dataset.frame, title: box.dataset.title || 'An animation', loading: 'eager', sandbox: 'allow-scripts allow-same-origin', referrerpolicy: 'no-referrer' })
        box.querySelector('.embed-wait') && box.querySelector('.embed-wait').remove()
        box.prepend(f)
    }
    function frameOut(b) { const f = b.querySelector('.embed[data-frame] iframe'); if (f) f.remove() }
    function replay() { const b = beats[i]; frameOut(b); frameIn(b) }
    deck.querySelectorAll('.boot[data-boot]').forEach((btn) => btn.addEventListener('click', () => {   // a live demo boots on a click, and is kept
        const box = btn.closest('.live-frame')
        if (box.querySelector('iframe')) return
        box.append(el('iframe', null, null, { src: btn.dataset.boot, title: btn.dataset.title || 'A live demo', sandbox: 'allow-scripts allow-same-origin', referrerpolicy: 'no-referrer' }))
        btn.textContent = 'Booting: one to two minutes'
        btn.disabled = true
    }))
    deck.querySelectorAll('.replay-btn').forEach((btn) => btn.addEventListener('click', replay))

    // ── counting up ────────────────────────────────────────────────────────
    function count(node) {
        if (node.dataset.counted) return
        node.dataset.counted = '1'
        const to = Number(node.dataset.count), t0 = performance.now(), dur = 1200
        const tick = (t) => { const p = Math.min(1, (t - t0) / dur); node.textContent = String(Math.round(to * (1 - Math.pow(1 - p, 3)))); if (p < 1) requestAnimationFrame(tick) }
        requestAnimationFrame(tick)
    }

    // ── showing a beat at a step ─────────────────────────────────────────────
    function render() {
        beats.forEach((b, n) => {
            b.classList.toggle('on', n === i)
            if (Math.abs(n - i) >= 2) frameOut(b)
        })
        const b = beats[i]
        frameIn(b)
        b.querySelectorAll('[data-step]').forEach((x) => x.classList.toggle('shown', Number(x.dataset.step) <= step))
        b.querySelectorAll('[data-count]').forEach((x) => {
            const host = x.closest('[data-step]')
            if (!host || Number(host.dataset.step) <= step) count(x)
            else { delete x.dataset.counted; x.textContent = '0' }
        })
        const max = stepsOf(b)
        where.textContent = `${i + 1} / ${beats.length} · ${b.dataset.partTitle}` + (max ? ` · step ${step} of ${max}` : '')
        fill.className = ''
        fill.dataset.p = String(Math.round(100 * (i + 1) / beats.length))
        bar.setAttribute('aria-valuenow', fill.dataset.p)
        bar.querySelectorAll('i').forEach((x) => { x.className = `w${Math.round(20 * (i + 1) / beats.length) * 5}` })
        prev.disabled = i === 0 && step === 0
        next.disabled = i === beats.length - 1 && step >= max
        if (history.replaceState) history.replaceState(null, '', location.pathname + location.search + '#b-' + b.dataset.id)
        notesPanel()
        curtain.hidden = !black
    }

    function notesPanel() {                                                            // what the presenter sees, beside the slide
        const b = beats[i], nx = beats[i + 1], src = b.querySelector('.notes')
        side.replaceChildren()
        side.hidden = !notes
        document.documentElement.classList.toggle('deck-notes', notes)
        if (!notes) return
        side.append(el('p', 'deck-side-k', `${i + 1}. ${b.dataset.partTitle} · planned ${mmss(Number(b.dataset.dur))}`), el('b', 'deck-side-t', b.dataset.title))
        const left = el('p', 'deck-side-left'); side.append(left)
        if (src) side.append(src.cloneNode(true))
        if (nx) side.append(el('p', 'deck-side-next', `Next: ${nx.dataset.title}`))
        tickClock()
    }

    function tickClock() {                                                             // the talk against the plan: teal ahead, amber a little late, red behind
        const done = beats.slice(0, i).reduce((n, b) => n + Number(b.dataset.dur || 0), 0)
        const elapsed = started ? (Date.now() - started) / 1000 : 0
        clock.textContent = started ? `${mmss(elapsed)} of ${mmss(plan)}` : `${mmss(plan)} planned · starts on the first move`
        clock.className = 'deck-clock ' + (!started ? '' : elapsed <= done + 15 ? 'ahead' : elapsed <= done + 90 ? 'late' : 'behind')
        const left = side.querySelector('.deck-side-left')
        if (left) { const s = Number(beats[i].dataset.dur) - (Date.now() - beatAt) / 1000; left.textContent = s >= 0 ? `${mmss(s)} left on this beat` : `${mmss(-s)} over on this beat`; left.className = 'deck-side-left ' + (s >= 0 ? 'ahead' : s > -30 ? 'late' : 'behind') }
    }
    setInterval(tickClock, 1000)

    function go(n, s, from) {
        n = Math.max(0, Math.min(beats.length - 1, n))
        if (n !== i) beatAt = Date.now()
        i = n; step = Math.max(0, Math.min(stepsOf(beats[i]), s))
        if (!started && !audience) { started = Date.now(); store.set({ started }) }
        render()
        if (channel && !from && !quiet) channel.postMessage({ i, step, black })
    }
    function forward() { if (step < stepsOf(beats[i])) go(i, step + 1); else if (i < beats.length - 1) go(i + 1, 0) }
    function backward() { if (step > 0) go(i, step - 1); else if (i > 0) go(i - 1, stepsOf(beats[i - 1])) }
    function toggleNotes() { notes = !notes; notesPanel() }
    function toggleGrid(on) { grid.hidden = on === undefined ? !grid.hidden : !on }
    function toggleBlack() { black = !black; render(); if (channel) channel.postMessage({ i, step, black }) }
    function full() { const d = document; if (d.fullscreenElement) d.exitFullscreen(); else if (d.documentElement.requestFullscreen) d.documentElement.requestFullscreen() }
    function leave() { document.documentElement.classList.remove('deck-on', 'deck-notes'); ui.remove(); side.remove(); bar.remove(); grid.remove(); help.remove(); curtain.remove(); beats.forEach((b) => { b.classList.add('on'); b.querySelectorAll('[data-step]').forEach((x) => x.classList.add('shown')) }); window.removeEventListener('keydown', keys) }

    prev.addEventListener('click', backward)
    next.addEventListener('click', forward)
    bNotes.addEventListener('click', toggleNotes)
    bAud.addEventListener('click', () => window.open(location.pathname + '?audience#b-' + beats[i].dataset.id, 'rm-present-audience', 'popup'))
    bAll.addEventListener('click', () => toggleGrid())
    bFull.addEventListener('click', full)
    bExit.addEventListener('click', leave)
    curtain.addEventListener('click', toggleBlack)

    function keys(e) {
        if (e.target.closest('input, textarea, select') || e.metaKey || e.ctrlKey || e.altKey) return
        const k = e.key
        if (k === 'ArrowRight' || k === ' ') { e.preventDefault(); forward() }
        else if (k === 'ArrowLeft') { e.preventDefault(); backward() }
        else if (k === 'ArrowDown' || k === 'PageDown' || k === 'n' || k === 'N') { e.preventDefault(); go(i + 1, 0) }
        else if (k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); go(i - 1, 0) }
        else if (k === 'Home') go(0, 0)
        else if (k === 'End') go(beats.length - 1, 0)
        else if (k === 'p' || k === 'P') toggleNotes()
        else if (k === 'a' || k === 'A') bAud.click()
        else if (k === 'g' || k === 'G' || k === 'o' || k === 'O') toggleGrid()
        else if (k === 'b' || k === 'B' || k === '.') toggleBlack()
        else if (k === 'f' || k === 'F') full()
        else if (k === 'r' || k === 'R') replay()
        else if (k === 't' || k === 'T') { started = Date.now(); store.set({ started }); tickClock() }
        else if (k === 'x' || k === 'X') leave()
        else if (k === '?') help.hidden = !help.hidden
        else if (k === 'Escape') { grid.hidden = true; help.hidden = true; if (black) toggleBlack() }
    }
    window.addEventListener('keydown', keys)
    if (channel) channel.onmessage = (m) => { quiet = true; black = !!m.data.black; go(m.data.i, m.data.step, true); quiet = false }

    const want = beats.findIndex((b) => '#b-' + b.dataset.id === location.hash)
    i = want >= 0 ? want : 0
    render()
    window.addEventListener('hashchange', () => {                                    // a link to a beat, on this page, goes to it
        const n = beats.findIndex((b) => '#b-' + b.dataset.id === location.hash)
        if (n >= 0 && n !== i) go(n, 0)
    })
}())
