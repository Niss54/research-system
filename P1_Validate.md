# P1 — Validate
> **Phase 1 of 7** · Problem → Opportunity Playbook · Created by [Nisha](https://nissh.info)

> 💡 **Two Ways to Run This System:**
> 1. **🤖 Mode 1 (Autonomous Local Engine - Recommended):** Clone the repo, set any API key in `.env`, run `python server.py`, and type your idea in any language (Hindi, Hinglish, English, etc.). All 7 agents run end-to-end automatically and generate your official watermarked PDF report!
> 2. **📋 Mode 2 (Manual Chaining with Claude / ChatGPT / Gemini - Free / No Local Setup):** Copy the prompt below into Claude.ai or ChatGPT (turn Web Search ON). When Claude gives the output, copy the `<!-- BEGIN P1_HANDOFF -->` block (or download/attach the output PDF) and feed it into [`P2_Top10.md`](./P2_Top10.md). Repeat until Phase 7!

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

> **Instructions:** Copy the full prompt below, replace `[WRITE YOUR PROBLEM HERE IN 2–3 LINES]` with your actual problem statement, and paste it into Claude (or run via the interactive UI / CLI).
> 
> 🔗 **Pipeline Connection:** The output of this phase produces a standardized `<!-- BEGIN P1_HANDOFF -->` block that you will paste directly into [`P2_Top10.md`](./P2_Top10.md).

```text
Problem statement: [WRITE YOUR PROBLEM HERE IN 2–3 LINES]
Target audience (optional / rough idea): [e.g. Freelancers, DevOps engineers, Small business owners]

Act as an evidence-driven startup problem validator. Validate if this is a REAL problem worth solving.

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
   Evidence: [real complaints, hours wasted, or financial loss found]

3. WILLINGNESS TO PAY — Do people already pay for partial solutions?
   Look for: paid apps, freelancers hired, courses bought, spreadsheets sold for this
   Evidence: [what you found]

SCORING:
• Frequency Daily/Weekly + Severity 7+ + WTP Yes → GO ✅
• 2 out of 3 strong → MAYBE ⚠️ — validate with real users before next step
• 1 out of 3 strong → NO-GO ❌ — rephrase problem or pivot

Output format (YOU MUST INCLUDE THE EXACT HANDOFF BLOCK BELOW):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVIDENCE SUMMARY:
[Provide 2-3 paragraphs analyzing the evidence found across web search]

<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: [Clearly restated problem in 1–2 sentences]
TARGET_AUDIENCE: [Specific ICP / audience facing this problem]
FREQUENCY: [Daily / Weekly / Monthly / Rarely]
FREQUENCY_EVIDENCE: [Summary of frequency signals from search]
SEVERITY: [N/10]
SEVERITY_EVIDENCE: [Summary of severity and pain signals]
WILLINGNESS_TO_PAY: [Yes / Partial / No]
WTP_EVIDENCE: [Evidence of monetization or paid workarounds]
KEY_SOURCES:
- [Source URL 1] — [Key takeaway]
- [Source URL 2] — [Key takeaway]
- [Source URL 3] — [Key takeaway]
VERDICT: [GO ✅ / MAYBE ⚠️ / NO-GO ❌]
VERDICT_REASONING: [2-line summary of verdict justification]
KEY_PAIN_SIGNALS:
- [Specific real-world complaint 1]
- [Specific real-world complaint 2]
- [Specific real-world complaint 3]
SEARCH_QUERIES_USED:
- [Query 1]
- [Query 2]
<!-- END P1_HANDOFF -->
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
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

## ➡️ Next Step & Data Handoff

**If GO ✅ or MAYBE ⚠️:**
1. Copy the entire `<!-- BEGIN P1_HANDOFF --> ... <!-- END P1_HANDOFF -->` block from your output.
2. Open [`P2_Top10.md`](./P2_Top10.md) and paste it directly into the designated `P1_HANDOFF` slot.
3. Phase 2 will automatically use the validated problem, target audience, and pain signals to find the 10 best competitors.

**If NO-GO ❌:**
> Rephrase the problem or pivot. Don't move to P2 without a GO or MAYBE — otherwise you will spend hours researching a problem people don't care to solve.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*

