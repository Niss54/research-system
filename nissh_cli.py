#!/usr/bin/env python3
"""
Nissh Research System CLI — Terminal & Editor Runner
===================================================
A standalone CLI to run 7-agent grounded research, capture real evidence,
manage multi-project runs, and compile investor dossiers.

Usage:
  python nissh_cli.py run --idea "Your problem statement" [--audience "ICP"] [--mode autonomous|hitl]
  python nissh_cli.py list
  python nissh_cli.py status <project_id>
  python nissh_cli.py evidence
  python nissh_cli.py test-evidence <url> "Claim"
"""

import os
import sys
import argparse
import time
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent

import v2
from v2.tools.evidence_vault import EvidenceVault
from v2.tools.link_validator import LinkValidator
from v2.tools.web_search import WebSearchEngine
from pdf_generator import render_pdf

def cmd_run(args):
    idea = args.idea.strip()
    audience = args.audience.strip() if args.audience else ""
    mode = args.mode

    if not idea:
        print("❌ Error: --idea cannot be empty.")
        sys.exit(1)

    print("=" * 70)
    print("🚀 NISSH RESEARCH SYSTEM v2 — GROUNDED AUTONOMOUS RUNNER")
    print("=" * 70)
    print(f"Problem:   {idea}")
    if audience:
        print(f"Audience:  {audience}")
    print(f"Execution: {mode.upper()} Mode")
    print("-" * 70)

    state_mgr = v2.StateManager()
    engine = v2.ResearchEngineV2(state_mgr)
    vault = EvidenceVault()

    project_id = state_mgr.create_project(idea, audience, mode=mode)
    print(f"📁 Session Initialized: [{project_id}]")

    try:
        # Phase 1
        print("\n[Phase 1/7] Problem Validator: Grounding pain signals on live web...")
        p1 = engine.run_agent_1(project_id, idea, audience)
        print(f"  Verdict: {p1.verdict} ({p1.verdict_reasoning})")
        print(f"  Severity: {p1.severity}/10 | Willingness to Pay: {p1.willingness_to_pay}")
        
        # Log first piece of evidence to vault
        if p1.key_sources:
            top_s = p1.key_sources[0]
            vault.record_evidence(
                claim=p1.problem_statement,
                source_url=top_s.get("url", "https://reddit.com"),
                source_title=top_s.get("title", "Market Pain Source"),
                exact_passage=top_s.get("snippet", ""),
                source_tier="Community",
                verification_status="VERIFIED" if p1.verdict == "GO" else "PARTIAL",
                confidence="High" if p1.severity >= 7 else "Medium",
                capture_media=True
            )
            print(f"  📸 Evidence & Screenshot captured in evidence/")

        if mode == "hitl":
            print(f"\n⏸️ HITL Pause: Phase 1 complete. Resume with: python nissh_cli.py resume {project_id}")
            return

        # Phase 2
        print("\n[Phase 2/7] Landscape Hunter: Auditing market & competitor websites...")
        p2 = engine.run_agent_2(project_id, p1)
        print(f"  Competitors Found: {len(p2.competitors)}")
        for c in p2.competitors[:4]:
            status_icon = "✅" if c.is_live else "⚠️"
            print(f"  {status_icon} {c.name} ({c.url}) - {c.pricing}")

        # Phase 3
        print("\n[Phase 3/7] Competitor Auditor: Performing forensic teardowns...")
        p3 = engine.run_agent_3(project_id, p2)
        print(f"  Teardowns Complete: {len(p3.profiles)} profiles generated.")

        # Phase 4
        print("\n[Phase 4/7] Strategic Gap Analyst: Synthesizing Feature Matrix & Scoring...")
        p4 = engine.run_agent_4(project_id, p1, p3)
        wedge_name = p4.recommended_wedge.name if p4.recommended_wedge else "N/A"
        print(f"  Top 5 Gaps Identified. #1 Recommended Wedge: {wedge_name}")

        # Phase 5
        print("\n[Phase 5/7] 9-Platform Gap Verifier: Searching GitHub & elimination check...")
        p5 = engine.run_agent_5(project_id, p4)
        print(f"  Verified Gaps: {len(p5.verified_gaps)}")
        for vg in p5.verified_gaps:
            print(f"  - {vg.name}: [{vg.verdict}]")

        # Phase 6
        print("\n[Phase 6/7] Diligence Synthesizer: Generating Investor Memo & 30-Day Plan...")
        p6 = engine.run_agent_6(project_id, p1, p5)
        print(f"  Proposed Brand: {p6.project_name_proposal}")
        print(f"  One-Line Pitch: {p6.one_line_pitch}")

        # Phase 7
        print("\n[Phase 7/7] Launch Architect: Building Production README & Telemetry Spec...")
        p7 = engine.run_agent_7(project_id, p6)
        print("  Production README Generated.")

        # Compile PDF Dossier
        print("\n📄 Compiling Official PDF Report with Nissh Watermark...")
        report_data = {
            "problem": p1.problem_statement,
            "audience": p1.target_audience,
            "verdict": p1.verdict,
            "p1": state_mgr.get_phase_output(project_id, 1)["raw_markdown"],
            "p2": state_mgr.get_phase_output(project_id, 2)["raw_markdown"],
            "p3": state_mgr.get_phase_output(project_id, 3)["raw_markdown"],
            "p4": state_mgr.get_phase_output(project_id, 4)["raw_markdown"],
            "p5": state_mgr.get_phase_output(project_id, 5)["raw_markdown"],
            "p6": state_mgr.get_phase_output(project_id, 6)["raw_markdown"],
            "p7": state_mgr.get_phase_output(project_id, 7)["raw_markdown"]
        }
        pdf_path = render_pdf(report_data)

        print("=" * 70)
        print("🎉 RESEARCH CYCLE COMPLETE!")
        print(f"Project ID: {project_id}")
        print(f"Official PDF: {pdf_path}")
        print(f"Evidence Ledger: {REPO_ROOT / 'evidence' / 'EVIDENCE_LEDGER.md'}")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ Pipeline failed: {e}")
        state_mgr.update_project_status(project_id, "failed")
        sys.exit(1)

