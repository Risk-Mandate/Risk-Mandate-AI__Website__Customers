// ── demo.js — plays the demos: a session, step by step, in a chat frame or on a drawn laptop ──
//
// Each <figure class="demo"> holds its whole session as a list, so without this file every
// line is simply there. With it, the reader gets a bar of the steps across the top, one mark
// per step, grouped by act and clickable, and controls under the frame: start again, back,
// play or pause, next, and which step of how many; the arrow keys step too. Back and next
// keep it playing if it was. It starts by itself only once the reader has scrolled and the
// frame is mostly on screen, plays once, and says plainly when it has reached the end. Before
// each new act it waits a few seconds, with a countdown the reader can pause or skip, so
// what just happened can sink in. For a reader who asked for reduced motion it never starts
// by itself and shows every step. What the person types is typed into the chat's input box;
// a new chat clears the screen, as it does.
// It keeps one thing in this browser, for the account page: how far the reader got in each
// example, under riskmandate.customers.progress. Only classes, attributes and text are set;
// no inline style, no network.

(function () {
    'use strict'
    const PAUSE    = Object.freeze({ user: 500, agent: 900, assistant: 1100, file: 350, ask: 600, ok: 500, sys: 700, tool: 700, deny: 800, prompt: 700, note: 300, act: 400, new: 700 })
    const TYPING   = 24                                                                   // ms per character, capped so a long line still types in about two seconds
    const BREATHE  = 6                                                                    // seconds of countdown before each act after the first
    const KEY      = 'riskmandate.customers.progress'
    const calm     = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const sleep    = (ms) => new Promise((ok) => window.setTimeout(ok, ms))
    let scrolled   = false
    window.addEventListener('scroll', () => { scrolled = true }, { passive: true, once: true })

    const progress = {
        read()        { try { return JSON.parse(window.localStorage.getItem(KEY) || '{}') } catch (e) { return {} } },
        note(id, n, of) {
            if (!id) return
            try {
                const all = this.read(), was = all[id] || { furthest: 0 }
                all[id] = { furthest: Math.max(was.furthest || 0, n), of, finished: !!was.finished || n === of, at: new Date().toISOString(), first: was.first || new Date().toISOString() }
                window.localStorage.setItem(KEY, JSON.stringify(all))
            } catch (e) { /* private window: fine */ }
        },
    }

    function el(tag, cls, text, attrs) {
        const node = document.createElement(tag)
        if (cls) node.className = cls
        if (text != null) node.textContent = text
        for (const [k, v] of Object.entries(attrs || {})) node.setAttribute(k, v)
        return node
    }

    function setUp(figure) {
        const list  = figure.querySelector('.demo-lines')
        const items = [...list.children].map((li) => ({ li, text: li.textContent, kind: li.dataset.kind }))
        const N     = items.length
        const chat  = figure.classList.contains('chat-frame')
        const input = figure.querySelector('.chat-input')
        const typed = figure.querySelector('.chat-typed')
        const id    = figure.dataset.example || figure.dataset.demo
        let n = calm ? N : 0, playing = false, run = 0, seen = false, waiting = 0

        figure.classList.add('demo-js')
        figure.querySelectorAll('.demo-replay').forEach((b) => b.remove())

        // the bar of steps, one mark per step, grouped by act
        const bar   = el('div', 'demo-steps', null, { role: 'group', 'aria-label': 'Steps' })
        let act = 0
        const marks = items.map((item, i) => {
            if (item.kind === 'act') act++
            const m = el('button', `ds ds-${item.kind}${act ? ' act-' + act : ''}`, null, { type: 'button', 'aria-label': `Go to step ${i + 1}` })
            m.addEventListener('click', () => jump(i + 1))
            bar.append(m)
            return m
        })
        const acts = items.filter((it) => it.kind === 'act').map((it) => it.text.replace(/^\d+ · /, ''))
        const head = figure.querySelector('.chat-window, .demo-laptop, .demo-browser')
        figure.insertBefore(bar, head)
        const hint = chat ? el('li', 'chat-hint shown', 'Press Play, or Next to go one step at a time.', { 'aria-hidden': 'true' }) : null   // an empty frame looks broken (run C1)
        if (hint) list.prepend(hint)

        // the end, said plainly
        const end   = el('div', 'demo-end', null, { role: 'status' })
        const again = el('button', 'dc dc-again', '↺ Start again', { type: 'button' })
        end.append(el('b', null, 'The end of this example.'), again)
        const tryIt = figure.closest('.ex-panel, main') && figure.closest('.ex-panel, main').querySelector('.try-box')
        if (tryIt) { const a = el('a', 'demo-end-try', 'Now try it yourself →', { href: '#' }); a.addEventListener('click', (e) => { e.preventDefault(); tryIt.scrollIntoView({ behavior: 'smooth', block: 'start' }) }); end.append(a) }
        head.after(end)

        // the controls
        const ctl     = el('div', 'demo-controls')
        const restart = el('button', 'dc dc-restart', '↺ Start again', { type: 'button', 'aria-label': 'Start again' })
        const back    = el('button', 'dc dc-back', '‹ Back', { type: 'button', 'aria-label': 'Back one step' })
        const toggle  = el('button', 'dc dc-play', '▶ Play', { type: 'button', 'aria-label': 'Play' })
        const next    = el('button', 'dc dc-next', 'Next ›', { type: 'button', 'aria-label': 'Next step' })
        const count   = el('span', 'dc-count', null, { 'aria-live': 'polite' })
        const wait    = el('span', 'dc-wait', null, { 'aria-live': 'polite' })
        ctl.append(restart, back, toggle, next, count, wait)
        end.after(ctl)
        if (!figure.hasAttribute('tabindex')) figure.tabIndex = -1

        function render() {
            let cleared = -1
            if (chat) items.forEach(({ kind }, i) => { if (kind === 'new' && i < n) cleared = i })
            items.forEach(({ li, text }, i) => {
                li.classList.toggle('shown', i < n)
                li.classList.toggle('gone', i < cleared)
                li.classList.remove('typing')
                if (li.textContent !== text) li.textContent = text
            })
            marks.forEach((m, i) => { m.classList.toggle('done', i < n); m.classList.toggle('now', i === n - 1) })
            if (hint) hint.hidden = n > 0
            if (typed) typed.textContent = ''
            if (input) input.classList.remove('is-typing')
            list.scrollTop = list.scrollHeight
            const actNow = items.slice(0, n).filter((it) => it.kind === 'act').length
            count.textContent = n === N ? `Done: step ${N} of ${N}` : `Step ${n} of ${N}` + (actNow ? ` · act ${actNow} of ${acts.length || 1}` : '')
            figure.classList.toggle('is-ended', n === N)
            figure.classList.toggle('is-playing', playing)
            back.disabled = n === 0
            next.disabled = n === N
            toggle.textContent = playing ? '❚❚ Pause' : n === N ? '↺ Play again' : '▶ Play'
            toggle.setAttribute('aria-label', playing ? 'Pause' : 'Play')
            if (!waiting) wait.textContent = ''
        }

        async function typeOut(item, mine) {                                          // the person's line, typed: into the input box in a chat, in place on a terminal
            const step = Math.max(8, Math.min(TYPING, 1800 / item.text.length))
            if (chat && typed) {
                input.classList.add('is-typing')
                for (let i = 1; i <= item.text.length; i++) {
                    if (mine !== run) return false
                    typed.textContent = item.text.slice(0, i)
                    await sleep(step)
                }
                await sleep(250)
                return mine === run
            }
            item.li.classList.add('shown', 'typing')
            for (let i = 1; i <= item.text.length; i++) {
                if (mine !== run) return false
                item.li.textContent = item.text.slice(0, i)
                if (i % 3 === 0) list.scrollTop = list.scrollHeight
                await sleep(step)
            }
            return mine === run
        }

        async function breathe(mine, label) {                                         // a countdown before a new act; pause stops it, next skips it
            for (let s = BREATHE; s > 0; s--) {
                if (mine !== run) return false
                waiting = s
                wait.textContent = `Next: ${label}, in ${s}s`
                await sleep(1000)
            }
            waiting = 0
            wait.textContent = ''
            return mine === run
        }

        async function play() {
            if (n === N) n = 0
            playing = true
            const mine = ++run
            render()
            while (playing && mine === run && n < N) {
                const item = items[n]
                if (item.kind === 'act' && n > 0) { if (!(await breathe(mine, item.text.replace(/^\d+ · /, '').replace(/\.$/, '')))) return }
                else await sleep(PAUSE[item.kind] || 500)
                if (mine !== run) return
                if (item.kind === 'user' && !(await typeOut(item, mine))) return
                n++
                progress.note(id, n, N)
                render()
            }
            if (mine === run) { playing = false; render() }
        }

        function halt() { run++; seen = true; waiting = 0; wait.textContent = '' }     // any use of the controls: the reader has taken over, so it never starts by itself
        function stop() { playing = false; halt(); render() }
        function jump(to) {                                                            // move to a step, and keep playing if it was
            const was = playing
            halt()
            n = Math.max(0, Math.min(N, to))
            progress.note(id, n, N)
            playing = false
            render()
            if (was && n < N) play()
        }

        toggle.addEventListener('click', () => (playing ? stop() : play()))
        next.addEventListener('click', () => jump(n + 1))
        back.addEventListener('click', () => jump(n - 1))
        restart.addEventListener('click', () => { halt(); n = 0; render(); play() })
        again.addEventListener('click', () => { halt(); n = 0; render(); play() })
        figure.addEventListener('keydown', (e) => {
            if (e.target.closest('button') && (e.key === ' ' || e.key === 'Enter')) return
            if (e.key === 'ArrowRight') { e.preventDefault(); next.click() }
            if (e.key === 'ArrowLeft')  { e.preventDefault(); back.click() }
        })
        render()

        if (calm || !('IntersectionObserver' in window)) return
        let visible = false
        const tryStart = () => { if (visible && scrolled && !seen) { seen = true; play() } }
        window.addEventListener('scroll', () => window.setTimeout(tryStart, 300), { passive: true })
        new IntersectionObserver((entries) => {
            for (const entry of entries) {
                visible = entry.intersectionRatio >= 0.6
                tryStart()                                                             // only once the reader has scrolled to it: never on a page that has just opened
                if (!entry.isIntersecting && playing) stop()
            }
        }, { threshold: [0, 0.6] }).observe(figure)
    }

    document.querySelectorAll('figure.demo').forEach(setUp)
}())
