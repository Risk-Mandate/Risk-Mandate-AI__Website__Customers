// ── storyboards.js — fills each storyboard on the page, then hands it to the kit ──
//
// The storyboard kit (api.storyboards.sgit.ai, loaded just before this file with its
// integrity strings) wires every .sb-viewer it finds when the page loads, and needs
// the storyboard's data inside it. So the page carries the viewer as a <template>,
// and this file fetches the bundle from this site, puts the viewer and its data in
// place, and asks the kit to wire it. Without JavaScript the panels are on the page
// as text. No storage of its own; the kit keeps the reader's viewing preferences.

(function () {
    'use strict'
    async function fill(host) {
        const wait = host.querySelector('.sb-wait')
        try {
            if (!window.StoryboardKit) throw new Error('the storyboard kit did not load')
            const response = await fetch(host.dataset.sbBundle)
            if (!response.ok) throw new Error(`${host.dataset.sbBundle} answered ${response.status}`)
            const bundle = await response.json()
            const viewer = host.querySelector('template.sb-template').content.firstElementChild.cloneNode(true)
            const data   = document.createElement('script')
            data.type        = 'application/json'
            data.className   = 'sb-data'
            data.textContent = JSON.stringify({ storyboard : bundle.storyboard, cast : bundle.cast })
            viewer.appendChild(data)
            host.appendChild(viewer)
            window.StoryboardKit.wire(host)
            if (wait) wait.remove()
        } catch (error) {
            if (wait) wait.textContent = `The storyboard could not be drawn here (${error.message}); its panels are below as text.`
        }
    }
    document.querySelectorAll('.sb-host[data-sb-bundle]').forEach(fill)
}())
