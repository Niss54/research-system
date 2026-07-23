# P1 — Validate
> **Phase 1 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

Is the problem real, or does it just feel real? Don't build a startup on assumptions. In this phase, you find real-world evidence — Reddit threads, forum complaints, reviews, and surveys — and decide whether to move forward or pivot.

**Goal:** Get a GO / MAYBE / NO-GO verdict backed by hard evidence before investing any more time.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Real evidence requires live search — without it, this prompt is half as effective |
| 🧠 Extended Thinking | **ON** | Deep reasoning for honest scoring, not surface-level validation |

> **How to enable in Claude.ai:**
> - Web Search → toggle via the search icon in the top bar
> - Extended Thinking → model selector → select "Extended thinking"

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Copy the full prompt below, replace `[WRITE YOUR PROBLEM HERE IN 2–3 LINES]` with your actual problem statement, and paste it into Claude.

```
Problem statement: [WRITE YOUR PROBLEM HERE IN 2–3 LINES]

Act as a startup problem validator. Validate if this is a REAL problem worth solving.

Use web search to find hard evidence:
□ Search "reddit [problem keyword] struggling OR frustrated OR annoying"
□ Search "[problem keyword] complaints forum OR community"
□ Search "how to solve [problem keyword]" — see demand for solutions
□ Search "[problem keyword] pain points survey OR report OR statistics"
□ Check App Store / Play Store reviews mentioning this problem

Evaluate on exactly 3 dimensions:

1. FREQUENCY — How often do people face this?
   Scale: Daily / Weekly / Monthly / Rarely
   Evidence: [what you found from web search]

2. SEVERITY — How much does it hurt? (1–10)
   1–3 = minor inconvenience | 4–6 = real friction | 7–10 = they'll pay to fix this
   Evidence: [real complaints or data found]

3. WILLINGNESS TO PAY — Do people already pay for partial solutions?
   Look for: paid apps, freelancers hired, courses bought for this
   Evidence: [what you found]

SCORING:
• Frequency Daily/Weekly + Severity 7+ + WTP Yes → GO ✅
• 2 out of 3 strong → MAYBE ⚠️ — validate with real users before next step
• 1 out of 3 strong → NO-GO ❌ — rephrase problem or pivot

Output format:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROBLEM: [clearly restated in one line]
FREQUENCY: [Daily/Weekly/Monthly/Rarely + evidence]
SEVERITY: [N/10 + evidence]
WILLINGNESS TO PAY: [Yes/No + evidence]
KEY SOURCES: [top 3–5 links found]
VERDICT: GO ✅ / MAYBE ⚠️ / NO-GO ❌ + 2-line reasoning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🗂️ How to Use

1. **Write your problem clearly** — avoid vague statements. "People don't like their jobs" → BAD. "Freelance designers in India can't track client revision cycles without losing scope" → GOOD
2. **Keep the problem statement to 2–3 lines** — one sentence isn't enough; an essay isn't needed either
3. **Paste the prompt into Claude** — make sure both Web Search and Extended Thinking are ON
4. **Wait for the full output** — Claude may take a while on this step; don't interrupt
5. **Note the verdict** — GO / MAYBE / NO-GO? You'll need this for P2

---

## ✅ Expected Output

Claude should return:

- **Validation verdict** — Strong / Moderate / Weak with reasoning
- **3-dimension scores** — Frequency, Severity, Willingness to Pay with real evidence
- **3–5 source links** — actual Reddit threads, forum posts, or surveys found via web search
- **Clear GO / MAYBE / NO-GO verdict** with 2-line reasoning

**Example of a good output:**
```
PROBLEM: Freelancers have no simple way to track revision cycles per client
FREQUENCY: Daily — multiple Reddit posts show this is a constant complaint
SEVERITY: 7/10 — lost revenue due to scope creep mentioned in 40+ G2 reviews
WILLINGNESS TO PAY: Yes — 3 paid tools ($15–$40/mo) exist but have poor UX
KEY SOURCES: reddit.com/r/freelance/…, g2.com/…, producthunt.com/…
VERDICT: GO ✅ — High frequency daily pain + users already paying = real opportunity
```

---

## 💡 Pro Tip

> **If you get a NO-GO, stop here.** Rephrase the problem — define it for a specific user and try again. If it's still weak after 3 rephrases, the problem genuinely doesn't exist at scale or is too niche to pursue.

**Got a MAYBE?** → That's acceptable. Move to P2, but make sure you talk to at least 5 real users in Week 2 before building anything.

---

## ⏱️ Time Estimate

**~20 minutes** — Claude takes 10–15 minutes with web search enabled. You can use 5 minutes to refine your problem statement before pasting.

---

## ➡️ Next Step

**If GO ✅ or MAYBE ⚠️** → Go to [`P2_Top10.md`](./P2_Top10.md) — paste your P1 verdict there.

**If NO-GO ❌** → Rephrase the problem. Don't move to P2 without a GO or MAYBE — the entire 4-hour cycle will be wasted.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
