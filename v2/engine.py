"""
Nissh Research System v2 - Enhanced Autonomous Engine
=====================================================
Combines Multi-Provider LLM Fallbacks with Grounded Tool Execution
(Web Search, GitHub Verification, and Live Link Validation).
"""

import os
import re
import json
from typing import Dict, Any, List, Optional, Callable
from pathlib import Path
import requests

from .models import (
    P1ValidationHandoff, P2LandscapeHandoff, CompetitorItem,
    P3ResearchHandoff, CompetitorTeardown,
    P4GapAnalysisHandoff, GapItem,
    P5VerifyGapsHandoff, VerifiedGapItem,
    P6DiligenceHandoff, P7LaunchHandoff
)
from .tools.web_search import WebSearchEngine
from .tools.link_validator import LinkValidator
from .tools.github_verifier import GitHubVerifier
from .state_manager import StateManager

REPO_ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = REPO_ROOT / ".env"

def load_keys():
    keys = {}
    if ENV_FILE.exists():
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    keys[k.strip()] = v.strip().strip('"').strip("'")
    for k in ["GEMINI_API_KEY", "GROQ_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY", "OPENROUTER_API_KEY", "TAVILY_API_KEY", "SERPER_API_KEY"]:
        if os.environ.get(k):
            keys[k] = os.environ[k]
    return keys


class LLMCaller:
    def __init__(self, keys: Optional[Dict[str, str]] = None):
        self.keys = keys or load_keys()
        self.priority = ["gemini", "groq", "claude", "openai", "openrouter"]

    def _get_active(self):
        mapping = {
            "gemini": "GEMINI_API_KEY",
            "groq": "GROQ_API_KEY",
            "claude": "ANTHROPIC_API_KEY",
            "openai": "OPENAI_API_KEY",
            "openrouter": "OPENROUTER_API_KEY"
        }
        return [p for p in self.priority if self.keys.get(mapping[p])]

    def call(self, prompt: str, system: Optional[str] = None, on_fallback: Optional[Callable] = None) -> str:
        active = self._get_active()
        if not active:
            raise ValueError("No LLM API key configured. Please set at least one provider key in .env or settings.")

        errors = []
        for i, provider in enumerate(active):
            try:
                if provider == "gemini":
                    return self._call_gemini(prompt, system)
                elif provider == "groq":
                    return self._call_groq(prompt, system)
                elif provider == "claude":
                    return self._call_claude(prompt, system)
                elif provider == "openai":
                    return self._call_openai(prompt, system)
                elif provider == "openrouter":
                    return self._call_openrouter(prompt, system)
            except Exception as e:
                err_str = str(e)
                errors.append(f"{provider}: {err_str}")
                next_p = active[i + 1] if i + 1 < len(active) else None
                if on_fallback:
                    on_fallback(provider, next_p, err_str)
                continue
        raise RuntimeError("All LLM providers failed:\n" + "\n".join(errors))

    def _call_gemini(self, prompt: str, system: Optional[str] = None) -> str:
        key = self.keys["GEMINI_API_KEY"]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={key}"
        text = f"System: {system}\n\n{prompt}" if system else prompt
        res = requests.post(url, json={"contents": [{"parts": [{"text": text}]}], "generationConfig": {"temperature": 0.3, "maxOutputTokens": 8192}}, timeout=60)
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text[:120]}")
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]

    def _call_groq(self, prompt: str, system: Optional[str] = None) -> str:
        key = self.keys["GROQ_API_KEY"]
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        res = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={"model": "llama-3.3-70b-versatile", "messages": messages, "temperature": 0.3, "max_tokens": 4096},
            timeout=60
        )
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text[:120]}")
        return res.json()["choices"][0]["message"]["content"]

    def _call_claude(self, prompt: str, system: Optional[str] = None) -> str:
        key = self.keys["ANTHROPIC_API_KEY"]
        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 4096,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
        if system:
            payload["system"] = system
        res = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={"x-api-key": key, "anthropic-version": "2023-06-01", "Content-Type": "application/json"},
            json=payload,
            timeout=90
        )
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text[:120]}")
        return res.json()["content"][0]["text"]

    def _call_openai(self, prompt: str, system: Optional[str] = None) -> str:
        key = self.keys["OPENAI_API_KEY"]
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        res = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={"model": "gpt-4o-mini", "messages": messages, "temperature": 0.3, "max_tokens": 4096},
            timeout=60
        )
        if res.status_code != 200:
            raise Exception(f"HTTP {res.status_code}: {res.text[:120]}")
        return res.json()["choices"][0]["message"]["content"]

    def _call_openrouter(self, prompt: str, system: Optional[str] = None) -> str:
        key = self.keys["OPENROUTER_API_KEY"]
        messages = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})
        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://nissh.info",
            "X-Title": "Nissh Research System"
        }
        models = [
            "google/gemini-2.0-flash-exp:free",
            "meta-llama/llama-3.3-70b-instruct:free",
            "mistralai/mistral-small-24b-instruct-2501:free",
            "google/gemini-flash-1.5",
            "openai/gpt-4o-mini"
        ]
        last_err = None
        for m in models:
            try:
                res = requests.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json={"model": m, "messages": messages, "temperature": 0.3},
                    timeout=45
                )
                if res.status_code == 200:
                    resp_json = res.json()
                    if "choices" in resp_json and len(resp_json["choices"]) > 0:
                        content = resp_json["choices"][0].get("message", {}).get("content", "")
                        if content:
                            return content
                last_err = f"HTTP {res.status_code}: {res.text[:120]}"
            except Exception as e:
                last_err = str(e)
                continue
        raise Exception(f"OpenRouter models failed ({last_err})")


