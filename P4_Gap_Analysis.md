# P4 — Gap Analysis
> **Phase 4 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

This is where the research becomes a decision. You paste all 10 competitor profiles from P3 into one session, and Claude builds a complete feature matrix — then identifies, categorizes, and scores every gap in the market.

**Goal:** A ranked list of real market opportunities, scored on user pain, market size, and build difficulty — with a single #1 recommendation on where to focus.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | This is a pure synthesis task — Claude needs time to reason across 10 profiles |
| 🔍 Web Search | **OFF** | All data comes from P3 research; no new searches needed here |

> **How to enable in Claude.ai:**
> - Extended Thinking → model selector → select "Extended thinking"
> - Make sure web search is toggled OFF to keep Claude focused on your research data

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, paste your problem statement and all 10 P3 profiles into the designated sections, and run in Claude with Extended Thinking ON.

```
Problem: [PROBLEM STATEMENT]

Below are deep-dive profiles for all 10 competing solutions:

[PASTE ALL 10 P3 RESEARCH PROFILES HERE]

Perform a comprehensive gap analysis. Think step-by-step, take your time.

── STEP 1: BUILD FEATURE MATRIX ──────────────────────────────
List every distinct feature/capability mentioned across all 10 solutions.
Build a table:
  • Rows = all distinct features found
  • Columns = 10 solution names
  • Cell values: ✓ (has it fully) | ~ (partial/basic version) | ✗ (missing)

── STEP 2: IDENTIFY GAPS ──────────────────────────────────────
After building the matrix, categorize:

A. FEATURE GAPS — rows that are mostly ✗ (nobody does this at all)
B. QUALITY GAPS — rows that are all ~ (everyone does it but does it badly)
C. AUDIENCE GAPS — user segment none of them serve well
D. PRICING GAPS — price points or models nobody offers
   (e.g. "all tools are enterprise-only, no option for solopreneurs")
E. WORKFLOW GAPS — integrations or use-case flows no one supports

── STEP 3: SCORE EACH GAP ────────────────────────────────────
For every gap found, rate it:
• USER PAIN: How much do users suffer? Evidence = complaint count from P3
  Rating: Low / Medium / High
• MARKET SIZE: How many users need this?
  Rating: Niche <10K / Small 10K–100K / Medium 100K–1M / Large 1M+
• BUILD DIFFICULTY: How hard to build?
  Rating: Easy / Medium / Hard / Very hard
• COMPETITIVE MOAT: How fast can competitors copy it if you build it?
  Rating: Low (anyone can copy) / Medium / High (hard to replicate)

── STEP 4: RANK OPPORTUNITIES ─────────────────────────────────
Score each gap: (User Pain × Market Size) ÷ Build Difficulty
Rank all gaps from highest to lowest.

Output:
1. Complete feature matrix table
2. All gaps found — categorized and scored
3. Top 5 ranked opportunities with score and brief reasoning
4. Your #1 recommended gap to focus on and why
```

---

## 🗂️ How to Use

1. **Paste all 10 P3 profiles** — do not leave any out; the matrix only works with the full dataset
2. **Keep Extended Thinking ON** — this is the most reasoning-intensive step in the entire pipeline
3. **Do not interrupt** — Claude will take longer than usual here; let it finish the full analysis
4. **Add this line to the end of your prompt** for better results: *"Take extra time before responding. Think through every gap carefully before scoring."*
5. **Save the full output** — you need the top 5 gaps list for P5

---

## ✅ Expected Output

Claude should return:

- **Complete feature matrix** — every feature × every competitor (✓ / ~ / ✗)
- **All gaps categorized** — Feature, Quality, Audience, Pricing, and Workflow gaps
- **Scoring for each gap** — User Pain, Market Size, Build Difficulty, Competitive Moat
- **Top 5 ranked opportunities** — with scores and brief reasoning for each
- **A single #1 recommendation** — the gap with the best combination of high pain, large market, and manageable build effort

---

## 💡 Pro Tip

> **Extended Thinking is non-negotiable for this step.** This is a pure synthesis task — no web searching, just deep reasoning across 10 profiles. Add *"Take extra time before responding. Think through every gap carefully before scoring."* to the end of your prompt.

Also: look closely at **Quality Gaps** (where all tools have `~`). These are often more valuable than Feature Gaps — the need is proven, but no one has executed it well. That's your opening.

---

## ⏱️ Time Estimate

**~30 minutes** — Claude takes 20–25 minutes in Extended Thinking mode for this step. You'll need a few minutes to assemble all 10 P3 profiles before pasting.

---

## ➡️ Next Step

Take the **Top 5 gaps** from P4's output → Go to [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md)

You'll verify each gap against exhaustive web search to confirm no one is already building a solution.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
