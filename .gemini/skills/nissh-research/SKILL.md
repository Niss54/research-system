---
name: nissh-research
description: >
  Autonomous 7-Agent Grounded Startup Research System by Nisha (nissh.info).
  DORMANT BY DEFAULT. MUST ONLY ACTIVATE WHEN THE USER EXPLICITLY ASKS FOR "use nissh skills",
  "nissh research", or "/nissh". NEVER intercepts general coding tasks, bug fixing,
  refactoring, or everyday edits.
triggers:
  - "use nissh skills"
  - "nissh research"
  - "/nissh"
---

# Nissh Research System — Antigravity Skill

An evidence-first, 7-agent autonomous intelligence runtime designed to validate startup ideas before writing code. Inspired by GPT Researcher, DeerFlow, Firecrawl, Hyperresearch, and FinRobot.

---

> [!CAUTION]
> ### 🛑 STRICT DORMANT ACTIVATION RULE
> **This skill must remain 100% DORMANT by default.**
> - Do **NOT** intercept general programming tasks, feature building, bug fixing, or regular user requests.
> - **ONLY activate when the user explicitly types:**
>   - 👉 **`use nissh skills`**
>   - 👉 **`nissh research`**
>   - 👉 **`/nissh`**
> - Unless the user provides one of these explicit trigger phrases, stay silent and do not interfere with normal workspace operations.

---

## ⚡ Instant One-Command NPX Execution (Dual-Mode Interactive Selection)

When you run `npx nissh-research` in any terminal, it prompts you interactively:

```text
? How would you like to run the Nissh Research System?
  [1] 🌐 Interactive Web UI  (Launches local server at localhost:5000 with visual playbook)
  [2] 💻 Local Code Editor   (Installs dormant skill into this project for Antigravity, VS Code, Claude)
```

Direct non-interactive shortcuts:
```bash
# Option 1: Direct Web UI launch
npx nissh-research web

# Option 2: Install skill into current project folder
npx nissh-research install

# Option 3: Run autonomous 7-agent pipeline in terminal
npx nissh-research run --idea "Freelancers lose hours to unpaid revisions" --audience "Freelance web designers"

# Option 4: Run in Human-in-the-Loop (HITL) Guided Mode (pauses after each phase)
npx nissh-research run --idea "Freelancers lose hours to unpaid revisions" --mode hitl

# Option 5: Inspect Evidence Ledger & local screenshots
npx nissh-research evidence

# Option 6: Capture a live webpage screenshot and log claim to Evidence Vault
npx nissh-research test-evidence "https://hellobonsai.com/pricing" "Bonsai has no automated revision gating"
```

---

## 🌐 Chrome DevTools MCP Integration (`chrome-devtools-mcp`)

> **Truth Over Hallucination:** Prompts alone cannot prevent LLMs from hallucinating forum links. Real verification requires driving an actual browser engine.

When running inside **Google Antigravity** or any MCP-compatible environment, agents have native access to the **`chrome-devtools-mcp`** server:

| MCP Tool | Purpose in Nissh Research System |
|---|---|
| `navigate_page` | Opens live competitor pricing pages, Reddit threads, G2 reviews, and news articles |
| `take_screenshot` | Captures high-resolution, full-page PNG proof into `evidence/screenshots/` |
| `take_snapshot` | Dumps the live DOM text/accessibility tree for parsing JavaScript-rendered SPAs |
| `evaluate_script` | Scrapes dynamic page elements, tables, and live pricing tiers directly |
| `click` / `wait_for` | Bypasses cookie banners and modal popups to read actual article content |

This evidence is directly recorded into [`evidence/EVIDENCE_LEDGER.md`](../../evidence/EVIDENCE_LEDGER.md) with cryptographic hash IDs and verification confidence levels.

---

## 🤖 The 7 Grounded Agents & Sequential Handoffs

Every phase produces a markdown handoff block that seamlessly connects to the next phase:

| Phase | Agent Role | Key Tool / Methodology | Handoff Contract |
|---|---|---|---|
| **P1** | **Problem Validator** | Live web search (Reddit, Google News) + Language Normalization | `<!-- BEGIN P1_HANDOFF -->` |
| **P2** | **Landscape Hunter** | Live competitor discovery + HTTP 200 URL check + Pricing snapshot | `<!-- BEGIN P2_HANDOFF -->` |
| **P3** | **Forensic Auditor** | 1-star & 2-star review mining (G2/Capterra) + "THIS TOOL DOES NOT" | `<!-- BEGIN P3_PROFILE -->` |
| **P4** | **Gap Analyst** | Cross-competitor feature matrix + deterministic opportunity formula | `<!-- BEGIN P4_HANDOFF -->` |
| **P5** | **9-Platform Verifier** | Multi-synonym sweep + GitHub public repository search (False gap prune) | `<!-- BEGIN P5_HANDOFF -->` |
| **P6** | **Diligence Synthesizer**| 9-column Evidence Ledger + Unit economics + 30-day GTM plan | `<!-- BEGIN P6_HANDOFF -->` |
| **P7** | **Launch Architect** | Production GitHub README + PostHog Product Telemetry Spec | Output `README.md` |

---

## 🏛️ Evidence Vault & Screenshot Provenance

All factual claims are recorded in `evidence/ledger.json` and mirrored in `evidence/EVIDENCE_LEDGER.md`:
- **Real Screenshots**: Headless Chrome and Chrome DevTools MCP capture pixel-perfect PNGs of news articles, forum threads, and competitor sites into `evidence/screenshots/`.
- **Clean HTML Snapshots**: Page text is archived in `evidence/snapshots/`.
- **Audit Table**: Each claim records `Source URL`, `Source Tier` (Primary / Secondary / Community), `Verification Status` (`VERIFIED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`), `Confidence`, and `Limitations`.

---

## 🔑 Multi-Provider Auto-Fallback

The engine automatically cascades across LLMs on rate-limits, quota exhaustion, or timeouts:
`Gemini 2.5/2.0 Flash` → `Groq (Llama 3.3 70B)` → `Claude 3.5 Sonnet` → `OpenAI (GPT-4o)` → `OpenRouter`
