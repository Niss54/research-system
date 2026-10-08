#!/usr/bin/env python3
"""
Startup Research System - Local Web & API Server
Serves the interactive UI, runs the 7-agent autonomous pipeline,
manages API key fallbacks, and serves the watermarked PDF report.
"""

import os
import sys
import threading
import json
from pathlib import Path
from flask import Flask, request, jsonify, send_file, Response

# Reconfigure stdout/stderr for UTF-8 on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent
ENV_FILE = REPO_ROOT / ".env"

from research_engine import MultiProviderLLM, AutonomousResearchOrchestrator, load_env_keys
from pdf_generator import render_pdf

app = Flask(__name__, static_folder=str(REPO_ROOT), static_url_path="")

# Global Pipeline Run State
pipeline_state = {
    "is_running": False,
    "current_agent": 0,
    "current_agent_name": "Idle",
    "status": "idle", # "idle", "running", "completed", "error"
    "logs": [],
    "fallback_events": [],
    "result": None,
    "error": None
}
state_lock = threading.Lock()

@app.route("/")
def index():
    return send_file(REPO_ROOT / "startup_research_playbook.html")

@app.route("/api/keys", methods=["GET"])
def get_keys_status():
    keys = load_env_keys()
    masked = {}
    for k in ["GEMINI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY"]:
        val = keys.get(k, "")
        if val:
            masked[k] = val[:6] + "..." + val[-4:] if len(val) > 10 else "***"
        else:
            masked[k] = ""
    return jsonify({
        "keys": masked,
        "has_at_least_one": any(bool(keys.get(k)) for k in ["GEMINI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY"])
    })

@app.route("/api/save-keys", methods=["POST"])
def save_keys():
    data = request.json or {}
    existing_keys = load_env_keys()
    
    for k in ["GEMINI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY"]:
        if k in data and data[k] and not data[k].startswith("***"):
            existing_keys[k] = data[k].strip()

    # Write to .env
    with open(ENV_FILE, "w", encoding="utf-8") as f:
        for k, v in existing_keys.items():
            f.write(f'{k}="{v}"\n')

    return jsonify({"status": "success", "message": "API keys saved to .env"})

@app.route("/api/run", methods=["POST"])
def start_research():
    global pipeline_state
    with state_lock:
        if pipeline_state["is_running"]:
            return jsonify({"status": "error", "message": "Research pipeline is already running."}), 400

    data = request.json or {}
    raw_idea = data.get("idea", "").strip()
    audience_hint = data.get("audience", "").strip()
    custom_keys = data.get("keys", {})

    if not raw_idea:
        return jsonify({"status": "error", "message": "Idea statement cannot be empty."}), 400

    # Merge keys
    all_keys = load_env_keys()
    for k, v in custom_keys.items():
        if v and not v.startswith("***"):
            all_keys[k] = v.strip()

    # Reset state
    with state_lock:
        pipeline_state = {
            "is_running": True,
            "current_agent": 1,
            "current_agent_name": "Problem Validator",
            "status": "running",
            "logs": [f"🚀 Pipeline started for problem: '{raw_idea[:60]}...'"],
            "fallback_events": [],
            "result": None,
            "error": None
        }

    def background_worker():
        global pipeline_state
        try:
            llm_engine = MultiProviderLLM(api_keys=all_keys)
            orchestrator = AutonomousResearchOrchestrator(llm_engine)

            def progress_callback(agent_num, name, status, msg, extra):
                with state_lock:
                    if status == "fallback_switch":
                        pipeline_state["fallback_events"].append(msg)
                        pipeline_state["logs"].append(f"⚡ {msg}")
                    else:
                        pipeline_state["current_agent"] = agent_num
                        pipeline_state["current_agent_name"] = name
                        pipeline_state["logs"].append(f"[{name}] {msg}")

            res = orchestrator.run_full_pipeline(raw_idea, audience_hint, progress_callback=progress_callback)
            
            with state_lock:
                pipeline_state["is_running"] = False
                pipeline_state["status"] = "completed"
                pipeline_state["result"] = res
                pipeline_state["logs"].append("🎉 7-Agent Research Cycle Complete! PDF Report Generated.")
        except Exception as e:
            err_str = str(e)
            with state_lock:
                pipeline_state["is_running"] = False
                pipeline_state["status"] = "error"
                pipeline_state["error"] = err_str
                pipeline_state["logs"].append(f"❌ Error: {err_str}")

    thread = threading.Thread(target=background_worker, daemon=True)
    thread.start()

    return jsonify({"status": "started", "message": "7 Autonomous Agents launched."})

@app.route("/api/status", methods=["GET"])
def get_status():
    with state_lock:
        return jsonify(pipeline_state)

@app.route("/api/download-pdf", methods=["GET"])
def download_pdf():
    pdf_path = REPO_ROOT / "workspace" / "STARTUP_RESEARCH_REPORT.pdf"
    if not pdf_path.exists():
        # Check if sample demo exists or generate default
        return jsonify({"status": "error", "message": "PDF report not yet generated. Please run the research pipeline first."}), 404
    
    return send_file(
        pdf_path,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="STARTUP_RESEARCH_REPORT.pdf"
    )

@app.route("/api/demo", methods=["POST"])
def load_demo():
    sample = {
        "problem": "Freelance web designers and developers in India and Southeast Asia struggle to manage scope creep and get paid for extra revision rounds. Clients repeatedly ask for 'one minor tweak' without approving change orders, causing freelancers to lose $500–$2,000/month in unbilled labor.",
        "audience": "Freelance web designers, UI/UX developers, and boutique creative agency owners",
        "verdict": "GO ✅",
        "p1": "Daily frequency, severity 8/10, proven willingness to pay for Bonsai/HoneyBook/Notion templates.",
        "p2": "Bonsai, HoneyBook, Contra, MarkUp.io, Pastell, Google Sheets + Stripe invoice.",
        "p3": "Bonsai: lacks automated revision counting. MarkUp.io: zero contract or payment gating.",
        "p4": "Top Gap: Automated Smart Scope Paywall & Gated Revision Submissions (Score 8.5/10).",
        "p5": "Verified Gap: Zero existing tools connect revision caps directly to Stripe change-order paywalls.",
        "p6": "ScopeLock: The automated client revision gatekeeper that stops scope creep.",
        "p7": "# 🛡️ ScopeLock\n> The automated client revision gatekeeper that stops scope creep and turns extra feedback into paid change orders."
    }
    pdf_path = render_pdf(sample)
    return jsonify({"status": "success", "message": "Demo loaded and PDF compiled.", "pdf_path": pdf_path})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"🚀 Nissh Startup Research System server running on http://localhost:{port}")
    app.run(host="0.0.0.0", port=port, debug=False)
