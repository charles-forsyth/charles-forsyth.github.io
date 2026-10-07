# charles-forsyth.github.io: Site Specification

Status: describes the site as built on 2026-10-04 (Field Notes added in PR #5)
Repo: `charles-forsyth/charles-forsyth.github.io` (public), branch `main`
Live: https://charles-forsyth.github.io/
Engine: none. Hand-written static HTML and CSS, served as-is (`.nojekyll`)
Deploy: GitHub Actions `Deploy` workflow uploads the repo root to GitHub Pages on every push to `main`
Last updated: 2026-10-04

This is Charles (Chuck) Forsyth's professional site: who he is, what he has built,
his CV, a long-form technical manual and dated technical reports. It may name him,
UC Riverside and his public repositories. It must not carry family, home, vendor or
personal-mail details (section 3).

---

## 1. Purpose

One place that answers, for a colleague, a hiring committee, a researcher or a
vendor: who is this person, what has he built, and can I trust what he writes.

It has six parts:

| Part                  | URL                                                                           | What it is                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Home                  | `/`                                                                           | Hero, about, vision, flagship projects, experiments, Field Manual teaser, live GitHub repo list, contact                         |
| CV                    | `/cv.html`, `/cv.pdf`                                                         | The one curriculum vitae, with a print-ready PDF                                                                                 |
| AI + HPC Field Manual | `/handbook/`                                                                  | 15-chapter, 2026 edition, every hardware figure sourced (about 98,000 words, 726 cited sources), plus the preserved 2019 edition |
| Field Notes           | `/papers/`                                                                    | Dated technical reports on real work, with charts from real data                                                                 |
| Project deep dives    | `/sigint-data-lake.html`, `/esp32-firmware-gallery.html`, `/truck/`, `/boat/` | Single-topic showcase pages                                                                                                      |

## 2. Principles

- **No build step.** Every page is a finished HTML file. What is in the repo is what is
  served. This keeps the site durable: it will still work in ten years with no
  toolchain.
- **One look.** Every page loads `style.css` (the "Forest Ranger" palette) and adds at
  most one section stylesheet. New sections reuse existing classes before adding new
  ones.
- **Every claim checkable.** Field Manual figures cite their sources; Field Notes link
  the public repos and specs they describe and say plainly what is private.
- **Honest.** Reports include what went wrong. No made-up numbers, no estimates passed
  off as measurements.
- **Plain ASCII in new prose.** No em or en dashes, smart quotes or emojis (older home
  page copy still has a few; do not add more).
- **Gate before merge.** Lint and tests run locally and in CI; every change goes through
  a PR.

## 3. Privacy and content boundaries

May appear: Chuck's name, title, UC Riverside, the UC system, public repos and their
specs, published talks, professional history, the names of private tools (as names
only, no links).

Must not appear: family members, the homestead's name or address, vehicle plates,
home network details (LAN IPs, device lists), vendors he is in disputes with, personal
email, lab budgets or researcher names from cloud cleanups, ticket numbers, cloud
billing or project IDs.

The pseudonymous Nordhaven site is a separate identity. Do not link Field Notes or the
Field Manual to individual Nordhaven posts, and do not quote Nordhaven text here. (The
home page footer does link to the Nordhaven home page; see section 12.)

## 4. Architecture

```
index.html ---- style.css ---- index.js (GitHub API repo list)
cv.html ------- style.css + cv.css            cv.pdf (printed from cv.html)
handbook/*.html style.css + handbook/handbook.css + highlight.js (CDN)
handbook/2019/  same, the 2019 edition preserved
papers/*.html - style.css + handbook/handbook.css + papers/papers.css
truck/, boat/ - style.css + truck.css / boat.css
sigint-data-lake.html, esp32-firmware-gallery.html - style.css + inline <style>/<script>
```

- Hosting: GitHub Pages, source "GitHub Actions" (shown as `legacy` build type by the
  API), no custom domain, HTTPS enforced.
- `Deploy` workflow (`.github/workflows/deploy.yml`): on push to `main` (and manual
  dispatch): checkout v4, configure-pages v5, upload-pages-artifact v3 with
  `path: '.'`, deploy-pages v4. It publishes the whole repo root, including dotfiles
  that Pages serves (see section 12).
- `CI` workflow (`.github/workflows/ci.yml`): on push and PR to `main`: Node 18,
  `npm ci`, `npm run lint`, `npm test`.
- External dependencies, all from CDNs: Font Awesome 6.0.0 (cdnjs), highlight.js
  11.9.0 with the `atom-one-dark` theme (Field Manual chapters only), the GitHub REST
  API (home page repo list). No fonts are downloaded; the type uses system fonts.

### 4.1 File map

| Path                                                                    | What it is                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `index.html`                                                            | Home page (about 700 lines)                                                                                              |
| `index.js`                                                              | Fetches `api.github.com/users/charles-forsyth/repos?sort=updated`, renders repo cards, filters by name                   |
| `style.css`                                                             | The site theme: palette, hero, buttons, sections, cards, repo grid, manual strip, footer, responsive (about 720 lines)   |
| `cv.html`, `cv.css`, `cv.pdf`                                           | CV page, its styles (timeline, skills grid, print rules), the PDF                                                        |
| `handbook/index.html`                                                   | Field Manual landing page: parts, chapter cards, 2019 edition box                                                        |
| `handbook/<slug>.html`                                                  | 15 chapters (13 new for 2026, `linux` kept from 2019, `glossary`)                                                        |
| `handbook/2019/*.html`                                                  | 7 preserved 2019 chapters: cloud, code, hardware, presentations, provisioning, slurm, software                           |
| `handbook/{code,hardware,...}.html`                                     | Meta-refresh stubs from old chapter URLs into `2019/`; `handbook/cv.html` redirects to `/cv.html`                        |
| `handbook/handbook.css`                                                 | Long-form layout shared by the manual and Field Notes (doc-hero, doc-nav, doc-toc, doc-content, doc-pager, manual cards) |
| `papers/index.html`                                                     | Field Notes list                                                                                                         |
| `papers/YYYY-MM-DD-<slug>.html`                                         | One report per file                                                                                                      |
| `papers/img/YYYY-MM-DD/*.png`                                           | That report's charts                                                                                                     |
| `papers/papers.css`                                                     | Figure frames and the notes list (about 50 lines)                                                                        |
| `sigint-data-lake.html`                                                 | OmNet architecture deep dive with a canvas network animation                                                             |
| `esp32-firmware-gallery.html`                                           | ESP32 firmware cards                                                                                                     |
| `truck/`, `boat/`                                                       | Fleet showcase pages with their own CSS and background images                                                            |
| `assets/`                                                               | Shared images (the SIGINT architecture diagram)                                                                          |
| `package.json`, `package-lock.json`                                     | Dev tooling only (lint, format, tests)                                                                                   |
| `eslint.config.mjs`, `.prettierrc`, `.htmlvalidate.json`, `cspell.json` | Tool configs                                                                                                             |
| `tests/*.test.js`                                                       | Vitest checks (20 tests)                                                                                                 |
| `.github/workflows/`                                                    | `ci.yml`, `deploy.yml`                                                                                                   |
| `robots.txt`                                                            | Allows all; names a sitemap that does not exist yet (section 12)                                                         |
| `README.md`                                                             | Public profile text about the OmNet architecture (not a dev guide)                                                       |
| `GEMINI.md`, `.squad/`                                                  | Notes and persona files from an earlier agent toolchain (served publicly, see 12)                                        |
| `docs/SPEC.md`                                                          | This document                                                                                                            |

## 5. Visual design

### 5.1 Palette ("Forest Ranger tech")

CSS custom properties in `style.css :root`. Every section stylesheet uses these.

| Token              | Value                   | Used for                                           |
| ------------------ | ----------------------- | -------------------------------------------------- |
| `--bg-deep`        | `#0a110d`               | Page background, `section-dark`                    |
| `--bg-surface`     | `#132219`               | `section-light`, cards                             |
| `--bg-surface-alt` | `#172a1f`               | Hero glow, sidebar, card hover surfaces            |
| `--primary`        | `#3c6e47`               | Primary buttons, kickers, the green glow           |
| `--primary-glow`   | `rgba(60,110,71,0.4)`   | Button and h1 glow                                 |
| `--accent`         | `#d4b886`               | Tan: h2 in heroes, secondary buttons, links, icons |
| `--accent-glow`    | `rgba(212,184,134,0.3)` | Secondary button hover                             |
| `--text-main`      | `#e4ebe6`               | Body text                                          |
| `--text-muted`     | `#8a9e91`               | Secondary text                                     |
| `--border-color`   | `#2a4232`               | Hairlines and card borders                         |

Charts in Field Notes use the same palette in matplotlib: background `#0a110d`,
surface `#132219`, accent `#d4b886`, green `#3c6e47`, text `#e4ebe6`.

### 5.2 Type

- `--font-main`: `'Segoe UI', system-ui, -apple-system, sans-serif` for everything.
- `--font-tech`: `'Courier New', Courier, monospace` for hero subtitles, buttons,
  kickers, part headings and labels. Uppercase with letter-spacing on buttons and
  kickers.
- Icons: Font Awesome 6.0.0, `fas` / `fab` class names. 6.0.0 has no `fa-x-twitter`
  (see 12).

### 5.3 Components

- **Hero** (`.hero`): radial green glow from the bottom, a faint 50 px grid overlay
  (`::before`, 5 percent opacity), centred h1 (3.8 rem, green text-shadow), tan mono
  h2, muted lead, `.cta-buttons`. Long-form pages use `.hero.doc-hero` (smaller
  padding) with a `.doc-kicker` line (mono, uppercase, green).
- **Buttons**: `.btn.btn-primary` (green fill, glow, inverts on hover),
  `.btn.btn-secondary` (tan outline, fills tan on hover), `.btn-link` (inline arrow
  link in cards). Cards for public projects that have a GitHub Pages showcase use
  `.card-links` with two links: Project Page (the showcase) and Repo (GitHub icon).
- **Sections**: alternate `section-light` (surface, borders, 80 px padding) and
  `section-dark`. Section titles are h3 with a Font Awesome icon.
- **Cards**: `.stat-card` (about grid), `.project-card` (flagship grid, equal heights,
  optional `.project-image` on top), `.experiment-card` (17 sandbox links),
  `.repo-card` (GitHub list), `.manual-card` (Field Manual landing), `.manual-strip`
  (row of chapter links on the home page). All lift 5 px and turn the border tan or
  green on hover.
- **Long-form layout** (`handbook.css`): sticky `.doc-nav` chapter strip under the hero,
  `.doc-layout` (240 px sticky `.doc-toc` + article), `.doc-layout-single` without a
  sidebar (max 860 px), `.doc-content` typography (h2 with rule, tan links, code
  blocks, zebra tables, blockquotes), `.doc-pager` previous/next, `ol.sources` with
  `li:target` highlight for citation jumps.
- **Field Notes extras** (`papers.css`): `.doc-figure` (framed chart with caption),
  `.notes-list` (date, title, summary per report).
- **CV** (`cv.css`): `.cv-hero`, `.cv-contact` row, `.cv-section`, `.cv-role`
  timeline with a dot per role, `.cv-dates`, `.cv-skill-grid`, `.cv-tags`, and
  `@media print` rules that turn the page into a clean black-on-white resume.

### 5.4 Responsive

- `style.css` at 768 px: about grid to one column, smaller hero, buttons stack,
  manual strip to two columns.
- `handbook.css` at 900 px: the sidebar stacks above the article, roadmap to one
  column.
- `cv.css` at 700 px, and print.
- Check every visual change at 1300 px and 400 px wide.

## 6. Sections in detail

### 6.1 Home (`index.html`)

Top to bottom:

1. `<head>`: title "Charles Forsyth | Architect of Agentic Ecosystems", description,
   keywords, Open Graph and Twitter card tags (image
   `assets/camp_tioga_sigint_arch.png`), canonical URL.
2. Hero: name, "Director of Research Computing & Architect of Sovereign Edge
   Ecosystems", a one-line lead, buttons: View Innovations, CV, Field Manual, Field
   Notes, All Repos, Contact Me.
3. `#about` (light): "From the Deckplates to the Data Center" (Navy radar to UC
   research computing), CV link, and four stat cards (Director, Architect, Educator,
   Outdoorsman).
4. `#vision` (dark): Directed Agentic Engineering and Squad Manager.
5. `#portfolio` (light): Flagship Innovations, 8 project cards (Aura, OmNet with the
   architecture image, Squad Manager, Deep Research, The Scientific Nexus, Skywalker,
   ESP32 Firmware Suite, Dodge Ram Daytona).
6. `#experiments` (dark): Applied Research & Experiments, 17 experiment cards linking
   to the `lordivxx.github.io` sandbox.
7. `#field-manual` (light): the manual teaser, a strip of 9 chapter links, buttons to
   the manual and to Field Notes.
8. `#github-repos` (dark): search box `#repo-search` and `#repo-list`, filled by
   `index.js` from the GitHub API (unauthenticated: 60 requests per hour per visitor
   IP; if it fails the section stays empty and logs to the console).
9. `#contact` footer: Nordhaven Chronicle, GitHub, LinkedIn, X, email, copyright.

Tests in `tests/repos.test.js` require the repos section, the search input, the list
container, a nav link to `#github-repos` and the fetch code. Keep those ids.

### 6.2 CV (`cv.html`, `cv.pdf`)

- The only CV on the site. Any other CV URL redirects here (`handbook/cv.html` does).
- Sections: Summary, Professional Experience (a timeline of roles with dates and
  bullets), Education, Teaching, plus skills and tags.
- Sources for edits, in order: existing CV files in `~/Documents` (newest Google Docs
  export is the base), NSF/SciENcv biosketches (ORCID, roles), the LinkedIn profile,
  `02 - Personal/About_Me.md` in the vault (not alone for dates; it has been wrong).
- `cv.pdf` is Chrome's print of `cv.html` (5 pages on 2026-10-04). Regenerate after any
  CV edit:
  `google-chrome --headless=new --no-pdf-header-footer --print-to-pdf=cv.pdf "file://$PWD/cv.html"`
  then check `pdfinfo cv.pdf` and open it once.

### 6.3 AI + HPC Field Manual (`handbook/`)

- 2026 edition, published 2026-09-24 (PR #4). 15 chapters in five parts:
  - Foundations: The Convergence
  - Hardware: Accelerators, Memory and Storage, Interconnects, Power Cooling and
    Facilities
  - Software and Operations: Systems Software, Scheduling, Observability, Operations
  - Workloads: Training at Scale, Inference at Scale, Scientific Computing, Cloud
  - Reference: Linux Essentials (from 2019, still current), Glossary
- Chapter page anatomy: `doc-hero` with kicker "AI + HPC Field Manual", the chapter
  strip (`doc-nav`, current chapter `class="active" aria-current="page"`), sidebar "On
  this page" listing every h2 (except Sources), the article, Key Takeaways, a numbered
  Sources list (`<ol class="sources">`, items `id="src-N"`), inline citations
  `<a href="#src-N">[N]</a>`, the pager, and highlight.js for `language-*` code blocks.
- Content rules (from the writing spec used to produce it): practitioner voice, plain
  ASCII, no hype words; every hard figure (bandwidth, capacity, FLOPS, power, dates)
  from a fetched source listed in that chapter; name the precision behind peak numbers;
  separate shipping from announced products; leave out what cannot be verified; code
  must be syntactically correct, with illustrative values marked. `Field note:`
  blockquotes for practical tips.
- The chapters were generated once from HTML fragments by a build script that lived in
  `/tmp/fm2026/` and is gone. The pages are now maintained by hand; section 9.3 says
  how.
- 2019 edition: preserved under `handbook/2019/` with an archive nav; the old chapter
  URLs (`handbook/code.html` and so on) are meta-refresh stubs into it. Originals are
  also backed up in `~/backups/legacy_charlesforsyth_site_20260924/handbook_2019_pages/`
  with mirror clones of the retired legacy repos.

### 6.4 Field Notes (`papers/`)

- Started 2026-10-04 with "One Day on the Research Stack" (the work of 2026-10-03:
  38 releases, 4 charts, about 3,800 words).
- Report anatomy: `doc-hero` with kicker "Field Notes | <date>", h1 title, h2 one-line
  summary, buttons back to All Field Notes and the main site; sidebar "On this page";
  sections typically Abstract, The Stack, one section per system, What Went Wrong,
  Patterns Worth Keeping, What Is Next, Repositories and Specs; a pager back to the
  list.
- Evidence rules: build from the record (the day's Hermes sessions in
  `~/.hermes/state.db`, `git log` and tags per repo, the specs and changelogs, live
  checks). Chart only real numbers. Link public repos only; name private ones without
  links and say so. Always include what went wrong.
- `papers/index.html` lists reports newest first in a `<ul class="notes-list">`.

### 6.5 Project deep dives

- `sigint-data-lake.html`: OmNet architecture page, inline `<style>` and a `<script>`
  that animates a network on `#network-canvas`. OPSEC-safe copy (no locations, IPs or
  device lists).
- `esp32-firmware-gallery.html`: six firmware cards, inline styles.
- `truck/` and `boat/`: fleet pages with their own CSS and photos; linked from the
  Dodge Ram card and elsewhere.
- These pages predate the current lint rules. `html-validate` reports 3 errors on the
  SIGINT page, 37 on the ESP32 page and 2 on the boat page; CI does not check them
  (only `index.html` is validated). Fix them when touching those pages.

### 6.6 Shared head and page conventions

Every page has: `<!doctype html>`, `lang="en"`, UTF-8, viewport, a title ending
`| Charles Forsyth` (manual chapters: `<Chapter> | AI + HPC Field Manual | Charles
Forsyth`), a meta description, a canonical URL, `style.css` (relative path), its
section CSS, Font Awesome. Long-form pages: back buttons to their section index and
the main site in the hero, a footer note with the same links.

### 6.7 Asset Fleet (removed 2026-10-04)

The generated asset inventory was taken down and scrubbed from git history because it
published property addresses, rent records and the home network map. Do not
republish an inventory here. The generator now lives in the private vault.

## 7. Tooling and checks

`npm ci` once (Node 18+; the laptop has Node 22), then:

| Command               | What it runs                                                                                                                                                |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `npm run lint`        | `eslint index.js`, `html-validate index.html`, `prettier --check style.css`, `prettier --check .` (every HTML, CSS, JS, JSON and Markdown file in the repo) |
| `npm test`            | `vitest run`: 20 checks (index structure, semantic tags, style.css exists, dev dependencies, config files, both workflows, the repos section)               |
| `npm run format`      | `prettier --write .`                                                                                                                                        |
| `npm run spell-check` | cspell over html/css/js/md (not in CI; `cspell.json` holds the word list)                                                                                   |

- Prettier: single quotes, semicolons (`.prettierrc`). Formatting differences fail CI,
  so run `npx prettier --write <changed files>` before committing.
- html-validate (`html-validate:recommended`, with trailing-whitespace, void-style and
  doctype-style off) rejects inline `style=""`, `<style>` inside body elements, raw
  `&`, and buttons without `type`. Move styles into the section stylesheet as classes.
- ESLint flat config: recommended + prettier, browser globals, `no-unused-vars` warns.
- Validate any new page by hand: `npx html-validate <file>` (CI only covers
  `index.html`).

## 8. Ship flow

1. `git checkout main && git pull && git checkout -b feat/<topic>`
2. Edit. Run `npx prettier --write <files>`, `npm run lint`, `npm test`,
   `npx html-validate <new or changed pages>`.
3. Preview: `python3 -m http.server 8771` in the repo root (background it), then
   headless screenshots:
   `google-chrome --headless=new --hide-scrollbars --window-size=1300,2600 --screenshot=/tmp/top.png http://localhost:8771/<page>`
   and the same at `400,1800`. Look at both; stop the server.
4. Privacy grep the diff for family names, the homestead's name and address, LAN IPs,
   personal email.
5. Commit, `git push -u origin feat/<topic>`, `gh pr create`, wait for `CI` to pass
   (`gh pr checks --watch`), `gh pr merge --merge --delete-branch`, then
   `git checkout main && git pull && git branch -D feat/<topic>`.
6. The `Deploy` workflow publishes in about a minute. Check the live URL with
   `?cb=$(date +%s)` and take a screenshot.

`main` has no branch protection; the PR discipline is the gate. If `CI` is already red
on `main`, fix that first so it cannot hide a new failure.

## 9. How to

### 9.1 Publish a Field Notes report

1. Gather evidence (6.4). Write down the numbers you will chart, with their source.
2. Charts: matplotlib with the site palette (5.1), saved as PNG to
   `papers/img/YYYY-MM-DD/`. Look at each chart once; fix overlapping labels.
3. Copy `papers/2026-10-03-one-day-on-the-research-stack.html` to
   `papers/YYYY-MM-DD-<slug>.html`. Change: title, meta description, canonical URL,
   kicker date, h1, h2, the sidebar list (one `<li>` per h2 id), the article, figures
   (`<figure class="doc-figure"><img src="img/..." alt="..."><figcaption>`), and the
   Repositories and Specs list.
4. Add it to the top of `papers/index.html` (`note-date`, h3 link, one-paragraph
   summary).
5. Optional: mention it on the home page only if it is a landmark.
6. Run the ship flow (section 8).

### 9.2 Edit the CV

Edit `cv.html` (keep the `.cv-role` structure: header with h4 title, `.cv-org`,
`.cv-dates`, then a `ul`). Regenerate `cv.pdf` (6.2). Ship.

### 9.3 Edit a Field Manual chapter

1. Edit `handbook/<slug>.html` directly inside `<article class="doc-content">`.
2. A new h2 needs a unique lowercase hyphenated id starting with a letter, and a
   matching `<li><a href="#id">` in the `doc-toc` list.
3. A new citation: add `<li id="src-N">` at the end of `ol.sources` and cite with
   `<a href="#src-N">[N]</a>`. Every listed source must be cited and every cite must
   resolve. Count check:
   `grep -c '<li id="src-' f.html` against
   `grep -o 'href="#src-[0-9]*"' f.html | sort -u | wc -l`.
4. Check for non-ASCII: `grep -nP '[^\x00-\x7F]' f.html`.
5. Spot-check any changed hardware figure against the vendor page.

### 9.4 Add a Field Manual chapter

1. Copy an existing chapter. Set title, description, canonical URL, hero icon and
   tagline, the article and sources.
2. Add the chapter to the `doc-nav` strip in **every** chapter file (15 files) in the
   same position, and fix the pager links of its neighbours.
3. Add a `manual-card` to `handbook/index.html` under the right part, and to the home
   page strip if it belongs there.
4. Run the source count check (9.3) and the ship flow.

### 9.5 Add a flagship project or an experiment

- Flagship: copy a `<div class="project-card">` in `#portfolio` (icon, h4, paragraph,
  `btn-link`). The grid is `repeat(auto-fit, minmax(300px, 1fr))`, three across at
  the 1100 px container, so 8 cards leave a short last row; add or remove in threes
  to keep rows full.
- Experiment: copy an `<div class="experiment-card">` in `#experiments`.
- A deep-dive page: new HTML file at the root using `style.css` plus a small section
  stylesheet (no inline styles, so it passes html-validate). Link it from its card.

### 9.6 Change colours or type

Edit the `:root` tokens in `style.css` only. Check the home page, a manual chapter, a
Field Notes report with charts, and the CV (screen and print) at both widths.
Regenerate any chart whose colours should follow.

## 10. Related sites and repos

- Nordhaven (`charles-forsyth/nordhaven`, `/nordhaven/`): the pseudonymous lodge
  chronicle, Jekyll, its own spec at `docs/SPEC.md` in that repo.
- `lordivxx.github.io`: personal experiments and the sandbox the experiment cards link
  to (old account, pushed over the `github.com-lordivxx` SSH alias, branch `master`).
- The retired `CharlesForsyth/charlesforsyth.github.io` legacy site: its content was
  migrated into the Field Manual on 2026-09-24; mirror clones are in
  `~/backups/legacy_charlesforsyth_site_20260924/`.

## 11. History

- 2026-02-17: launched (DAE branding); 02-18 QA pipeline (lint, tests, CI); 02-20
  Forest Ranger dark design (v1.3.0).
- 2026-02-25: fleet pages (truck, boat) and sanitized assets.
- 2026-03-28/29: OmNet/SIGINT architecture page, 17 experiments migrated from the
  sandbox, SEO metadata, Aura card.
- 2026-09-11: Nordhaven link in the footer. 09-20: ESP32 firmware gallery.
- 2026-09-24: legacy HPC site consolidated into the Field Manual; first green CI since
  at least 09-11; CV page and PDF (PR #3); the 2026 AI + HPC Field Manual (PR #4).
- 2026-10-04: Field Notes section and its first report (PR #5).

## 12. Known issues and open items

Ordered by how much they matter.

1. **Done 2026-10-04: Asset Fleet removed.** The pages and generator were deleted and
   purged from git history (force-push); GitHub may keep cached pull request diffs.
2. **The whole repo is published.** `Deploy` uploads `.`, so `GEMINI.md`,
   `.squad/`, `tests/`,
   `package.json` and this spec are all reachable on the live site. Nothing secret is in
   them today, but anything committed is public. Option: deploy a filtered folder
   (copy only the public files into `_site/` in the workflow), or keep the rule that
   nothing private is ever committed.
3. **The footer links Nordhaven by name.** "Nordhaven Chronicle" in the contact
   footer ties the pseudonymous site to this one. Nordhaven's privacy rule assumes the
   two are not linked. The steward's call whether to keep it.
4. `robots.txt` names `sitemap.xml`, which returns 404. Add a hand-written sitemap or
   remove the line.
5. Font Awesome 6.0.0 has no `fa-x-twitter`, so the X link in the footer shows no
   icon. Use `fab fa-twitter` or move the CDN to 6.5.x site-wide (58 references).
6. CI validates only `index.html`. Extend `lint:html` to `html-validate "**/*.html"`
   after fixing the 42 errors in the SIGINT, ESP32 and boat pages.
7. CI uses `actions/checkout@v3` and `setup-node@v3` with Node 18; bump to v4 and Node
   22 before GitHub retires them.
8. The Field Manual build script is gone; adding a chapter means editing the strip in
   15 files by hand (9.4). If chapters change often, write a small script that rebuilds
   the strip, sidebar and pager from the h2 ids.
9. Only the home page has Open Graph tags; the CV, the manual and Field Notes share
   poorly on social sites.
10. `README.md` is a public architecture write-up, not a developer guide; this spec is
    the developer guide.
