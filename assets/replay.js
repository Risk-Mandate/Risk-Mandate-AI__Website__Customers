// ── replay.js — plays a real run back: its screenshots, step by step, beside a flow chart and what each step means ──
//
// A <figure class="replay"> holds every step of a run as a list of screenshots (.rp-shots), a note per step
// (.rp-notes: what is on the screen, what it means, and, for an assistant's answer, what the page said it
// would write beside what it wrote), and a flow chart (.rp-flow) whose nodes name the steps they cover. Without
// this file all of it is simply on the page. With it, one step shows at a time, with the same controls as
// the demos (start again, back, play or pause, next, a bar of the steps grouped by section, the arrow keys),
// a pace, a countdown before each new section, and an end that says so. It starts by itself only once the
// reader has scrolled to it. If the figure names a storyboard (data-sync, the id of a .sb-host on the page)
// and a step names a panel (data-panel), the storyboard turns to that panel as the step plays: the real run
// and the drawn one, together. Only classes, attributes and text are set; no storage, no network.

(function () {
    'use strict'
    const PACES   = Object.freeze({ relaxed: 7000, normal: 4500, quick: 2500 })
    const BREATHE = 4
    const calm    = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const sleep   = (ms) => new Promise((ok) => window.setTimeout(ok, ms))
    let scrolled  = false
    window.addEventListener('scroll', () => { scrolled = true }, { passive: true, once: true })

    function el(tag, cls, text, attrs) {
        const node = document.createElement(tag)
        if (cls) node.className = cls
        if (text != null) node.textContent = text
        for (const [k, v] of Object.entries(attrs || {})) node.setAttribute(k, v)
        return node
    }

    function setUp(fig) {
        const shots = [...fig.querySelectorAll('.rp-shots > li')]
        const notes = [...fig.querySelectorAll('.rp-notes > li')]
        const nodes = [...fig.querySelectorAll('.rp-flow [data-steps]')]
        const place = fig.querySelector('.rp-place')
        const N     = shots.length
        let n = 1, playing = false, run = 0, seen = false, pace = 'normal'
        if (!N) return
        fig.classList.add('rp-js')

        const bar = el('div', 'demo-steps rp-bar', null, { role: 'group', 'aria-label': 'Steps' })
        let last = null
        const marks = shots.map((li, i) => {
            const m = el('button', 'ds' + (li.dataset.section !== last && i ? ' ds-act' : ''), null, { type: 'button', 'aria-label': `Go to step ${i + 1}: ${li.dataset.title || ''}` })
            last = li.dataset.section
            m.addEventListener('click', () => jump(i + 1))
            bar.append(m)
            return m
        })
        fig.insertBefore(bar, fig.firstElementChild)

        const end   = el('div', 'demo-end', null, { role: 'status' })
        const again = el('button', 'dc dc-again', '↺ Start again', { type: 'button' })
        end.append(el('b', null, 'The end of this replay.'), again)
        const ctl     = el('div', 'demo-controls')
        const restart = el('button', 'dc dc-restart', '↺ Start again', { type: 'button' })
        const back    = el('button', 'dc dc-back', '‹ Back', { type: 'button', 'aria-label': 'Back one step' })
        const toggle  = el('button', 'dc dc-play', '▶ Play', { type: 'button' })
        const next    = el('button', 'dc dc-next', 'Next ›', { type: 'button', 'aria-label': 'Next step' })
        const count   = el('span', 'dc-count', null, { 'aria-live': 'polite' })
        const wait    = el('span', 'dc-wait', null, { 'aria-live': 'polite' })
        const paceSel = el('select', 'rp-pace', null, { 'aria-label': 'Pace' })
        for (const p of Object.keys(PACES)) { const o = el('option', null, p, { value: p }); if (p === pace) o.selected = true; paceSel.append(o) }
        paceSel.addEventListener('change', () => { pace = paceSel.value })
        ctl.append(restart, back, toggle, next, count, el('label', 'rp-pace-label', 'Pace '), paceSel, wait)
        ctl.querySelector('.rp-pace-label').append(paceSel)
        fig.querySelector('figcaption') ? fig.insertBefore(ctl, fig.querySelector('figcaption')) : fig.append(ctl)
        ctl.before(end)
        if (!fig.hasAttribute('tabindex')) fig.tabIndex = -1

        const sync = fig.dataset.sync ? document.getElementById(fig.dataset.sync) : null
        function turnStoryboard(i) {                                                 // the drawn run follows the real one
            if (!sync) return
            const track = sync.querySelector('.sb-track')
            const panel = Number(shots[i - 1].dataset.panel)
            if (!track || !panel) return
            track.scrollTo({ left: (panel - 1) * track.clientWidth, behavior: calm ? 'auto' : 'smooth' })
        }

        function render() {
            shots.forEach((li, i) => li.classList.toggle('on', i === n - 1))
            notes.forEach((li, i) => li.classList.toggle('on', i === n - 1))
            nodes.forEach((node) => {
                const covers = node.dataset.steps.split(' ').map(Number)
                node.classList.toggle('on', covers.includes(n))
                node.classList.toggle('done', covers.some((s) => s < n) && !covers.includes(n))
            })
            marks.forEach((m, i) => { m.classList.toggle('done', i < n); m.classList.toggle('now', i === n - 1) })
            const li = shots[n - 1]
            if (place) place.textContent = li.dataset.where || ''
            fig.dataset.place = li.dataset.place || ''
            const img = li.querySelector('img')
            if (img && img.loading === 'lazy') img.loading = 'eager'
            const ahead = shots[n] && shots[n].querySelector('img')                    // fetch the next one before it is needed
            if (ahead) ahead.loading = 'eager'
            count.textContent = n === N && !playing ? `Done: step ${N} of ${N}` : `Step ${n} of ${N}`
            fig.classList.toggle('is-ended', n === N && !playing)
            back.disabled = n === 1
            next.disabled = n === N
            toggle.textContent = playing ? '❚❚ Pause' : n === N ? '↺ Play again' : '▶ Play'
            toggle.setAttribute('aria-label', playing ? 'Pause' : 'Play')
            turnStoryboard(n)
            if (sync && n === N && !playing && fig.dataset.panelEnd) {                // at the end, the storyboard's last word
                const track = sync.querySelector('.sb-track')
                if (track) track.scrollTo({ left: (Number(fig.dataset.panelEnd) - 1) * track.clientWidth, behavior: calm ? 'auto' : 'smooth' })
            }
        }

        async function play() {
            if (n === N) n = 1
            playing = true
            const mine = ++run
            render()
            while (playing && mine === run && n < N) {
                await sleep(PACES[pace])
                if (mine !== run) return
                if (shots[n].dataset.section !== shots[n - 1].dataset.section) {       // a new section: say what comes, and wait
                    for (let s = BREATHE; s > 0; s--) {
                        if (mine !== run) return
                        wait.textContent = `Next: ${shots[n].dataset.sectionTitle || 'the next part'}, in ${s}s`
                        await sleep(1000)
                    }
                    wait.textContent = ''
                }
                if (mine !== run) return
                n++
                render()
            }
            if (mine === run) { playing = false; render() }
        }
        function halt() { run++; seen = true; wait.textContent = '' }                 // any use of the controls: the reader has taken over, so it never starts by itself
        function stop() { playing = false; halt(); render() }
        function jump(to) { const was = playing; halt(); playing = false; n = Math.max(1, Math.min(N, to)); render(); if (was && n < N) play() }

        toggle.addEventListener('click', () => (playing ? stop() : play()))
        next.addEventListener('click', () => jump(n + 1))
        back.addEventListener('click', () => jump(n - 1))
        restart.addEventListener('click', () => { halt(); n = 1; render(); play() })
        again.addEventListener('click', () => { halt(); n = 1; render(); play() })
        nodes.forEach((node) => {
            node.setAttribute('role', 'button'); node.tabIndex = 0
            const go = () => jump(Number(node.dataset.steps.split(' ')[0]))
            node.addEventListener('click', go)
            node.addEventListener('keydown', (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go() } })
        })
        fig.addEventListener('keydown', (e) => {
            if (e.target.closest('button, select, [role="button"]') && (e.key === ' ' || e.key === 'Enter')) return
            if (e.key === 'ArrowRight') { e.preventDefault(); next.click() }
            if (e.key === 'ArrowLeft')  { e.preventDefault(); back.click() }
        })
        render()
        fig.rpJump = (to) => { fig.scrollIntoView({ behavior: calm ? 'auto' : 'smooth', block: 'start' }); jump(to) }

        if (calm || !('IntersectionObserver' in window)) return
        let visible = false
        const tryStart = () => { if (visible && scrolled && !seen) { seen = true; play() } }
        window.addEventListener('scroll', () => window.setTimeout(tryStart, 300), { passive: true })
        new IntersectionObserver((entries) => {
            for (const entry of entries) {
                visible = entry.intersectionRatio >= 0.5
                tryStart()
                if (!entry.isIntersecting && playing) stop()
            }
        }, { threshold: [0, 0.5] }).observe(fig)
    }

    document.querySelectorAll('figure.replay').forEach(setUp)
    document.addEventListener('click', (e) => {                                      // a link elsewhere on the page that opens a step: data-replay-jump="<figure id>:<step>"
        const a = e.target.closest('[data-replay-jump]')
        if (!a) return
        const [id, step] = a.dataset.replayJump.split(':')
        const fig = document.getElementById(id)
        if (!fig || !fig.rpJump) return
        e.preventDefault()
        fig.rpJump(Number(step))
    })
}())
