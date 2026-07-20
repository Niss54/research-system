# P5 — Verify Gaps
> **Phase 5 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

P4 mein jo gaps mile hain unhe ab confirm karo. Koi stealth startup toh nahi build kar raha? Koi open-source project already exists? Koi YC company recently funded toh nahi? Yeh phase last sanity check hai before you commit.

**Goal:** Confirmed / Partial / False verdict on each of the top 5 gaps — with evidence.

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Exhaustive search across 9+ platforms |
| 🔬 Deep Research Mode | **ON** | Multiple parallel searches needed per gap |
| 🧠 Extended Thinking | OFF | Discovery task, not synthesis |

> **How to enable in Claude.ai:**
> - Web Search → top bar search icon
> - Deep Research → model selector mein "Deep research" option

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** `[PROBLEM SPACE]` aur Top 5 gaps P4 se fill karo. Descriptions mein sirf 1–2 sentence likhna hai per gap — zyada nahi.

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

1. **P4 se Top 5 gaps copy karo** — naam aur ek line description per gap
2. **Problem space clear karo** — ek short phrase, e.g., "freelance client management" or "B2B invoice tracking"
3. **Deep Research + Web Search dono ON** — Deep research automatically multiple searches karega
4. **Claude bahut searches karega** — 40–50+ search queries normal hai is phase mein
5. **Verdicts carefully padho** — specifically FALSE GAP results
6. **Only ✅ and ⚠️ gaps aage jaayenge** — FALSE GAPs hata do list se

### Verdicts ko Interpret Karna

| Verdict | What it means | What to do |
|---------|---------------|-----------|
| ✅ CONFIRMED GAP | Nobody's building this | Include in P6 — yeh tera main opportunity hai |
| ⚠️ PARTIAL GAP | Someone is but doing it badly | Research their negative reviews immediately |
| ❌ FALSE GAP | Good solution already exists | Drop it — pivot to other gaps |

---

## ✅ Expected Output

Claude should return for each gap:

- **Verdict with evidence** — links to what was or wasn't found
- **For CONFIRMED:** Why gap exists + what changed recently + minimal version outline
- **For PARTIAL:** Name of weak solution + exact reason it's insufficient
- **For FALSE:** Competitor name + URL — remove this gap

**Example verdict:**
```
GAP 3: Mobile-first client portal for freelancers

VERDICT: ⚠️ PARTIAL GAP

Found: "Clientjoy" (clientjoy.io) launched 2021 — mobile app exists but 
has 2.1★ on Play Store, constant sync issues, no offline mode.

Why it's insufficient: App crashes on Android 13+, UI is not adapted for 
mobile-first use — it's a desktop web app with a wrapper.

Q1: Why hasn't anyone built this properly? Mobile-first requires 
separate codebase — most solo founders build web-first.
Q2: What changed? 60% of freelancers in SEA now primarily work on mobile.
Q3: Minimal version:
  • Native Android/iOS app (not webview)
  • Client approval flows with push notifications
  • Invoice creation from phone in < 2 min
  • Offline mode for proposals
  • WhatsApp integration for sharing
```

---

## 💡 Pro Tip

> **False gaps are NOT bad news** — matlab kisi ne idea validate kiya but poorly execute kiya. Unke negative reviews search karo turant. Partial gap + bad reviews = massive opportunity to do it 10× better.

**Ek aur bonus search add karo** for any ⚠️ PARTIAL gaps:

```
Search: "[weak solution name] negative reviews" on Reddit and G2
Search: "[weak solution name] alternative" — see who's searching for escape
```

Inke negative reviews = exact feature list tujhe build karna chahiye.

---

## ⏱️ Time Estimate

**~45 minutes** — Deep research per gap takes 8–10 min. 5 gaps × ~9 min = 45 min. Claude is doing real search work here.

---

## ➡️ Next Step

Take ALL outputs from P1 → P5 → Go to [`P6_Final_Report.md`](./P6_Final_Report.md)

P6 investor-ready report banata hai from everything compiled here. Only ✅ and ⚠️ gaps enter P6.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
