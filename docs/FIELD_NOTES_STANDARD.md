# Field Notes Standard (FNS-1)

The house standard for papers on charles-forsyth.github.io/papers. It plays the role the NSF PAPPG plays for proposals: fixed structure, fixed formatting, and claims a reviewer can check. A Field Note that breaks a MUST rule is not published.

MUST = required. SHOULD = expected unless the note says why not.

## 1. What a Field Note is

A dated technical report on real work Chuck directed: what was built, what it measured, what broke, and what was learned. It is not marketing, a tutorial or an opinion essay. Every factual claim can be traced to a repository, spec, test report, log or public page.

## 2. File, URL and metadata

1. MUST: one self-contained HTML file at `papers/YYYY-MM-DD-kebab-title.html`, where the date is the publication date.
2. MUST: copy the head of `papers/2026-10-27-directing-a-fleet-of-ai-builders.html` exactly, changing only these: `<title>` = `Title | Field Notes`; meta description (150-160 characters, a plain summary); canonical and og:url (the final URL); og:title; og:description (one or two sentences, up to 300 characters); og:type article; the shared og:image; twitter:card summary_large_image; stylesheets `../style.css`, `../handbook/handbook.css`, `papers.css`; Font Awesome 6.0.0.
3. MUST NOT: add inline `<style>`, new CSS files, scripts, trackers or external fonts. If a new element truly needs styling, add a small rule to `papers/papers.css` and say so in the handoff.

## 3. Page skeleton

The page MUST use the existing classes in this order:

1. `header.hero.doc-hero` holding `p.doc-kicker` (`<i class="fas fa-flask"></i> Field Notes | D Month YYYY`), `h1` (the title), `h2` (the subtitle, one sentence), and `.cta-buttons` with "All Field Notes" and "Main Site".
2. `main.section-light > .container.doc-layout` holding `aside.doc-toc` ("On this page", one link per h2) and `article.doc-content`.
3. At the end of the article, `nav.doc-pager`. Then `footer.section-dark` exactly as in the reference note.

## 4. Required sections (h2, in order)

| #      | Section         | id                          | Rules                                                                                                                                                                                      |
| ------ | --------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | Abstract        | `abstract`                  | 150-250 words, 2-3 paragraphs. What was done, the headline numbers, the main lesson. The last paragraph is the method statement (see section 6).                                           |
| 2      | Context         | `context` (or a fitting id) | The problem and why it matters to research computing. Who it serves. 1-3 paragraphs.                                                                                                       |
| 3-n    | Body            | descriptive ids             | 3-6 sections telling the work: design, what was built, how it runs, the results. Open each with the substance, never with a signpost ("This section shows", "In this section", "Here we"). |
| n+1    | What Went Wrong | `what-went-wrong`           | MUST exist. Real failures, limits and open risks. A note without failures is not credible.                                                                                                 |
| n+2    | Lessons         | `lessons`                   | 3-7 numbered lessons. Each is an imperative rule with one sentence of why.                                                                                                                 |
| n+3    | What's Next     | `next`                      | SHOULD. Short, concrete, no promises with dates you can't keep.                                                                                                                            |
| 2a     | Related Work    | `related-work`              | MUST. See 7a.                                                                                                                                                                              |
| last-1 | References      | `references`                | MUST. See 7a.                                                                                                                                                                              |
| last   | Sources         | `sources`                   | MUST. See section 7.                                                                                                                                                                       |

Length: 2,000-4,500 words of body text. Reading time SHOULD be 10-20 minutes.

## 5. Prose rules

1. Plain, direct English in the first person ("I"). Chuck's voice: casual-professional, concrete, no hype. Short sentences. Active voice.
2. MUST NOT: the words _delve, leverage, seamless, robust, cutting-edge, game-changer, revolutionize, unlock, empower, journey, landscape, tapestry, synergy, holistic, paradigm_; "It's not X, it's Y" constructions; rhetorical questions as section openers; em-dash chains (use commas, colons or full stops; at most one em-dash per section); exclamation marks.
3. Numbers: digits for 10 and up and for every measurement; units with a space (`2.09 PB`, `25 Gbps`, `48 h`); dates as `28 October 2026`; versions as `v0.10.1`.
4. Names: first use is the full name plus a short gloss ("the National Research Platform (NRP) Nautilus cluster, a national Kubernetes cluster"), then the short name. Spell out every acronym once.
5. Code, commands, file paths, flags and identifiers go in `<code>`. Multi-line commands go in `<pre><code>`. Never show a real secret, key, token, password, internal IP address, MAC address or Tailscale address.
6. Hedge honestly: "measured", "about", "in my tests", "not yet verified". Never round up.

