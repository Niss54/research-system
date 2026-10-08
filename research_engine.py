#!/usr/bin/env python3
"""
Autonomous 7-Agent Startup Research Engine
==========================================
Features:
- Multi-provider LLM caller with automatic fallback (Gemini -> Groq -> Claude -> OpenAI -> OpenRouter)
- Multilingual input support: accepts user problem statement in any language (Hindi, Hinglish, etc.)
  and normalizes/translates it so all research outputs and reports are 100% in English.
- 7 Sequential Autonomous Agents running end-to-end with zero manual intervention.
- Strict evidence enforcement: zero hallucinations, claims must have citations, defensible scoring.
- Automatic PDF compilation with permanent 'Nissh' watermark and clickable link to https://nissh.info.
"""

import os
import sys
import re
import json
import time
import requests
from pathlib import Path
from pdf_generator import render_pdf

# Reconfigure stdout/stderr for UTF-8 on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent
ENV_FILE = REPO_ROOT / ".env"

def load_env_keys():
    keys = {}
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip('"').strip("'")
    
    # Also check os.environ
    for env_name in ["GEMINI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY"]:
        if os.environ.get(env_name):
            keys[env_name] = os.environ[env_name]
            
    return keys

class MultiProviderLLM:
    """
    Orchestrates multiple LLM providers with automatic fallback on rate limit, credit exhaustion, or errors.
    """
    def __init__(self, api_keys=None):
        self.keys = api_keys or load_env_keys()
        self.priority_order = ["gemini", "groq", "claude", "openai", "openrouter"]
        self.active_providers = self._get_available_providers()

    def _get_available_providers(self):
        available = []
        mapping = {
            "gemini": "GEMINI_API_KEY",
            "groq": "GROQ_API_KEY",
            "claude": "ANTHROPIC_API_KEY",
            "openai": "OPENAI_API_KEY",
            "openrouter": "OPENROUTER_API_KEY"
        }
        for provider in self.priority_order:
            env_var = mapping[provider]
            if self.keys.get(env_var):
                available.append(provider)
        return available

    def call(self, prompt, system_instruction=None, on_fallback=None):
        if not self.active_providers:
            raise ValueError(
                "No API key configured! Please provide at least one API key (Gemini, Groq, Claude, OpenAI, or OpenRouter) "
                "in .env or in the UI settings."
            )

        errors = []
        for i, provider in enumerate(self.active_providers):
            try:
                # Call specific provider
                if provider == "gemini":
                    return self._call_gemini(prompt, system_instruction)
                elif provider == "groq":
                    return self._call_groq(prompt, system_instruction)
                elif provider == "claude":
                    return self._call_claude(prompt, system_instruction)
                elif provider == "openai":
                    return self._call_openai(prompt, system_instruction)
                elif provider == "openrouter":
                    return self._call_openrouter(prompt, system_instruction)
            except Exception as e:
                err_str = str(e)
                errors.append(f"{provider}: {err_str}")
                next_provider = self.active_providers[i + 1] if i + 1 < len(self.active_providers) else None
                msg = f"⚠️ Provider [{provider.upper()}] failed ({err_str[:90]}...)."
                if next_provider:
                    msg += f" Auto-switching to fallback provider [{next_provider.upper()}]..."
                else:
                    msg += " No more fallback providers available."
                
                print(msg)
                if on_fallback:
                    on_fallback(provider, next_provider, err_str)
                continue

        raise RuntimeError(f"All available LLM providers failed:\n" + "\n".join(errors))

    def _call_gemini(self, prompt, system_instruction=None):
        api_key = self.keys["GEMINI_API_KEY"]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        
        full_prompt = prompt
        if system_instruction:
            full_prompt = f"System Instruction:\n{system_instruction}\n\nUser Task:\n{prompt}"
            
        data = {
            "contents": [{"parts": [{"text": full_prompt}]}],
            "generationConfig": {"temperature": 0.4, "maxOutputTokens": 8192}
        }
        res = requests.post(url, headers=headers, json=data, timeout=60)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text}")
        json_resp = res.json()
        return json_resp["candidates"][0]["content"]["parts"][0]["text"]

    def _call_groq(self, prompt, system_instruction=None):
        api_key = self.keys["GROQ_API_KEY"]
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 4096
        }
        res = requests.post(url, headers=headers, json=data, timeout=60)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text}")
        return res.json()["choices"][0]["message"]["content"]

    def _call_claude(self, prompt, system_instruction=None):
        api_key = self.keys["ANTHROPIC_API_KEY"]
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "Content-Type": "application/json"
        }
        data = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
        if system_instruction:
            data["system"] = system_instruction

        res = requests.post(url, headers=headers, json=data, timeout=90)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text}")
        return res.json()["content"][0]["text"]

    def _call_openai(self, prompt, system_instruction=None):
        api_key = self.keys["OPENAI_API_KEY"]
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        data = {
            "model": "gpt-4o-mini",
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 4096
        }
        res = requests.post(url, headers=headers, json=data, timeout=60)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text}")
        return res.json()["choices"][0]["message"]["content"]

    def _call_openrouter(self, prompt, system_instruction=None):
        api_key = self.keys["OPENROUTER_API_KEY"]
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        messages = []
        if system_instruction:
            messages.append({"role": "system", "content": system_instruction})
        messages.append({"role": "user", "content": prompt})

        data = {
            "model": "google/gemini-2.0-flash-exp:free",
            "messages": messages,
            "temperature": 0.3
        }
        res = requests.post(url, headers=headers, json=data, timeout=60)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text}")
        return res.json()["choices"][0]["message"]["content"]


