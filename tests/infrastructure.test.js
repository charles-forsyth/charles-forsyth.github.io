import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('Project Hygiene Checks', () => {
  const projectRoot = path.resolve(__dirname, '..');

  it('should have a package.json file', () => {
    const packageJsonPath = path.join(projectRoot, 'package.json');
    expect(fs.existsSync(packageJsonPath)).toBe(true);
  });

  it('should have prettier as a devDependency', () => {
    const packageJsonPath = path.join(projectRoot, 'package.json');
    if (fs.existsSync(packageJsonPath)) {
      const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf-8'));
      expect(packageJson.devDependencies).toBeDefined();
      expect(packageJson.devDependencies.prettier).toBeDefined();
    }
  });

  it('should have a .gitignore file', () => {
    const gitignorePath = path.join(projectRoot, '.gitignore');
    expect(fs.existsSync(gitignorePath)).toBe(true);
  });

  it('should have a .prettierrc file', () => {
    const prettierrcPath = path.join(projectRoot, '.prettierrc');
    expect(fs.existsSync(prettierrcPath)).toBe(true);
  });

  it('should have a CI workflow file', () => {
    const workflowPath = path.join(projectRoot, '.github/workflows/ci.yml');
    expect(fs.existsSync(workflowPath)).toBe(true);
  });
});
