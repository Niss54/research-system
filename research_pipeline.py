#!/usr/bin/env python3
"""
Research System CLI Pipeline Runner
===================================
Connects and orchestrates Phases 1 through 7 of the Startup Research Playbook.
Automatically passes data between phases:
  P1 Validate -> P2 Top 10 -> P3 Research x10 -> P4 Gap Analysis -> P5 Verify Gaps -> P6 Final Report -> P7 Launch README
"""

import os
import sys
import re
import json
import argparse
import webbrowser
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Ensure UTF-8 output on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

REPO_ROOT = Path(__file__).resolve().parent
DEFAULT_WORKSPACE = REPO_ROOT / "workspace"

DEMO_DATA = {
    "problem": "Freelance web designers and developers in India and Southeast Asia struggle to manage scope creep and get paid for extra revision rounds. Clients repeatedly ask for 'one minor tweak' without approving change orders, causing freelancers to lose $500–$2,000/month in unbilled labor.",
    "audience": "Freelance web designers, UI/UX developers, and boutique agency owners handling client work with frequent revision cycles.",
    "p1_handoff": """<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: Freelancers lose significant revenue and unbilled hours managing client revision loops without automated scope enforcement or change order micro-payments.
TARGET_AUDIENCE: Freelance web designers, frontend developers, and boutique creative agencies.
FREQUENCY: Daily — revision scope friction occurs on nearly 80% of active client projects.
FREQUENCY_EVIDENCE: 45+ Reddit threads in r/freelance and r/webdev highlighting unpaid revisions as the #1 burnout factor.
SEVERITY: 8/10 — direct financial leakage of $500-$2,000/mo and frequent client relationship deterioration.
SEVERITY_EVIDENCE: Over 120 G2/Capterra reviews of generic invoicing tools complain about lack of deliverable and revision locking.
WILLINGNESS_TO_PAY: Yes — freelancers routinely pay $15-$45/mo for tools like HoneyBook, Bonsai, and Harvest that only partially address invoicing.
WTP_EVIDENCE: Active market adoption of contract templates, paid Notion project portals, and client management SaaS.
KEY_SOURCES:
- https://reddit.com/r/freelance/comments/scope_creep_unpaid_revisions
- https://www.g2.com/categories/freelance-management-systems
- https://producthunt.com/search?q=client+portal+invoicing
VERDICT: GO ✅
VERDICT_REASONING: High daily frequency coupled with direct financial pain and proven willingness to pay for client management solutions.
KEY_PAIN_SIGNALS:
- Awkwardness of asking clients for extra money mid-project
- Contracts state '3 revisions included' but there is no technical enforcement
- Clients withhold final milestone payment until infinite revisions are completed
SEARCH_QUERIES_USED:
- reddit freelance client endless revisions scope creep
- freelance invoice app revision tracking change order
<!-- END P1_HANDOFF -->""",
    "p2_handoff": """<!-- BEGIN P2_HANDOFF -->
PROBLEM_SPACE: Freelance Deliverable Scope Enforcement & Revision Paywall
TARGET_AUDIENCE: Freelancers and boutique creative agencies

TOP_10_TABLE:
| # | Name | URL | Type | Pricing | Target User | 3 Key Features | Primary Limitation / Workaround |
|---|------|-----|------|---------|-------------|----------------|----------------------------------|
| 1 | Bonsai (HelloBonsai) | https://hellobonsai.com | Direct | $25–$79/mo | Freelancers | Contracts, Invoicing, Proposals | Invoicing is decoupled from actual file revisions; no automatic scope lock |
| 2 | HoneyBook | https://honeybook.com | Direct | $19–$79/mo | Creative SMBs | Client flow, Invoices, Contracts | Heavy enterprise feel; US/Canada banking focus; lacks milestone revision gating |
| 3 | Contra | https://contra.com | Indirect | Free / 5% cut | Modern Freelancers | Portfolio, Contracts, Milestones | Marketplace walled garden; clients must register on Contra |
| 4 | Indy | https://weareindy.com | Direct | $12/mo | Solopreneurs | Simple proposals, tracker, bills | Basic static forms; zero automated deliverable approval workflows |
| 5 | MarkUp.io | https://markup.io | Indirect | Free / $15/mo | Designers & Agencies | Live visual feedback, comments | Focuses purely on visual feedback; zero billing or contract scope integration |
| 6 | Pastell | https://usepastell.com | Indirect | $19–$49/mo | Web Agencies | Website client feedback tool | No invoicing, contracts, or paid revision upsells |
| 7 | Wethos | https://wethos.co | Niche | Free / $15/mo | Creative Studios | Scope of work templates, pricing | Scoping templates exist only in static documents; no live runtime enforcement |
| 8 | Milanote | https://milanote.com | Indirect | $10/mo | Creatives | Moodboards, Client review boards | Visual canvas only; no client payment or revision counter |
| 9 | Notion Client Portal | https://notion.so | Workaround | $10–$25 (one-time) | DIY Freelancers | Deliverable tables, revision checkboxes | Requires manual freelancer updates; clients ignore checkbox limits |
| 10 | Google Sheets + Stripe Invoice | https://stripe.com | Workaround | 2.9% fee | Scrappy Builders | Manual revision log, ad-hoc invoice links | Awkward social friction sending manual extra invoices for small revisions |

COMPETITORS_FOR_P3:
1. Name: Bonsai | URL: https://hellobonsai.com | Type: Direct | Focus: All-in-one freelance management
2. Name: HoneyBook | URL: https://honeybook.com | Type: Direct | Focus: Client communication and billing
3. Name: Contra | URL: https://contra.com | Type: Indirect | Focus: Freelance marketplace and contract milestones
4. Name: Indy | URL: https://weareindy.com | Type: Direct | Focus: Budget-friendly freelance administration
5. Name: MarkUp.io | URL: https://markup.io | Type: Indirect | Focus: Visual design and website proofing
6. Name: Pastell | URL: https://usepastell.com | Type: Indirect | Focus: Digital agency client approval
7. Name: Wethos | URL: https://wethos.co | Type: Niche | Focus: Scope of work builder with crowdsourced pricing
8. Name: Milanote | URL: https://milanote.com | Type: Indirect | Focus: Creative project collaboration
9. Name: Notion Client Portal | URL: https://notion.so | Type: Workaround | Focus: DIY client deliverable tracker
10. Name: Google Sheets + Stripe Invoice | URL: https://stripe.com | Type: Workaround | Focus: Manual ad-hoc invoice and tracking
<!-- END P2_HANDOFF -->""",
    "p3_profiles": """<!-- BEGIN P3_PROFILE: Bonsai -->
COMPETITOR_NAME: Bonsai
WEBSITE: https://hellobonsai.com
TYPE: Direct
1. PRODUCT PROFILE: All-in-one freelance contract, invoicing, and CRM suite. User creates contract, tracks hours, generates invoice.
2. COMPANY INTEL: Founded 2015, raised ~$1.2M, team ~50, serving over 500,000 freelancers globally.
3. PRICING TIERS: Starter $25/mo, Professional $39/mo, Business $79/mo.
4. WHAT USERS LOVE: Professional looking invoice templates, unified time tracking, and simple contracts.
5. WHAT USERS HATE: Clunky mobile app, steep price increases over recent years, lacks real-time deliverable inspection.
6. CRITICAL GAPS: Contracts specify revision counts in text paragraphs, but the app does NOT count or gate revision requests.
THIS TOOL DOES NOT: automatically count client revision submissions, enforce contract revision limits, or trigger one-click micro-invoices for scope creep.
<!-- END P3_PROFILE: Bonsai -->

<!-- BEGIN P3_PROFILE: MarkUp.io -->
COMPETITOR_NAME: MarkUp.io
WEBSITE: https://markup.io
TYPE: Indirect
1. PRODUCT PROFILE: Visual commenting platform for websites, PDFs, and images. Clients point-and-click to leave change requests.
2. COMPANY INTEL: Owned by Ceros, venture backed, tens of thousands of active users.
3. PRICING TIERS: Free tier, Pro $15/mo.
4. WHAT USERS LOVE: Intuitive pin-point feedback on live staging sites without browser extensions.
5. WHAT USERS HATE: Makes it TOO EASY for clients to leave 100 nitpicky comments without knowing they are out of scope.
6. CRITICAL GAPS: Completely disconnected from contracts or money. Actually exacerbates scope creep by reducing client friction to comment.
THIS TOOL DOES NOT: track revision rounds, connect change requests to contracts, or require client payment approval for extra edits.
<!-- END P3_PROFILE: MarkUp.io -->""",
    "p4_handoff": """<!-- BEGIN P4_HANDOFF -->
PROBLEM_SPACE: Freelance Deliverable Scope Enforcement & Revision Paywall
TARGET_AUDIENCE: Freelance web designers and creative agencies

TOP_5_GAPS:
GAP 1: Automated Revision Gating (Smart Scope Paywall) — A deliverable portal where clients submit revision rounds with a strict counter (e.g. 2 of 2 used); round 3 triggers an automatic change-order invoice before the client can submit further comments.
GAP 2: Proofing-to-Billing Bridge — Direct integration between visual staging feedback (like MarkUp.io) and contract milestones, preventing clients from spamming unlimited minor tweaks.
GAP 3: Zero-Friction Frictionless Client Access — Client portal that requires no client login or password, using magic links and one-click Stripe payments for change orders.
GAP 4: Crowdsourced Scope-of-Work Benchmark — Suggests defensible revision policies and pricing per revision round based on project scope.
GAP 5: Independent Contract Revision Escrow — Milestone payments automatically released once revision round 2 is approved or if client stays silent for 7 business days.

#1_RECOMMENDED_GAP:
NAME: Automated Revision Gating (Smart Scope Paywall)
CATEGORY: Workflow & Pricing Gap
OPPORTUNITY_SCORE: 8.5/10 (High Pain 5/5 x Solid Market 4/5 x High Feasibility 4.5/5)
JUSTIFICATION: Eliminates the single most stressful social interaction for freelancers (asking clients for extra money) by shifting enforcement to software.
KEY_DIFFERENTIATOR: A client approval portal with an automated revision counter that converts excess client requests into instant paid change orders.
<!-- END P4_HANDOFF -->""",
    "p5_handoff": """<!-- BEGIN P5_HANDOFF -->
PROBLEM_SPACE: Freelance Deliverable Scope Enforcement & Revision Paywall
TARGET_AUDIENCE: Freelance web designers and boutique creative agencies

VERIFIED_GAPS:
- GAP 1: Automated Revision Gating (Smart Scope Paywall)
  VERDICT: CONFIRMED ✅
  EVIDENCE: Comprehensive search of Product Hunt, Indie Hackers, GitHub, and YC showed zero dedicated tools that enforce revision round limits with connected Stripe micro-billing. All existing feedback tools encourage unlimited commenting.
  WHY_UNBUILT: Traditional feedback tools focused on enterprise agency collaboration (Ceros/MarkUp.io) where billing is handled separately by account managers.
  WHY_NOW: Massive rise in solo freelance web developers (Webflow, Framer, Shopify) who need an automated bad-cop system for client revisions.
  MINIMAL_MVP_FEATURES:
  * Shareable deliverable link with revision counter (e.g., Round 1 of 2)
  * Point-and-click revision submission form with scope confirmation
  * Automated Stripe change-order paywall when revisions exceed included limit
  * Auto-approval countdown timer (approves deliverable if client silent for 7 days)

- GAP 2: Proofing-to-Billing Bridge
  VERDICT: PARTIAL ⚠️
  EVIDENCE: Some tools like Pastel offer approval buttons, but none integrate direct invoice generation or milestone release.
  WHY_UNBUILT: API fragmentation between project tools and accounting software.
  WHY_NOW: Stripe Elements and Webhook infrastructure allows seamless instant checkout.
  MINIMAL_MVP_FEATURES:
  * Embeddable client sign-off widget

FINAL_VIABLE_OPPORTUNITIES:
1. Automated Revision Gating (Smart Scope Paywall) — Defensible entry wedge for solo designers and boutique agencies.
2. Proofing-to-Billing Bridge — Secondary expansion into visual feedback tools.

RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: Automated Revision Gating (Smart Scope Paywall)
CORE_VALUE_PROP: "The polite bad-cop for your client projects. Never do an unpaid revision round again."
MVP_BUILD_SCOPE: Deliverable approval link + Revision round counter + Stripe change-order paywall + 7-day auto-acceptance timer.
<!-- END P5_HANDOFF -->""",
    "p6_handoff": """<!-- BEGIN P6_HANDOFF -->
PROJECT_NAME_PROPOSAL: ScopeLock
ONE_LINE_PITCH: The automated client revision gatekeeper that stops scope creep and turns extra feedback rounds into paid change orders.
PROBLEM_STATEMENT: Freelance designers lose an average of $1,200/month and 15 hours in unpaid revisions because existing tools don't link client feedback with contractual scope limits.
TARGET_AUDIENCE_ICP: Solo Webflow/Framer/Figma designers and boutique design studios charging $1,500–$10,000 per project.
CORE_DIFFERENTIATOR (THE VERIFIED GAP): Live deliverable approval portal with a hard revision counter that automatically gates submissions and bills extra rounds through Stripe before feedback reaches the freelancer.
MVP_CORE_FEATURES:
- Magic-link client deliverable portal (no client login required)
- Strict revision round counter (e.g. 2 of 2 included)
- Automatic Stripe change-order paywall when revision limit is reached ($150-$500 per extra round)
- 7-day auto-approval protection timer (releases milestone if client ghosts)
TECH_STACK_SUGGESTION: Next.js / TailwindCSS / Supabase / Stripe Elements / Vercel
COMPETITIVE_MOAT: Workflow embedding at the exact moment of client friction + high emotional switching cost once freelancer sets up client contracts.
30_DAY_LAUNCH_PLAN:
- Week 1: Launch interactive landing page & conduct 15 interviews with r/webdev & Twitter designers
- Week 2: Build MVP (Deliverable link, revision counter, Stripe checkout)
- Week 3: Onboard 10 beta freelancers on real live client projects
- Week 4: Public launch on Product Hunt, Twitter #buildinpublic, and Reddit communities
<!-- END P6_HANDOFF -->"""
}

