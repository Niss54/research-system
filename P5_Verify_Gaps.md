# P5 — Verify Gaps
> **Phase 5 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

The gaps identified in P4 came from analyzing existing competitors — but the analysis isn't complete until you confirm that no one is already filling those gaps. This phase runs an exhaustive search to verify each gap is genuinely open, partially open, or already being addressed.

**Goal:** A verified list of real, open market gaps — with only confirmed (✅) and partial (⚠️) gaps moving forward to the final report.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Must search broadly across many platforms to verify each gap |
| 🔬 Deep Research Mode | **ON** | Runs multiple searches automatically — ideal for exhaustive verification |
| 🧠 Extended Thinking | Optional | Useful if gaps are complex or overlapping |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar
> - Deep Research → available in Claude Pro; activates multi-step search automatically

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, paste your Top 5 gaps from P4, and run with Web Search and Deep Research both ON.

```
I've found these potential market gaps in [PROBLEM SPACE]:

GAP 1: [Name] — [1–2 sentence description of what's missing]
GAP 2: [Name] — [description]
GAP 3: [Name] — [description]
GAP 4: [Name] — [description]
GAP 5: [Name] — [description]

Mission: VERIFY each gap. Is it truly unfilled? Search hard before concluding.

For EACH gap, run ALL of these searches:
□ Google: "[gap keyword] software OR tool OR app"
□ Google: "[gap keyword] solution OR platform"
□ Product Hunt: site:producthunt.com "[gap keyword]"
□ Indie Hackers: site:indiehackers.com "[gap keyword]"
□ GitHub: "[gap keyword]" — any open-source solutions?
□ Y Combinator: ycombinator.com/companies "[gap keyword]"
□ BetaList / Uneed.app — any recent launches in this space?
□ News: "[gap keyword] startup" on TechCrunch or VentureBeat
□ LinkedIn: "[gap keyword] founder" — anyone building this stealth?

Verdict for each gap:
✅ CONFIRMED GAP — Nothing found after exhaustive search. Truly open.
⚠️ PARTIAL GAP — 1–2 weak/early solutions exist but serious gap remains.
   → Name the weak solution + explain exactly why it's insufficient.
❌ FALSE GAP — Good solution already exists.
   → Name it + URL. Remove from the list.

For each CONFIRMED or PARTIAL gap, also answer:
Q1: Why hasn't anyone built this? (Technical? Regulatory? Niche too small?)
Q2: What changed recently that makes this possible or needed NOW?
Q3: What would a minimal version look like? (3–5 bullet points)

Output: Verified gap report. Only ✅ and ⚠️ gaps move to the final report.
```

---

## 🗂️ How to Use

1. **Paste the exact gap descriptions from P4** — use the names and descriptions Claude gave you, not your own paraphrasing
2. **Let Claude search all 9 platforms per gap** — don't shorten the search list; thoroughness is the point
3. **Watch for stealth builders on LinkedIn** — some of the best competition is pre-launch
4. **Keep every gap's verdict separate** — don't let Claude combine or merge gaps during verification
5. **Only carry ✅ and ⚠️ gaps into P6** — remove false gaps from your working list

---

## ✅ Expected Output

Claude should return:

- **A verdict for each gap** — CONFIRMED / PARTIAL / FALSE — with evidence
- **For false gaps:** the solution name and URL that already fills the gap
- **For confirmed and partial gaps:**
  - Why the gap exists (technical, regulatory, market size?)
  - What recently changed to make it addressable now
  - What a minimal version would look like (3–5 features)
- **A clean final list** of only ✅ and ⚠️ gaps to carry into P6

---

## 💡 Pro Tip

> **False gaps are not bad news.** If someone already tried to fill the gap and failed, that's actually validation that the need is real. Search their negative reviews immediately — poor execution of a real need is one of the best opportunities to enter a market.

**Partial gap + bad reviews = massive opportunity to do it 10× better.**

Also: a gap where the only existing solution is a GitHub repo with 12 stars is effectively a confirmed gap. "Technically exists" doesn't mean "adequately served."

---

## ⏱️ Time Estimate

**~45 minutes** — the most search-intensive phase. Claude runs 9 searches per gap × 5 gaps = up to 45 search operations. Deep Research mode handles this automatically.

---

## ➡️ Next Step

Take your verified gaps (✅ and ⚠️ only) → Go to [`P6_Final_Report.md`](./P6_Final_Report.md)

Compile **all outputs from P1 through P5** — you'll paste everything into P6 to generate the final investor-ready report.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
