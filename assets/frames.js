// ── frames.js — an animation or live demo from another site, loaded only when the reader asks ──
//
// On /demos/ pages each .embed[data-frame] shows a Play button; pressing it loads the frame (the host must be one of
// the frame-src hosts this page's content security policy names). A .boot[data-boot] button does the same for a live
// demo, such as SHarness's kernel in a tab, which is heavy and is never loaded unasked. /present/ has its own player
// (assets/present.js) and is left alone. Only classes, attributes and text are set; no storage.

(function () {
    'use strict'
    if (document.getElementById('deck')) return
    const frame = (src, title) => {
        const f = document.createElement('iframe')
        f.src = src; f.title = title || 'An animation'
        f.setAttribute('sandbox', 'allow-scripts allow-same-origin'); f.setAttribute('referrerpolicy', 'no-referrer')
        return f
    }
    document.querySelectorAll('.embed[data-frame]').forEach((box) => {
        const btn = document.createElement('button')
        btn.type = 'button'; btn.className = 'btn btn-green embed-play'; btn.textContent = '▶ Play it here'
        btn.addEventListener('click', () => {
            const old = box.querySelector('iframe')
            if (old) old.remove()
            const wait = box.querySelector('.embed-wait'); if (wait) wait.hidden = true
            box.prepend(frame(box.dataset.frame, box.dataset.title))
            btn.textContent = '↺ Play again'
        })
        const cap = box.querySelector('figcaption')
        cap ? cap.prepend(btn) : box.append(btn)
    })
    document.querySelectorAll('.boot[data-boot]').forEach((btn) => btn.addEventListener('click', () => {
        const box = btn.closest('.live-frame')
        if (box.querySelector('iframe')) return
        box.append(frame(btn.dataset.boot, btn.dataset.title))
        btn.textContent = 'Booting: one to two minutes'
        btn.disabled = true
    }))
}())
