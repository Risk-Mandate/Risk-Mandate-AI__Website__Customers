// ── examples.js — the examples' tabs, the Claude or ChatGPT look, and the questions under each ──
//
// Tabs: without this file every example is on the page, one under the other, and each tab
// is a link to it. With it, one example shows at a time; the tab in the address (#ex-…)
// opens on load. The look: the chat frames are drawn like Claude's or ChatGPT's, and the
// reader's choice is kept in this browser for every frame. The questions: the answers are
// kept in this browser until the reader chooses Encrypt and send (assets/envelope.js) or Copy. Only classes, attributes and
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

    // ── the questions, and anything else a reader writes to us ─────────────────
    // Encrypt and send (assets/envelope.js) is the main way; Copy is the other; an email with the
    // same text appears only if sending fails. The answers are kept in this browser until sent.
    function wire(box, { form, subject, body, about, save }) {
        const send   = box.querySelector('.send-encrypted')
        const copy   = box.querySelector('.quiz-copy')
        const status = box.querySelector('.quiz-status')
        const mail   = box.querySelector('.quiz-mail')
        const peek   = box.querySelector('.send-preview code')
        const to     = box.dataset.to
        function update(keep) {
            const text = body()
            if (peek) peek.textContent = `To: the agent at ${to}\nSubject: ${subject()}\n\n${text}`
            if (mail) mail.href = `mailto:${to}?subject=${encodeURIComponent(subject())}&body=${encodeURIComponent(text)}`
            if (keep && save) save()
        }
        box.addEventListener('change', () => update(true))
        box.addEventListener('input', () => update(true))
        if (copy) copy.addEventListener('click', async () => {
            try { await navigator.clipboard.writeText(body()); status.textContent = 'Copied. Paste it anywhere.' }
            catch (e) { status.textContent = 'Your browser would not copy; the preview above has the same text.' }
        })
        send.addEventListener('click', async () => {
            if (!body().trim()) { status.textContent = 'There is nothing to send yet.'; return }
            send.disabled = true
            status.textContent = 'Encrypting in this browser, then sending\u2026'
            const r = window.RMSend ? await window.RMSend.send({ form, subject: subject(), body: body(), about }) : { ok: false, why: 'the sender did not load' }
            send.disabled = false
            if (r.ok) { status.textContent = `Sent, encrypted, at ${new Date().toLocaleTimeString()}. Only RiskMandate can read it. Thank you.`; if (mail) mail.hidden = true; box.classList.add('is-sent') }
            else { status.textContent = `It did not go (${r.why}). Copy it, or send it by email instead:`; if (mail) mail.hidden = false }
        })
        update(false)
    }

    document.querySelectorAll('.quiz').forEach((quiz) => {
        const slug    = quiz.dataset.quiz
        const version = quiz.dataset.exampleVersion
        const key     = QUIZ_KEY + slug
        const note    = quiz.querySelector('textarea')
        const subject = () => `Example ${slug} v${version}: answers`
        function answers() {
            const out = {}
            quiz.querySelectorAll('fieldset').forEach((fs) => {
                const on = fs.querySelector('input:checked')
                out[fs.dataset.q] = { q: fs.querySelector('legend').textContent, a: on ? on.parentElement.textContent.trim() : '' }
            })
            out.note = { q: 'Anything else:', a: note.value.trim() }
            return out
        }
        const body = () => {
            const lines = Object.values(answers()).filter((x) => x.a).map((x) => `${x.q} ${x.a}`)
            return lines.length ? [`Example ${slug}, version ${version}, from ${location.href.split('#')[0]}`, ''].concat(lines).join('\n') : ''
        }
        try {                                                                           // what this reader answered before, in this browser
            const kept = JSON.parse(store.get(key) || '{}')
            quiz.querySelectorAll('fieldset').forEach((fs) => {
                fs.querySelectorAll('input').forEach((i) => { if (i.parentElement.textContent.trim() === kept[fs.dataset.q]) i.checked = true })
            })
            if (kept.note) note.value = kept.note
        } catch (e) { /* nothing kept */ }
        wire(quiz, { form: 'example-answers', subject, body, about: `example ${slug} v${version}`,
                     save: () => store.set(key, JSON.stringify({ ...Object.fromEntries(Object.entries(answers()).map(([k, v]) => [k, v.a])), version, at: new Date().toISOString() })) })
    })

    document.querySelectorAll('.send-box').forEach((box) => {                          // a free message, on /feedback/, or a scenario, on the home page
        const text = box.querySelector('textarea')
        const who  = box.querySelector('input[name="who"]')
        const scen = box.classList.contains('scenario-box')
        wire(box, { form: scen ? 'scenario' : 'message', about: scen ? 'a scenario to add' : 'a message',
                    subject: () => scen ? 'A scenario to add' : `A message from ${who && who.value.trim() ? who.value.trim() : 'a reader'}`,
                    body: () => text.value.trim() ? (who && who.value.trim() ? `From: ${who.value.trim()}\n\n` : '') + text.value.trim() : '' })
    })
}())
