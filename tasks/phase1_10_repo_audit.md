# 🏛️ Phase 1: Deep Architectural Audit of 10 Benchmark Repositories

> **Audit Framework:** Evaluated through the **GRAVITAS Reliability Runtime**. Each repository is audited for its concrete architecture, real-world limitations, and the exact architectural pattern to incorporate into the **Nissh Research System v2**.

---

## 1. GPT Researcher (`assafelovic/gpt-researcher`)
* **Repository:** [assafelovic/gpt-researcher](https://github.com/assafelovic/gpt-researcher)
* **Core Specialty:** Autonomous web research, parallel sub-topic research, dynamic query generation, citations.
* **Architecture Teardown:**
  - **Planner Agent**: Decomposes high-level research questions into 3–5 targeted sub-queries.
  - **Worker Agents**: Concurrently execute web searches, scrape candidate URLs, and chunk/vectorize page text.
  - **Context Compression**: Rather than dumping entire web pages into prompt context, it performs semantic similarity search to extract only relevant paragraphs.
  - **Chief Editor / Publisher**: Synthesizes cross-source report with bracketed markdown citations `[Source Name: URL]`.
* **Critical Limitations:**
  - Explicitly carries an "experimental / as-is" disclaimer.
  - Bracketed citations do not guarantee factual truth; if scraped pages contain promotional fluff or false claims, the LLM incorporates them uncritically.
* **Adopted Pattern for Nissh v2:**
  - **Dynamic Multi-Query Expansion**: Agent 1 and Agent 2 will expand the user's idea into 3 specific search queries (Complaints, Existing Solutions, Workarounds).
  - **Context Compressor**: Scrape text and extract relevant 200-word snippets before feeding to LLM context to prevent token exhaustion.

---

## 2. DeerFlow (`bytedance/deer-flow`)
* **Repository:** [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
* **Core Specialty:** Long-running agents, subagents, persistent memory, tools, and stateful workflow coordination.
* **Architecture Teardown:**
  - Decouples task execution into stateful checkpoints.
  - Uses explicit message passing and state containers rather than fragile raw string piping.
  - Provides subagent isolation: Subagents have scoped tool definitions and independent scratchpads.
  - Supports Human-in-the-Loop (HITL) pause, review, and resumption without losing upstream compute.
* **Critical Limitations:**
  - Heavy runtime overhead if used for simple linear scripts; requires clear boundaries on state serialization.
* **Adopted Pattern for Nissh v2:**
  - **Checkpoint & Resume State Machine**: All 7 phases write immutable checkpoints to SQLite. If Agent 4 needs adjustments or fails, Agent 1–3 outputs are preserved.
  - **HITL Gateways**: Allow founders to approve or modify the competitor table before forensic teardowns run.

---

## 3. Firecrawl (`firecrawl/firecrawl`)
* **Repository:** [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)
* **Core Specialty:** Web search, dynamic JavaScript rendering, clean Markdown extraction, structured data schema.
* **Architecture Teardown:**
  - Headless browser rendering (Playwright/Puppeteer) bypasses single-page application (SPA) client-side hydration issues.
  - Strips CSS, SVGs, navbars, ads, and footers, converting raw DOM into clean, token-efficient GitHub-Flavored Markdown.
  - Offers LLM-directed structured extraction over crawled pages.
* **Critical Limitations:**
  - Self-hosted core is **AGPL-3.0 licensed** (requires strict licensing separation if packaged as a commercial skill).
  - High resource usage when running headless browsers at scale.
* **Adopted Pattern for Nissh v2:**
  - **DOM-to-Clean-Markdown Normalizer**: Local text stripper that strips HTML boilerplates, scripts, and CSS, turning competitor pricing pages into clean markdown tables before LLM analysis.
  - **Real Source Fetching**: Ingest real page body content, not just 2-line Google search snippets.

---

## 4. Hyperresearch (`jordan-gibbs/hyperresearch`)
* **Repository:** [jordan-gibbs/hyperresearch](https://github.com/jordan-gibbs/hyperresearch)
* **Core Specialty:** Evidence vault, source provenance, citation checking, contradiction analysis, source independence.
* **Architecture Teardown:**
  - **Immutable Evidence Ledger**: Every factual claim is recorded with `Source URL`, `Published Date`, `Retrieved Date`, `Exact Quote Passage`, and `Source Tier` (Primary / Secondary / Community).
  - **Contradiction Detector**: Flags discrepancies between what a company claims on its homepage vs what users report on forums.
  - **Source Independence Checker**: Checks whether multiple news articles originate from a single syndicated PR wire (preventing false consensus).
* **Critical Limitations:**
  - Benchmark claims (DRACO) are self-reported by the project authors and must be treated as architectural ideals rather than proven guarantees.
* **Adopted Pattern for Nissh v2:**
  - **Mandatory Upstream Evidence Ledger**: From Phase 1 onwards, every finding MUST carry an evidence ledger block with verification status (`VERIFIED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`).
  - **Local Evidence Snapshot Vault**: Save source links and automated local screenshots/HTML snapshots into `evidence/`.

---

## 5. RAGFlow (`infiniflow/ragflow`)
* **Repository:** [infiniflow/ragflow](https://github.com/infiniflow/ragflow)
* **Core Specialty:** Deep document intelligence, complex PDFs, government filings, layout-aware RAG.
* **Architecture Teardown:**
  - Deep document parsing that understands multi-column layouts, tables, and charts in financial PDFs.
  - Retains row/column semantics when converting PDF balance sheets into LLM-usable data.
* **Critical Limitations:**
  - Significant infrastructure requirements (Docker, OCR models, GPU acceleration for local inference).
* **Adopted Pattern for Nissh v2:**
  - **Structured Document Parser Adapter**: Provide clean integration hooks for founders uploading official PDF filings (MCA master data, SEBI annual reports, SEC 10-K).

---

## 6. PaperQA2 (`Future-House/paper-qa`)
* **Repository:** [Future-House/paper-qa](https://github.com/Future-House/paper-qa)
* **Core Specialty:** Scientific literature, claim verification, academic citations, retraction checks.
* **Architecture Teardown:**
  - Direct integration with Crossref, OpenAlex, PubMed, and Semantic Scholar.
  - Performs **Retraction Checks**: Verifies that cited scientific papers haven't been retracted or discredited.
  - Generates evidence matrices where claims are strictly bound to verifiable DOI references.
* **Critical Limitations:**
  - Narrow focus on academic/scientific literature; does not understand consumer SaaS pricing models.
* **Adopted Pattern for Nissh v2:**
  - **Academic & Patent Verification Hook**: For deep-tech or biotech startup ideas, invoke OpenAlex and Crossref APIs to check technical feasibility claims.

---

## 7. FinRobot (`AI4Finance-Foundation/FinRobot`)
* **Repository:** [AI4Finance-Foundation/FinRobot](https://github.com/AI4Finance-Foundation/FinRobot)
* **Core Specialty:** Deterministic financial calculations, valuation, risk analysis, 10-K financial modeling.
* **Architecture Teardown:**
  - **Strict Separation of Compute and Narrative**: Financial calculations (CAGR, LTV/CAC, TAM, DCF, Sensitivity) are calculated via deterministic Python code, NEVER generated subjectively by an LLM prompt.
  - LLMs are restricted to narrative interpretation of mathematically verified figures.
* **Critical Limitations:**
  - Designed for public corporate equity research (SEC filings); not tuned for zero-revenue pre-seed startup ideation.
* **Adopted Pattern for Nissh v2:**
  - **Deterministic Unit Economics Engine**: TAM, SAM, SOM, and pricing projections in Phase 6 will be computed by a deterministic Python calculator, eliminating hallucinated financial math.

---

## 8. OpenBB (`OpenBB-finance/OpenBB`)
* **Repository:** [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB)
* **Core Specialty:** Unified financial/economic data providers, Python SDK, REST API, Model Context Protocol (MCP).
* **Architecture Teardown:**
  - Standardizes data models across dozens of disparate financial and macroeconomic providers (FRED, World Bank, OECD, SEC EDGAR, RBI).
  - Exposes tool endpoints through standardized MCP servers, allowing agents to fetch authoritative market data dynamically.
* **Critical Limitations:**
  - OpenBB is an abstraction layer, NOT a data provider. Access requires underlying API keys for premium providers. Private startup data is limited.
* **Adopted Pattern for Nissh v2:**
  - **Official Macro Data Layer**: Connect macroeconomic indices (MoSPI, World Bank, RBI) into market size estimates via standardized API adapters.

---

## 9. BettaFish (`666ghj/BettaFish`)
* **Repository:** [666ghj/BettaFish](https://github.com/666ghj/BettaFish)
* **Core Specialty:** Multi-platform social listening, public opinion, customer sentiment, complaint clustering.
* **Architecture Teardown:**
  - Scrapes user discussions across diverse communities (Reddit, Weibo, Twitter, product reviews).
  - Clusters user complaints into semantic problem categories with frequency distribution.
* **Critical Limitations:**
  - Social media sentiment is volatile and vocal-minority biased; complaint volume does not automatically equate to Willingness-to-Pay (WTP).
* **Adopted Pattern for Nissh v2:**
  - **Hate/Complaint Mining Filter**: Specifically target search queries for `"hate [tool]"`, `"switched from [tool] to"`, and `"alternative to [tool] because"` to extract real switching catalysts.

---

## 10. PostHog (`PostHog/posthog`)
* **Repository:** [PostHog/posthog](https://github.com/PostHog/posthog)
* **Core Specialty:** Product telemetry, session replays, conversion funnels, in-product user surveys.
* **Architecture Teardown:**
  - Captures real user behavioral event streams after product launch.
  - Replaces pre-launch assumptions with observed empirical evidence (retention curves, drop-off points).
* **Critical Limitations:**
  - Operates only AFTER an MVP is deployed; cannot validate zero-to-one problem spaces before code exists.
* **Adopted Pattern for Nissh v2:**
  - **Phase 7 Telemetry Spec**: In addition to generating the GitHub README, Agent 7 will generate the **PostHog Event Tracking Plan** (Key validation events to track upon MVP launch).

---

## 11. Bonus: Local Deep Research (`LearningCircuit/local-deep-research`)
* **Repository:** [LearningCircuit/local-deep-research](https://github.com/LearningCircuit/local-deep-research)
* **Core Specialty:** Self-hosted, privacy-first deep research using local LLMs (Ollama/vLLM) and local search engines (SearXNG).
* **Adopted Pattern for Nissh v2:**
  - **Zero-Key Offline Fallback Mode**: When no commercial API keys (Tavily/OpenAI/Gemini) are present, gracefully use local LLMs and open web scrapers.
