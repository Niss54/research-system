# P3 — Research ×10
> **Phase 3 of 6** · Problem → Opportunity Playbook

---

## 🎯 What This Phase Does

P2 se mili 10 solutions ki list mein se har ek ka deep dive karo. Sirf homepage mat padho — actual user reviews, complaints, missing features, aur workarounds dhundho. Is phase ka output hi P4 gap analysis ka fuel hai.

**This prompt runs 10 times — one per competitor.**

**Goal:** 10 detailed competitor profiles, each ending with "THIS TOOL DOES NOT: [gap list]"

---

## ⚙️ Tools Required

| Tool | Status | Why |
|------|--------|-----|
| 🔍 Web Search | **ON** | Reviews, Reddit, G2, LinkedIn — sab search hoga |
| 🔬 Deep Research Mode | **ON** | Yeh automatically multiple searches karta hai ek prompt se |
| 🧠 Extended Thinking | OFF | Not needed — research task hai, synthesis nahi |

> **How to enable in Claude.ai:**
> - Web Search → top bar search icon
> - Deep Research → model selector mein "Deep research" ya "Research" option milega

---

## 📋 Copy-to-Paste Prompt

> **Instructions:** Yeh prompt **10 baar run karo** — ek baar per competitor. Har baar `[SOLUTION NAME]`, `[URL]`, aur `[PROBLEM SPACE]` replace karo P2 ke data se.

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

### Session Strategy

Ek session mein 2–3 competitors research kar le — context carry hota hai aur Claude better cross-referencing karta hai.

**Recommended batching:**
```
Session A → Competitors 1, 2, 3
Session B → Competitors 4, 5, 6
Session C → Competitors 7, 8, 9, 10
```

### Step-by-Step

1. **P2 table kholo** — pehle competitor ka naam, URL, aur problem space note karo
2. **Prompt mein fill karo** — teen placeholders replace karo: `[SOLUTION NAME]`, `[URL]`, `[PROBLEM SPACE]`
3. **Web Search + Deep Research ON** — dono zaroori hain
4. **Run karo, wait karo** — Deep research mode kaafi time leta hai (2–5 min per competitor)
5. **Output save karo** — Google Doc ya Notion mein paste karo — P4 mein yeh sab ek saath chahiye
6. **"THIS TOOL DOES NOT" line check karo** — yeh zaroor honi chahiye at the end
7. **Repeat for all 10** — ek ek karke

### Saving Your Outputs

Ek document banao `P3_Research_Outputs.txt` ya similar aur har profile paste karo isme:

```
══════════════════════════════════════
COMPETITOR 1: [Name]
══════════════════════════════════════
[Full Claude output here]
THIS TOOL DOES NOT: [gaps]

══════════════════════════════════════
COMPETITOR 2: [Name]
══════════════════════════════════════
[Full Claude output here]
THIS TOOL DOES NOT: [gaps]
...
```

---

## ✅ Expected Output (per competitor)

Each of 10 sessions should produce:

- **Product Profile** — exact user journey, core use case, positioning pitch
- **Company Intel** — founding, funding (Crunchbase verified), team size, revenue estimate
- **Pricing breakdown** — all tiers with what's behind the paywall
- **Top 3 loved features** — from real G2/Reddit reviews
- **Top 5 complaints** — specific, not vague
- **Critical gaps section** — 40% of the response focused on what's missing
- **"THIS TOOL DOES NOT:" line** at the very end — comma-separated gap list

**Example closing line:**
```
THIS TOOL DOES NOT: handle multi-client billing, support mobile, export to PDF, 
offer white-labeling, work offline, integrate with Figma, support INR pricing
```

---

## 💡 Pro Tip

> **Ek session mein 2–3 competitors research kar le** taki context intact rahe. Har research ke end mein "THIS TOOL DOES NOT" wali line zaroor add karao — P4 mein yeh bahut kaam aayegi comparison ke time.

**Section 6 (Gaps) pe focus karo** — yahi asli kaam hai. Agar Claude ne sirf 2–3 gaps diye hain, yeh prompt add karo:

```
Go deeper on Section 6. Search "[product name] missing feature" and 
"[product name] alternative" to find more specific gaps users mention.
```

---

## ⏱️ Time Estimate

**~2–3 hours total** — Deep research per competitor takes 10–20 min. 10 competitors × ~15 min average = 2–2.5 hours.

Break it into 3 sessions of 3–4 competitors each to avoid fatigue.

---

## ➡️ Next Step

Jab sab 10 competitor profiles ready hon → Go to [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md)

**P4 ke liye zaroor prepare karo:** Sab 10 profiles ek jagah paste ready rakho. P4 prompt ek shot mein sab kuch process karta hai.

---

*Part of the [Startup Research Playbook](./README.md) · 6-phase pipeline*