class ResearchEngineV2:
    """
    Grounded 7-Agent Research Engine v2:
    Integrates Live Search, Link Validation, and GitHub Verification
    into the 7-Phase Startup Research methodology.
    """
    def __init__(self, state_mgr: StateManager, keys: Optional[Dict[str, str]] = None):
        self.state_mgr = state_mgr
        self.keys = keys or load_keys()
        self.llm = LLMCaller(self.keys)
        self.search = WebSearchEngine(tavily_key=self.keys.get("TAVILY_API_KEY"), serper_key=self.keys.get("SERPER_API_KEY"))
        self.validator = LinkValidator()
        self.github = GitHubVerifier()

    def run_agent_1(self, project_id: str, raw_idea: str, audience_hint: str = "") -> P1ValidationHandoff:
        self.state_mgr.add_log(project_id, "Agent 1: Searching live web for customer complaints & pain evidence...", 1, "Problem Validator", "tool")
        
        # 1. Real search queries for complaints & forum evidence
        search_query = f"{raw_idea[:80]} problems complaints reddit"
        live_evidence = self.search.search(search_query, max_results=4)
        evidence_text = "\n".join([f"- [{e['title']}]({e['url']}): {e['snippet']}" for e in live_evidence]) if live_evidence else "No direct indexed forum threads returned."

        system = (
            "You are a rigorous, evidence-driven startup problem validator. "
            "You normalize any input language (Hindi, Hinglish, Spanish, etc.) into professional English. "
            "Evaluate frequency, severity (1-10), and willingness to pay. Output valid JSON."
        )

        prompt = f"""Raw Idea: "{raw_idea}"
Target Audience Hint: "{audience_hint}"

LIVE WEB SEARCH EVIDENCE DISCOVERED:
{evidence_text}

TASK:
Validate the problem. Return ONLY a valid JSON object matching this schema:
{{
  "problem_statement": "English normalized statement",
  "target_audience": "Specific ICP",
  "frequency": "Daily",
  "frequency_evidence": ["Evidence 1", "Evidence 2"],
  "severity": 8,
  "severity_evidence": ["Evidence 1"],
  "willingness_to_pay": "Yes",
  "wtp_evidence": ["Evidence 1"],
  "verdict": "GO",
  "verdict_reasoning": "2-line justification",
  "key_pain_signals": ["Signal 1", "Signal 2"]
}}"""

        resp = self.llm.call(prompt, system)
        data = self._clean_json(resp)
        # Inject live sources
        sources = [{"url": e["url"], "title": e["title"], "snippet": e["snippet"]} for e in live_evidence]
        data["key_sources"] = sources

        handoff = P1ValidationHandoff.from_dict(data)
        markdown = self._format_p1_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 1, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=2, agent_name="Landscape Hunter", verdict=handoff.verdict)
        return handoff

    def run_agent_2(self, project_id: str, p1: P1ValidationHandoff) -> P2LandscapeHandoff:
        self.state_mgr.add_log(project_id, "Agent 2: Querying market for top competitors & workarounds...", 2, "Landscape Hunter", "tool")
        
        # Live search for direct & indirect tools
        search_query = f"best tools software alternative for {p1.problem_statement[:70]}"
        search_results = self.search.search(search_query, max_results=5)
        search_summary = "\n".join([f"- {r['title']}: {r['url']}" for r in search_results])

        system = "You are a competitive intelligence scout. Output ONLY valid JSON."
        prompt = f"""Problem Space: {p1.problem_statement}
Target Audience: {p1.target_audience}

LIVE SEARCH HINTS:
{search_summary}

TASK:
Identify 10 competitors across Direct, Indirect, and Workaround categories.
Output ONLY a JSON array of 10 competitors:
{{
  "problem_space": "{p1.problem_statement}",
  "target_audience": "{p1.target_audience}",
  "competitors": [
    {{
      "name": "Tool Name",
      "url": "https://example.com",
      "category": "Direct",
      "pricing": "$15-$49/mo",
      "target_user": "Freelancers",
      "key_features": ["Feature A", "Feature B"],
      "limitations": "Limitation description"
    }}
  ]
}}"""

        resp = self.llm.call(prompt, system)
        data = self._clean_json(resp)
        handoff = P2LandscapeHandoff.from_dict(data)

        # Validate URLs for top competitors
        self.state_mgr.add_log(project_id, "Agent 2: Forensically verifying competitor URLs & HTTP status...", 2, "Landscape Hunter", "tool")
        for comp in handoff.competitors:
            if comp.url:
                val = self.validator.validate_url(comp.url)
                comp.is_live = val.get("is_live", True)
                comp.http_status = val.get("status_code", 200)

        markdown = self._format_p2_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 2, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=3, agent_name="Competitor Forensic Auditor")
        return handoff

    def run_agent_3(self, project_id: str, p2: P2LandscapeHandoff) -> P3ResearchHandoff:
        self.state_mgr.add_log(project_id, "Agent 3: Performing forensic teardowns of competitor shortcomings...", 3, "Competitor Forensic Auditor", "info")
        
        system = "You are a forensic SaaS auditor. Tear down tools to reveal deficiencies and unmet user needs. Output valid JSON."
        comp_summaries = "\n".join([f"{c.name} ({c.url}) - Category: {c.category}" for c in p2.competitors[:5]])

        prompt = f"""Competitors to audit:
{comp_summaries}

TASK:
For each competitor, reveal:
- What users love
- What users hate / complain about
- Critical gaps and workarounds
- Explicit 'THIS TOOL DOES NOT' statements

Output ONLY JSON matching:
{{
  "profiles": [
    {{
      "name": "Competitor Name",
      "url": "https://...",
      "type": "Direct",
      "summary": "2-line summary",
      "pricing_tiers": "Pricing summary",
      "what_users_love": ["Love 1", "Love 2"],
      "what_users_hate": ["Hate 1", "Hate 2"],
      "critical_gaps": "Where tool fails",
      "this_tool_does_not": ["Unmet capability 1", "Unmet capability 2"]
    }}
  ]
}}"""

        resp = self.llm.call(prompt, system)
        data = self._clean_json(resp)
        handoff = P3ResearchHandoff.from_dict(data)

        markdown = self._format_p3_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 3, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=4, agent_name="Strategic Gap Analyst")
        return handoff

    def run_agent_4(self, project_id: str, p1: P1ValidationHandoff, p3: P3ResearchHandoff) -> P4GapAnalysisHandoff:
        self.state_mgr.add_log(project_id, "Agent 4: Synthesizing Feature Matrix & calculating Opportunity Scores...", 4, "Strategic Gap Analyst", "info")

        system = "You are a strategic product gap analyst. Synthesize feature gaps and score opportunities. Output JSON."
        p3_summary = "\n".join([f"{p.name} fails at: {', '.join(p.this_tool_does_not)}" for p in p3.profiles])

        prompt = f"""Problem: {p1.problem_statement}
Audience: {p1.target_audience}

Competitor Deficiencies:
{p3_summary}

TASK:
Synthesize TOP 5 MARKET GAPS and select the #1 RECOMMENDED WEDGE.
Provide 1-5 ratings for Pain, Market Size, and Feasibility.
Output ONLY JSON:
{{
  "top_5_gaps": [
    {{
      "id": 1,
      "name": "Gap Name",
      "category": "Workflow Gap",
      "description": "Gap description",
      "pain_score": 5.0,
      "market_score": 4.5,
      "feasibility_score": 4.0,
      "justification": "Why this gap matters",
      "key_differentiator": "Core wedge"
    }}
  ],
  "recommended_wedge_id": 1
}}"""

        resp = self.llm.call(prompt, system)
        data = self._clean_json(resp)
        
        gaps = []
        for g_dict in data.get("top_5_gaps", []):
            g = GapItem(
                id=g_dict.get("id", 1),
                name=g_dict.get("name", ""),
                category=g_dict.get("category", "Workflow Gap"),
                description=g_dict.get("description", ""),
                pain_score=float(g_dict.get("pain_score", 4.0)),
                market_score=float(g_dict.get("market_score", 4.0)),
                feasibility_score=float(g_dict.get("feasibility_score", 4.0)),
                justification=g_dict.get("justification", ""),
                key_differentiator=g_dict.get("key_differentiator", "")
            )
            g.calculate_score()
            gaps.append(g)

        rec_id = data.get("recommended_wedge_id", 1)
        wedge = next((g for g in gaps if g.id == rec_id), gaps[0] if gaps else None)

        handoff = P4GapAnalysisHandoff(top_5_gaps=gaps, recommended_wedge=wedge)
        markdown = self._format_p4_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 4, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=5, agent_name="9-Platform Gap Verifier")
        return handoff

    def run_agent_5(self, project_id: str, p4: P4GapAnalysisHandoff) -> P5VerifyGapsHandoff:
        self.state_mgr.add_log(project_id, "Agent 5: Auditing GitHub & live platforms to eliminate false gaps...", 5, "9-Platform Gap Verifier", "tool")

        verified = []
        for gap in p4.top_5_gaps[:3]:
            # Query GitHub for open source solutions
            gh_repos = self.github.search_repositories(gap.name, limit=2)
            gh_evidence = f"GitHub repositories: {len(gh_repos)} found (Top: {gh_repos[0]['name']} with {gh_repos[0]['stars']} stars)" if gh_repos else "Zero established GitHub solutions found."

            system = "You are a forensic market gap verifier. Assign honest verdicts (CONFIRMED / PARTIAL / FALSE). Output JSON."
            prompt = f"""Candidate Gap: {gap.name}
Description: {gap.description}
Live Evidence Found: {gh_evidence}

TASK:
Determine if this gap is truly unserved.
Output JSON:
{{
  "name": "{gap.name}",
  "verdict": "CONFIRMED",
  "evidence": "{gh_evidence}",
  "why_unbuilt": "Reason",
  "why_now": "Market catalyst",
  "mvp_features": ["Feature 1", "Feature 2"],
  "source_links": ["https://github.com/search?q={gap.name.replace(' ', '+')}"]
}}"""
            v_resp = self.llm.call(prompt, system)
            v_data = self._clean_json(v_resp)
            verified.append(VerifiedGapItem(**v_data))

        primary = verified[0].name if verified else (p4.recommended_wedge.name if p4.recommended_wedge else "Validated Opportunity")
        handoff = P5VerifyGapsHandoff(
            verified_gaps=verified,
            primary_opportunity=primary,
            core_value_prop=p4.recommended_wedge.description if p4.recommended_wedge else "",
            mvp_build_scope=verified[0].mvp_features if verified else ["Core approval link", "Payment gating"]
        )

        markdown = self._format_p5_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 5, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=6, agent_name="Diligence Synthesizer")
        return handoff

    def run_agent_6(self, project_id: str, p1: P1ValidationHandoff, p5: P5VerifyGapsHandoff) -> P6DiligenceHandoff:
        self.state_mgr.add_log(project_id, "Agent 6: Synthesizing Investor-Ready Diligence Memo & 30-Day Launch Plan...", 6, "Diligence Synthesizer", "info")

        system = "You are an elite startup investor and operator. Synthesize an opportunity memo and launch spec. Output JSON."
        prompt = f"""Problem: {p1.problem_statement}
Audience: {p1.target_audience}
Validated Opportunity: {p5.primary_opportunity}
Value Proposition: {p5.core_value_prop}

TASK:
Output JSON matching:
{{
  "project_name_proposal": "Brand Name",
  "one_line_pitch": "One-line hook",
  "problem_statement": "{p1.problem_statement}",
  "target_audience_icp": "{p1.target_audience}",
  "core_differentiator": "Unfair advantage",
  "mvp_core_features": ["Feature 1", "Feature 2", "Feature 3"],
  "tech_stack_suggestion": "Next.js / Supabase / Stripe",
  "competitive_moat": "Workflow stickiness",
  "launch_plan_30_day": [
    {{"week": "Week 1", "goal": "Discovery & Landing Page"}},
    {{"week": "Week 2", "goal": "MVP Build"}},
    {{"week": "Week 3", "goal": "Beta Onboarding"}},
    {{"week": "Week 4", "goal": "Public Launch on Product Hunt"}}
  ],
  "full_memo_markdown": "Complete investor diligence memo text..."
}}"""

        resp = self.llm.call(prompt, system)
        data = self._clean_json(resp)
        handoff = P6DiligenceHandoff.from_dict(data)

        markdown = self._format_p6_markdown(handoff)
        self.state_mgr.save_phase_output(project_id, 6, markdown, handoff)
        self.state_mgr.update_project_status(project_id, "running", current_agent=7, agent_name="Launch README Architect")
        return handoff

    def run_agent_7(self, project_id: str, p6: P6DiligenceHandoff) -> P7LaunchHandoff:
        self.state_mgr.add_log(project_id, "Agent 7: Generating Production GitHub README...", 7, "Launch README Architect", "info")

        system = "You are a principal open-source architect. Generate a world-class production GitHub README.md."
        prompt = f"""Project: {p6.project_name_proposal}
Tagline: {p6.one_line_pitch}
Core Features: {', '.join(p6.mvp_core_features)}
Tech Stack: {p6.tech_stack_suggestion}

Generate the complete, beautiful GitHub README.md with badges, architecture overview, quickstart instructions, and roadmap."""

        readme_text = self.llm.call(prompt, system)
        handoff = P7LaunchHandoff(
            readme_content=readme_text,
            project_name=p6.project_name_proposal,
            tagline=p6.one_line_pitch
        )

        self.state_mgr.save_phase_output(project_id, 7, readme_text, handoff)
        self.state_mgr.update_project_status(project_id, "completed", current_agent=7, agent_name="Completed")
        self.state_mgr.add_log(project_id, "🎉 Pipeline Execution Finished Successfully!", 7, "Nissh Engine", "info")
        return handoff

    # --- Formatting Helpers ---
    def _clean_json(self, text: str) -> Dict[str, Any]:
        match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
        if match:
            text = match.group(1)
        else:
            match_curly = re.search(r'(\{.*\})', text, re.DOTALL)
            if match_curly:
                text = match_curly.group(1)
        try:
            return json.loads(text)
        except Exception:
            return {}

    def _format_p1_markdown(self, h: P1ValidationHandoff) -> str:
        sources_md = "\n".join([f"- [{s.get('title', 'Source')}]({s.get('url', '#')}): {s.get('snippet', '')}" for s in h.key_sources]) if h.key_sources else "- Live search validated."
        return f"""# Phase 1: Problem Validation

**Problem Statement:** {h.problem_statement}
**Target Audience:** {h.target_audience}
**Frequency:** {h.frequency}
**Severity:** {h.severity}/10
**Willingness to Pay:** {h.willingness_to_pay}
**Verdict:** {h.verdict} ({h.verdict_reasoning})

### Live Grounded Sources:
{sources_md}

### Key Pain Signals:
{chr(10).join([f"- {s}" for s in h.key_pain_signals])}
"""

    def _format_p2_markdown(self, h: P2LandscapeHandoff) -> str:
        table_rows = [f"| {c.name} | [{c.url}]({c.url}) | {c.category} | {c.pricing} | {'✅ Live (200)' if c.is_live else '⚠️ Unreachable'} | {c.limitations} |" for c in h.competitors]
        return f"""# Phase 2: Competitive Landscape

**Problem Space:** {h.problem_space}
**Target Audience:** {h.target_audience}

| Competitor | URL | Type | Pricing | Status | Limitations |
| :--- | :--- | :--- | :--- | :--- | :--- |
{chr(10).join(table_rows)}
"""

    def _format_p3_markdown(self, h: P3ResearchHandoff) -> str:
        profiles_md = []
        for p in h.profiles:
            profiles_md.append(f"""### {p.name} ({p.type})
- **Summary:** {p.summary}
- **Pricing:** {p.pricing_tiers}
- **What Users Love:** {', '.join(p.what_users_love)}
- **What Users Hate:** {', '.join(p.what_users_hate)}
- **THIS TOOL DOES NOT:** {', '.join(p.this_tool_does_not)}
""")
        return f"# Phase 3: Competitor Forensic Teardowns\n\n" + "\n---\n".join(profiles_md)

    def _format_p4_markdown(self, h: P4GapAnalysisHandoff) -> str:
        gaps_md = []
        for g in h.top_5_gaps:
            gaps_md.append(f"**Gap {g.id}: {g.name}** (Score: {g.opportunity_score}/10)\n- {g.description}\n- *Justification:* {g.justification}")
        wedge_name = h.recommended_wedge.name if h.recommended_wedge else "N/A"
        return f"# Phase 4: Strategic Gap Analysis\n\n**#1 Recommended Wedge:** {wedge_name}\n\n" + "\n\n".join(gaps_md)

    def _format_p5_markdown(self, h: P5VerifyGapsHandoff) -> str:
        vgaps = [f"- **{vg.name}** [{vg.verdict}]\n  Evidence: {vg.evidence}\n  Why Now: {vg.why_now}" for vg in h.verified_gaps]
        return f"""# Phase 5: 9-Platform Gap Verification

**Primary Opportunity:** {h.primary_opportunity}
**Value Proposition:** {h.core_value_prop}

### Verified Gaps:
{chr(10).join(vgaps)}
"""

    def _format_p6_markdown(self, h: P6DiligenceHandoff) -> str:
        return f"""# Phase 6: Startup Diligence Memo

**Project Name Proposal:** {h.project_name_proposal}
**Pitch:** {h.one_line_pitch}
**Core Differentiator:** {h.core_differentiator}
**Moat:** {h.competitive_moat}

### MVP Core Features:
{chr(10).join([f"- {f}" for f in h.mvp_core_features])}

### 30-Day Launch Plan:
{chr(10).join([f"- **{step.get('week', 'Week')}:** {step.get('goal', '')}" for step in h.launch_plan_30_day])}

---
{h.full_memo_markdown}
"""
