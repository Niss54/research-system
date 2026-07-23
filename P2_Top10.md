# P2 — Top 10
> **Phase 2 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

What solutions already exist in the market? Before building anything, you need a complete picture of the competitive landscape — not just the obvious big names, but niche tools, manual workarounds, and everything in between.

**Goal:** A clean table of 10 existing solutions that serve your problem space, ready to feed into P3 deep research.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Must search across multiple platforms to find all relevant solutions |
| 🧠 Extended Thinking | OFF | Not needed here — this is a discovery task, not synthesis |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, replace the placeholder with your validated problem from P1, and paste it into Claude.

```
Problem: [PASTE YOUR VALIDATED PROBLEM FROM P1 — include the P1 verdict here]

Find TOP 10 solutions that exist for this problem. Include a mix of:
- Direct competitors (solve the exact same problem)
- Indirect competitors (solve it partially or differently)
- Manual workarounds (Excel sheets, Notion templates, hiring agencies, DIY)

Search on ALL of these platforms:
□ Product Hunt → search "[problem keyword]"
□ G2.com → browse categories for "[problem space]"
□ Capterra → search "[keyword] software"
□ AlternativeTo.net → search "[keyword]"
□ Reddit → "[keyword] recommendations OR what do you use for"
□ App Store / Play Store → "[keyword]"
□ Google → "best [keyword] tools 2024 2025"
□ GitHub → "[keyword]" for open-source options

For each solution, capture this exact table:

| # | Name | URL | Type | Pricing | Target user | 3 key features |
|---|------|-----|------|---------|-------------|----------------|

Rules:
✓ Include at least 2 non-obvious or niche solutions (not just big names)
✓ Include 1–2 manual workarounds if people use spreadsheets or processes
✓ Note if any major solution shut down recently — that's a market signal
✓ Rank by market presence (most used / most recommended first)

Output: Clean table + one-line summary of what makes each solution unique.
```

---

## 🗂️ How to Use

1. **Paste your P1 verdict** — include the problem statement and the GO / MAYBE verdict from P1
2. **Let Claude search broadly** — don't guide it toward tools you already know; let it discover
3. **Don't stop at 7 or 8** — push for all 10, including at least one manual workaround
4. **Save the full table** — you'll run P3 once per row in this table
5. **Note any recently shut-down tools** — those are strong market signals worth investigating

---

## ✅ Expected Output

Claude should return:

- **A table of 10 solutions** — with URL, pricing, target user, and key features for each
- **A healthy mix** — major players, niche tools, and at least one manual workaround
- **One-line summary per solution** — what makes it unique or how it differs
- **Foundation for P3** — you'll use each row as input for one P3 research session

---

## 💡 Pro Tip

> **Manual workarounds are gold.** If people are building Excel sheets or Notion templates to solve this problem, that's a HUGE gap signal. It means the problem is real but no proper software exists yet — or the existing software is too complex, too expensive, or too generic.

Look specifically for comments like "I just use a spreadsheet for this" or "I hire a VA to manage this" — these are your best opportunities.

---

## ⏱️ Time Estimate

**~15 minutes** — Claude searches multiple platforms and assembles the table. Faster than P1 since no deep reasoning is needed.

---

## ➡️ Next Step

Go to [`P3_Research_x10.md`](./P3_Research_x10.md) — run the P3 prompt **once per solution** from your Top 10 table.

You'll run P3 ten times total — one session per competitor.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