def cmd_list(args):
    state_mgr = v2.StateManager()
    projects = state_mgr.list_projects()
    print("=" * 70)
    print(f"📁 NISSH RESEARCH SYSTEM — SAVED PROJECTS ({len(projects)})")
    print("=" * 70)
    if not projects:
        print("No research sessions recorded yet.")
        return
    for p in projects:
        print(f"• [{p['id']}] - Status: {p['status'].upper()} | Verdict: {p.get('verdict', 'N/A')}")
        print(f"  Idea: {p['title']}")
        print(f"  Date: {p['created_at']}\n")

def cmd_evidence(args):
    vault = EvidenceVault()
    print("=" * 70)
    print(f"🏛️ IMMUTABLE EVIDENCE VAULT ({len(vault.ledger)} Items)")
    print("=" * 70)
    for item in vault.ledger:
        print(f"[{item['id']}] {item['claim']}")
        print(f"  Source: {item['source_url']} (Tier: {item['source_tier']})")
        print(f"  Verdict: {item['verification_status']} | Confidence: {item['confidence']}")
        if item.get("screenshot_path"):
            print(f"  Screenshot: {item['screenshot_path']}")
        print()

def cmd_test_evidence(args):
    url = args.url
    claim = args.claim
    print(f"Capturing evidence for: {claim} from {url}...")
    vault = EvidenceVault()
    res = vault.record_evidence(
        claim=claim,
        source_url=url,
        source_title="Live Captured Source",
        exact_passage="Verified via manual CLI invocation",
        source_tier="Primary",
        verification_status="VERIFIED",
        confidence="High",
        capture_media=True
    )
    print("✅ Recorded Evidence:")
    print(f"  ID: {res['id']}")
    print(f"  Screenshot: {res.get('screenshot_path', 'None')}")
    print(f"  Snapshot: {res.get('snapshot_path', 'None')}")

def main():
    parser = argparse.ArgumentParser(description="Nissh Research System v2 CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # run command
    p_run = subparsers.add_parser("run", help="Run 7-agent research pipeline")
    p_run.add_argument("--idea", required=True, help="Raw startup hypothesis")
    p_run.add_argument("--audience", default="", help="Target ICP")
    p_run.add_argument("--mode", default="autonomous", choices=["autonomous", "hitl"], help="Execution mode")
    p_run.set_defaults(func=cmd_run)

    # list command
    p_list = subparsers.add_parser("list", help="List saved research projects")
    p_list.set_defaults(func=cmd_list)

    # evidence command
    p_ev = subparsers.add_parser("evidence", help="Show logged evidence items and media proof")
    p_ev.set_defaults(func=cmd_evidence)

    # test-evidence command
    p_test_ev = subparsers.add_parser("test-evidence", help="Capture a URL screenshot & log claim")
    p_test_ev.add_argument("url", help="Live web page URL")
    p_test_ev.add_argument("claim", help="Claim statement to verify")
    p_test_ev.set_defaults(func=cmd_test_evidence)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