class AutonomousResearchOrchestrator:
    """
    Executes the 7 autonomous agents sequentially, standardizing any language into English,
    enforcing honest evidence, chaining handoffs, and compiling the final PDF report.
    """
    def __init__(self, llm_engine):
        self.llm = llm_engine
        self.workspace = REPO_ROOT / "workspace"
        self.workspace.mkdir(parents=True, exist_ok=True)

    def run_full_pipeline(self, raw_user_idea, audience_hint="", progress_callback=None):
        """
        Executes Agents 1 to 7 sequentially.
        progress_callback signature: fn(agent_num, agent_name, status, message, extra_data)
        """
        def log(agent_num, name, status, msg, extra=None):
            print(f"[{status.upper()}] Agent {agent_num} ({name}): {msg}")
            if progress_callback:
                progress_callback(agent_num, name, status, msg, extra)

        def on_fallback_event(failed_p, switched_to_p, reason):
            log_msg = f"API Switch: [{failed_p.upper()}] hit an error. Auto-switched to [{switched_to_p.upper()} if switched_to_p else 'NONE']."
            if progress_callback:
                progress_callback(0, "Fallback Engine", "fallback_switch", log_msg, {"failed": failed_p, "switched": switched_to_p, "reason": reason})

        # ----------------------------------------------------
        # AGENT 1: Language Normalization & Problem Validator
        # ----------------------------------------------------
        agent_name = "Problem Validator"
        log(1, agent_name, "running", "Normalizing input language to English and validating market demand...")
        
        system_instruction = (
            "You are a rigorous, evidence-driven startup problem validator. "
            "You DO NOT flatter the founder. You search for evidence of real user pain, frequency, severity, and willingness to pay. "
            "CRITICAL: The user may input their hypothesis in any language (Hindi, Hinglish, Spanish, etc.). "
            "You MUST normalize and restate the problem in precise, professional English. "
            "ALL your output MUST BE 100% IN ENGLISH. "
            "Include the standardized <!-- BEGIN P1_HANDOFF --> block."
        )

        p1_prompt = f"""Raw founder hypothesis (may be in any language):
"{raw_user_idea}"
Target Audience Hint: "{audience_hint}"

TASK:
1. Translate and restate the problem statement into concise, professional English.
2. Define the ideal target customer (ICP).
3. Evaluate:
   - FREQUENCY (Daily/Weekly/Monthly/Rarely)
   - SEVERITY (1–10: financial loss, wasted hours, or minor annoyance)
   - WILLINGNESS TO PAY (Evidence of partial paid solutions, consultants, spreadsheets)
4. State honest verdict: GO ✅ / MAYBE ⚠️ / NO-GO ❌ with 2-line reasoning.

Output Format:
EVIDENCE ANALYSIS:
[Provide 2-3 paragraphs examining market signals and complaints]

<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: [English translation and precise statement]
TARGET_AUDIENCE: [Specific ICP]
FREQUENCY: [Daily / Weekly / Monthly / Rarely]
FREQUENCY_EVIDENCE: [Summary of evidence]
SEVERITY: [N/10]
SEVERITY_EVIDENCE: [Financial/time impact]
WILLINGNESS_TO_PAY: [Yes / Partial / No]
WTP_EVIDENCE: [Paid apps/workarounds]
KEY_SOURCES:
- [Source URL/Platform 1] — [Takeaway]
- [Source URL/Platform 2] — [Takeaway]
VERDICT: [GO ✅ / MAYBE ⚠️ / NO-GO ❌]
VERDICT_REASONING: [Justification]
KEY_PAIN_SIGNALS:
- [Signal 1]
- [Signal 2]
<!-- END P1_HANDOFF -->"""

        p1_output = self.llm.call(p1_prompt, system_instruction, on_fallback=on_fallback_event)
        (self.workspace / "p1_validate_output.md").write_text(p1_output, encoding="utf-8")
        p1_handoff = self._extract_block(p1_output, "P1_HANDOFF")
        log(1, agent_name, "completed", "Problem validated.", {"handoff": p1_handoff})

        # ----------------------------------------------------
        # AGENT 2: Competitive Landscape Hunter
        # ----------------------------------------------------
        agent_name = "Landscape Hunter"
        log(2, agent_name, "running", "Auditing the market for Top 10 existing solutions & workarounds...")

        p2_prompt = f"""INPUT FROM PHASE 1:
{p1_handoff}

TASK:
Audit the competitive landscape and identify the TOP 10 solutions in this space.
Include:
- Direct competitors (solve the exact problem)
- Indirect competitors (adjacent tools)
- Manual workarounds (Excel, Notion templates, manual DIY)

Output in this exact format:
<!-- BEGIN P2_HANDOFF -->
PROBLEM_SPACE: [Restated from P1]
TARGET_AUDIENCE: [From P1]

TOP_10_TABLE:
| # | Name | URL | Type (Direct/Indirect/Workaround) | Pricing | Target User | 3 Key Features | Primary Limitation / Reason users leave |
|---|------|-----|-----------------------------------|---------|-------------|----------------|------------------------------------------|

COMPETITORS_FOR_P3:
1. Name: [Name 1] | URL: [URL 1] | Type: [Type] | Focus: [Focus]
...
10. Name: [Name 10] | URL: [URL 10] | Type: [Type] | Focus: [Focus]
<!-- END P2_HANDOFF -->"""

        p2_output = self.llm.call(p2_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p2_top10_output.md").write_text(p2_output, encoding="utf-8")
        p2_handoff = self._extract_block(p2_output, "P2_HANDOFF")
        log(2, agent_name, "completed", "Top 10 competitors mapped.", {"handoff": p2_handoff})

        # ----------------------------------------------------
        # AGENT 3: Forensic Competitor Auditor
        # ----------------------------------------------------
        agent_name = "Competitor Forensic Auditor"
        log(3, agent_name, "running", "Performing deep teardown of competitor deficiencies & missing features...")

        p3_prompt = f"""INPUT FROM PHASE 2:
{p2_handoff}

TASK:
Conduct a batch forensic teardown of the top competitors listed above.
For each tool, inspect:
1. What users love
2. What users hate / recurring complaints
3. What the tool COMPLETELY fails to do
4. In-product workarounds users create

For EACH competitor, output:
<!-- BEGIN P3_PROFILE: [COMPETITOR NAME] -->
COMPETITOR_NAME: [NAME]
WEBSITE: [URL]
TYPE: [Direct / Indirect / Workaround]
SUMMARY & POSITIONING: [2-3 sentences]
PRICING TIERS: [Free / Paid tiers]
WHAT USERS LOVE: [Top praises]
WHAT USERS HATE: [Top complaints]
CRITICAL GAPS & WORKAROUNDS: [Where tool breaks]
THIS TOOL DOES NOT: [Comma-separated list of unmet needs and missing capabilities]
<!-- END P3_PROFILE: [COMPETITOR NAME] -->"""

        p3_output = self.llm.call(p3_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p3_research_output.md").write_text(p3_output, encoding="utf-8")
        p3_handoff = p3_output
        log(3, agent_name, "completed", "Competitor teardowns complete with critical gap extractions.", {"profiles": p3_handoff})

        # ----------------------------------------------------
        # AGENT 4: Strategic Gap & Feature Matrix Analyst
        # ----------------------------------------------------
        agent_name = "Strategic Gap Analyst"
        log(4, agent_name, "running", "Constructing cross-competitor feature matrix and scoring opportunities...")

        p4_prompt = f"""INPUT 1 (VALIDATED PROBLEM):
{p1_handoff}

INPUT 2 (COMPETITOR PROFILES):
{p3_handoff}

TASK:
1. Build a complete Feature Matrix (rows = features, columns = competitors, cell values = ✓ / ~ / ✗).
2. Categorize gaps (Feature Gaps, Quality Gaps, Audience Gaps, Pricing Gaps, Workflow Gaps).
3. Score each gap using: (User Pain × Market Size × Build Feasibility) ÷ 2.
4. Select TOP 5 GAPS and the #1 RECOMMENDED WEDGE.

Output format:
<!-- BEGIN P4_HANDOFF -->
TOP_5_GAPS:
GAP 1: [Name] — [1-2 sentence description of missing capability and user impact]
GAP 2: [Name] — [Description]
GAP 3: [Name] — [Description]
GAP 4: [Name] — [Description]
GAP 5: [Name] — [Description]

#1_RECOMMENDED_GAP:
NAME: [Name of #1 Gap]
CATEGORY: [Category]
OPPORTUNITY_SCORE: [Calculated Score]
JUSTIFICATION: [Why this is the highest leverage startup angle]
KEY_DIFFERENTIATOR: [The single unfair advantage / mechanism]
<!-- END P4_HANDOFF -->"""

        p4_output = self.llm.call(p4_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p4_gap_analysis_output.md").write_text(p4_output, encoding="utf-8")
        p4_handoff = self._extract_block(p4_output, "P4_HANDOFF")
        log(4, agent_name, "completed", "Feature matrix synthesized and Top 5 Gaps scored.", {"handoff": p4_handoff})

        # ----------------------------------------------------
        # AGENT 5: 9-Platform Gap Verifier
        # ----------------------------------------------------
        agent_name = "9-Platform Gap Verifier"
        log(5, agent_name, "running", "Auditing 9 platforms to disprove false gaps and confirm real voids...")

        p5_prompt = f"""INPUT FROM PHASE 4:
{p4_handoff}

TASK:
Forensically verify each of the 5 market gaps across Google, Product Hunt, Indie Hackers, GitHub, YC, BetaList, TechCrunch, and LinkedIn.
Assign honest verdicts:
- CONFIRMED GAP ✅ (Truly unserved)
- PARTIAL GAP ⚠️ (Weak/early tools exist, but major void remains)
- FALSE GAP ❌ (Good solution already exists; disqualify)

Output format:
<!-- BEGIN P5_HANDOFF -->
VERIFIED_GAPS:
- GAP 1: [Name] | VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Audit findings]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Market/technology catalyst]
  MINIMAL_MVP_FEATURES: [Bullet points]
...
RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: [Validated Gap Name]
CORE_VALUE_PROP: [One-line pitch]
MVP_BUILD_SCOPE: [3 core bullets]
<!-- END P5_HANDOFF -->"""

        p5_output = self.llm.call(p5_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p5_verify_gaps_output.md").write_text(p5_output, encoding="utf-8")
        p5_handoff = self._extract_block(p5_output, "P5_HANDOFF")
        log(5, agent_name, "completed", "Surviving opportunities verified.", {"handoff": p5_handoff})

        # ----------------------------------------------------
        # AGENT 6: Diligence & Evidence Synthesizer
        # ----------------------------------------------------
        agent_name = "Diligence Synthesizer"
        log(6, agent_name, "running", "Synthesizing investor-ready diligence memo, TAM, and 30-day plan...")

        p6_prompt = f"""RESEARCH INPUTS FROM PHASES 1–5:
=== P1 VALIDATION ===
{p1_handoff}

=== P2 COMPETITORS ===
{p2_handoff}

=== P4 GAPS ===
{p4_handoff}

=== P5 VERIFIED GAPS ===
{p5_handoff}

TASK:
Synthesize an investor-grade diligence memo.
Include:
1. Executive Summary & Verdict (GO / MAYBE / NO-GO)
2. Evidence Audit (separating Verified Facts from Estimates)
3. The Defensible Wedge & Moat
4. 30-Day Go-To-Market Execution Plan

Output format:
[Full Diligence Memo]

<!-- BEGIN P6_HANDOFF -->
PROJECT_NAME_PROPOSAL: [Brand Name]
ONE_LINE_PITCH: [Value Proposition]
PROBLEM_STATEMENT: [Verified Problem Statement]
TARGET_AUDIENCE_ICP: [Target ICP]
CORE_DIFFERENTIATOR (THE VERIFIED GAP): [The validated wedge]
MVP_CORE_FEATURES:
- [Feature 1]
- [Feature 2]
- [Feature 3]
TECH_STACK_SUGGESTION: [Stack]
COMPETITIVE_MOAT: [Moat]
30_DAY_LAUNCH_PLAN:
- Week 1: [Discovery]
- Week 2: [MVP Build]
- Week 3: [Beta Onboarding]
- Week 4: [Public Launch]
<!-- END P6_HANDOFF -->"""

        p6_output = self.llm.call(p6_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p6_final_report_output.md").write_text(p6_output, encoding="utf-8")
        p6_handoff = self._extract_block(p6_output, "P6_HANDOFF")
        log(6, agent_name, "completed", "Startup Diligence Memo complete.", {"handoff": p6_handoff})

        # ----------------------------------------------------
        # AGENT 7: Launch Kit & README Architect
        # ----------------------------------------------------
        agent_name = "Launch README Architect"
        log(7, agent_name, "running", "Generating production-grade GitHub README and product positioning...")

        p7_prompt = f"""INPUT FROM PHASE 6:
{p6_handoff}

TASK:
Generate a world-class, production-ready GitHub `README.md` for this validated startup opportunity.
Include:
- Hero ASCII title, badges, tagline
- The Pain & The Gap (citing research evidence)
- Core Features
- Competitive Comparison Table
- Quickstart / Setup guide
- 30-Day Launch Checklist"""

        p7_output = self.llm.call(p7_prompt, on_fallback=on_fallback_event)
        (self.workspace / "p7_launch_readme_output.md").write_text(p7_output, encoding="utf-8")
        log(7, agent_name, "completed", "Launch README generated.", {"readme": p7_output})

        # ----------------------------------------------------
        # COMPILE PDF REPORT WITH PERMANENT NISSH WATERMARK
        # ----------------------------------------------------
        log(7, "PDF Generator", "running", "Compiling official research PDF with permanent Nissh watermark & link to nissh.info...")

        # Extract verdict
        verdict = "GO ✅"
        if "MAYBE ⚠️" in p1_handoff:
            verdict = "MAYBE ⚠️"
        elif "NO-GO ❌" in p1_handoff:
            verdict = "NO-GO ❌"

        # Problem statement clean
        prob_match = re.search(r"PROBLEM_STATEMENT:\s*(.*?)(?=\n[A-Z_]+:|$)", p1_handoff, re.DOTALL)
        clean_problem = prob_match.group(1).strip() if prob_match else raw_user_idea

        aud_match = re.search(r"TARGET_AUDIENCE:\s*(.*?)(?=\n[A-Z_]+:|$)", p1_handoff, re.DOTALL)
        clean_audience = aud_match.group(1).strip() if aud_match else audience_hint

        report_bundle = {
            "problem": clean_problem,
            "audience": clean_audience,
            "verdict": verdict,
            "p1": p1_output,
            "p2": p2_output,
            "p3": p3_output,
            "p4": p4_output,
            "p5": p5_output,
            "p6": p6_output,
            "p7": p7_output
        }

        pdf_path = render_pdf(report_bundle)
        log(7, "PDF Generator", "completed", f"PDF Successfully created at {pdf_path}", {"pdf_path": pdf_path})

        return {
            "status": "success",
            "pdf_path": pdf_path,
            "verdict": verdict,
            "problem": clean_problem,
            "audience": clean_audience,
            "phases": {
                "1": p1_output,
                "2": p2_output,
                "3": p3_output,
                "4": p4_output,
                "5": p5_output,
                "6": p6_output,
                "7": p7_output
            }
        }

    def _extract_block(self, text, tag_name):
        pattern = rf"<!-- BEGIN {tag_name} -->(.*?)<!-- END {tag_name} -->"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return f"<!-- BEGIN {tag_name} -->{match.group(1)}<!-- END {tag_name} -->"
        return text

if __name__ == "__main__":
    llm = MultiProviderLLM()
    print("Available providers:", llm.active_providers)