## 6. Method and AI disclosure (MUST)

The last paragraph of the Abstract states how the work and the note were produced, in this pattern: _"The work was directed by me and carried out with AI agents under written briefs, independent checks and explicit approval steps. Figures come from [named sources]. This note was drafted with AI assistance from those records and reviewed by me."_

## 7. Claims and sources (the core of the standard)

1. MUST: every number, version, date, count and named outcome traces to a source: a public repo, a commit, a tag or release, a spec section, a test report, a public page, or a named private record ("the gateway usage report"). Private sources are named, not linked.
2. MUST: the Sources section lists each public repository or page as a link (`target="_blank" rel="noopener"`) with a one-line description, then the private records used, by name.
3. MUST NOT: invent, estimate without saying so, or "improve" a figure. If a figure can't be verified from the records, cut it or mark it as unverified.
4. SHOULD: link a claim inline to its repo or spec the first time it appears.
5. The writer keeps a claims ledger (kept outside the site repo): one line per factual claim with its source path or URL. It is not published, but the reviewer checks against it.

## 7a. Citations and bibliography (MUST)

1. Every Field Note has a Related Work section (h2 `related-work`, after Context) of 300-700 words placing the work against prior research, standards and comparable systems, and a References section (h2 `references`) before Sources.
2. In-text citations are numbered in order of first use as superscript links: `<sup class="cite"><a href="#ref-3">[3]</a></sup>`. Every reference is cited at least once; every citation resolves.
3. References use ACM reference format in an `<ol class="sources">` with `id="ref-N"` on each `<li>`: authors, year, title, venue/publisher, and a DOI link (`https://doi.org/...`) or stable URL. 10-25 entries. Peer-reviewed work, standards (NIST, RFC), official project/vendor documentation and agency pages only; no blogs unless primary-source and named as such.
4. Every reference is verified to exist (DOI resolves or URL returns 200) and to support the sentence that cites it. Research tools may suggest references; none is used unverified.
5. Sources (section 7) remains for the author's own repositories and records; References are external literature.

## 8. Figures, tables and code

1. Figures: `figure.doc-figure` with `img` (alt text describing the content, not "image") and a `figcaption` that starts "Figure N." and explains what to see. Images go in `papers/img/YYYY-MM-DD/`, PNG or SVG, under 400 KB each. Only real screenshots, real data or diagrams drawn from real architecture; no stock or AI-generated images.
2. Tables: real `<table>` with `<thead>`, for comparisons and numbers. Caption with a paragraph above starting "Table N."
3. Diagrams SHOULD be inline SVG or ASCII in `<pre>` when a picture explains architecture better than prose.
4. Every figure and table is referenced in the text before it appears.

## 8a. Typography (MUST)

Layout lives in `papers/papers.css` (no inline styles): body measure 72ch, line-height 1.72, h2 with a top rule and 2.6em space above; tables are booktabs style (heavy top and bottom rule, light header rule, no vertical rules) with numeric cells marked `class="num"` (right-aligned, tabular figures); table captions are a `<p class="table-caption">` directly above the table starting "Table N."; figure captions are a `figcaption` below the frame starting "Figure N."; inline `<code>` sits tight against following punctuation with no space; the hero subtitle is proportional type. Check rendering with a desktop and a phone screenshot before handoff.

## 8b. PDF edition (MUST; the PDF is the primary artifact)

