# P3 — Research ×10
> **Phase 3 of 7** · Problem → Opportunity Playbook · Created by [Nisha](https://nissh.info)

> 💡 **Two Ways to Run This Phase:**
> 1. **🤖 Mode 1 (Autonomous Local Engine):** Handled automatically when running `python server.py`.
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT):** Paste the competitor list from `<!-- BEGIN P2_HANDOFF -->` into Claude. Run single-competitor or batch prompts. Collect the `<!-- BEGIN P3_PROFILE: ... -->` outputs and paste them into [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md).

---

## 🎯 What This Phase Does

For each of the 10 competitors found in Phase 2, you conduct a deep-dive research investigation. This phase uncovers what each tool actually does, how real users feel about it, and — most importantly — what it completely fails to do.

**Goal:** 10 detailed competitor profiles, each ending with a `THIS TOOL DOES NOT:` summary line that feeds directly into P4 gap analysis.

---

## 📥 Input Contract (From Phase 2)

This phase consumes the competitor list from [`P2_Top10.md`](./P2_Top10.md):
- Target problem space & audience (from `P1_HANDOFF`)
- The 10 competitors identified in `<!-- BEGIN P2_HANDOFF -->` (`COMPETITORS_FOR_P3`)

You can run this phase in two ways:
1. **Single-Competitor Deep Dive (Recommended for Claude.ai manual sessions):** Run the single prompt 10 times (one per competitor) to keep context fresh.
2. **Batch Competitor Research (Recommended for Web App / CLI / Fast Mode):** Research competitors in batches of 3–5 or all 10 together.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Needs to pull live user reviews, pricing pages, and company traction |
| 🔬 Deep Research Mode | **ON** | Automatically runs multi-query searches — essential for uncovering hidden complaints |
| 🧠 Extended Thinking | Optional | Helpful for detecting subtle user workarounds |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar
> - Deep Research → available in Claude Pro; runs multi-step search automatically

---

## 📋 Copy-to-Paste Prompt (Option A: Single Competitor Deep Dive)

> **Instructions:** Run this prompt once per competitor from your P2 list (10 runs total). Fill in the competitor name, URL, and context from Phase 2.

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 2:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPETITOR NAME: [NAME FROM P2]
WEBSITE: [URL FROM P2]
COMPETITOR TYPE: [Direct / Indirect / Workaround]
PROBLEM SPACE & AUDIENCE: [FROM P1 / P2 HANDOFF]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: COMPETITIVE DEEP DIVE & GAP EXTRACTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Act as a forensic startup researcher. Conduct an aggressive, evidence-backed teardown of this product within our problem space. Search deeply across G2, Trustpilot, Capterra, Reddit, GitHub, and review boards before responding.

── 1. PRODUCT PROFILE & USER WORKFLOW ──────────────────────────
- What exactly does it do? (Step-by-step user journey)
- Core use case it was actually built for
- How does it position itself — what is their primary value proposition?

── 2. COMPANY INTEL & TRACTION ────────────────────────────────
- Founded: When and by whom?
- Funding & Stage: Check Crunchbase, LinkedIn, PitchBook
- Estimated scale: Search "[name] revenue", employee count on LinkedIn, or SimilarWeb traffic
- Active development status: When was their latest product update or blog post?

── 3. PRICING & VALUE PACKAGING ───────────────────────────────
- Complete pricing breakdown (Free / Starter / Pro / Enterprise)
- What critical capabilities are locked behind the highest paywall?
- Any common pricing complaints in customer reviews?

── 4. WHAT USERS LOVE ★★★★★ ──────────────────────────────────
Search "[name] review" on G2, Trustpilot, Reddit, App Store:
- Top 3 capabilities users genuinely praise
- Why do existing users stay or recommend it?

── 5. WHAT USERS HATE & COMPLAIN ABOUT ★☆☆☆☆ ─────────────────
Search "[name] complaints", "[name] alternative", "[name] negative review", "[name] bugs reddit":
- Top 5 recurring user complaints
- Most-requested missing features
- Primary reasons users churn or switch away

── 6. CRITICAL GAPS & FAILURES ← MOST IMPORTANT SECTION ──────
- What does this tool COMPLETELY fail to do?
- Which specific user segment is neglected or poorly served?
- What workarounds do users invent INSIDE or BESIDE this product?
  (e.g. "users export to CSV and clean manually in Excel because tool lacks X")
- What is the #1 feature users desperately wish it had?

