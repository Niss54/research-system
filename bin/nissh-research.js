#!/usr/bin/env node

/**
 * Nissh Research System — Universal NPX Runner
 * ============================================
 * Created by Nishant Maurya (https://nissh.info)
 * 
 * Interactive Dual-Mode Launcher:
 *   Mode 1: 🌐 Interactive Web UI & Playbook (localhost:5000)
 *   Mode 2: 💻 Local Code Editor / Antigravity Skill Installation
 * 
 * Invariant:
 *   Skill remains 100% DORMANT and only activates when user explicitly says "use nissh skills".
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const readline = require('readline');

const PKG_ROOT = path.resolve(__dirname, '..');
const CLI_PATH = path.join(PKG_ROOT, 'nissh_cli.py');
const SERVER_PATH = path.join(PKG_ROOT, 'server.py');

function getPythonCommand() {
  const candidates = process.platform === 'win32'
    ? ['python', 'py', 'python3']
    : ['python3', 'python'];
  return candidates[0];
}

const pythonCmd = getPythonCommand();
const args = process.argv.slice(2);

function printBanner() {
  console.log(`\x1b[36m
  _   _ _           _        ____                               _     
 | \\ | (_)___ ___  | |__    |  _ \\ ___  ___  ___  __ _ _ __ ___| |__  
 |  \\| | / __/ __| | '_ \\   | |_) / _ \\/ __|/ _ \\/ _\` | '__/ __| '_ \\ 
 | |\\  | \\__ \\__ \\ | | | |  |  _ <  __/\\__ \\  __/ (_| | | | (__| | | |
 |_| \\_|_|___/___/ |_| |_|  |_| \\_\\___||___/\\___|\\__,_|_|  \\___|_| |_|
                                                         v2.0.2
\x1b[0m\x1b[90m  Autonomous 7-Agent Grounded Startup Research | nissh.info\x1b[0m\n`);
}

function launchWebUI() {
  console.log('\x1b[32m🚀 Launching Nissh Research Web UI & Server...\x1b[0m');
  console.log('\x1b[90m   Local server: http://localhost:5000\x1b[0m\n');

  const child = spawn(pythonCmd, [SERVER_PATH], {
    cwd: process.cwd(),
    stdio: 'inherit',
    env: { ...process.env, PYTHONPATH: PKG_ROOT }
  });

  child.on('error', (err) => {
    console.error(`\x1b[31m❌ Failed to start Python server: ${err.message}\x1b[0m`);
    console.log('Please ensure Python 3.9+ is installed and available in your PATH.');
    process.exit(1);
  });

  setTimeout(() => {
    const openCmd = process.platform === 'win32' ? 'start' : (process.platform === 'darwin' ? 'open' : 'xdg-open');
    spawn(openCmd, ['http://localhost:5000'], { shell: true, stdio: 'ignore' });
  }, 1500);
}

function installLocalSkill() {
  const cwd = process.cwd();
  console.log(`\x1b[32m📦 Installing Nissh Research Skill into local project...\x1b[0m`);
  console.log(`\x1b[90m   Target Workspace: ${cwd}\x1b[0m\n`);

  // Target directories for Antigravity & local editors
  const geminiSkillDir = path.join(cwd, '.gemini', 'skills', 'nissh-research');
  const projectSkillDir = path.join(cwd, 'skills', 'nissh-research');
  const evidenceDir = path.join(cwd, 'evidence');

  [geminiSkillDir, projectSkillDir, path.join(evidenceDir, 'screenshots'), path.join(evidenceDir, 'snapshots')].forEach(dir => {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  });

  // Copy SKILL.md
  const srcSkill = path.join(PKG_ROOT, 'skills', 'nissh-research', 'SKILL.md');
  if (fs.existsSync(srcSkill)) {
    fs.copyFileSync(srcSkill, path.join(geminiSkillDir, 'SKILL.md'));
    fs.copyFileSync(srcSkill, path.join(projectSkillDir, 'SKILL.md'));
  }

  // Copy P1 to P7 markdown prompts
  ['P1_Validate.md', 'P2_Top10.md', 'P3_Research_x10.md', 'P4_Gap_Analysis.md', 'P5_Verify_Gaps.md', 'P6_Final_Report.md', 'P7_Make_README.md'].forEach(file => {
    const src = path.join(PKG_ROOT, file);
    if (fs.existsSync(src)) {
      fs.copyFileSync(src, path.join(cwd, file));
    }
  });

  console.log(`\x1b[32m✅ Nissh Research Skill successfully installed!\x1b[0m`);
  console.log(`
\x1b[1m📁 Installed Locations:\x1b[0m
  • Antigravity Skill: \x1b[36m.gemini/skills/nissh-research/SKILL.md\x1b[0m
  • Local Skill Copy:  \x1b[36mskills/nissh-research/SKILL.md\x1b[0m
  • 7 Agent Prompts:   \x1b[36mP1_Validate.md → P7_Make_README.md\x1b[0m
  • Evidence Vault:    \x1b[36mevidence/\x1b[0m

\x1b[1m🛡️ MANDATORY DORMANT RULE CONFIGURED:\x1b[0m
  Ye skill aapke code editor mein bilkul \x1b[33mDORMANT\x1b[0m rahegi aur kisi normal coding kaam mein taang nahi adegi.
  
  Jab aapko market research run karni ho, tab chat mein likhein:
  👉 \x1b[32m"use nissh skills"\x1b[0m ya \x1b[32m"nissh research"\x1b[0m
  aur apna problem hypothesis likhein. Tabhi agents activate honge!
`);
}

function runCli(commandArgs) {
  const child = spawn(pythonCmd, [CLI_PATH, ...commandArgs], {
    cwd: process.cwd(),
    stdio: 'inherit',
    env: { ...process.env, PYTHONPATH: PKG_ROOT }
  });

  child.on('error', (err) => {
    console.error(`\x1b[31m❌ Failed to execute command: ${err.message}\x1b[0m`);
    console.log('Please ensure Python 3.9+ is installed and available in your PATH.');
    process.exit(1);
  });

  child.on('exit', (code) => {
    process.exit(code || 0);
  });
}

// Main logic
printBanner();

if (args.length === 0) {
  // Interactive Prompt
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  console.log('\x1b[1mHow would you like to run the Nissh Research System?\x1b[0m\n');
  console.log('  \x1b[36m[1]\x1b[0m 🌐 \x1b[1mInteractive Web UI\x1b[0m  (Launches local server at localhost:5000 with visual playbook)');
  console.log('  \x1b[36m[2]\x1b[0m 💻 \x1b[1mLocal Code Editor\x1b[0m   (Installs dormant skill into this project for Antigravity, VS Code, Claude)\n');

  rl.question('Select an option [1 or 2] (Default: 1): ', (answer) => {
    rl.close();
    const choice = answer.trim();
    if (choice === '2' || choice.toLowerCase() === 'local' || choice.toLowerCase() === 'skill') {
      installLocalSkill();
    } else {
      launchWebUI();
    }
  });

} else if (args[0] === 'web' || args[0] === 'serve' || args[0] === '--web') {
  launchWebUI();
} else if (args[0] === 'install' || args[0] === 'skill' || args[0] === '--skill') {
  installLocalSkill();
} else {
  runCli(args);
}
