# P6 — Final Report
> **Phase 6 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

Sab kuch ek jagah. P1 se P5 tak ke sare outputs ek massive prompt mein paste karo aur Claude ek professional, structured startup opportunity report generate karega — co-founders ya investors ko directly dikhao.

**Goal:** 6-section investor-ready startup opportunity report with GO/NO-GO/PIVOT recommendation + 30-day action plan.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | This is the final synthesis — Claude ko full depth mein sochna hai |
| 🔍 Web Search | **OFF** | Sab research complete ho chuka hai — fresh search needed nahi |

> **How to enable in Claude.ai:**
> - Extended Thinking → model selector → "Extended thinking" option
> - Web Search → OFF rakho

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** `[PROBLEM STATEMENT]` aur `[TODAY'S DATE]` bharo. Phir P1–P5 ke sare outputs respective sections mein paste karo. Yeh ek very long prompt hoga — yeh normal hai.

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
MUST BUILD — core, without these don't launch:
• [Feature] → why it's non-negotiable

SHOULD BUILD — these make you win against competitors:
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

1. **Sab 5 phase outputs ready karo** — P1, P2, P3 (×10), P4, P5 — ek doc mein organized
2. **Problem statement aur date add karo** — simple hai
3. **Sab paste karo ek saath** — yeh longest prompt hai poore pipeline mein, normal hai
4. **Extended Thinking ON, Web Search OFF** — yeh critical hai
5. **Wait for full response** — 10–15 min lag sakte hain, interrupt bilkul mat karo
6. **Report ek markdown/doc mein save karo** — yeh shareable artifact hai

### Apne Final Report Ko Polish Karo (Optional)

Report aane ke baad:
- Claims jinhein verify nahi kiya → highlight karo, manually check karo
- Numbers aur estimates (TAM, revenue, users) → always double-check independently
- Section 5 (product direction) → share with 2–3 potential users aur feedback lo

---

## ✅ Expected Output

A complete 6-section report including:

- **Section 1:** Executive Summary + clear GO / NO-GO / PIVOT recommendation
- **Section 2:** ICP, current workarounds, cost of problem, user voice
- **Section 3:** Competitive landscape table + market map + what they all miss
- **Section 4:** Top 3 ranked opportunities + revenue + build estimates + #1 recommendation
- **Section 5:** Must Build / Should Build / Skip Now product roadmap
- **Section 6:** 30-day action plan + user interview script + community launch plan

**This report is ready to share with:**
- Co-founders — to align on the problem and opportunity
- Early advisors or mentors — for strategic feedback
- Potential investors — as a pre-seed opportunity memo

---

## 💡 Pro Tip

> **Report aane ke baad seedha share mat karo.** Jo claims tujhe doubtful lagein unhe mark kar aur manually verify kar. Claude synthesis well karta hai but numbers aur estimates tujhe personally check karne chahiye.

**Specific things to verify manually:**
- Market size numbers — cross-check with Statista or industry reports
- Revenue estimates — validate with similar SaaS pricing benchmarks
- ICP definition — confirm with 2 real interviews before locking in

**To make it even better**, add this line at the end of the prompt:
```
After writing the full report, add one final section titled 
"ASSUMPTIONS TO VERIFY" — list every estimate or claim that 
needs real-world confirmation before building.
```

---

## ⏱️ Time Estimate

**~20 minutes** — Prompt assembly 5–10 min (pasting all outputs), Claude response 10–15 min with Extended Thinking.

---

## 🏁 You're Done

Congratulations — you've completed the full 6-phase startup research pipeline.

**Total time invested:** ~4–5 hours
**What you now have:** A data-backed opportunity report most startup teams spend weeks trying to build.

**What comes next:**
1. Week 1 → Build landing page (from Section 6 plan)
2. Week 2 → Talk to 10 real users
3. Week 3 → Define 3-feature MVP
4. Week 4 → Launch + community distribution

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
