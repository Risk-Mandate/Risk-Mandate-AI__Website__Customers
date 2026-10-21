// ── theme.js — six themes, one attribute, one storage key ─────────────────────
//
// A CLASSIC SCRIPT, loaded in <head> without defer, before the stylesheets, so the
// theme is set before the first paint and nothing flashes. It does nothing slow.
// The stored value is checked against THEMES before it reaches the DOM: local
// storage is writable by anything on this origin, so an unknown value is the
// default rather than an attribute nobody declared. With nothing stored, the
// reader's prefers-color-scheme picks between the two defaults; the first choice
// in the picker ends that, and from then on the reader's word is the one kept.
// The choice stays in this browser and never leaves it. The list repeats
// data/themes.json; tests/build/test_themes.py checks the two agree. The colours
// are in assets/themes.css; this file never names one.

(function () {
    'use strict'
    const KEY     = 'riskmandate.customers.theme'
    const LIGHT   = 'riskmandate'
    const DARK    = 'canvas'
    const THEMES  = Object.freeze({
        riskmandate : 'RiskMandate',
        canvas      : 'Canvas',
        night       : 'Night',
        ember       : 'Ember',
        paper       : 'Paper',
        blueprint   : 'Blueprint',
    })
    const root    = document.documentElement
    const known   = (name) => Object.prototype.hasOwnProperty.call(THEMES, name)

    function stored() {
        try { const v = window.localStorage.getItem(KEY); return known(v) ? v : null } catch (error) { return null }   // storage blocked: still a colour, just not remembered
    }
    function system() {
        try { return window.matchMedia('(prefers-color-scheme: dark)').matches ? DARK : LIGHT } catch (error) { return LIGHT }
    }
    function current() { return stored() || system() }
    function apply(name) {
        root.dataset.theme = known(name) ? name : LIGHT
        mark()
    }
    function choose(name) {
        if (!known(name)) return
        try { window.localStorage.setItem(KEY, name) } catch (error) { /* applied, not remembered */ }
        apply(name)
    }

    // the picker: chrome.py draws it in the header; this marks the current entry and wires it
    function mark() {
        const name = root.dataset.theme
        for (const button of document.querySelectorAll('[data-theme-pick]')) {
            button.setAttribute('aria-pressed', button.dataset.themePick === name ? 'true' : 'false')
        }
        const toggle = document.querySelector('.theme-pick > button')
        if (!toggle) return
        const swatch = toggle.querySelector('.sw')
        const label  = toggle.querySelector('.name')
        if (swatch) swatch.className = 'sw sw-' + name
        if (label)  label.textContent = THEMES[name] || THEMES[LIGHT]
    }
    function wire() {
        const pick = document.querySelector('.theme-pick')
        if (!pick) return
        const toggle = pick.querySelector(':scope > button')
        const menu   = pick.querySelector('ul')
        const close  = () => { menu.hidden = true; toggle.setAttribute('aria-expanded', 'false') }
        toggle.addEventListener('click', (event) => {
            event.stopPropagation()
            menu.hidden = !menu.hidden
            toggle.setAttribute('aria-expanded', String(!menu.hidden))
            if (!menu.hidden) { const on = menu.querySelector('[aria-pressed="true"]'); if (on) on.focus() }
        })
        menu.addEventListener('click', (event) => {
            const button = event.target.closest('[data-theme-pick]')
            if (!button) return
            choose(button.dataset.themePick)
            close()
            toggle.focus()
        })
        menu.addEventListener('keydown', (event) => {                                       // the arrows move, Escape closes and returns focus
            const list = [...menu.querySelectorAll('[data-theme-pick]')]
            const i    = list.indexOf(document.activeElement)
            if (event.key === 'ArrowDown') { event.preventDefault(); list[(i + 1) % list.length].focus() }
            else if (event.key === 'ArrowUp') { event.preventDefault(); list[(i - 1 + list.length) % list.length].focus() }
            else if (event.key === 'Escape') { close(); toggle.focus() }
        })
        document.addEventListener('click', (event) => { if (!pick.contains(event.target)) close() })
        mark()
    }

    apply(current())
    try {                                                                                   // the system can change while the page is open; follow it only until the reader has chosen
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { if (!stored()) apply(system()) })
    } catch (error) { /* an old browser: no following */ }
    window.addEventListener('storage', (event) => { if (event.key === KEY) apply(current()) })   // another tab chose: follow it
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire)
    else wire()
}())
