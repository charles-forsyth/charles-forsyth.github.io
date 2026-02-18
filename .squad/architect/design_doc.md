# Mission: Add GitHub Repositories Feature

## Mission Goal

Display a searchable list of GitHub repositories from `https://github.com/charles-forsyth` at the bottom of the portfolio page, with a navigation link in the header.

## Technical Design

- **Fetching:** Use `fetch('https://api.github.com/users/charles-forsyth/repos')` on page load.
- **Rendering:**
  - Create a `<section id="github-repos">` at the bottom of `index.html`.
  - Add a search input: `<input type="text" id="repo-search" placeholder="Search repos...">`.
  - Display repositories as cards (`.repo-card`) inside a container (`#repo-list`).
  - Show name, description, stars (`stargazers_count`), and language.
- **Filtering:** Add an event listener to `#repo-search` to filter the displayed list by name.
- **Navigation:** Add a link `<a href="#github-repos">Projects</a>` to the main navigation.
- **Styling:** Update `style.css` to style the repo cards and search input (grid layout, responsive).

## Workflow

1. **DevOps:** Bump version to `1.1.0`.
2. **Sentinel:** Create `tests/repos.test.js` to verify section existence.
3. **Grunt:** Implement HTML structure, CSS styles, and JavaScript logic.
4. **Gatekeeper:** Verify tests pass (`npm test`).
5. **UAT:** Verify functionality manually/visually.
