# P5 — Verify Gaps (v2 Grounded Edition)
> **Phase 5 of 7** · Forensic Gap Verification & Bullshit Detection · Created by [Nisha](https://nissh.info)

> 💡 **Execution Modes:**
> 1. **🤖 Mode 1 (Autonomous Local CLI / UI):** Runs automated live queries against GitHub, Product Hunt, and web search engines to challenge candidate gaps.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the `<!-- BEGIN P4_HANDOFF -->` block into the prompt below. Feed resulting `<!-- BEGIN P5_HANDOFF -->` into [`P6_Final_Report.md`](./P6_Final_Report.md).

---

## 🎯 What This Phase Does

Acts as the adversarial **"Bullshit Detector"** of your startup thesis.
In v2, you do NOT assume a missing search result equals an unbuilt opportunity:
- **Absence of Evidence is NOT Evidence of Absence**: If you search "revision paywall" and find nothing, you must try synonyms ("change order billing", "milestone feedback approval", "design proofing scope lock").
- **Search Coverage Log**: Record the exact platforms and query permutations tested.
- **GitHub & Open Source Sweep**: Check if developers already solved this via open-source tools or browser scripts.
- **Why Unbuilt & Why Now**: If a gap is genuinely unbuilt, why hasn't someone done it in the last 10 years? What technological (APIs, LLMs, Stripe micro-billing) or cultural shift makes it viable today?

---

## ⚙️ Tools Required

| Tool | Status | Why |
|---|---|---|
| 🔍 Live Web Search | **MANDATORY** | Deep multi-synonym search across Google, GitHub, and Product Hunt |
| 🐙 GitHub API | **ACTIVE** | Query repository stars, topics, and code for open-source competitors |
| 🧠 Extended Reasoning | **ON** | Disprove confirmation bias and weed out false gaps |

---

## 📋 Copy-to-Paste Prompt

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 4:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE YOUR ENTIRE P4_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: ADVERSARIAL GAP VERIFICATION (9-PLATFORM FORENSIC AUDIT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as an adversarial venture auditor. Your job is to DISPROVE the candidate gaps identified in Phase 4.
Assume every gap has already been built by someone, somewhere, under a different name or feature set.

FORENSIC AUDIT PROTOCOL:
1. Synonym & Substitute Permutations:
   - For each gap, generate 3-4 semantic synonyms (e.g., "revision paywall" → "change order billing", "scope enforcement tool", "client approval gate").
2. Multi-Platform Search:
   - Google / Web Search (synonyms + "software" / "tool")
   - GitHub (search repository topics and READMEs)
   - Product Hunt (historical launches from 2020-2026)
   - Indie Hackers / Hacker News (Show HN / Ask HN threads)
   - YC Directory (search alumni companies)
3. Assign Honest Forensic Verdicts:
   - CONFIRMED GAP ✅: Truly unserved across all synonym searches.
   - PARTIAL GAP ⚠️: Solutions exist, but are complex enterprise tools, abandoned plugins, or fragmented across multiple apps.
   - FALSE GAP ❌: High-quality, modern solutions already exist under another name (DISQUALIFY THIS GAP).
4. The "Why Unbuilt" & "Why Now" Test:
   - If CONFIRMED, why wasn't this built 5 years ago? (API limits, cultural inertia, high cost).
   - What changed NOW that makes it a winning opportunity today?

OUTPUT FORMAT (MUST INCLUDE EXACT HANDOFF BLOCK):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEARCH COVERAGE AUDIT LOG:
| Gap Name | Synonyms Tested | Platforms Audited | Existing Substitutes Found | Verdict |
| :--- | :--- | :--- | :--- | :---: |

<!-- BEGIN P5_HANDOFF -->
PROBLEM_SPACE: [From P4]
TARGET_AUDIENCE: [From P4]

VERIFIED_GAPS:
- GAP 1: [Name]
  VERDICT: [CONFIRMED ✅ / PARTIAL ⚠️ / FALSE ❌]
  SYNONYMS_SEARCHED: ["Synonym A", "Synonym B", "Synonym C"]
  COUNTEREXAMPLES_DISCOVERED: [List any tools or repos that came close and why they fall short]
  EVIDENCE_AUDIT: [Exact findings across Google, GitHub, and Product Hunt]
  WHY_UNBUILT: [Structural or market reason it wasn't built historically]
  WHY_NOW: [The immediate technology or market catalyst]
  MINIMAL_MVP_FEATURES:
  - [Core capability 1]
  - [Core capability 2]
  - [Core capability 3]

- GAP 2: [Name]
  ...
- GAP 5: [Name]

RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: [Validated Winning Gap Name]
CORE_VALUE_PROP: [One-line punchy promise: "Never X again. Always Y."]
WHY_NOW_CATALYST: [Specific timing catalyst]
MVP_BUILD_SCOPE:
- [Must-have 1]
- [Must-have 2]
- [Must-have 3]
<!-- END P5_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔗 Next Phase Handoff
Copy the `<!-- BEGIN P5_HANDOFF -->` block into [`P6_Final_Report.md`](./P6_Final_Report.md).