OUTPUT FORMAT (YOU MUST WRAP YOUR ANSWER IN THE STANDARDIZED PROFILE BLOCK):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<!-- BEGIN P3_PROFILE: [COMPETITOR NAME] -->
COMPETITOR_NAME: [COMPETITOR NAME]
WEBSITE: [URL]
TYPE: [Direct / Indirect / Workaround]

1. PRODUCT PROFILE:
[Detailed summary of product, user journey, and positioning]

2. COMPANY INTEL:
[Founders, funding, employee count, traction estimate]

3. PRICING TIERS:
[All tiers, paywalled features, pricing friction]

4. WHAT USERS LOVE:
- [Praise 1]
- [Praise 2]
- [Praise 3]

5. WHAT USERS HATE:
- [Complaint 1]
- [Complaint 2]
- [Complaint 3]
- [Complaint 4]
- [Complaint 5]

6. CRITICAL GAPS:
- Neglected Segment: [Who suffers most]
- User Workaround: [Manual hack users resort to]
- Missing Core Capability: [What tool completely fails to do]

THIS TOOL DOES NOT: [Comma-separated list of all unmet needs, missing features, and limitations discovered]
<!-- END P3_PROFILE: [COMPETITOR NAME] -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📋 Copy-to-Paste Prompt (Option B: Batch Research Mode)

> **Instructions:** If you want to analyze multiple competitors in a single session, use this prompt with the list from `P2_Top10.md`.

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INPUT FROM PHASE 2:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEM SPACE: [FROM P1 / P2 HANDOFF]
TARGET AUDIENCE: [FROM P1 / P2 HANDOFF]

COMPETITORS TO RESEARCH:
[PASTE ROWS OR COMPETITOR LIST FROM P2_HANDOFF HERE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TASK: BATCH COMPETITIVE PROFILE & GAP EXTRACTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
For EACH competitor listed above, conduct an independent research investigation.
Search web reviews, pricing, Reddit discussions, and complaints.

For EACH competitor, output a separate profile block formatted exactly as:

<!-- BEGIN P3_PROFILE: [COMPETITOR NAME] -->
COMPETITOR_NAME: [NAME]
WEBSITE: [URL]
TYPE: [Direct / Indirect / Workaround]
SUMMARY & POSITIONING: [2-3 sentences]
PRICING TIERS: [Free / Paid tiers + limitations]
WHAT USERS LOVE: [Top 2-3 praises]
WHAT USERS HATE: [Top 3-5 complaints]
CRITICAL GAPS & WORKAROUNDS: [What it fails to do + what manual workarounds users create]
THIS TOOL DOES NOT: [Comma-separated list of all unmet needs and gaps]
<!-- END P3_PROFILE: [COMPETITOR NAME] -->
```

---

## 🗂️ How to Use

1. **Extract your competitor list** from the `<!-- BEGIN P2_HANDOFF -->` block in Phase 2.
2. **Execute research**:
   - In manual mode: run Option A for each competitor in a separate session.
   - In automated / web app mode: use Option B or the interactive competitor tabs.
3. **Verify the ending line**: Every profile MUST include `THIS TOOL DOES NOT:` — this is the critical fuel for Phase 4.
4. **Collect all 10 profiles** — keep the `<!-- BEGIN P3_PROFILE: ... -->` blocks ready.

---

## ✅ Expected Output

For each competitor, you receive a standardized profile block capturing:
- Core product mechanics and positioning
- Pricing tiers and locked features
- Real user sentiment (praises and complaints with evidence)
- In-product workarounds and neglected user segments
- Explicit `THIS TOOL DOES NOT:` summary line

---

## 💡 Pro Tip

> **Look closely at user workarounds.** When a user says: *"I love the tool, but I have to export to Excel every Friday to reconcile X"* — that is a validated, high-ticket startup opportunity waiting to be built.

---

## ⏱️ Time Estimate

- **Manual (10 sessions):** ~2–3 hours total (~15 min per competitor)
- **Batch / Web App / CLI:** ~15–30 minutes total

---

## ➡️ Next Step & Data Handoff

1. Collect all 10 `<!-- BEGIN P3_PROFILE: ... --> ... <!-- END P3_PROFILE -->` blocks.
2. Open [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md).
3. Paste your Phase 1 problem statement and all 10 P3 profiles into the designated slots.
4. Phase 4 will synthesize the feature matrix and score the market gaps.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
