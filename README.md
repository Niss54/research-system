# 🚀 Problem → Opportunity Playbook

<div align="center">

**A 6-phase AI-powered startup research system — from problem to opportunity, backed by evidence.**

![Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange?style=flat-square&logo=anthropic)
![Phases](https://img.shields.io/badge/Phases-6%20Pipeline-blueviolet?style=flat-square)
![Research Time](https://img.shields.io/badge/Research%20Time-4--5%20Hours-green?style=flat-square)
![Language](https://img.shields.io/badge/Language-English-blue?style=flat-square)
![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen?style=flat-square)

> *"Validate first, build second. This playbook ensures you solve a real problem — not an assumption."*

</div>

---

## 📌 Project Overview

**Problem → Opportunity Playbook** is a structured, AI-powered research framework that helps startup founders and indie hackers:

- **Validate** whether a problem is real or just feels real
- **Map** what solutions already exist in the market
- **Identify** genuine gaps that competitors are missing
- **Build** an evidence-backed startup opportunity report — ready for investors and co-founders

This system works with **Claude AI** (using web search + extended thinking mode). Every phase contains a ready-to-paste prompt — just copy it, paste it into Claude, and get your output.

---

## 🗂️ File Structure

```
research-system/
│
├── README.md                   ← You are here
│
├── P1_Validate.md              ← Is the problem real or not?
├── P2_Top10.md                 ← What solutions already exist in the market?
├── P3_Research_x10.md          ← Deep dive into each competitor
├── P4_Gap_Analysis.md          ← Feature matrix + identify real gaps
├── P5_Verify_Gaps.md           ← Confirm gaps before building
├── P6_Final_Report.md          ← Investor-ready opportunity report
│
└── startup_research_playbook.html  ← Interactive web version (rendered UI)
```

---

## 🔁 The 6-Phase Pipeline

```
P1 Validate  →  P2 Top 10  →  P3 Research ×10  →  P4 Gap Analysis  →  P5 Verify Gaps  →  P6 Final Report
```

| Phase | Name | Goal | Time | Claude Settings |
|-------|------|------|------|-----------------|
| **P1** | Validate | Is the problem real or just a feeling? Find evidence. | ~20 min | 🌐 Web Search + 🧠 Extended Thinking |
| **P2** | Top 10 | Identify the top 10 existing solutions in the market | ~15 min | 🌐 Web Search |
| **P3** | Research ×10 | Deep dive into each competitor (run 10 times) | ~2–3 hrs | 🌐 Web Search + 🔬 Deep Research |
| **P4** | Gap Analysis | Build a feature matrix and surface real gaps | ~30 min | 🧠 Extended Thinking (no search) |
| **P5** | Verify Gaps | Confirm no one else is already solving the gaps | ~45 min | 🌐 Web Search + 🔬 Deep Research |
| **P6** | Final Report | Everything in one professional report | ~20 min | 🧠 Extended Thinking (no search) |

**Total time: ~4–5 hours for a complete research cycle**

---

## 🚦 How to Use This System

### Step 1 — Define your problem
Write your problem statement in 2–3 lines. Be clear and specific.

```
❌ Weak:  "I want to improve productivity"
✅ Strong: "Freelance designers struggle to track client invoices —
            they use 3–4 tools that don't sync with each other"
```

### Step 2 — Start with P1
1. Open `P1_Validate.md`
2. Open **Claude.ai** or any Claude-based tool
3. Turn **Web Search ON** (toggle in the top bar)
4. Turn **Extended Thinking ON** (in the model selector)
5. Copy the prompt, fill in your problem statement, and paste it into Claude

### Step 3 — Save your output and paste it into the next phase
> ⚠️ **CRITICAL:** This is a chain. Every phase's output must be pasted into the next phase's prompt.
> Skipping a step will significantly reduce the quality of your results.

```
P1 output → paste into P2 prompt
P2 output → paste into P3 prompt (run 10 times, once per competitor)
P3 outputs (all 10) → paste into P4 prompt
P4 output → paste into P5 prompt
P1 + P2 + P3 + P4 + P5 outputs → paste into P6 prompt
```

### Step 4 — Check the verdict at every phase

| Verdict | Meaning | Action |
|---------|---------|--------|
| ✅ GO | Strong signal — move forward | Proceed to the next phase |
| ⚠️ MAYBE | Mixed signals | Validate with real users first |
| ❌ NO-GO | Problem is weak | **STOP** — rephrase the problem or pivot |

---

## ⚙️ Claude Settings Guide

| Setting | When to turn ON | Where to find it |
|---------|-----------------|------------------|
| 🌐 **Web Search** | Required for P1, P2, P3, P5 | Search icon in the Claude.ai top bar |
| 🧠 **Extended Thinking** | P1, P4, P6 — synthesis tasks | Model selector dropdown |
| 🔬 **Deep Research Mode** | Best for P3 and P5 | Claude Pro features |

> **Note:** Without the correct settings, prompts will be only half as effective. Always check settings before starting each phase.

---

## 📋 Phase Quick Reference

<details>
<summary><strong>P1 — Validate</strong> (click to expand)</summary>

**Objective:** Is the problem real, or does it just feel real? Find hard evidence first.

**What it searches:**
- Reddit complaint and frustration threads
- App Store / Play Store reviews
- Survey data and statistics
- Demand signals for existing solutions

**Expected Output:**
- Validation score: Strong / Moderate / Weak
- 3–5 source links with real user pain signals
- Clear **GO / MAYBE / NO-GO** verdict with reasoning

**Pro Tip:** If you get a NO-GO, stop here. Rephrase the problem — define it for a specific user and try again. If it's still weak after 3 rephrases, the problem genuinely doesn't exist at scale or is too niche.

📄 **Full prompt:** [`P1_Validate.md`](P1_Validate.md)

</details>

<details>
<summary><strong>P2 — Top 10</strong> (click to expand)</summary>

**Objective:** What solutions already exist in the market? Identify the best 10 competitors.

**Searches across:** Product Hunt, G2, Capterra, AlternativeTo, Reddit, App Store, GitHub

**Expected Output:**
- Table of 10 solutions: URL, pricing, target user, key features
- Mix of: major players + niche tools + manual workarounds
- Foundation for P3 deep research

**Pro Tip:** Manual workarounds are gold. If people are building Excel sheets or Notion templates to solve the problem — that's a HUGE gap signal. It means the problem is real but no proper software exists yet.

📄 **Full prompt:** [`P2_Top10.md`](P2_Top10.md)

</details>

<details>
<summary><strong>P3 — Research ×10</strong> (click to expand)</summary>

**Objective:** Deep dive into each competitor — what it covers, what it doesn't. Run this prompt 10 times.

**Each profile covers:**
- Product profile + user journey
- Company intel (funding, team size, revenue)
- Pricing tiers + pricing complaints
- What users love ★★★★★
- What users hate ★☆☆☆☆
- Critical gaps ← MOST IMPORTANT SECTION

**Expected Output:**
- 10 detailed competitor profiles (one session per competitor)
- A "THIS TOOL DOES NOT" summary line for each tool
- Raw material for the P4 gap analysis

**Pro Tip:** Research 2–3 competitors per session to keep context intact. Always make sure Claude ends each profile with the "THIS TOOL DOES NOT" line — it becomes essential during P4.

📄 **Full prompt:** [`P3_Research_x10.md`](P3_Research_x10.md)

</details>

<details>
<summary><strong>P4 — Gap Analysis</strong> (click to expand)</summary>

**Objective:** Paste all 10 profiles together — Claude will build a feature matrix and surface the real gaps.

**Produces:**
- Feature matrix: all 10 solutions × all features found (✓ / ~ / ✗)
- Gap categories: Feature, Quality, Audience, Pricing, Workflow
- Scoring formula: `(User Pain × Market Size) ÷ Build Difficulty`

**Expected Output:**
- Full feature matrix table
- All gaps categorized and scored
- Top 5 ranked opportunities with scores and reasoning
- A single #1 recommended gap to focus on

**Pro Tip:** Make sure Extended Thinking is ON for this step. Add this to the end of the prompt: *"Take extra time before responding. Think through every gap carefully before scoring."*

📄 **Full prompt:** [`P4_Gap_Analysis.md`](P4_Gap_Analysis.md)

</details>

<details>
<summary><strong>P5 — Verify Gaps</strong> (click to expand)</summary>

**Objective:** Confirm the gaps found in P4 — is anyone already building this?

**Searches:** Google, Product Hunt, Indie Hackers, GitHub, YC Companies, BetaList, TechCrunch, LinkedIn

**Gap Verdicts:**
- ✅ **CONFIRMED GAP** — Nothing found after exhaustive search. Truly open.
- ⚠️ **PARTIAL GAP** — 1–2 weak or early solutions exist but a serious gap remains.
- ❌ **FALSE GAP** — A solid solution already exists. Remove from the list.

**Expected Output:**
- Verified verdict on each gap with supporting evidence
- Why the gap exists and what recently changed to make it possible
- A minimal version description for each confirmed gap

**Pro Tip:** False gaps are NOT bad news — it means someone validated the idea but executed poorly. Search their negative reviews immediately. Partial gap + bad reviews = a massive opportunity to do it 10× better.

📄 **Full prompt:** [`P5_Verify_Gaps.md`](P5_Verify_Gaps.md)

</details>

<details>
<summary><strong>P6 — Final Report</strong> (click to expand)</summary>

**Objective:** Everything in one place. A professional report you can share directly with co-founders or investors.

**Report Sections:**
1. Executive Summary (GO / NO-GO / PIVOT recommendation)
2. Problem Deep Dive (ICP, current workarounds, cost of inaction)
3. Competitive Landscape (market map, what all competitors miss)
4. Your Opportunity (top 3 gaps, revenue potential, build effort)
5. Product Direction (MUST BUILD / SHOULD BUILD / SKIP)
6. 30-Day Action Plan (landing page → user interviews → MVP → launch)

**Expected Output:**
- Investor-ready startup opportunity report
- Prioritized product roadmap
- 30-day action plan with a real user interview script

**Pro Tip:** Don't share the report immediately after it's generated. Mark any claims that seem doubtful and manually verify them. Claude synthesizes well, but revenue figures and user estimates should always be personally checked.

📄 **Full prompt:** [`P6_Final_Report.md`](P6_Final_Report.md)

</details>

---

## 💡 Pro Tips (System-Level)

```
✅ DO
├── Complete each phase fully before moving to the next
├── Use a new Claude session per competitor in P3
├── Paste ALL 10 P3 outputs together into P4
├── Manually fact-check key claims after P6
└── Got a NO-GO at P1? Rephrase — don't waste 4–5 hours on a weak problem

❌ DON'T
├── Skip P1 — the entire cycle can become a waste without validation
├── Change web search settings mid-prompt
├── Put multiple competitors into a single P3 prompt
├── Share the P6 report without verification
└── Treat Claude's estimates as ground truth — always verify
```

---

## 🤝 Contributing

Contributions are welcome! If you have better prompts, improvements, or ideas for new phases — open a PR.

### How to Contribute

1. **Fork** this repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/research-system.git
   cd research-system
   ```

2. **Create a branch** for your feature
   ```bash
   git checkout -b improve/p3-prompt-v2
   ```

3. **Make your changes** and test them with Claude
   - For prompt changes: test in an actual Claude session first
   - Update the expected output section if the output changes
   - Add or update the pro tip if you have a better one

4. **Commit** with a clear message
   ```bash
   git commit -m "feat(P3): add Glassdoor to competitor research search list"
   ```

5. **Push** and **open a Pull Request**
   ```bash
   git push origin improve/p3-prompt-v2
   ```

### Contribution Ideas

| Type | Examples |
|------|---------|
| 🔧 Prompt improvements | Better search queries, clearer output formats |
| 📊 New gap categories | E.g., geographic gaps, language gaps |
| 🌐 New search sources | New platforms to check in P2, P3, or P5 |
| 🌍 Translations | Prompts fully translated to Hindi or other languages |
| 📝 Case studies | Real examples of the system in action |
| 🐛 Bug reports | Prompts that produce bad or incomplete output |

### Contribution Guidelines

- **One phase per PR** — avoid mixing changes across multiple phases
- **Real testing required** — include actual Claude output in the PR description, not just theoretical changes
- **Keep the voice consistent** — clear, direct, and actionable
- If you add a new file, update the File Structure section in this README as well

---

## 📊 Expected Total Output

After a complete P1 → P6 cycle, you will have:

- ✅ **Evidence-backed problem validation** (real data, real links)
- ✅ **Competitive landscape map** (10 solutions, fully profiled)
- ✅ **Feature matrix** (every feature vs. every competitor)
- ✅ **Ranked opportunity list** (gaps scored on pain × market × difficulty)
- ✅ **Verified gaps** (confirmed against an exhaustive search)
- ✅ **Investor-ready report** (6 sections, GO/NO-GO decision, 30-day plan)

---

## ⚠️ Important Disclaimers

- Claude AI can **hallucinate** — especially around revenue figures and user numbers. Manually verify important claims from the P6 report.
- **Market estimates** are rough signals, not authoritative data. For TAM/SAM, consult proper market research reports.
- This system **accelerates** market research — it does not replace actual customer conversations. User interviews in the P6 30-day plan are non-negotiable.

---

## 📄 License

Licensed under the **Apache License 2.0** — free to use, modify, and distribute.  
See the [`LICENSE`](LICENSE) file for full terms.

---

## 🙌 Acknowledgements

Built for the builder who validates first, builds second.
Inspired by the startup research frameworks of YC, Indie Hackers, and every founder who wasted 6 months building the wrong thing.

---

<div align="center">

**⭐ If this was useful, leave a star — it helps other founders find it too**

Made with ❤️ for the global startup community

</div>