class ResearchPipeline:
    def __init__(self, workspace_path=DEFAULT_WORKSPACE):
        self.workspace = Path(workspace_path)
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.state_file = self.workspace / "pipeline_state.json"
        self.state = self.load_state()

    def load_state(self):
        if self.state_file.exists():
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return {
            "problem": "",
            "audience": "",
            "phases": {
                "1": {"status": "pending", "output_file": "p1_validate_output.md", "handoff": ""},
                "2": {"status": "pending", "output_file": "p2_top10_output.md", "handoff": ""},
                "3": {"status": "pending", "output_file": "p3_research_output.md", "handoff": ""},
                "4": {"status": "pending", "output_file": "p4_gap_analysis_output.md", "handoff": ""},
                "5": {"status": "pending", "output_file": "p5_verify_gaps_output.md", "handoff": ""},
                "6": {"status": "pending", "output_file": "p6_final_report_output.md", "handoff": ""},
                "7": {"status": "pending", "output_file": "p7_launch_readme_output.md", "handoff": ""}
            }
        }

    def save_state(self):
        with open(self.state_file, "w", encoding="utf-8") as f:
            json.dump(self.state, f, indent=2, ensure_ascii=False)

    def extract_handoff(self, text, phase_num):
        pattern = rf"<!-- BEGIN P{phase_num}_HANDOFF -->(.*?)<!-- END P{phase_num}_HANDOFF -->"
        match = re.search(pattern, text, re.DOTALL)
        if match:
            return f"<!-- BEGIN P{phase_num}_HANDOFF -->{match.group(1)}<!-- END P{phase_num}_HANDOFF -->"
        if phase_num == 3:
            profiles = re.findall(r"<!-- BEGIN P3_PROFILE:.*?<!-- END P3_PROFILE:[^>]*-->", text, re.DOTALL)
            if profiles:
                return "\n\n".join(profiles)
        return text

    def init_project(self, problem, audience=""):
        self.state["problem"] = problem
        self.state["audience"] = audience
        self.save_state()
        print(f"✅ Research Project Initialized in {self.workspace}")
        print(f"   Problem: {problem}")
        if audience:
            print(f"   Audience: {audience}")
        print("\nNext step: Run `python research_pipeline.py prompt 1` to generate Phase 1 prompt.")

    def get_prompt(self, phase_num):
        phase_str = str(phase_num)
        p1_file = self.workspace / self.state["phases"]["1"]["output_file"]
        p2_file = self.workspace / self.state["phases"]["2"]["output_file"]
        p3_file = self.workspace / self.state["phases"]["3"]["output_file"]
        p4_file = self.workspace / self.state["phases"]["4"]["output_file"]
        p5_file = self.workspace / self.state["phases"]["5"]["output_file"]
        p6_file = self.workspace / self.state["phases"]["6"]["output_file"]

        p1_h = self.state["phases"]["1"]["handoff"] or (p1_file.read_text(encoding="utf-8") if p1_file.exists() else "")
        p2_h = self.state["phases"]["2"]["handoff"] or (p2_file.read_text(encoding="utf-8") if p2_file.exists() else "")
        p3_h = self.state["phases"]["3"]["handoff"] or (p3_file.read_text(encoding="utf-8") if p3_file.exists() else "")
        p4_h = self.state["phases"]["4"]["handoff"] or (p4_file.read_text(encoding="utf-8") if p4_file.exists() else "")
        p5_h = self.state["phases"]["5"]["handoff"] or (p5_file.read_text(encoding="utf-8") if p5_file.exists() else "")
        p6_h = self.state["phases"]["6"]["handoff"] or (p6_file.read_text(encoding="utf-8") if p6_file.exists() else "")

        problem = self.state.get("problem", "[ENTER YOUR PROBLEM STATEMENT]")
        audience = self.state.get("audience", "[ENTER YOUR TARGET AUDIENCE]")

        if phase_str == "1":
            return f"""Problem statement: {problem}
Target audience: {audience}

Act as an evidence-driven startup problem validator. Validate if this is a REAL problem worth solving.

Use web search to find hard evidence:
□ Search "reddit [problem keyword] struggling OR frustrated OR annoying"
□ Search "[problem keyword] complaints forum OR community"
□ Search "how to solve [problem keyword]" — see demand for solutions
□ Search "[problem keyword] pain points survey OR report OR statistics"
□ Check App Store / Play Store reviews mentioning this problem

Evaluate on exactly 3 dimensions:
1. FREQUENCY — Daily / Weekly / Monthly / Rarely
2. SEVERITY — 1–10 (1-3 minor, 4-6 friction, 7-10 high financial/time cost)
3. WILLINGNESS TO PAY — Do people already pay for partial solutions?

SCORING:
• Frequency Daily/Weekly + Severity 7+ + WTP Yes → GO ✅
• 2 out of 3 strong → MAYBE ⚠️
• 1 out of 3 strong → NO-GO ❌

Output format (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: {problem}
TARGET_AUDIENCE: {audience}
FREQUENCY: [Daily/Weekly/Monthly/Rarely]
FREQUENCY_EVIDENCE: [Summary]
SEVERITY: [N/10]
SEVERITY_EVIDENCE: [Summary]
WILLINGNESS_TO_PAY: [Yes/No]
WTP_EVIDENCE: [Summary]
KEY_SOURCES:
- [Source URL 1]
- [Source URL 2]
VERDICT: [GO ✅ / MAYBE ⚠️ / NO-GO ❌]
VERDICT_REASONING: [2-line summary]
KEY_PAIN_SIGNALS:
- [Signal 1]
- [Signal 2]
<!-- END P1_HANDOFF -->"""

        elif phase_str == "2":
            if not p1_h:
                print("⚠️ Warning: Phase 1 output not found. Run Phase 1 first or supply handoff block.")
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 1:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p1_h if p1_h else f"Problem: {problem}\\nAudience: {audience}"}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: COMPETITIVE LANDSCAPE DISCOVERY (TOP 10 SOLUTIONS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a market intelligence researcher. Based on the validated problem statement, target audience, and pain signals from Phase 1 above, identify the TOP 10 solutions that exist in the market.

Include a balanced mix:
- Direct competitors
- Indirect competitors
- Manual workarounds (Excel sheets, Notion templates, hiring agencies, DIY)

OUTPUT FORMAT (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
<!-- BEGIN P2_HANDOFF -->
PROBLEM_SPACE: {problem}
TARGET_AUDIENCE: {audience}

TOP_10_TABLE:
| # | Name | URL | Type | Pricing | Target User | 3 Key Features | Primary Limitation / Workaround |
|---|------|-----|------|---------|-------------|----------------|----------------------------------|

COMPETITORS_FOR_P3:
1. Name: [Name 1] | URL: [URL 1] | Type: [Type] | Focus: [Focus]
...
10. Name: [Name 10] | URL: [URL 10] | Type: [Type] | Focus: [Focus]
<!-- END P2_HANDOFF -->"""

        elif phase_str == "3":
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 2:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p2_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: BATCH COMPETITIVE PROFILE & GAP EXTRACTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For EACH competitor listed in the P2 handoff, conduct an independent research investigation.
Search web reviews, pricing, Reddit discussions, and user complaints.

For EACH competitor, output a separate profile block formatted exactly as:
<!-- BEGIN P3_PROFILE: [COMPETITOR NAME] -->
COMPETITOR_NAME: [NAME]
WEBSITE: [URL]
TYPE: [Direct / Indirect / Workaround]
SUMMARY & POSITIONING: [2-3 sentences]
PRICING TIERS: [Free / Paid tiers + limitations]
WHAT USERS LOVE: [Top 2-3 praises]
WHAT USERS HATE: [Top 3-5 complaints]
CRITICAL GAPS & WORKAROUNDS: [What it fails to do + what manual hacks users create]
THIS TOOL DOES NOT: [Comma-separated list of all unmet needs and gaps]
<!-- END P3_PROFILE: [COMPETITOR NAME] -->"""

        elif phase_str == "4":
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 1: VALIDATED PROBLEM & AUDIENCE (FROM P1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p1_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 2: ALL 10 COMPETITOR PROFILES (FROM P3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p3_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: STRATEGIC GAP ANALYSIS & OPPORTUNITY SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a chief product strategist and venture scout. Conduct an exhaustive gap analysis across all 10 competing solutions.

1. Build complete Feature Matrix table (rows = features, columns = competitors, ✓ / ~ / ✗)
2. Categorize gaps: Feature Gaps, Quality Gaps, Audience Gaps, Pricing Gaps, Workflow Gaps
3. Score each gap: (User Pain × Market Size × Build Feasibility) ÷ 2
4. Select top 5 opportunities and #1 recommended gap

OUTPUT FORMAT (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
<!-- BEGIN P4_HANDOFF -->
PROBLEM_SPACE: {problem}
TARGET_AUDIENCE: {audience}

TOP_5_GAPS:
GAP 1: [Name] — [1-2 sentence description of missing capability and user impact]
GAP 2: [Name] — [description]
GAP 3: [Name] — [description]
GAP 4: [Name] — [description]
GAP 5: [Name] — [description]

#1_RECOMMENDED_GAP:
NAME: [Name of #1 Gap]
CATEGORY: [Category]
OPPORTUNITY_SCORE: [Score]
JUSTIFICATION: [Why this is highest leverage]
KEY_DIFFERENTIATOR: [The single unfair advantage / core mechanism]
<!-- END P4_HANDOFF -->"""

        elif phase_str == "5":
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 4:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p4_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: EXHAUSTIVE GAP VERIFICATION (9-PLATFORM AUDIT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Verify each of the 5 market gaps across Google, Product Hunt, Indie Hackers, GitHub, YC, BetaList, TechCrunch, and LinkedIn.

Verdicts:
✅ CONFIRMED GAP — Nothing viable found after exhaustive search. Truly open.
⚠️ PARTIAL GAP — 1–2 weak/early tools exist, but major void remains.
❌ FALSE GAP — Solid solution already exists. Disqualify.

OUTPUT FORMAT (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
<!-- BEGIN P5_HANDOFF -->
PROBLEM_SPACE: {problem}
TARGET_AUDIENCE: {audience}

VERIFIED_GAPS:
- GAP 1: [Name] | VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Catalyst]
  MINIMAL_MVP_FEATURES: [Bullet list]
...
FINAL_VIABLE_OPPORTUNITIES:
1. [Name] — [One-line summary]
RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: [Name]
CORE_VALUE_PROP: [One-line pitch]
MVP_BUILD_SCOPE: [3 bullet points]
<!-- END P5_HANDOFF -->"""

        elif phase_str == "6":
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH INPUTS (ATTACHED FROM PHASES 1–5):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━ P1 — VALIDATION RESULTS ━━━━━━━━━━━━━━━━━━━
{p1_h}

━━━ P2 — TOP 10 SOLUTIONS ━━━━━━━━━━━━━━━━━━━━━
{p2_h}

━━━ P3 — COMPETITIVE PROFILES ━━━━━━━━━━━━━━━━━
{p3_h}

━━━ P4 — GAP ANALYSIS ━━━━━━━━━━━━━━━━━━━━━━━━━
{p4_h}

━━━ P5 — VERIFIED GAPS ━━━━━━━━━━━━━━━━━━━━━━━━
{p5_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: EVIDENCE-VERIFIED STARTUP OPPORTUNITY REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Synthesize and independently verify the research across P1–P5. Produce a professional diligence memo with Claim Audit, Executive Summary, Competitive Landscape, Defensible Opportunity, and 30-Day Plan.

At the very end of your response, output:
<!-- BEGIN P6_HANDOFF -->
PROJECT_NAME_PROPOSAL: [Name]
ONE_LINE_PITCH: [Value proposition]
PROBLEM_STATEMENT: [Verified problem statement]
TARGET_AUDIENCE_ICP: [Customer persona]
CORE_DIFFERENTIATOR (THE VERIFIED GAP): [Validated gap]
MVP_CORE_FEATURES:
- [Feature 1]
- [Feature 2]
- [Feature 3]
TECH_STACK_SUGGESTION: [Stack]
COMPETITIVE_MOAT: [Moat]
30_DAY_LAUNCH_PLAN:
- Week 1: [Landing page & 15 discovery calls]
- Week 2: [MVP core build]
- Week 3: [Alpha onboarding]
- Week 4: [Public launch]
<!-- END P6_HANDOFF -->"""

        elif phase_str == "7":
            return f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 6:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{p6_h}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: GENERATE THE ULTIMATE GITHUB README & LAUNCH KIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Using the verified startup opportunity and MVP specifications from Phase 6 above, write a single, complete, PERFECT `README.md` for this new project.

Produce RAW, READY-TO-PUBLISH MARKDOWN ONLY:
1. Hero header with ASCII banner, badges, tagline
2. Problem & The Gap (citing research evidence)
3. Key Features & Workflow
4. Competitive Comparison Matrix (Us vs Competitor 1 vs Competitor 2 vs Workarounds)
5. Architecture & Tech Stack (Mermaid diagram)
6. Quickstart / Setup (30-second commands)
7. 30-Day Roadmap Checklist
8. License & Contribution Guidelines"""

        else:
            return f"Invalid phase number: {phase_num}. Use 1 through 7."

    def save_output(self, phase_num, content):
        phase_str = str(phase_num)
        if phase_str not in self.state["phases"]:
            print(f"❌ Error: Invalid phase {phase_num}")
            return

        out_file = self.workspace / self.state["phases"][phase_str]["output_file"]
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(content)

        handoff = self.extract_handoff(content, int(phase_num))
        self.state["phases"][phase_str]["status"] = "completed"
        self.state["phases"][phase_str]["handoff"] = handoff
        self.save_state()

        print(f"✅ Phase {phase_num} Output saved to: {out_file}")
        if handoff:
            print(f"📦 Extracted Handoff Block ({len(handoff)} chars) ready for Phase {int(phase_num)+1}!")
        print(f"➡️ Ready to run Phase {int(phase_num)+1}: `python research_pipeline.py prompt {int(phase_num)+1}`")

    def load_demo(self):
        self.state["problem"] = DEMO_DATA["problem"]
        self.state["audience"] = DEMO_DATA["audience"]

        phases_map = {
            "1": DEMO_DATA["p1_handoff"],
            "2": DEMO_DATA["p2_handoff"],
            "3": DEMO_DATA["p3_profiles"],
            "4": DEMO_DATA["p4_handoff"],
            "5": DEMO_DATA["p5_handoff"],
            "6": DEMO_DATA["p6_handoff"],
            "7": "# ScopeLock — Smart Revision Paywall for Freelancers\n\n> The automated client revision gatekeeper that stops scope creep.\n"
        }

        for p_num, content in phases_map.items():
            out_file = self.workspace / self.state["phases"][p_num]["output_file"]
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(content)
            self.state["phases"][p_num]["status"] = "completed"
            self.state["phases"][p_num]["handoff"] = content

        self.save_state()
        print("⚡ Sample Research Project Loaded Successfully into workspace!")
        self.compile_dossier()

    def print_status(self):
        print("\n" + "="*50)
        print("📊 STARTUP RESEARCH SYSTEM — PIPELINE STATUS")
        print("="*50)
        print(f"Workspace: {self.workspace}")
        print(f"Problem:   {self.state.get('problem') or 'Not set'}")
        print(f"Audience:  {self.state.get('audience') or 'Not set'}")
        print("-" * 50)
        phase_names = {
            "1": "Validate",
            "2": "Top 10 Solutions",
            "3": "Research x10",
            "4": "Gap Analysis",
            "5": "Verify Gaps",
            "6": "Final Report",
            "7": "Launch README"
        }
        for p in range(1, 8):
            p_str = str(p)
            status = self.state["phases"][p_str]["status"]
            has_h = bool(self.state["phases"][p_str]["handoff"])
            icon = "✅" if status == "completed" else "⏳"
            h_icon = "📦 Linked" if has_h else "❌ Unlinked"
            print(f"Phase {p} [{phase_names[p_str]:<18}]: {icon} {status.upper():<10} | {h_icon}")
        print("="*50 + "\n")

    def compile_dossier(self):
        dossier_file = self.workspace / "COMPLETE_RESEARCH_DOSSIER.md"
        sections = [
            "# 🚀 COMPLETE STARTUP RESEARCH DOSSIER",
            f"**Problem:** {self.state.get('problem', 'N/A')}",
            f"**Target Audience:** {self.state.get('audience', 'N/A')}",
            "\n---\n"
        ]

        phase_titles = {
            "1": "Phase 1: Problem Validation",
            "2": "Phase 2: Top 10 Existing Solutions",
            "3": "Phase 3: Deep Competitor Profiles",
            "4": "Phase 4: Strategic Gap Analysis & Matrix",
            "5": "Phase 5: Exhaustive Gap Verification",
            "6": "Phase 6: Final Evidence-Verified Diligence Report",
            "7": "Phase 7: Product Launch README & Pitch"
        }

        for p in range(1, 8):
            p_str = str(p)
            out_file = self.workspace / self.state["phases"][p_str]["output_file"]
            sections.append(f"## {phase_titles[p_str]}\n")
            if out_file.exists():
                content = out_file.read_text(encoding="utf-8")
                sections.append(content)
            else:
                sections.append("*Not completed yet.*")
            sections.append("\n\n---\n")

        with open(dossier_file, "w", encoding="utf-8") as f:
            f.write("\n".join(sections))

        print(f"🏆 Complete Research Dossier Compiled: {dossier_file}")
        return dossier_file

    def serve_ui(self, port=8000):
        os.chdir(REPO_ROOT)
        print(f"🌐 Launching Interactive Research Playbook UI on http://localhost:{port}/startup_research_playbook.html")
        webbrowser.open(f"http://localhost:{port}/startup_research_playbook.html")
        httpd = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server.")

def main():
    parser = argparse.ArgumentParser(description="Startup Research System Pipeline Runner")
    subparsers = parser.add_subparsers(dest="command")

    # init command
    init_parser = subparsers.add_parser("init", help="Initialize a new research project")
    init_parser.add_argument("problem", help="Problem statement in 2-3 lines")
    init_parser.add_argument("--audience", default="", help="Target audience / ICP")

    # prompt command
    prompt_parser = subparsers.add_parser("prompt", help="Generate prompt for a phase with attached previous outputs")
    prompt_parser.add_argument("phase", type=int, choices=range(1, 8), help="Phase number (1 to 7)")

    # save command
    save_parser = subparsers.add_parser("save", help="Save AI response for a phase")
    save_parser.add_argument("phase", type=int, choices=range(1, 8), help="Phase number (1 to 7)")
    save_parser.add_argument("--file", help="Path to file containing response")
    save_parser.add_argument("--text", help="Direct text of response")

    # status command
    subparsers.add_parser("status", help="View pipeline completion and data link status")

    # compile command
    subparsers.add_parser("compile", help="Compile all phase outputs into a single research dossier")

    # demo command
    subparsers.add_parser("demo", help="Load full sample research project (ScopeLock)")

    # serve command
    serve_parser = subparsers.add_parser("serve", help="Launch interactive browser web UI")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port to serve on")

    args = parser.parse_args()
    pipeline = ResearchPipeline()

    if args.command == "init":
        pipeline.init_project(args.problem, args.audience)
    elif args.command == "prompt":
        print(pipeline.get_prompt(args.phase))
    elif args.command == "save":
        content = ""
        if args.file:
            content = Path(args.file).read_text(encoding="utf-8")
        elif args.text:
            content = args.text
        else:
            print("Paste the AI response below (Enter EOF / Ctrl+D or Ctrl+Z on empty line to finish):")
            content = sys.stdin.read()
        pipeline.save_output(args.phase, content)
    elif args.command == "status":
        pipeline.print_status()
    elif args.command == "compile":
        pipeline.compile_dossier()
    elif args.command == "demo":
        pipeline.load_demo()
    elif args.command == "serve":
        pipeline.serve_ui(args.port)
    else:
        pipeline.print_status()
        print("Run `python research_pipeline.py --help` for available commands.")

if __name__ == "__main__":
    main()
