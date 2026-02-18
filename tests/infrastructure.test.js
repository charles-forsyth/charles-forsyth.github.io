import { describe, it, expect } from 'vitest';
import fs from 'node:fs';
import path from 'node:path';

describe('Project Hygiene Checks', () => {
  const projectRoot = path.resolve(__dirname, '..');

  it('should have a package.json file', () => {
    const packageJsonPath = path.join(projectRoot, 'package.json');
    expect(fs.existsSync(packageJsonPath)).toBe(true);
  });

  describe('Dependencies', () => {
    let packageJson = {};
    const packageJsonPath = path.join(projectRoot, 'package.json');

    if (fs.existsSync(packageJsonPath)) {
      packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf-8'));
    }

    it('should have prettier as a devDependency', () => {
      expect(packageJson.devDependencies).toBeDefined();
      expect(packageJson.devDependencies.prettier).toBeDefined();
    });

    it('should have eslint as a devDependency', () => {
      expect(packageJson.devDependencies).toBeDefined();
      expect(packageJson.devDependencies.eslint).toBeDefined();
    });

    it('should have html-validate as a devDependency', () => {
      expect(packageJson.devDependencies).toBeDefined();
      expect(packageJson.devDependencies['html-validate']).toBeDefined();
    });
  });

  describe('Configuration Files', () => {
    it('should have a .gitignore file', () => {
      const gitignorePath = path.join(projectRoot, '.gitignore');
      expect(fs.existsSync(gitignorePath)).toBe(true);
    });

    it('should have a .prettierrc file', () => {
      const prettierrcPath = path.join(projectRoot, '.prettierrc');
      expect(fs.existsSync(prettierrcPath)).toBe(true);
    });

    it('should have an .eslintrc.json file', () => {
      const eslintrcPath = path.join(projectRoot, '.eslintrc.json');
      expect(fs.existsSync(eslintrcPath)).toBe(true);
    });

    it('should have an .htmlvalidate.json file', () => {
      const htmlvalidatePath = path.join(projectRoot, '.htmlvalidate.json');
      // Some projects use .htmlvalidate.json, others use html-validate.json
      // The design doc specifies .htmlvalidate.json
      expect(fs.existsSync(htmlvalidatePath)).toBe(true);
    });
  });

  describe('Workflows', () => {
    it('should have a CI workflow file', () => {
      const workflowPath = path.join(projectRoot, '.github/workflows/ci.yml');
      expect(fs.existsSync(workflowPath)).toBe(true);
    });

    it('should have a Deploy workflow file', () => {
      const workflowPath = path.join(projectRoot, '.github/workflows/deploy.yml');
      expect(fs.existsSync(workflowPath)).toBe(true);
    });
  });

  describe('Source Files', () => {
    it('should have an index.js file', () => {
      const indexJsPath = path.join(projectRoot, 'index.js');
      expect(fs.existsSync(indexJsPath)).toBe(true);
    });
  });
});
