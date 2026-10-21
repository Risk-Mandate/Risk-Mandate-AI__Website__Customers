# The themes: six, one attribute, and how to add a seventh

*customers.riskmandate.ai · operations · written at v0.2.0 (2026-10-21) · CC BY 4.0*

The site has six themes, picked from the pill in the header and kept in the reader's browser. RiskMandate is the default and the first: riskmandate.ai's look, paper and green. Canvas is its dark variant, riskmandate.ai's dark hero band used as the whole page. The other four are newsroom.sgit.ai's themes, from its v0.12.12 of 13 October 2026, with the newsroom's values mapped onto this site's tokens.

| Theme | Mode | What it is | From |
|---|---|---|---|
| RiskMandate | light | paper and green, the default | riskmandate.ai |
| Canvas | dark | dark, green | riskmandate.ai's dark hero, as a whole page |
| Night | dark | dark, teal | newsroom.sgit.ai Night |
| Ember | dark | dark, amber | newsroom.sgit.ai Ember |
| Paper | light | warm cream, terracotta | newsroom.sgit.ai Paper |
| Blueprint | light | white, electric blue | newsroom.sgit.ai Blueprint |

## How it works

- **One attribute.** `assets/theme.js` sets `data-theme` on the html element before the first paint: it is a classic script in the head, loaded before the stylesheets, so the page never flashes the default first.
- **The reader's word is kept.** The stored choice comes first. With nothing stored, a system set to dark opens in Canvas and anything else in RiskMandate; the first choice in the picker ends that. The choice is one key in local storage, `riskmandate.customers.theme`, and never leaves the device. Print is the default theme on white, whatever the reader reads in.
- **Every colour is a token.** `assets/themes.css` is the only file on the site that writes a colour. It has one block per theme and every block defines every token. `assets/site.css` reads the tokens and writes no colour of its own.
- **The picker is drawn by the build.** `admin/build/chrome.py` writes the list from `data/themes.json` into every page's header; `theme.js` wires it and marks the current entry. Without JavaScript there is no choice and the page is the default.

## What the gate checks

`tests/build/test_themes.py` fails the build when any of these stop being true:

1. `data/themes.json`, `theme.js` and `themes.css` name the same themes, in the same order, with the default first and the same storage key.
2. Every theme block defines exactly the tokens the default defines; no theme falls through to another's colour.
3. No colour is written in `site.css`, the scripts or any page.
4. Each swatch in the picker is its theme's own `--rm-swatch`.
5. Each theme's `color-scheme` matches its mode, so the browser's own controls and scrollbars follow it.
6. In every theme, the pairs a reader reads hold their contrast: text, muted text, links and button ink at 4.5:1; labels, the hero's accent words and the step states at the levels their size allows.

The last check found one thing on the first run. riskmandate.ai's green, `#1A7F5A`, is 4.24:1 on its own alternate band, under the 4.5:1 a link needs. The accent here is `#187A56`, one shade darker and 4.53:1 there; the swatch and the shipped chip keep the brand green.

## Adding a theme

1. Add a row to `data/themes.json`: an id of lower-case letters, a name, a mode, a note of three or four words, and where it came from.
2. Add the id and name to `THEMES` in `assets/theme.js`, in the same position.
3. Copy the default block in `assets/themes.css`, rename it `:root[data-theme="<id>"]`, and give every token a value; add the `.sw-<id>` swatch.
4. Run `python3 admin/build/gate.py --build`. The contrast check names each pair that falls short; fix the value, not the threshold.
