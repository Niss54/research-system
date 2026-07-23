# P3 — Research ×10
> **Phase 3 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

For each of the 10 competitors found in P2, you run one deep-dive research session. This phase uncovers what each tool actually does, how users feel about it, and — most importantly — what it completely fails to do.

**Goal:** 10 detailed competitor profiles, each ending with a "THIS TOOL DOES NOT" summary line that feeds directly into P4 gap analysis.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Needs to pull live reviews, pricing, and company data |
| 🔬 Deep Research Mode | **ON** | Automatically runs multiple searches from a single prompt — ideal for this task |
| 🧠 Extended Thinking | Optional | Can help with the gaps section if you want deeper analysis |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar
> - Deep Research → available in Claude Pro; activates multi-step search automatically

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Run this prompt **once per competitor** — 10 times total. Replace the name, URL, and problem space each time.

```
COMPETITIVE DEEP DIVE: [SOLUTION NAME]
Website: [URL]
Context: Building a solution for [PROBLEM SPACE]. This is competitor research.

Research this product thoroughly. Search aggressively before answering.

── 1. PRODUCT PROFILE ─────────────────────────────────────
- What exactly does it do? (step-by-step user journey)
- Core use case it's built for
- How it positions itself — what's their main pitch

── 2. COMPANY INTEL ───────────────────────────────────────
- Founded: when and by whom?
- Funding: check Crunchbase and LinkedIn
- Estimated users or revenue: search "[name] revenue" or check SimilarWeb
- Team size: LinkedIn company page

── 3. PRICING ─────────────────────────────────────────────
- All pricing tiers (Free / Starter / Pro / Enterprise)
- What's locked behind paywall
- Any pricing complaints in reviews?

── 4. WHAT USERS LOVE ★★★★★ ─────────────────────────────
Search: "[name] review" on G2, Trustpilot, Reddit, App Store
- Top 3 things users genuinely praise
- Why do users stay or recommend it?

── 5. WHAT USERS HATE ★☆☆☆☆ ─────────────────────────────
Search: "[name] problems", "[name] alternative", "[name] review negative"
Also check their Twitter/X and any public feedback board
- Top 5 complaints
- Most-requested missing features
- Why do users switch away?

── 6. CRITICAL GAPS ← MOST IMPORTANT SECTION ────────────
- What does it COMPLETELY fail to do?
- Which user segment does it NOT serve well?
- What workarounds do users create INSIDE this product?
  (e.g. "users export to Excel because tool can't do X" = unmet need)
- What is the #1 feature users wish it had?

Output: Full profile. Give 40% of the response to section 6 (gaps only).
End with exactly this line:
THIS TOOL DOES NOT: [comma-separated list of all gaps found]
```

---

## 🗂️ How to Use

1. **Open your P2 table** — you'll work through each row one by one
2. **Start a fresh Claude session per competitor** — don't chain multiple competitors in one session; context quality drops
3. **Fill in the name, URL, and problem space** for each run
4. **Do not skip Section 6** — this is the most valuable section and feeds directly into P4
5. **Save each output separately** — label them Competitor 1, Competitor 2, etc.
6. **Make sure every profile ends with** `THIS TOOL DOES NOT:` — you'll need this line in P4

---

## ✅ Expected Output

For each of the 10 competitors, Claude should return:

- **Full product profile** — what it does, how it works, who it's for
- **Company snapshot** — founding date, funding, team size, estimated users
- **Pricing breakdown** — all tiers and what's behind the paywall
- **Top 3 things users love** — sourced from real reviews
- **Top 5 complaints** — with evidence from G2, Reddit, App Store, etc.
- **Critical gaps section** — 40% of the response dedicated to what it fails to do
- **"THIS TOOL DOES NOT" line** — comma-separated list of all gaps found

---

## 💡 Pro Tip

> **Research 2–3 competitors per session** to keep your context window intact and your workflow efficient. Always make sure Claude ends each profile with the `THIS TOOL DOES NOT` line — this becomes essential raw material when you run the gap analysis in P4.

Also: pay close attention to **workarounds users create inside the product** (e.g., "I export to CSV and process in Excel because the tool can't filter by X"). These in-product workarounds are your clearest signal of unmet needs.

---

## ⏱️ Time Estimate

**~2–3 hours total** — approximately 15–20 minutes per competitor with Deep Research mode active. Plan for a full work session or split across two days.

---

## ➡️ Next Step

Once all 10 profiles are complete → Go to [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md)

Paste **all 10 profiles together** into the P4 prompt in a single session. Do not run P4 with partial profiles — the feature matrix requires all 10 to be meaningful.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
