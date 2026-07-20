# P4 — Gap Analysis
> **Phase 4 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

P3 ke sab 10 competitor profiles ek jagah paste karo aur Claude ko feature matrix banane do. Yeh phase pure synthesis hai — web search nahi chahiye, sirf deep thinking chahiye. Claude har feature across 10 tools map karega aur genuine gaps nikaalega.

**Goal:** Feature matrix + ranked list of top 5 market gaps — kahan genuinely koi nahi hai.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🧠 Extended Thinking | **ON** | Pure synthesis task — Claude ko sochne ka waqt chahiye |
| 🔍 Web Search | **OFF** | Sab data already P3 mein aa chuka hai, fresh search distract karega |

> **How to enable in Claude.ai:**
> - Extended Thinking → model selector → "Extended thinking" option
> - Web Search → OFF rakho (toggle down)

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** `[PROBLEM STATEMENT]` replace karo apne problem se. `[PASTE ALL 10 P3 RESEARCH PROFILES HERE]` ki jagah P3 ke sab 10 outputs paste karo (hanji, sab ek saath).

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

1. **Sab 10 P3 profiles ek doc mein ready rakh** — copy-paste fast karna hoga
2. **Prompt mein problem statement add karo** — pehle wali P1 se lelo
3. **10 profiles paste karo** — haan, sab ek saath, prompt ke andar. Yeh ek LONG prompt hoga
4. **Extended Thinking ON, Web Search OFF** — yeh bilkul zaroori hai
5. **Kuch add karo prompt ke end mein (optional but powerful):**

```
Take extra time before responding. Think through every gap carefully 
before scoring. Don't rush to output.
```

6. **Claude zyada time lega** — Extended thinking ke saath 5–10 min possible hai. Wait karo.
7. **Top 5 gaps note karo** — yeh P5 mein jaayenge for verification

---

## ✅ Expected Output

Claude should return:

- **Complete feature matrix table** — rows = features, columns = tools, cells = ✓ / ~ / ✗
- **Gaps categorized into 5 types** — Feature, Quality, Audience, Pricing, Workflow
- **Each gap scored** — User Pain, Market Size, Build Difficulty, Competitive Moat
- **Top 5 opportunities ranked** with score formula result + reasoning
- **#1 recommended gap** with 3-line explanation of why to focus here

**Example gap entry:**
```
GAP: Mobile-first experience
Type: Feature Gap
User Pain: High (mentioned in 7 of 10 tool reviews)
Market Size: Large (1M+ freelancers use mobile-first)
Build Difficulty: Medium
Competitive Moat: Medium (takes 6+ months to rebuild properly)
Score: High × Large ÷ Medium = Priority A
```

---

## 💡 Pro Tip

> **Extended thinking mode zaroor ON karo** — yeh pure synthesis task hai, web search nahi chahiye. Prompt ke end mein ye add karo: *"Take extra time before responding. Think through every gap carefully before scoring."*

**Context window ka dhyan rakho** — 10 full competitor profiles bohot bade hote hain. Agar Claude respond nahi kar raha ya timeout ho raha hai, profiles ko split karo:

```
Run 1: Competitors 1–5 → get partial matrix
Run 2: Competitors 6–10 → extend the matrix
Run 3: Combine both matrices, score gaps, rank opportunities
```

---

## ⏱️ Time Estimate

**~30 minutes** — Prompt prepare karne mein 10 min (all 10 profiles paste karna), Claude response 15–20 min with Extended Thinking.

---

## ➡️ Next Step

Take the **Top 5 gaps** from P4 output → Go to [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md)

P5 mein yeh gaps web search se verify hongi — koi pehle se toh nahi bana raha yeh secretly?

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
