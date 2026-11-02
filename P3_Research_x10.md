# P3 — Research x10 (v2 Grounded Edition)
> **Phase 3 of 7** · Forensic Competitor Teardowns · Created by [Nisha](https://nissh.info)

> 💡 **Execution Modes:**
> 1. **🤖 Mode 1 (Autonomous Local CLI / UI):** Runs parallel forensic teardowns of competitors, extracting exact review complaints and missing feature vectors.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the `<!-- BEGIN P2_HANDOFF -->` block into the prompt below. Feed resulting `<!-- BEGIN P3_PROFILE -->` blocks into [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md).

---

## 🎯 What This Phase Does

Performs a forensic teardown of the top solutions discovered in Phase 2.
In v2, you do NOT estimate or invent competitor weaknesses:
- **Verified Review Quotes**: Extract exact user quotes from 1-star and 2-star reviews on G2, Trustpilot, Capterra, and Reddit.
- **Explicit "THIS TOOL DOES NOT" Boundaries**: Formulate the non-negotiable boundaries of what the tool fails to do.
- **In-Product Workarounds**: Document the clumsy manual hacks users are forced to create when using the tool.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|---|---|---|
| 🔍 Live Web Search | **MANDATORY** | Query `"tool complaints"`, `"tool hate"`, `"tool review 1 star"`, and documentation |
| 🧠 Extended Reasoning | **ON** | Extract structural architectural limitations, not temporary bugs |

---

## 📋 Copy-to-Paste Prompt

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 2:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE YOUR ENTIRE P2_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: FORENSIC COMPETITOR TEARDOWNS (BATCH RESEARCH)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a forensic SaaS product auditor. For the competitors listed in Phase 2, conduct a rigorous teardown to uncover their core shortcomings, blindspots, and user churn triggers.

FOR EACH COMPETITOR, SEARCH & AUDIT:
1. Product Architecture: How is it positioned? What is the core workflow?
2. Real Pricing Snapshot: What are the current plan limits, hidden fees, and paywalls?
3. What Users Love: High-performing features that you should NOT attempt to copy head-on.
4. What Users Hate (1-2 Star Reviews): Look up exact complaints on G2, Reddit, and Twitter.
5. In-Product Workarounds: What manual tricks do users build to bypass the tool's limitations?
6. The Hard Boundary ("THIS TOOL DOES NOT"): Explicitly state what the tool physically cannot do.

OUTPUT FORMAT (GENERATE A PROFILE FOR EACH COMPETITOR):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<!-- BEGIN P3_PROFILE: [COMPETITOR NAME] -->
COMPETITOR_NAME: [Name]
WEBSITE: [Live URL]
TYPE: [Direct / Indirect / Workaround]
SUMMARY_POSITIONING: [2-line summary of product offering and target audience]
PRICING_TIERS: [Free tier / Starter $X / Pro $Y / Enterprise]
WHAT_USERS_LOVE:
- [Praised capability 1]
- [Praised capability 2]
WHAT_USERS_HATE (VERIFIED QUOTES/COMPLAINTS):
- "[Exact quote or synthesis of recurring complaint 1]" (Source: G2/Reddit)
- "[Exact quote or synthesis of recurring complaint 2]" (Source: Capterra/Trustpilot)
CRITICAL_GAPS_AND_WORKAROUNDS:
- [Where the product breaks down in practice and what DIY hacks users create]
THIS TOOL DOES NOT: [Comma-separated explicit list of unmet needs and missing features]
<!-- END P3_PROFILE: [COMPETITOR NAME] -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔗 Next Phase Handoff
Copy all `<!-- BEGIN P3_PROFILE -->` blocks along with the `P1_HANDOFF` block into [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md).
