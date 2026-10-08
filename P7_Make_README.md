# P7 — Launch README & Positioning Kit
> **Phase 7 of 7 · Problem → Opportunity Playbook · Execution Capstone · Created by [Nisha](https://nissh.info)**

> 💡 **Two Ways to Run This Phase:**
> 1. **🤖 Mode 1 (Autonomous Local Engine):** Handled automatically when running `python server.py`.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the `<!-- BEGIN P6_HANDOFF -->` block into the prompt below in Claude / ChatGPT. The AI generates your production-ready GitHub `README.md` launch kit!

---

## 🎯 What This Phase Does

Research without execution is merely theory.
Once you reach Phase 6, you possess an evidence-verified startup opportunity, a defensible market gap, an ideal customer profile (ICP), and an MVP scope.

In **Phase 7**, you transform that research into the face of your project: a world-class, battle-tested GitHub `README.md`, product landing copy, hero badges, competitive differentiation table, and developer quickstart.

**Goal:** Turn your validated research dossier into an irresistible GitHub README and launch kit that immediately attracts co-founders, early adopters, GitHub stars, and investors.

---

## 📥 Input Contract (From Phase 6)

This phase consumes the output of [`P6_Final_Report.md`](./P6_Final_Report.md):
- The `<!-- BEGIN P6_HANDOFF -->` block containing:
  - Proposed Project Name
  - One-line Pitch
  - Problem Statement
  - Target Audience / ICP
  - Core Differentiator (The Gap)
  - MVP Core Features
  - Tech Stack Suggestion
  - 30-Day Launch Plan

*(Optional: If you have already started writing code or have a project repository/ZIP, you can also paste your directory structure or upload your ZIP file).*

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | High-fidelity technical writing, copywriting, and architecture modeling |
| 🔍 Web Search | Optional | Useful if you want to pull live shield badge links or check existing repo names |

---

## 📋 Copy-to-Paste Prompt (Mode A: Research-to-Launch README)

> **Instructions:** Copy the prompt below, paste your `<!-- BEGIN P6_HANDOFF -->` block from Phase 6 into the input section, and run in Claude.

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 6 (RESEARCH DOSSIER HANDOFF):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P6_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: GENERATE THE ULTIMATE GITHUB README & LAUNCH KIT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
You are a world-class technical writer, open-source evangelist, and developer marketer who has studied the highest-converting and most beloved GitHub READMEs (e.g. gofiber/fiber, httpie, lobehub/lobe-chat, sniffnet, PostHog, Supabase, and dbt-core).

Using the verified startup opportunity and MVP specifications from Phase 6 above, write a single, complete, PERFECT `README.md` for this new project.

Produce RAW, READY-TO-PUBLISH MARKDOWN ONLY. Follow this exact structure:

─────────────────────────────────────────────────
1. HERO HEADER (Center Aligned)
─────────────────────────────────────────────────
- Text ASCII-art banner with the project name
- Project Title with primary emoji
- Sharp tagline (≤15 words, zero fluff, answers: "What does it do for me?")
- Badge Row: Tech stack badges, license, build status, discord/community, stars
- Quick call-to-action link ("Get Started →" | "View Demo" | "Read Whitepaper")

─────────────────────────────────────────────────
2. THE PAIN & THE GAP (Why This Exists)
─────────────────────────────────────────────────
- The Problem: 2–3 sentences quoting real user frustrations discovered during research
- The Status Quo: Why existing tools fail (summarize what the 10 competitors miss)
- The Breakthrough: What our solution does differently (the verified gap)

─────────────────────────────────────────────────
3. KEY FEATURES (Visual & Focused)
─────────────────────────────────────────────────
- 3–4 core feature cards highlighting the MVP capabilities
- Use clean Markdown formatting, code snippets, or ASCII workflow diagrams
- "Before vs. After" comparison snippet

─────────────────────────────────────────────────
4. COMPETITIVE MATRIX (Why Choose Us)
─────────────────────────────────────────────────
- Comparison table: Us vs. Top Competitor 1 vs. Top Competitor 2 vs. Manual Workaround
- Features compared: The exact gap capabilities validated in Phase 4 & 5

─────────────────────────────────────────────────
5. ARCHITECTURE & TECH STACK
─────────────────────────────────────────────────
- Mermaid diagram showing data flow / system architecture
- Bullet points detailing the chosen lightweight tech stack and rationale

─────────────────────────────────────────────────
6. QUICKSTART / INSTALLATION (30 Seconds to Run)
─────────────────────────────────────────────────
- Prerequisites
- Step-by-step setup commands (e.g. git clone, install dependencies, run dev)
- Environment variables table (`.env.example`)

─────────────────────────────────────────────────
7. ROADMAP & 30-DAY PLAN
─────────────────────────────────────────────────
- Interactive checklist reflecting the 30-day roadmap from Phase 6
  - [x] Phase 1–6 Research & Market Validation Complete
  - [ ] Alpha prototype
  - [ ] Community beta
  - [ ] Launch

─────────────────────────────────────────────────
8. CONTRIBUTING & LICENSE
─────────────────────────────────────────────────
- Open source contribution guidelines
- License badge and details (Apache 2.0 / MIT)

Output the raw markdown for `README.md` immediately. No introductory commentary.
```

---

## 📋 Copy-to-Paste Prompt (Mode B: Existing Codebase / ZIP Audit)

> **Instructions:** If you already wrote code in this workspace and want Claude to inspect your actual files/ZIP, use this prompt:

```text
You are a world-class technical writer and open-source documentation expert.
I have provided my project files / codebase.
Your ONLY job is to:
1. Silently analyze the code structure and architecture.
2. Ingest the problem, target audience, and competitive gaps from the research system.
3. Output a single, complete, PERFECT README.md following the structure in Mode A above.
Do NOT explain what you are doing. Output the raw markdown ONLY.
```

---

## 🗂️ How to Use

1. Grab the `<!-- BEGIN P6_HANDOFF -->` block from the end of your Phase 6 report.
2. Paste it into the Mode A prompt above.
3. Run with Claude (or click "Generate README" in `startup_research_playbook.html`).
4. Save the generated content directly as your new project's `README.md`.

---

## ✅ Expected Output

- A professional, high-converting GitHub `README.md`
- Accurate reflection of the evidence and competitor gaps found in P1–P6
- Architecture diagram and setup instructions
- Immediate readiness for GitHub, Product Hunt, and Hacker News launch

---

## 🏆 The Complete Pipeline Completed!

You have completed the entire 7-phase research and execution pipeline:

```text
P1 Validate → P2 Top 10 → P3 Research ×10 → P4 Gap Analysis → P5 Verify Gaps → P6 Final Report → P7 Launch README
```

You started with an unverified assumption and ended with:
1. Proven user demand
2. Deep competitive teardowns
3. Mathematically scored market voids
4. Stealth competitor verification
5. Defensible investor-grade diligence memo
6. Production-ready open-source launch README

---

*Part of the [Startup Research Playbook](./README.md) · 7-phase end-to-end pipeline*
