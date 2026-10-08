# P4 — Gap Analysis
> **Phase 4 of 7** · Problem → Opportunity Playbook · Created by [Nisha](https://nissh.info)

> 💡 **Two Ways to Run This Phase:**
> 1. **🤖 Mode 1 (Autonomous Local Engine):** Handled automatically when running `python server.py`.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste `<!-- BEGIN P1_HANDOFF -->` and all `<!-- BEGIN P3_PROFILE: ... -->` outputs into Claude (turn Extended Thinking ON). Copy the resulting `<!-- BEGIN P4_HANDOFF -->` block and feed it into [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md).

---

## 🎯 What This Phase Does

This is where competitor research transforms into strategic decision-making. You combine all 10 competitor profiles from Phase 3 into one synthesis session. Claude builds a complete cross-competitor feature matrix, groups market voids into 5 distinct categories, and scores each opportunity with a mathematical formula.

**Goal:** A ranked list of verified market opportunities, scored on user pain, market size, and build difficulty — with a single #1 recommendation on where to focus, formatted ready for Phase 5 verification.

---

## 📥 Input Contract (From Phase 1 & Phase 3)

This phase requires:
1. Validated Problem Statement & Target Audience from [`P1_Validate.md`](./P1_Validate.md) (`P1_HANDOFF`)
2. All 10 Competitor Profiles generated in [`P3_Research_x10.md`](./P3_Research_x10.md) (`<!-- BEGIN P3_PROFILE: ... -->` blocks)

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | Crucial — this is deep synthesis across 10 products requiring meticulous cross-comparison |
| 🔍 Web Search | **OFF** | All evidence is supplied by P3 profiles; turn off search to keep the model focused on your collected data |

> **How to enable in Claude.ai:**
> - Extended Thinking → model selector → select "Extended thinking"
> - Web Search → turn OFF

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, attach your Phase 1 problem and all 10 Phase 3 profiles into the designated input sections, and run in Claude with Extended Thinking ON.
>
> 🔗 **Pipeline Connection:** The output of this phase produces a structured `<!-- BEGIN P4_HANDOFF -->` block that you will paste directly into [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md).

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 1: VALIDATED PROBLEM & AUDIENCE (FROM P1)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P1_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 2: ALL 10 COMPETITOR PROFILES (FROM P3)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE ALL 10 P3_PROFILE BLOCKS HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: STRATEGIC GAP ANALYSIS & OPPORTUNITY SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a chief product strategist and venture scout. Conduct an exhaustive gap analysis across all 10 competing solutions. Think step-by-step, audit every capability, and take extra time before responding.

── STEP 1: COMPREHENSIVE FEATURE MATRIX ────────────────────────
Identify every distinct feature, capability, workflow, and integration mentioned across the 10 competitor profiles.
Construct a complete matrix table:
- Rows = Distinct features / capabilities found
- Columns = The 10 solution names
- Values:
  ✓ = Full, robust native capability
  ~ = Basic, partial, clunky, or requires paid add-on / third-party integration
  ✗ = Completely missing / not supported

── STEP 2: CATEGORIZE DISCOVERED GAPS ──────────────────────────
Group every identified market deficiency into these 5 categories:
A. FEATURE GAPS: Rows that are mostly ✗ (capabilities nobody offers)
B. QUALITY GAPS: Rows that are all ~ (everyone offers it, but users complain it is slow, confusing, or broken)
C. AUDIENCE GAPS: High-value user segments that existing players ignore or price out
D. PRICING GAPS: Flawed pricing models (e.g. enterprise-only gating, punitive per-seat tiers, lack of usage-based options)
E. WORKFLOW GAPS: Broken user handoffs, missing syncs, or friction requiring external workarounds

── STEP 3: SCORE EACH GAP ──────────────────────────────────────
Rate every discovered gap across 4 dimensions:
1. USER PAIN (1–5):
   1 = Minor convenience | 3 = Real annoyance | 5 = Loss of revenue/hours (strong complaints in P3)
2. MARKET SIZE (1–5):
   1 = Tiny niche (<10k users) | 3 = Solid SMB market (100k–1M) | 5 = Massive global demand (1M+)
3. BUILD DIFFICULTY (1–5):
   1 = Very hard (deep AI/custom infra/regulatory) | 3 = Moderate full-stack | 5 = Lean MVP (can build in 2–4 weeks)
4. COMPETITIVE MOAT (1–5):
   1 = Easily copied in a weekend | 3 = Moderate retention | 5 = Defensible network effects or workflow lock-in

── STEP 4: OPPORTUNITY RANKING FORMULA ─────────────────────────
Calculate Opportunity Score for each gap:
Formula: (User Pain × Market Size × Build Feasibility) ÷ 2
Rank all gaps from highest score to lowest score.

OUTPUT FORMAT (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FULL FEATURE MATRIX:
[Output the complete Markdown table comparing features across all 10 tools]

DETAILED GAP BREAKDOWN:
[Detail the analysis for each category: Feature, Quality, Audience, Pricing, Workflow]

OPPORTUNITY LEADERBOARD:
[Table of all evaluated gaps sorted by Opportunity Score with metric breakdown]

<!-- BEGIN P4_HANDOFF -->
PROBLEM_SPACE: [Restated problem space]
TARGET_AUDIENCE: [Primary ICP]

TOP_5_GAPS:
GAP 1: [Name of Gap 1] — [1–2 sentence description of missing capability, who it impacts, and why current tools fail]
GAP 2: [Name of Gap 2] — [Description]
GAP 3: [Name of Gap 3] — [Description]
GAP 4: [Name of Gap 4] — [Description]
GAP 5: [Name of Gap 5] — [Description]

#1_RECOMMENDED_GAP:
NAME: [Name of #1 Gap]
CATEGORY: [Feature / Quality / Audience / Pricing / Workflow]
OPPORTUNITY_SCORE: [Score]
JUSTIFICATION: [3-line explanation of why this is the highest leverage angle for a new startup]
KEY_DIFFERENTIATOR: [The single unfair advantage or core mechanism this product must possess]
<!-- END P4_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🗂️ How to Use

1. **Paste your Phase 1 handoff** and **all 10 Phase 3 profiles** into the prompt.
2. **Keep Extended Thinking ON** — this step requires maximum analytical reasoning.
3. **Inspect Quality Gaps closely**: If all tools have `~` on a critical workflow, users are tolerating mediocre software — that is your easiest market entry.
4. **Copy the `<!-- BEGIN P4_HANDOFF -->` block** from the output — it feeds directly into Phase 5.

---

## ✅ Expected Output

Claude will return:
- Complete feature matrix table across 10 tools
- Rigorous breakdown of Feature, Quality, Audience, Pricing, and Workflow voids
- Opportunity scoring table ranking all opportunities
- Clean `<!-- BEGIN P4_HANDOFF -->` block with the Top 5 gaps ready for verification

---

## 💡 Pro Tip

> **Don't ignore Quality Gaps.** Founders often hunt for brand new features that nobody has ever built. But building a clean, lightning-fast 10× better version of a feature that all competitors execute poorly is historically the highest-probability path to startup success.

---

## ⏱️ Time Estimate

**~30 minutes** — Claude takes 15–20 minutes in Extended Thinking mode to cross-evaluate 10 products.

---

## ➡️ Next Step & Data Handoff

1. Copy the `<!-- BEGIN P4_HANDOFF --> ... <!-- END P4_HANDOFF -->` block.
2. Open [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md).
3. Paste the block into the Phase 5 prompt.
4. Phase 5 will run live searches across 9 databases to ensure nobody else is already solving these gaps in stealth.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
