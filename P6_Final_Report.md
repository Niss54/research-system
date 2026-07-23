# P6 — Final Report
> **Phase 6 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

Everything in one place. You paste all outputs from P1 through P5 into a single prompt, and Claude synthesizes a complete, structured startup opportunity report — ready to share with co-founders, investors, or use as your own build/no-build decision framework.

**Goal:** A professional, evidence-backed report with a clear GO / NO-GO / PIVOT recommendation and a 30-day action plan.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | Synthesizing 5 phases of research requires deep, structured reasoning |
| 🔍 Web Search | **OFF** | All data comes from previous phases — no new searches needed |

> **How to enable in Claude.ai:**
> - Extended Thinking → model selector → select "Extended thinking"
> - Turn web search OFF to keep Claude focused on your compiled research

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, fill in your problem statement and today's date, then paste all outputs from P1 through P5 into their respective sections.

```
Create a STARTUP OPPORTUNITY REPORT.

Problem: [PROBLEM STATEMENT]
Date: [TODAY'S DATE]

All research below:
━━━ P1 — VALIDATION RESULTS ━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P1 OUTPUT]

━━━ P2 — TOP 10 SOLUTIONS ━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P2 OUTPUT]

━━━ P3 — COMPETITIVE PROFILES (all 10) ━━━━━━━━━━━━
[PASTE ALL 10 P3 OUTPUTS]

━━━ P4 — GAP ANALYSIS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P4 OUTPUT]

━━━ P5 — VERIFIED GAPS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P5 OUTPUT]

Write the complete report with these exact sections:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1: EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Problem in 2–3 sentences
- Market size signal (from validation evidence)
- What the market is missing (top gap in one line)
- Recommendation: GO ✅ / NO-GO ❌ / PIVOT ↩️ + 2-line reasoning

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2: PROBLEM DEEP DIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- ICP (Ideal Customer Profile): Role, company size, industry, location
- How they cope today (current workarounds they use)
- Cost of not solving: time lost, money wasted, stress caused
- Key user quotes (paraphrased from P3 research)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3: COMPETITIVE LANDSCAPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Summary table of all 10 solutions
- Market map (group them into 2–3 categories)
- What they collectively do well
- The pattern they all miss — this is the real opportunity

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4: YOUR OPPORTUNITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Top 3 confirmed gaps (priority ranked).
For each gap:
  → What's missing and why it matters
  → Estimated users affected
  → Revenue potential (rough range)
  → Build effort estimate

Recommended gap to target: [#1 with 3-line reasoning]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5: PRODUCT DIRECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MUST BUILD — core features; don't launch without these:
• [Feature] → why it's non-negotiable

SHOULD BUILD — these help you win against competitors:
• [Feature] → which gap it fills

SKIP FOR NOW — crowded or not your focus in v1:
• [Feature] → why to defer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6: 30-DAY ACTION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Week 1 (Days 1–7): Build a landing page for the solution.
  Goal: 50 email signups = demand confirmed. 0 signups = rethink.

Week 2 (Days 8–14): Talk to 10 real potential users (not friends).
  Interview script:
  Q1: "Tell me about the last time you dealt with [problem]."
  Q2: "What do you currently use to handle this?"
  Q3: "What would your ideal solution look like?"
  Q4: "Would you pay $X/month for this? Why or why not?"

Week 3 (Days 15–21): Define the MVP scope.
  What's in v0.1? Max 3 core features. Nothing else.

Week 4 (Days 22–30): Launch to first users.
  Join 3 online communities where your ICP is active and share.

Output: Professional, structured report. Use tables where data is comparative.
Cite which research phase each key claim comes from (e.g. "from P3 reviews").
```

---

## 🗂️ How to Use

1. **Compile all previous outputs** before starting — have P1 through P5 saved and ready to paste
2. **Do not skip any section** — the report structure is designed to build a complete decision framework
3. **Fill in today's date** — this timestamps the research and makes the report shareable
4. **Let Claude finish fully** — this is the longest generation in the pipeline; do not interrupt
5. **Review before sharing** — mark any figures or claims you want to verify manually

---

## ✅ Expected Output

Claude should return a complete 6-section report including:

- **Executive Summary** — clear GO / NO-GO / PIVOT with 2-line reasoning
- **Problem Deep Dive** — ICP definition, current workarounds, cost of inaction
- **Competitive Landscape** — market map and what all 10 competitors collectively miss
- **Your Opportunity** — top 3 confirmed gaps with revenue potential and build estimates
- **Product Direction** — MUST BUILD / SHOULD BUILD / SKIP prioritization
- **30-Day Action Plan** — landing page → user interviews → MVP → launch, with a full interview script

---

## 💡 Pro Tip

> **Do not share the report immediately after it's generated.** Go through it once and mark any claims that seem doubtful — especially revenue figures, market size estimates, and user numbers. Claude synthesizes research well, but quantitative estimates should always be personally verified before you present them to investors or co-founders.

The qualitative sections (gaps, product direction, ICP) are usually very reliable. The numbers are starting points, not ground truth.

---

## ⏱️ Time Estimate

**~20 minutes** — Claude takes 15–20 minutes in Extended Thinking mode to synthesize all 5 phases. The bulk of your time is in assembling the inputs (5–10 minutes of copy-pasting).

---

## 🏁 You're Done

You now have a complete startup opportunity report. Here's what to do next:

| If the verdict is... | Next action |
|----------------------|-------------|
| ✅ GO | Build the landing page this week. Start collecting emails. |
| ↩️ PIVOT | Pick the #1 gap from Section 4 and restart from P1 with the refined problem |
| ❌ NO-GO | The research saved you months. Pick a new problem and restart. |

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
