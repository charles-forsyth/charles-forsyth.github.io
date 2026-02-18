# Design Document: Project Hygiene Update

## 1. Mission Overview

**Objective:** Update the `charles-forsyth.github.io` repository to establish proper engineering standards, specifically focusing on version control hygiene (`.gitignore`) and development tooling configuration.
**Target Audience:** Charles Forsyth (Director of Research Computing).

## 2. Technology Stack & Language

Given the nature of the project (Static Website hosted on GitHub Pages), the stack is defined as:

- **Core:** HTML5, CSS3 (No preprocessors/bundlers as per existing architecture).
- **Dev Tooling:** Node.js (specifically for code formatting and linting).
  - **Package Manager:** `npm`
  - **Formatter:** `prettier`

## 3. Toolchain Definition

To ensure consistency and prevent "formatting wars", we will introduce a lightweight development toolchain.

### 3.1. Dependencies (`package.json`)

- `prettier`: For automatic code formatting of HTML, CSS, and JSON files.

### 3.2. Configuration

- **`.gitignore`**: A comprehensive ignore file covering:
  - OS system files (`.DS_Store`, `Thumbs.db`)
  - Node.js dependencies (`node_modules/`)
  - IDE configurations (`.vscode/`, `.idea/`)
  - Gemini/Agent temporary files (`.gemini/tmp/`)
  - Log files (`npm-debug.log`)
- **`.prettierrc`**: Configuration for Prettier to align with the user's style (if known, otherwise standard defaults: 2 spaces, single quotes where applicable).

## 4. Source Control & Directory Structure

The existing structure will be preserved, with the addition of configuration files in the root.

```
/
├── .gitignore          # [NEW] Git ignore definitions
├── .prettierrc         # [NEW] Prettier configuration
├── package.json        # [NEW] Dev dependencies
├── index.html          # [EXISTING] Entry point
├── style.css           # [EXISTING] Stylesheet
├── GEMINI.md           # [EXISTING] Project context
├── .nojekyll           # [EXISTING] GitHub Pages flag
└── .squad/             # [EXISTING] Agent configurations
```

## 5. CI/CD Workflow

We will implement a GitHub Actions workflow to enforce these standards.

- **File:** `.github/workflows/ci.yml`
- **Trigger:** Push to `master`/`main` and Pull Requests.
- **Job:** `check-format`
  - Checkout code.
  - Setup Node.js.
  - Install dependencies (`npm ci`).
  - Run Prettier check (`npx prettier --check .`).

## 6. Implementation Plan

1.  **Initialize Node.js:** Create `package.json`.
2.  **Install Prettier:** `npm install --save-dev prettier`.
3.  **Create Configs:** Write `.gitignore` and `.prettierrc`.
4.  **Format Code:** Run `npx prettier --write .` to baseline the repository.
5.  **Setup CI:** Create `.github/workflows/ci.yml`.
