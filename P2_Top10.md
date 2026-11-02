# P2 — Top 10 (v2 Grounded Edition)
> **Phase 2 of 7** · Competitive Landscape & Adoption Audit · Created by [Nisha](https://nissh.info)

> 💡 **Execution Modes:**
> 1. **🤖 Mode 1 (Autonomous Local CLI / UI):** Run `python -m v2.cli run --from-phase 2` or use the web interface. Competitor websites are pinged via live HTTP checks and adoption signals are logged.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the `<!-- BEGIN P1_HANDOFF -->` block from Phase 1 into the prompt below. Feed resulting `<!-- BEGIN P2_HANDOFF -->` into [`P3_Research_x10.md`](./P3_Research_x10.md).

---

## 🎯 What This Phase Does

Discovers the real solutions customers use today — direct competitors, adjacent suites, and manual workarounds.
In v2, you do NOT rank tools by surface-level Google search ranking:
- **Verified Adoption Signals**: Look for real active user counts, public disclosures (LinkedIn headcount, Crunchbase/MCA funding, G2 review counts), and live pricing snapshots.
- **Live URL Verification**: Confirm competitor websites are active and accessible.
- **Defunct Player Audit**: Check if any competitors shut down recently (often reveals unit-economic death traps or unmonetizable markets).

---

## ⚙️ Tools Required

| Tool | Status | Why |
|---|---|---|
| 🔍 Live Web Search | **MANDATORY** | Query Product Hunt, G2, AlternativeTo, GitHub, and pricing pages |
| 🌐 Live URL Pinger | **ACTIVE** | Verify websites respond with HTTP 200 and aren't 404s |
| 🧠 Extended Reasoning | **ON** | Cross-tool comparison and categorization |

---

## 📋 Copy-to-Paste Prompt

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 1:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE YOUR ENTIRE P1_HANDOFF BLOCK HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: COMPETITIVE LANDSCAPE & ADOPTION AUDIT (TOP 10 SOLUTIONS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a forensic market intelligence researcher. Based on the validated problem space and pain signals from Phase 1, audit the TOP 10 solutions in the market.

REQUIREMENTS:
1. Balanced Distribution:
   - Direct Competitors: 4-5 tools solving the core problem
   - Indirect / Adjacent Suites: 3-4 tools solving a broader workflow
   - Manual Workarounds: 1-2 manual DIY patterns (Notion + Stripe, Zapier + Google Sheets)
2. Adoption Grounding:
   - Do NOT just rank by SEO listicles.
   - For each tool, find concrete evidence of adoption (approximate review count on G2/Capterra, estimated user base, or funding status).
   - Capture current 2026 pricing tiers (Free, Starter, Pro).
3. Dead Tool Warning: Note if any notable player in this niche died or pivoted.

OUTPUT FORMAT (MUST INCLUDE EXACT HANDOFF BLOCK):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LANDSCAPE OVERVIEW:
[Provide 2-3 paragraphs examining market maturity, consolidation patterns, and pricing trends]

<!-- BEGIN P2_HANDOFF -->
PROBLEM_SPACE: [Restated from P1]
TARGET_AUDIENCE: [From P1]

TOP_10_TABLE:
| # | Name | Live URL | Type (Direct/Indirect/Workaround) | Pricing Snapshot | Adoption Evidence (Reviews/Users) | 3 Core Capabilities | Primary Failure / Reason Users Leave |
|---|------|----------|-----------------------------------|------------------|------------------------------------|---------------------|--------------------------------------|
| 1 | [Name 1] | [URL 1] | Direct | $XX/mo | 120+ G2 reviews, ~$2M ARR | [Feat 1, Feat 2, Feat 3] | [Limitation] |
...
| 10| [Name 10]| [URL 10] | Workaround | Free/DIY | Widespread Reddit mentions | [Feat 1, Feat 2, Feat 3] | [Limitation] |

COMPETITORS_FOR_P3:
1. Name: [Tool 1] | URL: [URL 1] | Type: [Direct] | Focus: [Focus Area] | Pricing: [Pricing]
2. Name: [Tool 2] | URL: [URL 2] | Type: [Direct] | Focus: [Focus Area] | Pricing: [Pricing]
...
10. Name: [Tool 10] | URL: [URL 10] | Type: [Workaround] | Focus: [Focus Area] | Pricing: [Pricing]
<!-- END P2_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🔗 Next Phase Handoff
Copy the `<!-- BEGIN P2_HANDOFF -->` block into [`P3_Research_x10.md`](./P3_Research_x10.md).
