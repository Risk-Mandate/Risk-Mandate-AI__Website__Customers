// ── demo.js — plays the demos: a session, line by line, on a drawn laptop or browser ──
//
// Each <figure class="demo"> holds its whole session as a list, so without this file,
// or for a reader who asked for reduced motion, every line is simply there. With it,
// the lines are hidden and shown in order once the figure scrolls into view: what the
// person types is typed out, what the agent and the harness answer appears after a
// pause, the screen scrolls with it, and the session starts again after a rest while
// it stays on screen. "Play again" restarts it. Only classes and text are set; no
// inline style, no storage, no network.

(function () {
    'use strict'
    const PAUSE  = Object.freeze({ user: 500, agent: 900, file: 350, ask: 600, ok: 500, sys: 700, tool: 600, deny: 800, prompt: 700, note: 300 })
    const TYPING = 28                                                                     // ms per character, capped so a long line still types in about two seconds
    const REST   = 5000
    const calm   = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const sleep  = (ms) => new Promise((ok) => window.setTimeout(ok, ms))

    function setUp(figure) {
        const list  = figure.querySelector('.demo-lines')
        const items = [...list.children].map((li) => ({ li, text: li.textContent, kind: li.dataset.kind }))
        let run = 0, visible = false, playing = false
        figure.classList.add('demo-js')                                               // hidden until it plays, so the first frame is not the whole session

        async function play() {
            if (playing) return
            playing = true
            const mine = ++run
            items.forEach(({ li }) => li.classList.remove('shown', 'typing'))
            list.scrollTop = 0
            for (const { li, text, kind } of items) {
                if (mine !== run) return
                await sleep(PAUSE[kind] || 500)
                li.classList.add('shown')
                if (kind === 'user') {
                    li.classList.add('typing')
                    const step = Math.max(8, Math.min(TYPING, 2000 / text.length))
                    for (let i = 1; i <= text.length; i++) {
                        if (mine !== run) return
                        li.textContent = text.slice(0, i)
                        if (i % 3 === 0) list.scrollTop = list.scrollHeight
                        await sleep(step)
                    }
                    li.classList.remove('typing')
                }
                list.scrollTop = list.scrollHeight
            }
            await sleep(REST)
            playing = false
            if (mine === run && visible) play()
        }

        function restart() { run++; playing = false; items.forEach(({ li, text }) => { li.textContent = text }); play() }

        const replay = figure.querySelector('.demo-replay')
        if (replay) replay.addEventListener('click', restart)
        if (!('IntersectionObserver' in window)) { visible = true; play(); return }
        new IntersectionObserver((entries) => {
            for (const entry of entries) {
                visible = entry.isIntersecting
                if (visible && !playing) play()
            }
        }, { threshold: 0.35 }).observe(figure)
    }

    if (calm) return                                                                      // every line stays shown, still and complete
    document.querySelectorAll('figure.demo').forEach(setUp)
}())
