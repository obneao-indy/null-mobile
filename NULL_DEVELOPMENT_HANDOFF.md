# NULL Development Handoff

Updated: 2026-06-03

## Current Public Build

- GitHub repository: https://github.com/obneao-indy/null-mobile
- Public playtest URL: https://obneao-indy.github.io/null-mobile/
- Published branches:
  - `main`
  - `gh-pages`

## What Was Built

`NULL` is currently a single-page mobile playtest build. It is implemented as a static HTML game with embedded CSS and JavaScript.

Core flow:

- Title screen: `NULL`
- Home menu:
  - `ENCOUNTER`
  - `BUILD ROOM`
  - `OPTIONS`
  - `HELP`
- Enemy select:
  - `Black Circle`
- Battle:
  - Drag movement on mobile
  - WASD movement on PC
  - Auto-fire player bullets
  - Enemy 3-way shots
  - 90-second timer
  - 3 player HP pips
  - Pause, retry, defeat, reward screens
- Progression:
  - Local save via `localStorage`
  - First kill can grant `巨大化`
  - Later drops can include `散弾`

## Files

- `index.html`: full playable build
- `server.mjs`: local static server for PC testing
- `package.json`: `npm start` shortcut
- `.github/workflows/pages.yml`: GitHub Pages deployment workflow
- `.nojekyll`: disables Jekyll processing
- `README.md`: public URL and local run notes

## Local Run

```powershell
node server.mjs
```

Default local URL:

```text
http://127.0.0.1:4183/
```

## Notes From This Chat

- The first attempt used a LAN URL from the `異界駅監査業務` workspace:
  - `http://192.168.179.10:4183/`
- That failed on phone because the PC Wi-Fi profile was `Public` and Windows/router restrictions likely blocked inbound local access.
- The final solution was to publish via GitHub Pages so mobile can open it without same-Wi-Fi LAN access.
- The `juju-members-card` repository/page must not be used for NULL.
- A temporary attempt to use `toaru-rekishi` was not pushed and was cleaned up.

## Next Development Ideas

- Add more enemies and enemy selection cards.
- Split `index.html` into separate `src` files once iteration slows down.
- Improve mobile balance:
  - enemy bullet speed
  - player hit radius
  - first-kill drop pacing
- Add a visible debug/reset-save option for testing.
- Add real screen-size QA for common phone aspect ratios.
