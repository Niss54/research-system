---
name: nissh-research
description: >
  Autonomous 7-Agent Grounded Startup Research System by Nisha (nissh.info).
  Validates startup problem hypotheses, captures real evidence with browser screenshots,
  tears down competitors, computes deterministic opportunity scores, eliminates false gaps,
  and compiles investor diligence dossiers with permanent watermarked PDFs.
license: Apache-2.0
---

# Nissh Research System — Antigravity Skill

An evidence-first, 7-agent autonomous intelligence runtime designed to validate startup ideas before writing code. Inspired by GPT Researcher, DeerFlow, Firecrawl, Hyperresearch, and FinRobot.

---

## ⚡ Quick CLI Commands

Run these directly from your terminal or Antigravity bash/powershell session:

```bash
# 1. Run full 7-agent research pipeline autonomously
python nissh_cli.py run --idea "Freelancers lose hours to unpaid revisions" --audience "Freelancers & boutique agencies"

# 2. Run in Human-in-the-Loop (HITL) Guided Mode (pauses after each phase)
python nissh_cli.py run --idea "Freelancers lose hours to unpaid revisions" --mode hitl

# 3. View captured evidence, source quotes, and browser screenshots
python nissh_cli.py evidence

# 4. Capture a live webpage screenshot and log claim to Evidence Vault
python nissh_cli.py test-evidence "https://hellobonsai.com" "Bonsai has no automated revision gating"

# 5. List all past research projects in local SQLite database
python nissh_cli.py list

# 6. Launch interactive Web UI & API server
python server.py
```

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
- **Real Screenshots**: Headless Chrome captures pixel-perfect PNGs of news articles, forum threads, and competitor sites into `evidence/screenshots/`.
- **Clean HTML Snapshots**: Page text is archived in `evidence/snapshots/`.
- **Audit Table**: Each claim records `Source URL`, `Source Tier` (Primary / Secondary / Community), `Verification Status` (`VERIFIED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`), `Confidence`, and `Limitations`.

---

## 🔑 Multi-Provider Auto-Fallback

The engine automatically cascades across LLMs on rate-limits, quota exhaustion, or timeouts:
`Gemini 2.5/2.0 Flash` → `Groq (Llama 3.3 70B)` → `Claude 3.5 Sonnet` → `OpenAI (GPT-4o)` → `OpenRouter`
