# Design Document: Quality Assurance & Publishing Pipeline

## 1. Mission Overview

**Objective:** Establish a robust error-checking pipeline and automated publishing workflow for the `charles-forsyth.github.io` portfolio.
**Mission:** "Check for errors and publish."
**Target Audience:** Charles Forsyth (Director of Research Computing).

## 2. Technology Stack & Language

The project is a static website. We will use a **Node.js-based toolchain** for development hygiene and **GitHub Actions** for CI/CD.

- **Core:**
  - HTML5 (Semantic Markup)
  - CSS3 (Custom Properties, Flexbox/Grid)
  - JavaScript (ES6+, Vanilla)
- **Dev Tooling (Node.js):**
  - **Package Manager:** `npm`
  - **Formatter:** `prettier` (Code style enforcement)
  - **Linter:** `eslint` (JavaScript error checking)
  - **Validator:** `html-validate` (HTML standards compliance)

## 3. Toolchain Definition

### 3.1. Dependencies (`package.json`)

- `prettier`: Formatting for HTML, CSS, JS, JSON.
- `eslint`: Static analysis for `index.js`.
- `eslint-config-prettier`: Disables conflicting ESLint rules.
- `html-validate`: Checks for HTML errors (unclosed tags, invalid attributes).

### 3.2. Configuration

- **`.gitignore`**: Standard exclusions (`node_modules/`, `.DS_Store`, `.gemini/`, etc.).
- **`.prettierrc`**: Standard formatting rules (2 spaces, single quotes).
- **`.eslintrc.json`**: Basic recommended JS rules (`eslint:recommended`).
- **`.htmlvalidate.json`**: HTML validation rules (`"extends": ["html-validate:recommended"]`).

## 4. Architecture & Directory Structure

The structure remains flat for simplicity, with configuration files at the root.

```
/
├── .github/
│   └── workflows/
│       ├── ci.yml          # [NEW] Lint & Test workflow
│       └── deploy.yml      # [NEW] Deploy to GitHub Pages workflow
├── .gitignore              # [NEW] Git ignore definitions
├── .prettierrc             # [NEW] Prettier config
├── .eslintrc.json          # [NEW] ESLint config
├── package.json            # [NEW] Dependencies
├── index.html              # [EXISTING] Main content
├── index.js                # [EXISTING] Interactive logic
├── style.css               # [EXISTING] Styles
└── GEMINI.md               # [EXISTING] Project context
```

## 5. CI/CD Workflows (`.github/workflows/`)

### 5.1. Continuous Integration (`ci.yml`)

- **Trigger:** Push to any branch, Pull Requests.
- **Jobs:**
  - `lint`: Runs `eslint`, `prettier --check`, and `html-validate`.

### 5.2. Continuous Deployment (`deploy.yml`)

- **Trigger:** Push to `master` (or `main`) _only after CI passes_.
- **Job:** `deploy`
  - Uses `actions/upload-pages-artifact` and `actions/deploy-pages`.
  - Ensures the live site is always a clean, validated build.

## 6. Implementation Plan

1.  **Initialize:** Create `package.json` and install dev dependencies.
2.  **Configure:** Create `.gitignore`, `.prettierrc`, `.eslintrc.json`.
3.  **Baseline:** Run `prettier --write .` and fix any initial linting errors.
4.  **Automate:** Create `.github/workflows/ci.yml` and `.github/workflows/deploy.yml`.
5.  **Verify:** Run the full lint command locally to ensure "zero errors" before pushing.
