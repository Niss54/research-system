# P1 — Validate (v2 Grounded Edition)
> **Phase 1 of 7** · Startup Problem Validation & Evidence Ledger · Created by [Nisha](https://nissh.info)

> 💡 **Execution Modes:**
> 1. **🤖 Mode 1 (Autonomous Local CLI / UI):** Run `python -m v2.cli run --idea "..."` or launch `python server.py`. It uses live search tools, captures screenshots into `evidence/screenshots/`, and compiles your verified dossier.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT / Gemini):** Copy the prompt below into your LLM (turn Web Search ON). When completed, copy the `<!-- BEGIN P1_HANDOFF -->` block into [`P2_Top10.md`](./P2_Top10.md).

---

## 🎯 What This Phase Does

Separates genuine customer agony from founder wishful thinking. In v2, you do NOT rely on simulated memory or generic Reddit summaries:
- **Mandatory Evidence Ledger**: Log every claim with exact quoted passages, source tiers, and publication dates.
- **Multi-Source Validation**: Cross-reference user complaints with newspaper reports, industry surveys, and commercial payment behavior.
- **Local Evidence Vaulting**: Take real browser screenshots and HTML snapshots into `evidence/` to prove market demand.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|---|---|---|
| 🔍 Live Web Search | **MANDATORY** | Query Reddit, Google News, industry reports, and customer review portals |
| 📸 Evidence Capture | **ACTIVE** | Archive real URLs, quotes, and screenshots in local `evidence/` |
| 🧠 Extended Reasoning | **ON** | Objective, adversarial evaluation without flattery |

---

## 📋 Copy-to-Paste Prompt

```text
Problem statement: [WRITE YOUR PROBLEM HERE IN 2–3 LINES]
Target audience: [e.g., Freelance web designers, SMB accountants, DevOps engineers]
Target geography: [e.g., India, Southeast Asia, Global Remote]

Act as an adversarial, evidence-driven startup validator inspired by Hyperresearch and BettaFish.
Validate if this problem represents an urgent, unserved pain with verified willingness-to-pay (WTP).

EXECUTE MANDATORY SEARCH INVESTIGATION:
1. Community Pain: Search "reddit [problem keyword] (frustrated OR terrible OR broken OR lost hours)"
2. Financial Loss: Search "[problem keyword] (financial loss OR unbilled hours OR revenue leak OR cost)"
3. Commercial Workarounds: Search "how to solve [problem keyword] template OR spreadsheet OR consulting"
4. Industry / Press Coverage: Search "[problem keyword] market report OR news survey OR statistics"

EVALUATE 3 CRITICAL VECTORS:
1. FREQUENCY: Daily (80%+ projects) / Weekly / Monthly / Rarely
2. SEVERITY (1-10): Quantifiable financial or hour drain (1-3 minor friction, 4-6 irritation, 7-10 urgent bleed)
3. WILLINGNESS-TO-PAY (WTP): Concrete proof of payment (existing subscriptions, hired virtual assistants, paid Notion kits)

OUTPUT FORMAT (MUST INCLUDE EXACT HANDOFF BLOCK):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVIDENCE AUDIT & METHODOLOGY:
[Provide 2-3 paragraphs examining market signals, news statistics, and actual user complaints with citations]

<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: [Normalized, professional English restatement]
TARGET_AUDIENCE: [Specific Ideal Customer Profile (ICP)]
TARGET_GEOGRAPHY: [Geographic boundary]
FREQUENCY: [Daily / Weekly / Monthly / Rarely]
FREQUENCY_EVIDENCE: [Exact citation of frequency]
SEVERITY: [N/10]
SEVERITY_EVIDENCE: [Financial or time impact with numbers]
WILLINGNESS_TO_PAY: [Yes / Partial / No]
WTP_EVIDENCE: [Real products or services users currently pay for]

EVIDENCE_LEDGER:
- CLAIM: [Core pain claim 1]
  SOURCE_URL: [Active URL]
  SOURCE_TIER: [Primary / Secondary / Community]
  EXACT_PASSAGE: "[Exact quote from forum or article]"
  VERIFICATION: [VERIFIED / PARTIAL / UNVERIFIED]
  CONFIDENCE: [High / Medium / Low]
  LIMITATION: [What this source does NOT prove]

- CLAIM: [Core pain claim 2]
  SOURCE_URL: [Active URL]
  SOURCE_TIER: [Primary / Secondary / Community]
  EXACT_PASSAGE: "[Exact quote from forum or article]"
  VERIFICATION: [VERIFIED / PARTIAL / UNVERIFIED]
  CONFIDENCE: [High / Medium / Low]
  LIMITATION: [What this source does NOT prove]

VERDICT: [GO ✅ / MAYBE ⚠️ / NO-GO ❌]
VERDICT_REASONING: [2-line justification]
KEY_PAIN_SIGNALS:
- [Real complaint signal 1]
- [Real complaint signal 2]
- [Real complaint signal 3]
<!-- END P1_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔗 Next Phase Handoff
After generating this output:
1. Verify source URLs are reachable (HTTP 200).
2. Take screenshots of primary articles and store in `evidence/screenshots/`.
3. Copy the `<!-- BEGIN P1_HANDOFF -->` block into [`P2_Top10.md`](./P2_Top10.md).
