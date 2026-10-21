// ── copy.js — the Copy buttons beside every snippet ──────────────────────────────
//
// A button with data-copy="<id>" copies the text of the element with that id, and
// says so for two seconds. Without JavaScript, or where the clipboard is refused,
// the text is still there to select by hand, and the button says that instead.
// No storage, no network.

(function () {
    'use strict'
    function say(button, text) {
        const was = button.dataset.label || button.textContent
        button.dataset.label = was
        button.textContent = text
        window.setTimeout(() => { button.textContent = was }, 2000)
    }
    document.addEventListener('click', (event) => {
        const button = event.target.closest && event.target.closest('button[data-copy]')
        if (!button) return
        const source = document.getElementById(button.dataset.copy)
        if (!source) return
        const text = source.textContent.replace(/\n+$/, '')
        if (!navigator.clipboard) { say(button, 'Select and copy'); return }
        navigator.clipboard.writeText(text).then(() => say(button, 'Copied'), () => say(button, 'Select and copy'))
    })
}())
