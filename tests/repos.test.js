import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('GitHub Repos Section', () => {
  const projectRoot = path.resolve(__dirname, '..');
  const indexHtmlPath = path.join(projectRoot, 'index.html');
  const htmlContent = fs.readFileSync(indexHtmlPath, 'utf-8');

  it('should have a section for GitHub repositories', () => {
    expect(htmlContent).toContain('<section id="github-repos"');
    expect(htmlContent).toContain('</section>');
  });

  it('should have a search input for repositories', () => {
    expect(htmlContent).toContain('<input');
    expect(htmlContent).toContain('id="repo-search"');
  });

  it('should have a container for the repository list', () => {
    expect(htmlContent).toContain('<div id="repo-list"');
  });

  it('should have a navigation link to the repositories section', () => {
    expect(htmlContent).toContain('href="#github-repos"');
  });

  it('should include JavaScript for fetching repositories', () => {
     // Check for either an inline script or external script file reference
    const hasInlineScript = htmlContent.includes('<script>') && htmlContent.includes('fetch(');
    const hasExternalScript = htmlContent.includes('<script src="index.js"></script>');
    expect(hasInlineScript || hasExternalScript).toBe(true);
  });
});
