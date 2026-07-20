# P1 — Validate
> **Phase 1 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

Problem real hai ya sirf tujhe lag raha hai? Assumptions pe startup mat bana. Is phase mein real-world evidence dhundho — Reddit threads, forum complaints, reviews, aur surveys — aur decide karo ki aage badhna chahiye ya pivot.

**Goal:** GO / MAYBE / NO-GO verdict with hard evidence before investing any more time.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Real evidence dhundhna zaroori hai — bina search ke yeh prompt half-effective hai |
| 🧠 Extended Thinking | **ON** | Deep reasoning for honest scoring, not surface-level validation |

> **How to enable in Claude.ai:**
> - Web Search → top bar search icon se toggle karo
> - Extended Thinking → model selector → "Extended thinking" option

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Neeche diya gaya poora prompt copy karo, `[APNA PROBLEM YAHAN 2-3 LINES MEIN LIKHO]` ki jagah apna actual problem likho, aur Claude mein paste karo.

```
Problem statement: [APNA PROBLEM YAHAN 2-3 LINES MEIN LIKHO]

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

1. **Problem likho clearly** — vague mat likho. "People don't like their jobs" → BAD. "Freelance designers in India can't track client revision cycles without losing track of scope" → GOOD
2. **Problem statement 2–3 lines mein** — ek sentence enough nahi hai, essay bhi nahi chahiye
3. **Prompt paste karo** Claude mein — Web Search aur Extended Thinking dono ON rakho
4. **Wait for full output** — Claude kaafi time le sakta hai is step mein, interrupt mat karo
5. **Verdict note karo** — GO / MAYBE / NO-GO? Yeh P2 mein chahiye

---

## ✅ Expected Output

Claude should return:

- **Validation verdict** — Strong / Moderate / Weak + reasoning
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

> **Agar NO-GO aaya toh abhi ruk.** Problem ko rephrase karo — ek specific user ke liye define karo aur dobara try karo. 3 rephrases ke baad bhi weak hai toh problem genuinely nahi hai ya bahut niche hai.

**MAYBE aaya?** → Yeh acceptable hai. P2 mein jaao but Week 2 mein zaroor 5 real users se baat karo before building anything.

---

## ⏱️ Time Estimate

**~20 minutes** — Claude 10–15 min leta hai web search ke saath. Tum 5 min mein problem statement refine kar sakte ho.

---

## ➡️ Next Step

**If GO ✅ or MAYBE ⚠️** → Go to [`P2_Top10.md`](./P2_Top10.md) — P1 verdict paste karo wahan.

**If NO-GO ❌** → Rephrase karo. P2 pe mat jaao without a GO or MAYBE — warna pure 4-hour cycle waste hoga.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
