import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('Content Checks', () => {
  const projectRoot = path.resolve(__dirname, '..');
  const indexHtmlPath = path.join(projectRoot, 'index.html');

  it('should have an index.html file', () => {
    expect(fs.existsSync(indexHtmlPath)).toBe(true);
  });

  it('index.html should be valid HTML5', () => {
    const html = fs.readFileSync(indexHtmlPath, 'utf-8');
    expect(html).toContain('<!DOCTYPE html>');
    expect(html).toContain('<html');
    expect(html).toContain('</html>');
    expect(html).toContain('<body');
    expect(html).toContain('</body>');
  });

  it('should have a style.css file', () => {
    const styleCssPath = path.join(projectRoot, 'style.css');
    expect(fs.existsSync(styleCssPath)).toBe(true);
  });
});
