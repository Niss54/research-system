# 🚀 Nissh Research System: 7-Agent Autonomous Startup Intelligence

<div align="center">

**From Multilingual Startup Idea to Investor-Ready Watermarked PDF Report — Powered by 7 Sequential AI Agents with Auto-Fallback.**

[![Built by Nisha](https://img.shields.io/badge/Author-Nishant%20Maurya%20(Nissh)-6366f1?style=for-the-badge&logo=safari&logoColor=white)](https://nissh.info)
[![Portfolio](https://img.shields.io/badge/Portfolio-nissh.info-ec4899?style=for-the-badge)](https://nissh.info)
[![License](https://img.shields.io/badge/License-Apache%202.0-10b981?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9+-38bdf8?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Models Supported](https://img.shields.io/badge/LLMs-Gemini%20|%20Groq%20|%20Claude%20|%20OpenAI-facc15?style=for-the-badge)](https://github.com/Niss54/research-system)

> *"Never build a startup on assumptions. Validate with hard evidence, verify competitor voids across 9 platforms, and generate honest investor-grade diligence."*

[Explore Portfolio (nissh.info)](https://nissh.info) · [View Pipeline Architecture](PIPELINE_FLOW.md) · [Quickstart](#-quickstart-guide)

</div>

---

## 🌟 What Makes This System Unique?

1. **Multilingual Single-Input Field:** Type your startup idea in **any language** (Hindi, Hinglish, Spanish, English, etc.). The system automatically standardizes and translates the hypothesis into crisp English for research.
2. **Auto-Fallback Multi-Provider Engine:** Set at least 1 compulsory API key, and optionally 2–3 fallback keys (**Gemini → Groq → Claude → OpenAI → OpenRouter**). If provider credits exhaust or rate limits hit mid-pipeline (e.g. at Stage 4), it seamlessly shifts to the next provider without crashing your research!
3. **7 Sequential Evidence-First Agents:** 100% honest evaluation. If an idea is flawed or has low willingness to pay, the system gives a strict **NO-GO ❌** verdict with cited evidence — zero flattery, zero hallucinations.
4. **Permanent 'NISSH' Watermark & Clickable Link:** The automatically compiled PDF includes unremovable vector-layer watermarks (`NISSH • NISSH.INFO`) and clickable hyperlinks to Nisha's portfolio: [https://nissh.info](https://nissh.info).
5. **Two Execution Modes:**
   - **Mode 1 (Autonomous Local Engine):** Run locally with Flask, stream live agent logs, and download the finished PDF in one click.
   - **Mode 2 (Manual Prompt Chaining):** For users who don't want to run locally or configure API keys — copy the 7 standardized Markdown files (`P1` to `P7`) one-by-one into Claude.ai or ChatGPT.

---

## 🤖 The 7 Autonomous Agents Workflow

```text
[User Startup Idea (Any Language)]
                │
                ▼
Agent 1: Problem Validator ──► Checks frequency, severity (1-10), WTP & GO/MAYBE/NO-GO verdict
                │
                ▼
Agent 2: Landscape Hunter  ──► Maps Top 10 direct, indirect & manual workarounds (Excel, Notion)
                │
                ▼
Agent 3: Forensic Auditor  ──► Conducts 360° competitor teardown & extracts "THIS TOOL DOES NOT"
                │
                ▼
Agent 4: Gap Strategist    ──► Feature Matrix + Mathematical Scoring: (Pain × Market) / Difficulty
                │
                ▼
Agent 5: 9-Platform Verifier──► Audits Google, Product Hunt, GitHub, YC, IndieHackers for False Gaps
                │
                ▼
Agent 6: Diligence Synthesizer──► Synthesizes Investor Memo, Verified Moats & 30-Day Launch Roadmap
                │
                ▼
Agent 7: Launch README Architect──► Builds production GitHub README.md with hero badges & setup
                │
                ▼
[Official Vector PDF Report Generated with Permanent NISSH Watermark & Link to nissh.info]
```

| Agent # | Agent Name | Core Mission | Key Output |
|:---:|---|---|---|
| **1** | **Problem Validator** | Normalizes language to English; searches Reddit, G2, forums for real pain | `<!-- BEGIN P1_HANDOFF -->` (Verdict: GO/MAYBE/NO-GO) |
| **2** | **Landscape Hunter** | Discovers existing tools, niche software, and manual workarounds | `<!-- BEGIN P2_HANDOFF -->` (Top 10 Competitors Table) |
| **3** | **Forensic Auditor** | Deep-dives into user complaints, missing features, and limitations | `<!-- BEGIN P3_PROFILE -->` (10 In-depth teardowns) |
| **4** | **Gap Strategist** | Builds full feature matrix and scores market gaps | `<!-- BEGIN P4_HANDOFF -->` (Top 5 Scored Gaps & #1 Wedge) |
| **5** | **9-Platform Verifier** | Verifies voids across 9 platforms to eliminate false leads | `<!-- BEGIN P5_HANDOFF -->` (Confirmed vs False Gaps) |
| **6** | **Diligence Synthesizer**| Synthesizes investor diligence memo, facts vs assumptions, 30-day GTM | `<!-- BEGIN P6_HANDOFF -->` (Startup Diligence Dossier) |
| **7** | **Launch Kit Architect**| Generates production-ready GitHub `README.md` and positioning kit | Complete launch `README.md` |

---

## ⚡ Quickstart Guide

### 🤖 Option A: Autonomous Local Engine (Recommended)

Run the autonomous 7-agent system locally with the modern, animated web interface:

```bash
# 1. Clone repository
git clone https://github.com/Niss54/research-system.git
cd research-system

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure API keys (or configure directly in the UI modal)
cp .env.example .env

# 4. Launch the local web server
python server.py
```

Now open **`http://localhost:5000`** in your browser:
1. Click **🔑 API Keys & Fallback Setup** to enter your keys (at least 1 key is required; add 2–3 for auto-fallback protection).
2. Type or paste your startup idea in **any language** in the main input box.
3. Click **🚀 Launch 7 Autonomous Agents**.
4. Watch the live terminal logs and visual status cards as each agent executes.
5. Click **📥 Download PDF Report** to get your official report with the permanent `NISSH` watermark!

---

### 📋 Option B: Manual Prompt Chaining (Free / No Setup / Claude or ChatGPT)

If you do not wish to clone the repository or set up API keys locally, you can use the 7 standardized Markdown prompt files directly with [Claude.ai](https://claude.ai) or [ChatGPT](https://chatgpt.com):

1. **Step 1:** Open [`P1_Validate.md`](./P1_Validate.md). Copy the prompt, paste your problem statement, turn **Web Search ON**, and run.
   - *Output:* Claude returns evidence and an `<!-- BEGIN P1_HANDOFF -->` block (or output PDF).
2. **Step 2:** Open [`P2_Top10.md`](./P2_Top10.md). Paste your P1 handoff block (or attach the P1 output PDF/text) into the designated slot. Run to get `<!-- BEGIN P2_HANDOFF -->`.
3. **Step 3:** Open [`P3_Research_x10.md`](./P3_Research_x10.md). Attach the competitor list from P2 and generate teardowns for each competitor.
4. **Step 4:** Open [`P4_Gap_Analysis.md`](./P4_Gap_Analysis.md). Paste the P1 and P3 blocks (Extended Thinking ON). Get `<!-- BEGIN P4_HANDOFF -->`.
5. **Step 5:** Open [`P5_Verify_Gaps.md`](./P5_Verify_Gaps.md). Paste the P4 gaps and let Claude audit 9 platforms for false gaps. Get `<!-- BEGIN P5_HANDOFF -->`.
6. **Step 6:** Open [`P6_Final_Report.md`](./P6_Final_Report.md). Paste all previous handoff blocks to synthesize your complete Diligence Memo.
7. **Step 7:** Open [`P7_Make_README.md`](./P7_Make_README.md). Attach the P6 handoff block to produce your production GitHub `README.md`!

---

## 🔑 Multi-Provider API Keys & Auto-Fallback Architecture

The system connects to multiple AI providers. You must provide **at least ONE** key. If multiple keys are provided, the engine automatically prioritizes and fails over:

```text
Priority 1: Google Gemini (High Speed / Free Tier)
   └─► If rate limited or quota exhausted:
Priority 2: Groq (Llama 3.3 70B Versatile @ 500+ tokens/sec)
   └─► If failed:
Priority 3: Anthropic Claude (Claude 3.5 Sonnet / Extended Thinking)
   └─► If failed:
Priority 4: OpenAI (GPT-4o / GPT-4o-mini)
   └─► If failed:
Priority 5: OpenRouter (Universal AI Gateway)
```

Configure in your `.env` file or directly in the UI modal:
```env
GEMINI_API_KEY="AIzaSy..."
GROQ_API_KEY="gsk_..."
ANTHROPIC_API_KEY="sk-ant-..."
OPENAI_API_KEY="sk-proj-..."
OPENROUTER_API_KEY="sk-or-..."
```

---

## 📄 Official Watermarked PDF Report

When the 7-agent cycle completes, the engine compiles a multi-page, publication-grade PDF using vector printing:
- **Permanent Watermark:** Background diagonal vector layers repeating `NISSH • NISSH.INFO` across every page.
- **Clickable Hyperlinks:** Active header and footer links directly navigating to **[https://nissh.info](https://nissh.info)**.
- **Evidence Formatting:** Clear separation between verified facts and assumptions, full feature matrices, competitor limitations, and a 30-day MVP roadmap.

To manually re-render or compile an existing report to PDF:
```bash
python pdf_generator.py
```

---

## 💻 Python CLI Runner

You can also run every phase directly from your command line:

```bash
# Initialize project
python research_pipeline.py init "Freelance designers losing money on extra revisions" --audience "Freelance Designers"

# Generate prompt for any phase
python research_pipeline.py prompt 1
python research_pipeline.py prompt 2

# Save AI output & extract handoff contract
python research_pipeline.py save 1 --file p1_output.txt

# Inspect pipeline status
python research_pipeline.py status

# Compile full research dossier
python research_pipeline.py compile
```

---

## 📁 Repository Structure

```text
research-system/
├── .env.example                  ← Multi-provider API keys template
├── requirements.txt              ← Python package dependencies
├── server.py                     ← Flask backend with REST APIs & background worker
├── research_engine.py            ← 7-Agent autonomous orchestrator & fallback caller
├── pdf_generator.py              ← Chrome/Edge headless vector PDF generator (Watermarked)
├── research_pipeline.py          ← Python CLI runner & state manager
├── startup_research_playbook.html← Modern animated frontend UI (nissh.info theme)
│
├── P1_Validate.md                ← Agent 1: Evidence validation & GO/MAYBE/NO-GO verdict
├── P2_Top10.md                   ← Agent 2: Competitive landscape & Top 10 solutions
├── P3_Research_x10.md            ← Agent 3: Forensic competitor deep dives & limitations
├── P4_Gap_Analysis.md            ← Agent 4: Feature matrix & scored market gaps
├── P5_Verify_Gaps.md             ← Agent 5: 9-platform verification to kill false gaps
├── P6_Final_Report.md            ← Agent 6: Investor-ready diligence memo & MVP spec
├── P7_Make_README.md             ← Agent 7: Production GitHub README & launch kit
│
├── PIPELINE_FLOW.md              ← Mermaid sequence diagrams & handshake contracts
└── workspace/                    ← Saved agent outputs, dossier, and generated PDF
```

---

## 👨‍💻 Created by Nisha

**Nishant Maurya (Nissh)**  
- 🌐 **Official Portfolio:** [https://nissh.info](https://nissh.info)  
- 💡 **Founder:** Sight Pro  
- 🏆 **Achievements:** MLH Hack Days Winner  
- 💼 **Focus:** Full-Stack AI Systems, Autonomous Multi-Agent Workflows, High-Impact Product Engineering  

---

## 📜 License

Licensed under the [Apache License 2.0](LICENSE). Free for founders, builders, and indie hackers worldwide.
