#!/usr/bin/env node

/**
 * Nissh Research System — NPX Runner
 * ==================================
 * Created by Nishant Maurya (https://nissh.info)
 * 
 * Runs the 7-Agent Autonomous Startup Research System locally:
 *   npx nissh-research                         # Launches interactive Web UI & Playbook
 *   npx nissh-research web                     # Starts local web server on port 5000
 *   npx nissh-research run --idea "..."        # Runs 7-agent pipeline in terminal
 *   npx nissh-research evidence                # Displays evidence vault & screenshots
 *   npx nissh-research list                    # Lists saved research sessions
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const PKG_ROOT = path.resolve(__dirname, '..');
const CLI_PATH = path.join(PKG_ROOT, 'nissh_cli.py');
const SERVER_PATH = path.join(PKG_ROOT, 'server.py');

// Detect Python binary
function getPythonCommand() {
  const candidates = process.platform === 'win32'
    ? ['python', 'py', 'python3']
    : ['python3', 'python'];
  return candidates[0];
}

const args = process.argv.slice(2);
const pythonCmd = getPythonCommand();

// Header banner
console.log(`\x1b[36m
  _   _ _           _        ____                               _     
 | \\ | (_)___ ___  | |__    |  _ \\ ___  ___  ___  __ _ _ __ ___| |__  
 |  \\| | / __/ __| | '_ \\   | |_) / _ \\/ __|/ _ \\/ _\` | '__/ __| '_ \\ 
 | |\\  | \\__ \\__ \\ | | | |  |  _ <  __/\\__ \\  __/ (_| | | | (__| | | |
 |_| \\_|_|___/___/ |_| |_|  |_| \\_\\___||___/\\___|\\__,_|_|  \\___|_| |_|
                                                         v2.0.0
\x1b[0m\x1b[90m  Autonomous 7-Agent Grounded Startup Research | nissh.info\x1b[0m\n`);

if (args.length === 0 || args[0] === 'web' || args[0] === 'serve') {
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

  // Open browser after 1.5s
  setTimeout(() => {
    const openCmd = process.platform === 'win32' ? 'start' : (process.platform === 'darwin' ? 'open' : 'xdg-open');
    spawn(openCmd, ['http://localhost:5000'], { shell: true, stdio: 'ignore' });
  }, 1500);

} else {
  // Forward commands directly to nissh_cli.py
  const child = spawn(pythonCmd, [CLI_PATH, ...args], {
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
