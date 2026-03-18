const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

function scaffold(projectName) {
    const projectPath = path.resolve(process.cwd(), projectName);

    console.log(`Scaffolding new Gemini project: ${projectName}...`);

    if (!fs.existsSync(projectPath)) {
        fs.mkdirSync(projectPath, { recursive: true });
    }

    process.chdir(projectPath);

    // 1. Initialize Git if needed
    if (!fs.existsSync(path.join(projectPath, '.git'))) {
        execSync('git init');
        console.log('Initialized new Git repository.');
    }

    // 2. Create .gitignore
    const gitignore = `node_modules/
tmp/
.env
.DS_Store
# Only keep session history, ignore the latest snapshot
session_logs/latest-session.md
`;
    fs.writeFileSync('.gitignore', gitignore);

    // 3. Create GEMINI.md
    const geminiMd = `# ${projectName}

## Project Goals
- (Add primary goals here)

## Core Standards
- Use the Gemini CLI for automated workflows.
- Maintain a clear TODO.md for task tracking.
- Log all sessions to project-local session_logs/.
`;
    fs.writeFileSync('GEMINI.md', geminiMd);

    // 4. Create TODO.md
    const todoMd = `# Project Plan: ${projectName}

- [ ] Initial project setup.
- [ ] Define core requirements.
- [ ] Begin development.
`;
    fs.writeFileSync('TODO.md', todoMd);

    // 5. Initial Commit
    execSync('git add .');
    try {
        execSync('git commit -m "initial: scaffolded project with gemini standards"');
    } catch (e) {
        // May fail if user details are not configured, that's okay
        console.warn('Initial commit failed (possibly missing git config).');
    }

    console.log(`Success! Project ${projectName} is ready in ${projectPath}.`);
}

const args = process.argv.slice(2);
if (args.length < 1) {
    console.log('Usage: node scaffold.cjs "<project-name>"');
    process.exit(1);
}

scaffold(args[0]);
