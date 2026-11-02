# Phase 5: Adversarial Gap Verification (9-Platform Sweep)

## Search Coverage & Synonym Log
- Synonyms Tested: `"deceased estate claim software India"`, `"asset transfer after death service"`, `"succession certificate online assistance"`, `"bereavement notification service India"`, `"settled estate deceased account closure"`.
- Platforms Searched: Google, Product Hunt, GitHub, YC Directory, Tracxn, MCA Company Records, SEBI Filings.

## Verification Findings
- **Is this a clean, virgin market gap?** **NO.** Yellow SMART is actively operating in this exact space in India.
- **Verdict on Gap:** **PARTIAL GAP ⚠️** (Yellow exists, but operates primarily as a high-touch agency rather than self-serve automation).

<!-- BEGIN P5_HANDOFF -->
PROBLEM_SPACE: Deceased Estate Settlement & Cross-Institution Asset Transfer
TARGET_AUDIENCE: Surviving heirs and estate executors in India

VERIFIED_GAPS:
- GAP 1: Cross-Institution Estate Settlement Platform
  VERDICT: PARTIAL ⚠️ (Active direct competitor Yellow SMART exists in India; Settld exists in UK)
  SYNONYMS_SEARCHED: ["deceased claim service India", "bereavement asset transfer", "succession certificate assistance"]
  COUNTEREXAMPLES_DISCOVERED: Yellow SMART (getyellow.in) has direct post-demise offerings.
  EVIDENCE_AUDIT: Yellow provides on-ground assistance for bank, demat, and property transfers; market is NOT empty.
  WHY_UNBUILT_AS_PURE_SOFTWARE: Indian banks require physical signatures, indemnity stamp paper, and branch manager discretion. Pure digital-only transmission cannot bypass physical verification today.
  WHY_NOW: SEBI's September 2025 circular mandates smoother nominee-to-heir transmission; RBI UDGAM portal creates public awareness of unclaimed inheritance.
  MINIMAL_MVP_FEATURES:
  - Smart claim dossier compiler (pre-fills SBI, HDFC, ICICI, Zerodha deceased forms)
  - Legal status triage (Will vs No Will, Nominee vs Non-Nominee, Dispute vs Amicable)
  - Document checklist generator with notarization and stamp paper guidance
  - Professional escalation marketplace (curated CAs and estate lawyers)

RECOMMENDED_WEDGE:
PRIMARY_OPPORTUNITY: Cross-Institution Settlement Dossier Generator (Hybrid SaaS + Legal Escalation)
CORE_VALUE_PROP: "The compassionate estate settlement copilot. One place to claim and transfer all family assets without paying thousands to touts."
WHY_NOW_CATALYST: SEBI and RBI regulatory mandates for standardized deceased claim settlement + growing awareness of digital asset discovery.
MVP_BUILD_SCOPE:
- Deceased asset inventory builder
- 5 Major Bank/Demat claim packet generator
- Status tracker dashboard
<!-- END P5_HANDOFF -->
