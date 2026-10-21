// ── demo.js — plays the demos: a session, step by step, in a chat frame or on a drawn laptop ──
//
// Each <figure class="demo"> holds its whole session as a list, so without this file every
// line is simply there. With it, the reader gets controls under the frame: play and pause,
// back, next, start again, and which step of how many; the arrow keys step too, when the
// frame has focus. It plays once, the first time it scrolls into view, and stops at the end;
// for a reader who asked for reduced motion it does not play by itself and shows every step.
// What the person types is typed out (into the chat's input box, in a chat frame), and a
// new chat clears the screen, as it does. Only classes, attributes and text are set; no
// inline style, no storage, no network.

(function () {
    'use strict'
    const PAUSE  = Object.freeze({ user: 500, agent: 900, assistant: 1100, file: 350, ask: 600, ok: 500, sys: 700, tool: 700, deny: 800, prompt: 700, note: 300, act: 900, new: 700 })
    const TYPING = 24                                                                     // ms per character, capped so a long line still types in about two seconds
    const calm   = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const sleep  = (ms) => new Promise((ok) => window.setTimeout(ok, ms))

    function button(cls, label, text) {
        const b = document.createElement('button')
        b.type = 'button'
        b.className = cls
        b.setAttribute('aria-label', label)
        b.textContent = text
        return b
    }

    function setUp(figure) {
        const list  = figure.querySelector('.demo-lines')
        const items = [...list.children].map((li) => ({ li, text: li.textContent, kind: li.dataset.kind }))
        const chat  = figure.classList.contains('chat-frame')
        const input = figure.querySelector('.chat-input')
        const typed = figure.querySelector('.chat-typed')
        let n = calm ? items.length : 0, playing = false, run = 0, seen = false

        figure.classList.add('demo-js')
        figure.querySelectorAll('.demo-replay').forEach((b) => b.remove())
        const bar     = document.createElement('div')
        bar.className = 'demo-controls'
        const restart = button('dc dc-restart', 'Start again', '↺ Start again')
        const back    = button('dc dc-back', 'Back one step', '‹ Back')
        const toggle  = button('dc dc-play', 'Play', '▶ Play')
        const next    = button('dc dc-next', 'Next step', 'Next ›')
        const count   = document.createElement('span')
        count.className = 'dc-count'
        count.setAttribute('aria-live', 'polite')
        bar.append(restart, back, toggle, next, count)
        figure.insertBefore(bar, figure.querySelector('figcaption'))
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
            if (typed) typed.textContent = ''
            if (input) input.classList.remove('is-typing')
            list.scrollTop = list.scrollHeight
            count.textContent = `Step ${n} of ${items.length}`
            back.disabled    = n === 0
            next.disabled    = n === items.length
            toggle.textContent = playing ? '❚❚ Pause' : n === items.length ? '↺ Play again' : '▶ Play'
            toggle.setAttribute('aria-label', playing ? 'Pause' : 'Play')
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

        async function play() {
            if (n === items.length) n = 0
            playing = true
            const mine = ++run
            render()
            while (playing && mine === run && n < items.length) {
                const item = items[n]
                await sleep(PAUSE[item.kind] || 500)
                if (mine !== run) return
                if (item.kind === 'user' && !(await typeOut(item, mine))) return
                n++
                render()
            }
            if (mine === run) { playing = false; render() }
        }

        function stop() { playing = false; run++; render() }

        toggle.addEventListener('click', () => (playing ? stop() : play()))
        next.addEventListener('click', () => { stop(); if (n < items.length) n++; render() })
        back.addEventListener('click', () => { stop(); if (n > 0) n--; render() })
        restart.addEventListener('click', () => { stop(); n = 0; render(); play() })
        figure.addEventListener('keydown', (e) => {
            if (e.target.closest('button') && (e.key === ' ' || e.key === 'Enter')) return
            if (e.key === 'ArrowRight') { e.preventDefault(); next.click() }
            if (e.key === 'ArrowLeft')  { e.preventDefault(); back.click() }
        })
        render()

        if (calm || !('IntersectionObserver' in window)) return
        new IntersectionObserver((entries) => {
            for (const entry of entries) {
                if (entry.isIntersecting && !seen) { seen = true; play() }               // once, the first time it is seen; after that the reader decides
                if (!entry.isIntersecting && playing) stop()
            }
        }, { threshold: 0.35 }).observe(figure)
    }

    document.querySelectorAll('figure.demo').forEach(setUp)
}())
