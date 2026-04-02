const fs = require('fs');
const path = require('path');

async function main() {
  const rootDir = process.cwd();
  const roadmapPath = path.join(rootDir, 'ROADMAP.md');
  const templatePath = path.join(__dirname, '..', 'references', 'roadmap-template.md');
  const backlogPath = path.join(rootDir, 'backlog.md');

  if (fs.existsSync(roadmapPath)) {
    console.log('ROADMAP.md already exists.');
    return;
  }

  let roadmapContent = '';
  if (fs.existsSync(templatePath)) {
    roadmapContent = fs.readFileSync(templatePath, 'utf8');
  } else {
    console.error('Roadmap template not found.');
    process.exit(1);
  }

  if (fs.existsSync(backlogPath)) {
    console.log('Found backlog.md. Attempting to populate ROADMAP.md...');
    const backlogContent = fs.readFileSync(backlogPath, 'utf8');
    // Basic heuristic: look for tasks in backlog.md and move them to SOON or LATER
    // For now, we'll just keep the template as-is but add a note.
    roadmapContent += '\n\n*Note: initial roadmap generated with backlog.md present. Please manually audit and organize tasks.*';
  }

  fs.writeFileSync(roadmapPath, roadmapContent);
  console.log(`✅ ROADMAP.md initialized at ${roadmapPath}`);
}

main();
