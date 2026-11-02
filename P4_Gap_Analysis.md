# P4 — Gap Analysis (v2 Grounded Edition)
> **Phase 4 of 7** · Strategic Feature Matrix & Opportunity Scoring · Created by [Nisha](https://nissh.info)

> 💡 **Execution Modes:**
> 1. **🤖 Mode 1 (Autonomous Local CLI / UI):** Automatically synthesizes feature matrices and computes opportunity scores with sensitivity checks.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste `P1_HANDOFF` and all `P3_PROFILE` blocks into the prompt below. Feed resulting `<!-- BEGIN P4_HANDOFF -->` into [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md).

---

## 🎯 What This Phase Does

Cross-references validated customer pain from Phase 1 against the competitor deficiencies uncovered in Phase 3.
In v2, you do NOT rely on fixed, subjective scores:
- **Feature Matrix (`✓` / `~` / `✗`)**: Compares all 10 competitors across critical workflow capabilities.
- **Evidence-Backed Opportunity Scoring**: Calculates scores with explicit justifications for User Pain (1-5), Market Size (1-5), and Build Feasibility (1-5).
- **Sensitivity & Incumbent Risk Check**: Analyzes what happens if an incumbent adds this feature as an update.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|---|---|---|
| 🧠 Extended Reasoning | **MANDATORY** | Complex matrix synthesis, multi-variable scoring, and sensitivity analysis |

---

## 📋 Copy-to-Paste Prompt

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 1 (VALIDATED PROBLEM FROM PHASE 1):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE YOUR P1_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT 2 (COMPETITOR PROFILES FROM PHASE 3):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE ALL P3_PROFILE BLOCKS HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: FEATURE MATRIX, GAP DISCOVERY & SENSITIVITY SCORING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a strategic product partner and venture analyst. Cross-reference the validated user pain against the competitor teardowns.

TASKS:
1. Cross-Competitor Feature Matrix:
   - Identify 6-8 core feature capabilities.
   - Map each competitor: [✓ = Fully supported] | [~ = Clunky/Partial] | [✗ = Unsupported/Missing].
2. Identify Top 5 Market Gaps:
   - Classify each: Workflow Gap, Pricing Gap, Audience Gap, or Integration Gap.
3. Opportunity Scoring Formula:
   - User Pain (1-5): Evidence of acute financial/emotional drain.
   - Market Size (1-5): Addressable customer base in target geography.
   - Build Feasibility (1-5): MVP buildable by a small team within 3-4 weeks.
   - Score = (Pain × Market × Feasibility) / 2 [Normalized to 10 max].
4. Sensitivity & Incumbent Defense Analysis:
   - For each gap, identify the primary risk: Why hasn't an incumbent built this? Can they replicate it in a weekend?
5. Select the #1 RECOMMENDED WEDGE.

OUTPUT FORMAT (MUST INCLUDE EXACT HANDOFF BLOCK):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FEATURE COMPARISON MATRIX:
| Capability | Competitor 1 | Competitor 2 | ... | Competitor 10 | Gap Verdict |
| :--- | :---: | :---: | :---: | :---: | :--- |

<!-- BEGIN P4_HANDOFF -->
PROBLEM_SPACE: [Restated from P1]
TARGET_AUDIENCE: [From P1]

TOP_5_GAPS:
- GAP 1: [Name]
  CATEGORY: [Workflow / Pricing / Integration / Audience Gap]
  DESCRIPTION: [1-2 sentences on what is missing and how users suffer]
  PAIN_SCORE: [1-5] | MARKET_SCORE: [1-5] | FEASIBILITY_SCORE: [1-5]
  OPPORTUNITY_SCORE: [N/10]
  SENSITIVITY_RISK: [Why incumbents haven't done it & defense against copycats]

- GAP 2: [Name]
  ...
- GAP 5: [Name]

#1_RECOMMENDED_GAP:
NAME: [Name of #1 Gap]
CATEGORY: [Category]
OPPORTUNITY_SCORE: [Calculated Score]
JUSTIFICATION: [Why this is the highest leverage startup angle]
KEY_DIFFERENTIATOR: [The single unfair advantage / mechanism]
CORE_WEDGE_MECHANISM: [How this feature acts as a trojan horse into the customer's daily workflow]
<!-- END P4_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔗 Next Phase Handoff
Copy the `<!-- BEGIN P4_HANDOFF -->` block into [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md).
