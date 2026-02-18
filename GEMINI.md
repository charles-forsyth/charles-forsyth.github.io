# charles-forsyth.github.io

## Project Overview
This repository contains the source code for the personal portfolio website of **Charles Forsyth**, Director of Research Computing at UCR and Architect of Agentic Ecosystems. The site showcases his work in High-Performance Computing (HPC), Directed Agentic Engineering (DAE), and key innovations like the Squad Manager and Skywalker systems.

## Tech Stack
*   **HTML5:** Semantic markup structure (`index.html`).
*   **CSS3:** Custom styling with CSS variables and responsive Grid/Flexbox layouts (`style.css`).
*   **Font Awesome:** Used for icons (via CDN).
*   **Hosting:** GitHub Pages (served directly).

## Architecture
This is a **static website** with no build step.
*   **`index.html`**: The single entry point containing all content.
*   **`style.css`**: The single stylesheet controlling the visual presentation.
*   **`.nojekyll`**: A marker file that instructs GitHub Pages to bypass Jekyll processing, ensuring files are served exactly as is.
*   **`.squad/`**: Configuration directory for the **Skywalker Squad** autonomous agents, containing persona definitions and project metadata.

## Development Workflow
1.  **Edit:** Modify `index.html` for content changes or `style.css` for visual updates.
2.  **Preview:** Open `index.html` in a local web browser. No local server is strictly required, though a simple HTTP server (e.g., `python3 -m http.server`) is recommended for accurate path resolution.
3.  **Deploy:** Commit and push changes to the `master` (or `main`) branch. GitHub Pages will automatically update the live site.

## Key Projects Featured
The portfolio highlights the following "Flagship Innovations":
*   **Squad Manager:** A recursive Gemini skill for deploying AI squads.
*   **Deep Research:** An autonomous research CLI.
*   **Automated Science:** A self-generating knowledge base for UCR HPC.
*   **Skywalker:** A fleet compliance engine for Google Cloud.

## Agentic Context
This project is equipped with **Skywalker Squad** configurations (`.squad/`), allowing specialized AI agents (Architect, DevOps, Gatekeeper, Grunt, Sentinel, UAT) to maintain and evolve the site autonomously.
