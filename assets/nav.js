// ── nav.js — the header interaction: the phone menu button and tap-to-open groups ──
//
// On a desktop a dropdown opens on hover and :focus-within in CSS alone, and
// every group label is a link to that section's own page, so if this file never
// loads the nav still works. This handles the rest: the phone menu button, and
// the fact that a finger has no hover. Served from this origin only (CSP
// script-src 'self'). No storage, no network, no state beyond the open class.

(function () {
    'use strict'
    const top = document.querySelector('header.top')
    if (!top) return
    const toggle = top.querySelector('.navtoggle')
    if (toggle) {
        toggle.addEventListener('click', () => {
            const open = top.classList.toggle('nav-open')
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false')
        })
    }
    // On a touch screen the first tap on a group label opens its menu, a second
    // follows the link. Only where a dropdown is actually drawn; in the phone
    // menu the children are already visible.
    document.addEventListener('click', (event) => {
        const link = event.target.closest && event.target.closest('header.top .navgroup > .navgroup-btn')
        const open = top.querySelector('.navgroup.open')
        if (open && (!link || link.parentNode !== open)) open.classList.remove('open')
        if (!link || !window.matchMedia || !window.matchMedia('(hover: none)').matches) return
        const group = link.parentNode
        const menu  = group.querySelector('.navmenu')
        if (menu && window.getComputedStyle(menu).position === 'absolute' && !group.classList.contains('open')) {
            event.preventDefault()
            group.classList.add('open')
        }
    })
    // Escape closes whatever is open, so keyboard users get out the same way everywhere.
    document.addEventListener('keydown', (event) => {
        if (event.key !== 'Escape') return
        const open = top.querySelector('.navgroup.open')
        if (open) open.classList.remove('open')
        if (top.classList.contains('nav-open')) {
            top.classList.remove('nav-open')
            if (toggle) toggle.setAttribute('aria-expanded', 'false')
        }
    })
}())