1. Source (kept outside the site repo, with the ledger): `main.tex`, `refs.bib`, `figures/` (TikZ or vector PDF only). Build with `latexmk -pdf` (TeX Live at /Library/TeX/texbin) to `papers/pdf/<slug>.pdf`.
2. Class `\documentclass[sigconf,nonacm]{acmart}` (two-column ACM, no ACM copyright block), with `\DocumentMetadata{pdfversion=1.7,pdfstandard=A-2b,lang=en-US}` as the first line for PDF/A-2b (not pdfx: it clashes with acmart's hyperxmp and fails veraPDF), metadata via `\hypersetup` (title, author, keywords, language en-US). Author block: Charles E. Forsyth III, University of California, Riverside, ORCID 0000-0003-4872-0296. CCS concepts and keywords included.
3. Bibliography: BibTeX with `ACM-Reference-Format`. Only references verified to exist (DOI resolves via Crossref/doi.org or URL returns 200) and to support the citing sentence; metadata (authors, title, venue, year, pages) taken from Crossref, not from memory. Numbered citations `\cite{}`; every entry cited.
4. Typography gates: zero `Overfull \hbox` and zero undefined references/citations in the log; booktabs tables with `\toprule/\midrule/\bottomrule`, no vertical rules, numbers right-aligned (`S` or `r` columns); captions above tables, below figures; wide tables/figures use `table*`/`figure*`; code via `listings` or `verbatim` sized to fit the column; no widows of headings at column bottoms; all fonts embedded (`pdffonts` shows emb=yes for all).
5. Validation: `verapdf --flavour 2b <pdf>` passes (if veraPDF is installed); `pdffonts` all embedded; `pdfinfo` shows Title/Author.
6. Web page: the HTML note stays the web edition, adds a prominent "Download PDF" button linking `pdf/<slug>.pdf`, carries the same Related Work and References (numbered), and matches the PDF's content.

## 9. Disclosure and safety

0. Depersonalize with representative values. Architecture may be described in full. Specific identifying details are replaced with representative stand-ins and the note says so once (in the Abstract method paragraph or a short note under Context: "Names, addresses and some figures are representative."). Use: IP addresses from documentation ranges (192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24) or generic RFC 1918 examples; hostnames like `core`, `gw-1`, `lab-a`; people and labs as role names ("a chemistry lab", "Researcher A"); per-person or per-lab figures rounded or scaled, while aggregate system figures stay real and sourced. Representative values never change a conclusion, and the claims ledger maps each stand-in to the real record.

1. MUST NOT publish (even as stand-ins, no real values): secrets, credentials, internal IPs, MACs, hostnames that reveal internal layout, home address or location details beyond "a rural homestead in north-central Pennsylvania", family members' names, student or researcher data, lab names tied to incidents or spending, dollar figures for named researchers, vendor disputes, ticket numbers.
2. Work notes describe UCR systems Chuck runs (Ursa Major, CephRDS, the AI gateway, NRP namespace). They MUST NOT make claims about systems run by other units (for example the HPCC) beyond public facts.
3. Respect stated postures: describe security choices as decisions with their reasoning; do not publish exploit-relevant detail.

## 10. Index and site wiring

1. MUST: add an entry at the top of `papers/index.html` in the existing `notes-list` format (date, h3 link, one-paragraph summary under 60 words).
2. MUST: add the URL to `sitemap.xml`.
3. SHOULD: link earlier related Field Notes inline where relevant.

## 11. Quality gates (before a note may publish)

1. `npx html-validate papers/<file>.html` passes, and `npx prettier --check papers/<file>.html` passes (run `prettier --write` first).
2. `npx cspell papers/<file>.html` is clean (add true project words to `cspell.json`).
3. `npm test` passes.
4. Every internal anchor in the TOC resolves; every external link returns 200.
5. Word count is within section 4's limits; banned-word grep (section 5.2) is empty.
6. Claims ledger complete; an independent reviewer has checked a sample of at least 10 claims, or all of them for notes under 30 claims.
7. Chuck has read it and said publish. Nothing is pushed before that.

## 12. Checklist for the handoff

- [ ] File name, head metadata and skeleton match sections 2-3
- [ ] Required sections present and in order; Abstract 150-250 words with the method statement
- [ ] Body 2,000-4,500 words; banned words absent
- [ ] Every claim in the ledger with a source; Sources section complete
- [ ] No secrets, IPs, MACs, private data or dollar figures for named people
- [ ] Figures and tables numbered, captioned and referenced
- [ ] Gates 1-5 pass; output pasted in the handoff
