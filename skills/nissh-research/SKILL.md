---
name: nissh-research
description: >
  Autonomous 7-Agent Grounded Startup Research System by Nisha (nissh.info).
  Validates startup problem hypotheses, captures real evidence with browser screenshots & Chrome DevTools MCP,
  tears down competitors, computes deterministic opportunity scores, eliminates false gaps,
  and compiles investor diligence dossiers with permanent watermarked PDFs.
license: Apache-2.0
---

# Nissh Research System — Antigravity Skill

An evidence-first, 7-agent autonomous intelligence runtime designed to validate startup ideas before writing code. Inspired by GPT Researcher, DeerFlow, Firecrawl, Hyperresearch, and FinRobot.

---

## ⚡ Instant One-Command NPX Execution (No Setup Required)

Run the full system anywhere via **NPX** (published on npm registry):

```bash
# 1. Launch Interactive Web UI & Playbook on localhost:5000
npx nissh-research

# 2. Run full 7-agent pipeline autonomously in terminal
npx nissh-research run --idea "Freelancers lose hours to unpaid revisions" --audience "Freelance web designers"

# 3. Run in Human-in-the-Loop (HITL) Guided Mode (pauses after each phase)
npx nissh-research run --idea "Freelancers lose hours to unpaid revisions" --mode hitl

# 4. Inspect Evidence Ledger & local screenshots
npx nissh-research evidence

# 5. Capture a live webpage screenshot and log claim to Evidence Vault
npx nissh-research test-evidence "https://hellobonsai.com" "Bonsai has no automated revision gating"
```

Or run via local Python CLI:
```bash
python nissh_cli.py run --idea "..."
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

### Example Agent Invocation with Chrome DevTools MCP:
```json
{
  "ServerName": "chrome-devtools-mcp",
  "ToolName": "navigate_page",
  "Arguments": { "url": "https://hellobonsai.com/pricing" }
}
```
Followed by:
```json
{
  "ServerName": "chrome-devtools-mcp",
  "ToolName": "take_screenshot",
  "Arguments": { "filePath": "evidence/screenshots/screenshot_bonsai_pricing.png" }
}
```
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
