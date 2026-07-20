# P2 — Top 10
> **Phase 2 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

Market mein pehle se kya solutions hain? Best 10 competitors identify karo — direct, indirect, aur manual workarounds sab mila ke. Yeh phase P3 ke liye raw material hai. Jitna accurate yahan, utna deeper research aage.

**Goal:** Clean table of 10 solutions — name, URL, pricing, target user, 3 key features.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Competitors dhundhna hai across multiple platforms |
| 🧠 Extended Thinking | OFF | Straightforward discovery task — normal mode enough hai |

> **How to enable in Claude.ai:**
> - Web Search → top bar search icon se toggle karo

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** `[VALIDATED PROBLEM FROM P1 — paste P1 verdict here]` ki jagah apna P1 output paste karo.

```
Problem: [VALIDATED PROBLEM FROM P1 — paste P1 verdict here]

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

1. **P1 output paste karo** — poora verdict aur evidence paste karo prompt mein
2. **Web Search ON rakho** — Claude multiple sites search karega ek saath
3. **Table review karo** carefully — koi obvious player miss hua toh manually add karo
4. **Type column check karo** — Direct / Indirect / Manual Workaround — teeno categories mein kuch hona chahiye
5. **Yeh list save karo** — P3 mein har ek competitor ke liye ek deep dive session karna hai

---

## ✅ Expected Output

Claude should return:

- **10-row table** with Name, URL, Type, Pricing, Target User, 3 Key Features
- **Mix of types** — at least 2 direct competitors, 1–2 indirect, 1–2 manual workarounds
- **One-line unique angle** per solution — what makes each one different
- **Market signals** — koi band hua tool? koi recent funding? mention hona chahiye

**Example row format:**
```
| 3 | Notion + Template | notion.so | Manual Workaround | Free / $8/mo | Freelancers, PMs | Custom fields, DB views, shareable |
```

---

## 💡 Pro Tip

> **Manual workarounds are gold.** Agar log Excel ya Notion bana rahe hain problem solve karne ke liye — yeh HUGE gap signal hai. Matlab problem real hai but ek proper software abhi tak nahi bana.

**Tool band ho gaya recently?** → Even bigger signal. Users are stranded and actively looking for alternatives. Note the shutdown date and search for Reddit threads asking for alternatives.

---

## ⏱️ Time Estimate

**~15 minutes** — Claude 10–12 min leta hai across 8 platforms. Quick hai compared to P3.

---

## ➡️ Next Step

Copy the full P2 table → Go to [`P3_Research_x10.md`](./P3_Research_x10.md)

Yahan listed **10 solutions mein se ek ek ko** P3 prompt se deep research karna hai. Ek session = ek competitor.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
