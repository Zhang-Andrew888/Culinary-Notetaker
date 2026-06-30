# MiseNote — Frontend (React + Vite)

A private cooking journal: keep recipes, attach dated cooking-log notes, and
organize recipes into cookbooks. This is the **frontend**, built in React +
Vite from the hi-fi design (`MiseNote Hi-Fi.dc.html`). It runs standalone on
sample data — no backend required to try it.

## Run it

```bash
cd misenote-frontend
npm install
npm run dev          # http://localhost:5173
```

Other scripts: `npm run build` (production bundle to `dist/`), `npm run preview`
(serve the build).

> Requires Node 18+.

## Stack

- **React 18** + **react-router-dom 6** (routing)
- **Vite 5** (dev server + build)
- Plain CSS with custom properties — no UI framework, so the design tokens stay
  legible and easy to retheme. Fonts (Newsreader + Hanken Grotesk) load from
  Google Fonts in `index.html`.

## Structure

```
misenote-frontend/
├── index.html              # font links + root
├── src/
│   ├── main.jsx            # entry (Router + StrictMode)
│   ├── App.jsx             # routes
│   ├── index.css           # design tokens (:root) + all component styles
│   ├── data.js             # sample recipes / logs / cookbooks (API-shaped)
│   ├── components/
│   │   ├── AppLayout.jsx   # sidebar + content shell (logged-in)
│   │   ├── Sidebar.jsx     # olive nav with active state
│   │   └── ImageSlot.jsx   # drag-drop / click photo slot, localStorage-backed
│   └── pages/
│       ├── Landing.jsx     # /
│       ├── Login.jsx       # /login   (tabs; "Log in" → /recipes)
│       ├── Recipes.jsx     # /recipes (home — recipe grid)
│       ├── RecipeDetail.jsx# /recipes/:id (ingredients, steps, cooking log)
│       ├── CreatePage.jsx  # /create  (Recipe ⇄ Cookbook toggle)
│       └── Cookbooks.jsx   # /cookbooks (list + detail panel)
```

## Routes

| Path | Screen | Notes |
|---|---|---|
| `/` | Landing | logged-out; "Begin now" → `/login` |
| `/login` | Log in / Sign up | tab toggle; submitting routes to `/recipes` |
| `/recipes` | Recipe list (home) | cards link to detail |
| `/recipes/:id` | Recipe detail + cooking log | add-log form prepends, sorts newest-first |
| `/create` | Create | segmented Recipe/Cookbook; ingredient/step rows add & remove; cookbook recipe picker toggles |
| `/cookbooks` | Cookbooks | click a card to load its detail panel |

## Design system

Everything lives in `src/index.css` under `:root`. The palette follows a
**60 / 30 / 10** split:

- **60% cream** `#f5f1de` — app background (`--cream`), with warm-white surfaces
  for cards/inputs (`--surface #fdfbf2`).
- **30% olive-charcoal** `#41493b` — body text, headings, the sidebar, borders,
  dividers (`--ink` + alpha variants).
- **10% leaf-green** `#5b8c3e` — accent only: active states, tags, the brand
  glyph, focus rings. Buttons with text use the **darkened** `#4a7332`
  (`--green-btn`) with white text to clear WCAG AA. Green is never used for small
  body text.

Type: **Newsreader** (`--serif`) for display/titles and log dates;
**Hanken Grotesk** (`--sans`) for everything else. Radii, shadows, and the paper
grain overlay are tokenized too. Component states (default / hover / active /
focus) are real CSS pseudo-classes on `.btn`, `.nav-item`, `.recipe-card`,
`.input`, etc.

## Image slots

`<ImageSlot>` is the photo placeholder used across the app. Drag an image file
onto it (or click to browse); it stores a data URL in `localStorage` keyed by
`id`, so your photos survive reloads. The API has no image fields, so these are
intentionally a **client-only** feature — see below.

## Wiring a real backend

`src/data.js` uses the documented MiseNote API field names
(`dish_name`, `cuisine_area`, `steps[]`, `ingredients[{name, amount}]`,
`book_name`, `recipe_ids[]`), so swapping sample data for live calls is a
focused change. When you do:

- **Auth** is JWT (access + refresh). Store tokens on login/register; send
  `Authorization: Bearer …`; refresh on 401; "Log out" just discards tokens.
- **Lists are unpaginated arrays** — any search/sort/filter is client-side.
- **Cookbook contents are id-only** (`recipe_ids` / `GET /cookbooks/{id}/recipes/`)
  — resolve ids against the loaded recipe list (as `Cookbooks.jsx` already does).
- **Recipe logs** have no ordering guarantee — sort by `date` descending
  (as `RecipeDetail.jsx` does).
- **No image / description / author / link fields exist server-side.** The cover
  photos, descriptions, and the optional Author/Link inputs are net-new — add the
  backing columns/storage or keep them client-side.

## Not included (suggested next steps)

- Real authentication + data fetching (currently sample data + client routing)
- Loading / empty / error states (empty states are the first thing a new user
  sees — worth designing next)
- `Cook Later` and `Profile` screens (shown in the sidebar as placeholders)
- Mobile / responsive layout (this implements the desktop design)
