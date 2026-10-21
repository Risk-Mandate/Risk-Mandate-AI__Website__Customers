// ── examples.js — the examples' tabs, the Claude or ChatGPT look, and the questions under each ──
//
// Tabs: without this file every example is on the page, one under the other, and each tab
// is a link to it. With it, one example shows at a time; the tab in the address (#ex-…)
// opens on load. The look: the chat frames are drawn like Claude's or ChatGPT's, and the
// reader's choice is kept in this browser for every frame. The questions: the answers
// become the body of an email the reader sends themselves, or copies; until then they are
// kept in this browser only. Nothing is sent by this file. Only classes, attributes and
// text are set.

(function () {
    'use strict'
    const LOOK_KEY = 'riskmandate.customers.look'
    const QUIZ_KEY = 'riskmandate.customers.quiz.'
    const store    = {
        get(k)    { try { return window.localStorage.getItem(k) } catch (e) { return null } },
        set(k, v) { try { window.localStorage.setItem(k, v) } catch (e) { /* private window: fine */ } },
    }

    // ── tabs ──────────────────────────────────────────────────────────────────
    document.querySelectorAll('[data-tabs]').forEach((box) => {
        const tabs   = [...box.querySelectorAll('[role="tab"]')]
        const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')))
        box.classList.add('tabs-js')
        function show(i, focus) {
            tabs.forEach((t, j) => {
                t.setAttribute('aria-selected', String(i === j))
                t.tabIndex = i === j ? 0 : -1
                panels[j].hidden = i !== j
            })
            if (focus) tabs[i].focus()
        }
        tabs.forEach((t, i) => {
            t.addEventListener('click', (e) => { e.preventDefault(); show(i); history.replaceState(null, '', '#' + panels[i].id) })
            t.addEventListener('keydown', (e) => {
                if (e.key === 'ArrowRight') { e.preventDefault(); show((i + 1) % tabs.length, true) }
                if (e.key === 'ArrowLeft')  { e.preventDefault(); show((i - 1 + tabs.length) % tabs.length, true) }
            })
        })
        const wanted = panels.findIndex((p) => '#' + p.id === location.hash)
        show(wanted >= 0 ? wanted : 0)
        box.querySelectorAll('a[href="#examples-start"]').forEach((a) => a.addEventListener('click', () => show(0)))
    })

    // ── the look ──────────────────────────────────────────────────────────────
    const frames = [...document.querySelectorAll('.chat-frame')]
    function look(name) {
        frames.forEach((f) => {
            f.classList.toggle('look-claude', name === 'claude')
            f.classList.toggle('look-chatgpt', name === 'chatgpt')
            f.querySelectorAll('[data-look]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.look === name)))
        })
    }
    frames.forEach((f) => f.querySelectorAll('[data-look]').forEach((b) => b.addEventListener('click', () => { look(b.dataset.look); store.set(LOOK_KEY, b.dataset.look) })))
    if (frames.length) look(store.get(LOOK_KEY) === 'chatgpt' ? 'chatgpt' : 'claude')

    // ── the questions ─────────────────────────────────────────────────────────
    document.querySelectorAll('.quiz').forEach((quiz) => {
        const slug    = quiz.dataset.quiz
        const key     = QUIZ_KEY + slug
        const send    = quiz.querySelector('.quiz-send')
        const copy    = quiz.querySelector('.quiz-copy')
        const status  = quiz.querySelector('.quiz-status')
        const note    = quiz.querySelector('textarea')
        const subject = `Example ${slug} v${quiz.dataset.exampleVersion}`

        function answers() {
            const out = {}
            quiz.querySelectorAll('fieldset').forEach((fs) => {
                const on = fs.querySelector('input:checked')
                out[fs.dataset.q] = { q: fs.querySelector('legend').textContent, a: on ? on.parentElement.textContent.trim() : '' }
            })
            out.note = { q: 'Anything else', a: note.value.trim() }
            return out
        }
        function body(a) {
            return [`${subject}, from ${location.href.split('#')[0]}`, '']
                .concat(Object.values(a).filter((x) => x.a).map((x) => `${x.q} ${x.a}`)).join('\n')
        }
        function update(save) {
            const a = answers()
            send.href = `mailto:${quiz.dataset.to}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body(a))}`
            if (save) store.set(key, JSON.stringify(Object.fromEntries(Object.entries(a).map(([k, v]) => [k, v.a]))))
        }
        try {                                                                           // what this reader answered before, in this browser
            const kept = JSON.parse(store.get(key) || '{}')
            quiz.querySelectorAll('fieldset').forEach((fs) => {
                fs.querySelectorAll('input').forEach((i) => { if (i.parentElement.textContent.trim() === kept[fs.dataset.q]) i.checked = true })
            })
            if (kept.note) note.value = kept.note
        } catch (e) { /* nothing kept */ }
        quiz.addEventListener('change', () => update(true))
        note.addEventListener('input', () => update(true))
        copy.addEventListener('click', async () => {
            try { await navigator.clipboard.writeText(body(answers())); status.textContent = 'Copied. Paste it anywhere, or into an email to us.' }
            catch (e) { status.textContent = 'Your browser would not copy; the Send by email button has the same text.' }
        })
        send.addEventListener('click', () => { status.textContent = 'Your email app should open with your answers in it. Thank you.' })
        update(false)
    })
}())
