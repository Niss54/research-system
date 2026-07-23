# 🚀 Problem → Opportunity Playbook

<div align="center">

**A 6-phase AI-powered startup research system — problem se opportunity tak, evidence ke saath.**

![Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange?style=flat-square&logo=anthropic)
![Phases](https://img.shields.io/badge/Phases-6%20Pipeline-blueviolet?style=flat-square)
![Research Time](https://img.shields.io/badge/Research%20Time-4--5%20Hours-green?style=flat-square)
![Language](https://img.shields.io/badge/Language-Hinglish-red?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

> *"Validate pehle, build baad mein. Yeh playbook ensure karta hai ki tu real problem solve kare — assumptions pe nahi."*

</div>

---

## 📌 Project Overview

**Problem → Opportunity Playbook** ek structured, AI-powered research framework hai jo startup founders aur indie hackers ko help karta hai:

- **Validate** karna ki problem real hai ya sirf lag raha hai
- **Map** karna ki market mein pehle se kya solutions hain
- **Identify** karna real gaps jo competitors miss kar rahe hain
- **Build** karna evidence-backed startup opportunity report — investors aur co-founders ke liye ready

Yeh system **Claude AI** ke saath kaam karta hai (web search + extended thinking mode ke saath). Har phase mein ek ready-to-paste prompt hai — bilkul copy karo, Claude mein paste karo, output lao.

---

## 🗂️ File Structure

```
startup-research-playbook/
│
├── README.md                   ← You are here
│
├── phases/
│   ├── P1-validate.md          ← Problem real hai ya nahi?
│   ├── P2-top10.md             ← Market mein kya solutions hain?
│   ├── P3-research-x10.md      ← Har competitor ka deep dive
│   ├── P4-gap-analysis.md      ← Feature matrix + gaps identify karo
│   ├── P5-verify-gaps.md       ← Gaps confirm karo before building
│   └── P6-final-report.md      ← Investor-ready opportunity report
│
└── startup_research_playbook.html  ← Interactive web version (rendered UI)
```

---

## 🔁 The 6-Phase Pipeline

```
P1 Validate  →  P2 Top 10  →  P3 Research ×10  →  P4 Gap Analysis  →  P5 Verify Gaps  →  P6 Final Report
```

| Phase | Name | Goal | Time | Claude Settings |
|-------|------|------|------|-----------------|
| **P1** | Validate | Problem real hai ya sirf feel ho raha? Evidence dhundo. | ~20 min | 🌐 Web Search + 🧠 Extended Thinking |
| **P2** | Top 10 | Market ke best 10 solutions identify karo | ~15 min | 🌐 Web Search |
| **P3** | Research ×10 | Har competitor ka deep dive (10 baar run karo) | ~2–3 hrs | 🌐 Web Search + 🔬 Deep Research |
| **P4** | Gap Analysis | Feature matrix banao, real gaps nikalo | ~30 min | 🧠 Extended Thinking (no search) |
| **P5** | Verify Gaps | Koi aur toh build nahi kar raha? Confirm karo. | ~45 min | 🌐 Web Search + 🔬 Deep Research |
| **P6** | Final Report | Sab kuch ek professional report mein | ~20 min | 🧠 Extended Thinking (no search) |

**Total time: ~4–5 hours for a complete research cycle**

---

## 🚦 How to Use This System

### Step 1 — Apni problem define karo
Pehle apni problem statement 2–3 lines mein likho. Clear aur specific hona zaroori hai.

```
❌ Weak: "Productivity improve karna chahta hoon"
✅ Strong: "Freelance designers ko client invoice tracking bahut mushkil lagta hai —
            woh 3–4 tools use karte hain jo sync nahi karte"
```

### Step 2 — P1 se shuru karo
1. `phases/P1-validate.md` khullo
2. **Claude.ai** ya koi Claude-based tool khullo
3. **Web Search ON** karo (top bar mein toggle)
4. **Extended Thinking ON** karo (model selector mein)
5. Prompt copy karo, apna problem statement fill karo, paste karo

### Step 3 — Output save karo, next phase mein paste karo
> ⚠️ **CRITICAL:** Yeh ek chain hai. Har phase ka output NEXT phase ke prompt mein paste karna hai.  
> Agar step skip kiya toh quality significantly drop hogi.

```
P1 output → paste into P2 prompt
P2 output → paste into P3 prompt (10 baar)
P3 outputs (sab 10) → paste into P4 prompt
P4 output → paste into P5 prompt
P1 + P2 + P3 + P4 + P5 outputs → paste into P6 prompt
```

### Step 4 — Verdict check karo at every phase

| Verdict | Matlab | Action |
|---------|--------|--------|
| ✅ GO | Strong signal — aage badho | Next phase pe jao |
| ⚠️ MAYBE | Mixed signals | Real users se validate karo pehle |
| ❌ NO-GO | Problem weak hai | **RUK JAO** — problem rephrase karo ya pivot karo |

---

## ⚙️ Claude Settings Guide

| Setting | Kab ON karo | Kahan milega |
|---------|-------------|--------------|
| 🌐 **Web Search** | P1, P2, P3, P5 ke liye zaroori | Claude.ai top bar mein search icon |
| 🧠 **Extended Thinking** | P1, P4, P6 ke liye — synthesis tasks | Model selector dropdown |
| 🔬 **Deep Research Mode** | P3 aur P5 ke liye best | Claude Pro features mein |

> **Note:** Bina correct settings ke prompts half-effective kaam karte hain. Settings zaroor check karo har phase se pehle.

---

## 📋 Phase Quick Reference

<details>
<summary><strong>P1 — Validate</strong> (click to expand)</summary>

**Objective:** Problem real hai ya sirf tujhe lag raha hai? Real evidence dhundho pehle.

**What it searches:**
- Reddit complaints aur frustration threads
- App Store / Play Store reviews
- Survey data aur statistics
- Existing solution demand signals

**Expected Output:**
- Validation score: Strong / Moderate / Weak
- 3–5 source links with actual user pain signals
- Clear **GO / MAYBE / NO-GO** verdict with reasoning

**Pro Tip:** Agar NO-GO aaya toh abhi ruk. Problem ko rephrase kar — ek specific user ke liye define karo aur dobara try karo. 3 rephrases ke baad bhi weak hai toh problem genuinely nahi hai ya bahut niche hai.

📄 **Full prompt:** [`phases/P1-validate.md`](phases/P1-validate.md)

</details>

<details>
<summary><strong>P2 — Top 10</strong> (click to expand)</summary>

**Objective:** Market mein pehle se kya solutions hain? Best 10 competitors identify karo.

**Searches across:** Product Hunt, G2, Capterra, AlternativeTo, Reddit, App Store, GitHub

**Expected Output:**
- Table of 10 solutions: URL, pricing, target user, key features
- Mix of: big players + niche tools + manual workarounds
- Foundation for P3 deep research

**Pro Tip:** Manual workarounds are gold. Agar log Excel ya Notion bana rahe hain problem solve karne ke liye — yeh HUGE gap signal hai. Matlab problem real hai but ek proper software abhi tak nahi bana.

📄 **Full prompt:** [`phases/P2-top10.md`](phases/P2-top10.md)

</details>

<details>
<summary><strong>P3 — Research ×10</strong> (click to expand)</summary>

**Objective:** Har competitor ka deep dive — kya cover karta hai, kya nahi. Yeh prompt 10 baar run karo.

**Each profile covers:**
- Product profile + user journey
- Company intel (funding, team, revenue)
- Pricing tiers + complaints
- What users love ★★★★★
- What users hate ★☆☆☆☆
- Critical gaps ← MOST IMPORTANT SECTION

**Expected Output:**
- 10 detailed competitor profiles (one per session)
- "THIS TOOL DOES NOT" summary line per tool
- Raw material for P4 gap analysis

**Pro Tip:** Ek session mein 2–3 competitors research kar le taki context intact rahe. Har research ke end mein "THIS TOOL DOES NOT" wali line zaroor add karao.

📄 **Full prompt:** [`phases/P3-research-x10.md`](phases/P3-research-x10.md)

</details>

<details>
<summary><strong>P4 — Gap Analysis</strong> (click to expand)</summary>

**Objective:** Sab 10 profiles ek saath paste karo — Claude feature matrix banayega aur asli gaps nikaalega.

**Produces:**
- Feature matrix: all 10 solutions × all features found (✓ / ~ / ✗)
- Gap categories: Feature, Quality, Audience, Pricing, Workflow
- Scoring formula: `(User Pain × Market Size) ÷ Build Difficulty`

**Expected Output:**
- Full feature matrix table
- All gaps categorized and scored
- Top 5 ranked opportunities
- #1 recommended gap to focus on

**Pro Tip:** Extended thinking mode zaroor ON karo is step ke liye. Prompt ke end mein add karo: *"Take extra time before responding. Think through every gap carefully before scoring."*

📄 **Full prompt:** [`phases/P4-gap-analysis.md`](phases/P4-gap-analysis.md)

</details>

<details>
<summary><strong>P5 — Verify Gaps</strong> (click to expand)</summary>

**Objective:** Jo gaps mile hain unhe confirm karo — koi aur toh nahi bana raha pehle se?

**Searches:** Google, Product Hunt, Indie Hackers, GitHub, YC Companies, BetaList, TechCrunch, LinkedIn

**Gap Verdicts:**
- ✅ **CONFIRMED GAP** — Nothing found. Truly open.
- ⚠️ **PARTIAL GAP** — 1–2 weak solutions exist but serious gap remains.
- ❌ **FALSE GAP** — Good solution already exists. Remove from list.

**Expected Output:**
- Verified verdict on each gap with evidence
- Why the gap exists and what changed recently
- Minimal version description for confirmed gaps

**Pro Tip:** False gaps are NOT bad news — matlab kisi ne idea validate kiya but poorly execute kiya. Unke negative reviews search karo turant. Partial gap + bad reviews = massive opportunity to do it 10× better.

📄 **Full prompt:** [`phases/P5-verify-gaps.md`](phases/P5-verify-gaps.md)

</details>

<details>
<summary><strong>P6 — Final Report</strong> (click to expand)</summary>

**Objective:** Sab kuch ek jagah. Professional report — co-founders ya investors ko directly dikhao.

**Report Sections:**
1. Executive Summary (GO / NO-GO / PIVOT recommendation)
2. Problem Deep Dive (ICP, workarounds, cost of inaction)
3. Competitive Landscape (market map, what all miss)
4. Your Opportunity (top 3 gaps, revenue potential)
5. Product Direction (MUST BUILD / SHOULD BUILD / SKIP)
6. 30-Day Action Plan (landing page → interviews → MVP → launch)

**Expected Output:**
- Investor-ready startup opportunity report
- Prioritized product roadmap
- 30-day action plan with user interview script

**Pro Tip:** Report aane ke baad seedha share mat karo. Jo claims tujhe doubtful lagein unhe mark kar aur manually verify kar. Claude synthesis well karta hai but numbers aur estimates tujhe personally check karne chahiye.

📄 **Full prompt:** [`phases/P6-final-report.md`](phases/P6-final-report.md)

</details>

---

## 💡 Pro Tips (System-Level)

```
✅ DO
├── Har phase complete karo before moving to next
├── P3 ke liye naya Claude session per competitor use karo
├── P4 mein SARE 10 P3 outputs ek saath paste karo
├── P6 ke baad key claims ko manually fact-check karo
└── P1 pe NO-GO mila? Rephrase karo — 4-5 hrs waste mat karo

❌ DON'T
├── P1 skip mat karo — warna poora cycle waste ho sakta hai
├── Web search settings change mat karo mid-prompt
├── P3 mein multiple competitors ek hi prompt mein mat daalo
├── P6 report ko bina verification ke investors ko mat share karo
└── Claude ke estimates ko gospel truth mat maano — verify karo
```

---

## 🤝 Contributing

Contributions welcome hain! Agar tumhare paas better prompts hain, improvements hain, ya nayi phases ke ideas hain — PR open karo.

### How to Contribute

1. **Fork** this repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/startup-research-playbook.git
   cd startup-research-playbook
   ```

2. **Branch** banao apne feature ke liye
   ```bash
   git checkout -b improve/p3-prompt-v2
   ```

3. **Changes karo** aur test karo Claude ke saath
   - Prompt changes ke liye: actual Claude session mein test karo, pehle
   - Expected output section update karo if output changes
   - Pro tip add/update karo if you have a better one

4. **Commit** karo with a clear message
   ```bash
   git commit -m "feat(P3): add Glassdoor to competitor research search list"
   ```

5. **Push** karo aur **Pull Request** kholo
   ```bash
   git push origin improve/p3-prompt-v2
   ```

### Contribution Ideas

| Type | Examples |
|------|---------|
| 🔧 Prompt improvements | Better search queries, clearer output formats |
| 📊 New gap categories | E.g., geographic gaps, language gaps |
| 🌐 New search sources | New platforms to check in P2/P3/P5 |
| 🌍 Translations | Prompts in full Hindi, English, or other languages |
| 📝 Case studies | Real examples of the system in action |
| 🐛 Bug reports | Prompts that give bad/incomplete output |

### Contribution Guidelines

- **Ek PR mein ek phase** — mixed changes avoid karo
- **Real testing required** — sirf theoretical nahi, actual Claude output include karo in PR description
- **Hinglish preferred** — system ki voice consistent rakho
- Agar naya file add kar rahe ho, file structure section update karo README mein bhi

---

## 📊 Expected Total Output

Ek complete P1→P6 cycle ke baad tumhare paas hoga:

- ✅ **Evidence-backed problem validation** (real data, real links)
- ✅ **Competitive landscape map** (10 solutions, fully profiled)
- ✅ **Feature matrix** (every feature vs. every competitor)
- ✅ **Ranked opportunity list** (gaps scored on pain × market × difficulty)
- ✅ **Verified gaps** (confirmed against exhaustive search)
- ✅ **Investor-ready report** (6 sections, GO/NO-GO decision, 30-day plan)

---

## ⚠️ Important Disclaimers

- Claude AI mein **hallucination** ho sakta hai — especially revenue figures aur user numbers mein. P6 report ke claims manually verify karo important ones ke liye.
- **Market estimates** are rough signals, not authoritative data. TAM/SAM ke liye proper market research reports dekho.
- Yeh system **market research ko accelerate** karta hai — replace nahi karta actual customer conversations. P6 ke 30-day plan mein user interviews MUST hai.

---

## 📄 License

MIT License — freely use karo, modify karo, share karo. Credit doge toh acha lagega 🙏

---

## 🙌 Acknowledgements

Built for the builder who validates first, builds second.  
Inspired by the startup research frameworks of YC, Indie Hackers, and every founder who wasted 6 months building the wrong thing.

---

<div align="center">

**⭐ Agar yeh useful laga toh star karo — dusre founders ko bhi help milegi**

Made with ❤️ for the Indian startup ecosystem

</div>
