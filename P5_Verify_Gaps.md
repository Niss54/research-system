# P5 — Verify Gaps
> **Phase 5 of 7** · Problem → Opportunity Playbook · Created by [Nisha](https://nissh.info)

> 💡 **Two Ways to Run This Phase:**
> 1. **🤖 Mode 1 (Autonomous Local Engine):** Handled automatically when running `python server.py`.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the `<!-- BEGIN P4_HANDOFF -->` block into the prompt below. Run in Claude (Web Search ON) across 9 platforms. Copy the resulting `<!-- BEGIN P5_HANDOFF -->` block and feed it into [`P6_Final_Report.md`](./P6_Final_Report.md).

---

## 🎯 What This Phase Does

The gaps identified in Phase 4 were discovered by auditing established competitors — but you must confirm that no stealth startups, open-source projects, or new launches are already filling those exact voids. This phase conducts an exhaustive forensic search across 9 platforms to verify whether each gap is genuinely open.

**Goal:** A verified roster of defensible market opportunities, filtering out false leads and promoting only Confirmed (✅) and Partial (⚠️) gaps to the final report.

---

## 📥 Input Contract (From Phase 4)

This phase consumes the output of [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md):
- Problem space & Target audience
- The `<!-- BEGIN P4_HANDOFF -->` block containing `TOP_5_GAPS` and `#1_RECOMMENDED_GAP`

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Mandatory — searches across live databases to catch stealth startups |
| 🔬 Deep Research Mode | **ON** | Runs multi-platform queries automatically |
| 🧠 Extended Thinking | Optional | Useful for assessing partial vs false gaps |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar
> - Deep Research → toggle on Claude Pro

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, paste your `<!-- BEGIN P4_HANDOFF -->` block from Phase 4 into the input section, and run with Web Search and Deep Research ON.
>
> 🔗 **Pipeline Connection:** The output of this phase produces a structured `<!-- BEGIN P5_HANDOFF -->` block that feeds directly into [`P6_Final_Report.md`](./P6_Final_Report.md).

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 4:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P4_HANDOFF BLOCK HERE]
(Or specify: Problem space + Top 5 gap names and descriptions)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: EXHAUSTIVE GAP VERIFICATION (9-PLATFORM AUDIT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a skeptical venture scout and market investigator. Your mission is to attempt to DISPROVE these 5 market gaps. If someone has already built a great solution, find it and disqualify the gap immediately.

For EACH of the 5 gaps listed in the P4 handoff, run ALL 9 of these searches:
□ Google: "[gap keyword] software OR tool OR app"
□ Google: "[gap keyword] solution OR platform"
□ Product Hunt: site:producthunt.com "[gap keyword]"
□ Indie Hackers: site:indiehackers.com "[gap keyword]"
□ GitHub: "[gap keyword]" (check for active open-source repos)
□ Y Combinator: ycombinator.com/companies "[gap keyword]"
□ BetaList / Uneed.app: recent launches and stealth projects
□ TechCrunch / VentureBeat: "[gap keyword] funding OR startup"
□ LinkedIn: "[gap keyword] founder" (stealth founders)

VERDICT CRITERIA FOR EACH GAP:
✅ CONFIRMED GAP — Nothing viable found after exhaustive search. Completely unserved.
⚠️ PARTIAL GAP — 1–2 weak, buggy, abandoned, or early projects exist, but a massive void remains.
   → Name the existing tool + explain why it fails to adequately solve the problem.
❌ FALSE GAP — A well-executed, modern solution already exists.
   → Name it + provide URL + explain why it completely satisfies this need. Remove from roadmap.

FOR EVERY CONFIRMED (✅) OR PARTIAL (⚠️) GAP, ANSWER:
Q1: Why hasn't anyone solved this yet? (Technical hurdle? Misaligned incentives? Niche too small until now?)
Q2: What changed recently that makes this buildable or urgent NOW? (New AI capability, API, regulatory shift, workflow change)
Q3: What would a minimal viable version (MVP) look like? (3–5 bullet points)

OUTPUT FORMAT (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DETAILED VERIFICATION LOG:
[For each of the 5 gaps, provide the specific search findings, URLs checked, and analysis]

<!-- BEGIN P5_HANDOFF -->
PROBLEM_SPACE: [Restated problem space]
TARGET_AUDIENCE: [Primary ICP]

VERIFIED_GAPS:
- GAP 1: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary of search results and competitors discovered]
  WHY_UNBUILT: [Technical, business, or market reason]
  WHY_NOW: [Recent catalyst making this viable today]
  MINIMAL_MVP_FEATURES:
  * [Feature 1]
  * [Feature 2]
  * [Feature 3]

- GAP 2: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Catalyst]
  MINIMAL_MVP_FEATURES: [Features]

- GAP 3: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Catalyst]
  MINIMAL_MVP_FEATURES: [Features]

- GAP 4: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Catalyst]
  MINIMAL_MVP_FEATURES: [Features]

- GAP 5: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  EVIDENCE: [Summary]
  WHY_UNBUILT: [Reason]
  WHY_NOW: [Catalyst]
  MINIMAL_MVP_FEATURES: [Features]

FINAL_VIABLE_OPPORTUNITIES (Only ✅ and ⚠️ gaps):
1. [Name] — [One-line summary of market entry opportunity]
2. [Name] — [One-line summary]

RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: [Single best gap to attack first]
CORE_VALUE_PROP: [Why users will switch on Day 1]
MVP_BUILD_SCOPE: [Clear 3-bullet description of the minimal product]
<!-- END P5_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🗂️ How to Use

1. **Paste the `<!-- BEGIN P4_HANDOFF -->` block** directly into the prompt.
2. **Turn Web Search & Deep Research ON** — verification requires active external queries.
3. **Inspect FALSE Gaps carefully**: If a gap is marked ❌ FALSE GAP, look at user reviews of that existing product. If users complain about reliability or pricing, it may transform into a high-value Partial Gap.
4. **Copy the `<!-- BEGIN P5_HANDOFF -->` block** from the output — it feeds directly into Phase 6.

---

## ✅ Expected Output

Claude will return:
- Full verification logs across 9 platforms for all 5 gaps
- Rigorous verdicts: CONFIRMED ✅, PARTIAL ⚠️, or FALSE ❌
- "Why hasn't this been built?" and "Why now?" analysis for each survivor
- Clean `<!-- BEGIN P5_HANDOFF -->` block ready for Phase 6 report generation

---

## 💡 Pro Tip

> **"Technically exists" does NOT mean "Adequately served."** If the only existing solution for a gap is an unmaintained GitHub repository with 15 stars or an enterprise tool costing $20,000/year, that is an open commercial runway for an indie builder or startup.

---

## ⏱️ Time Estimate

**~30–45 minutes** — Claude runs multiple cross-platform searches per gap.

---

## ➡️ Next Step & Data Handoff

1. Copy the `<!-- BEGIN P5_HANDOFF --> ... <!-- END P5_HANDOFF -->` block.
2. Collect the handoff blocks from **Phase 1, Phase 2, Phase 3, Phase 4, and Phase 5**.
3. Open [`P6_Final_Report.md`](./P6_Final_Report.md).
4. Paste all handoff blocks to generate the investor-ready final report.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
