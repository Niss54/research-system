# P6 — Final Report

> **Phase 6 of 6 · Problem → Opportunity Playbook · Evidence-Verified Edition**

---

## 🎯 What This Phase Does

Everything in one place.

You paste all outputs from P1 through P5 into this phase. Claude must **synthesize the research AND independently fact-check the important claims before producing the final report.**

The final report must be suitable for:

* Co-founders
* Hackathon judges
* Startup planning
* Customer discovery
* Investor discussion
* Internal build/no-build decisions

### Core principle

**Never convert an unverified claim into a fact.**

P6 is not allowed to blindly trust P1-P5.

P1-P5 are research inputs, not unquestionable truth.

---

## ⚙️ Tools Required

| Tool                       | Status | Why                                                               |
| -------------------------- | ------ | ----------------------------------------------------------------- |
| 🧠 Extended Thinking       | **ON** | Deep synthesis, contradiction detection and evidence evaluation   |
| 🔍 Web Search              | **ON** | Every material factual claim must be independently verified       |
| 🌐 Primary-source browsing | **ON** | Open and inspect the original source, not only the search snippet |

> **Important:** Web Search MUST remain ON for P6.
>
> P6 is an evidence-verification stage, not only a writing stage.

---

# 📋 Copy-to-Paste Prompt

```text
Create an EVIDENCE-VERIFIED STARTUP OPPORTUNITY REPORT.

Problem:
[PROBLEM STATEMENT]

Research date:
[TODAY'S DATE]

IMPORTANT:
The P1-P5 material below is research input, NOT automatically verified truth.

Your job is NOT to simply summarize P1-P5.

Your job is to:

1. Synthesize P1-P5.
2. Independently verify every important factual claim using fresh web research.
3. Detect contradictions between P1-P5 and current external evidence.
4. Remove unsupported claims.
5. Clearly separate:
   - VERIFIED FACT
   - PARTIALLY VERIFIED
   - UNVERIFIED
   - ESTIMATE
   - INFERENCE
   - CONTRADICTED
6. Never invent a source, quotation, statistic, company capability, market number, funding number, customer number, research result, publication date or competitor feature.
7. Never present an estimate as a fact.
8. Never present an AI-generated assumption as evidence.
9. Never claim "100% of competitors", "all tools", "no competitor", "everyone", "only", "zero", or similar universal statements unless an exhaustive and documented audit actually proves it.
10. If evidence is insufficient, say so explicitly.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RESEARCH INPUTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━ P1 — VALIDATION RESULTS ━━━━━━━━━━━━━━━━━━━
[PASTE P1 OUTPUT]

━━━ P2 — TOP 10 SOLUTIONS ━━━━━━━━━━━━━━━━━━━━━
[PASTE P2 OUTPUT]

━━━ P3 — COMPETITIVE PROFILES ━━━━━━━━━━━━━━━━━
[PASTE ALL P3 OUTPUTS]

━━━ P4 — GAP ANALYSIS ━━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P4 OUTPUT]

━━━ P5 — VERIFIED GAPS ━━━━━━━━━━━━━━━━━━━━━━━━
[PASTE P5 OUTPUT]


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 0 — CLAIM AUDIT BEFORE WRITING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before writing the report, extract every material claim from P1-P5.

A material claim includes:

- Market size
- CAGR
- User count
- Customer count
- Repository count
- Funding amount
- Pricing
- Number of competitors
- Product capabilities
- Security claims
- CVEs
- Attack rates
- Detection rates
- Breach costs
- Time-to-contain statistics
- Research findings
- Publication dates
- Company acquisitions
- Company ownership
- Customer adoption
- Revenue projections
- TAM/SAM/SOM
- Pain-point statistics
- Quotes
- Any claim used to justify GO / NO-GO / PIVOT

Create an internal evidence ledger.

For every material claim record:

CLAIM
SOURCE FROM P1-P5
EXTERNAL SOURCE
SOURCE TYPE
PUBLICATION DATE
DATE VERIFIED
WHAT THE SOURCE ACTUALLY SAYS
VERDICT
CONFIDENCE

Allowed verdicts:

✅ VERIFIED
🟡 PARTIALLY VERIFIED
⚠️ UNVERIFIED
🔴 CONTRADICTED
📊 ESTIMATE
🧠 INFERENCE

Do NOT include the internal ledger unless useful, but use it to control the final report.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE HIERARCHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Prefer sources in this order:

TIER 1 — PRIMARY / AUTHORITATIVE

- Official company documentation
- Official company security advisories
- Official GitHub repositories
- NVD / CVE records
- Government sources
- Regulatory sources
- Official Hugging Face documentation/statistics
- Official standards organizations
- Original research papers
- DOI / publisher pages
- arXiv when the original paper is not yet formally published

TIER 2 — HIGH-QUALITY SECONDARY

- Reputable security research firms
- Reputable market research firms
- Established technology publications
- Established financial/business reporting

TIER 3 — COMMUNITY

- Reddit
- Hacker News
- GitHub issues
- Forums
- Product Hunt
- Discord
- Community discussions

Community sources may establish:

- User complaints
- User sentiment
- Workarounds
- Demand signals
- Anecdotal experiences

But community posts MUST NOT be used alone to establish:

- Market size
- Global user counts
- Revenue
- Funding
- Security effectiveness
- Scientific claims
- Company valuation

Never use a search-result snippet as the final evidence.
Open the actual source and verify the surrounding context.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VERIFICATION RULES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RULE 1 — NO FABRICATION

Never invent:

- citations
- URLs
- paper titles
- author names
- statistics
- publication dates
- company capabilities
- quotes
- funding
- customer numbers

If you cannot verify it:

write "UNVERIFIED".

Do not guess.

RULE 2 — PRIMARY SOURCE CHECK

Whenever a claim concerns a company product, first check:

- Official website
- Official documentation
- Official GitHub
- Official security/advisory page

Whenever a claim concerns a CVE:

- Check NVD
- Check the relevant vendor/project advisory where available

Whenever a claim concerns research:

- Check the original paper
- Verify publication status
- Verify publication date
- Verify what was actually tested

RULE 3 — DATE ACCURACY

Never confuse:

- arXiv submission date
- preprint date
- conference date
- journal acceptance date
- journal publication date
- webpage update date

Use the exact date that the source supports.

Never write:

"Published in May 2026"

when the source only proves:

"Preprint available in 2024"

or vice versa.

RULE 4 — MARKET SIZE

A market-size figure must include:

- Market definition
- Geography
- Time period
- Source
- Report/publisher
- Whether it is total AI security, AI vulnerability scanning, model security, or the specific problem

Do NOT use a broad AI-security market figure and present it as the market size of this specific startup opportunity.

When multiple market estimates exist:

show a range and explain the difference.

RULE 5 — COMPETITOR CLAIMS

Never write:

"Nobody does this."

Instead use language such as:

"Among the tools reviewed in this audit, we did not find evidence of..."

Only write:

"0/10 tools"

when:

- Exactly 10 tools were audited
- Each tool was actually inspected
- The feature matrix records evidence
- The audit date is stated

If the audit is incomplete, write:

"Not established by this research."

RULE 6 — QUANTITATIVE CLAIMS

Every number must have one of:

- Verified source
- Clearly labeled estimate
- Clearly labeled model assumption

Examples:

BAD:
"50,000 MLOps teams exist."

GOOD:
"Estimated 50,000–150,000 teams based on [method/source]; this is a directional estimate, not an authoritative count."

BAD:
"The startup can generate $8M ARR."

GOOD:
"Illustrative revenue scenario: $8M ARR if X customers pay Y. This is a model assumption, not validated revenue."

RULE 7 — RESEARCH CLAIMS

Never strengthen a research paper's conclusion.

Example:

BAD:
"The attack survives 90% of fine-tuning."

unless the source actually tested that exact scenario.

GOOD:
"The cited study reported X under Y experimental conditions."

Always preserve the study's:

- model
- dataset
- attack type
- embedding rate
- detection method
- experimental conditions

RULE 8 — USER QUOTES

Only use a quotation if the original quote can be verified.

Otherwise:

- paraphrase it
- identify the source
- do not use quotation marks

Never create an AI-generated quote.

RULE 9 — NEGATIVE CLAIMS

Negative claims require stronger evidence than positive claims.

For example:

"The product does not support feature X"

requires checking current documentation.

"The entire industry does not support feature X"

requires a documented industry-wide audit.

Prefer scoped wording.

RULE 10 — CURRENT INFORMATION

For information that can change:

- company funding
- pricing
- acquisitions
- product features
- repository counts
- model counts
- user counts
- market statistics
- competitors

use the most recent reliable source available as of the research date.

Include "as of [date]" where useful.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFLICT RESOLUTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

If P1-P5 conflicts with a current primary source:

DO NOT silently choose one.

Report:

Previous research claimed:
"[claim]"

Current verified evidence says:
"[updated claim]"

Final decision:
Use the current verified source.

If two high-quality sources disagree:

- show both
- explain why they differ
- do not manufacture a single number

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CONFIDENCE SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use these levels:

🟢 HIGH CONFIDENCE
Directly supported by a primary or authoritative source.

🟡 MEDIUM CONFIDENCE
Supported by multiple credible sources but not directly authoritative.

🟠 LOW CONFIDENCE
Limited evidence, indirect evidence, community evidence or directional estimate.

🔴 NOT VERIFIED
Insufficient evidence.

Do not hide low-confidence information.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Now write the report.

Use exactly these sections:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 1 — EXECUTIVE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Include:

1. Problem
2. Verified evidence that the problem exists
3. Market-size signal
4. Top verified gap
5. GO / NO-GO / PIVOT recommendation
6. Confidence level

Every important factual statement must have a source.

Do not claim that the opportunity is guaranteed.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 2 — PROBLEM DEEP DIVE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Include:

- ICP
- Roles
- Company profile
- Geography
- Current workflow
- Current workarounds
- Documented pain points
- Cost of not solving
- User sentiment
- Verified user quotes or clearly labeled paraphrases

Separate:

FACTS
from
ESTIMATES
from
INFERENCES.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 3 — COMPETITIVE LANDSCAPE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create a table:

| Tool | Category | What it actually does | Pricing | Relevant capability | Evidence | Verified date | Confidence |

Only include capabilities supported by evidence.

Then classify competitors into 2–4 categories.

Then answer:

"What do these products collectively cover?"

"What remains insufficiently addressed?"

Use:

"Among the products audited..."

instead of unsupported universal claims.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 4 — VERIFIED OPPORTUNITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Rank the top 3 gaps.

For each:

1. Gap
2. Evidence
3. Existing alternatives
4. Why the gap matters
5. Users affected
6. Revenue opportunity
7. Build difficulty
8. Confidence
9. What remains unverified

Revenue numbers MUST be labeled:

- Evidence-based
- Scenario
- Estimate
- Assumption

Never label a projection as validated revenue.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 5 — PRODUCT DIRECTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MUST BUILD

Only features directly justified by verified evidence.

SHOULD BUILD

Features supported by evidence but not essential.

SKIP FOR NOW

Features that are:

- crowded
- expensive
- unvalidated
- outside the core differentiation
- dependent on unproven assumptions

For every feature explain the evidence behind the decision.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SECTION 6 — 30-DAY VALIDATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Do NOT treat the business as already validated.

The purpose of the next 30 days is to validate the remaining uncertainty.

WEEK 1 — Demand Validation

- Landing page
- Clear problem statement
- Waitlist
- Measure:
  - visitors
  - signups
  - signup conversion

Do not claim:
"50 signups = market validated."

Instead:

"50 qualified signups would be a positive demand signal."

Define:

- weak signal
- moderate signal
- strong signal

WEEK 2 — Customer Interviews

Interview at least 10 real ICP users.

Ask:

Q1:
"Tell me about the last time you downloaded or deployed an external AI model."

Q2:
"What security checks did you perform?"

Q3:
"What tools did you use?"

Q4:
"What did those tools fail to detect or explain?"

Q5:
"How much time did the current workflow take?"

Q6:
"What would make you trust a weight-level security scanner?"

Q7:
"Would you pay for it? What budget would this come from?"

Q8:
"What would prevent adoption?"

WEEK 3 — Technical Validation

Build the smallest technical prototype.

Measure:

- Detection rate
- False-positive rate
- False-negative rate where measurable
- Runtime
- Memory usage
- Model formats supported
- Attack types supported
- Attack types NOT supported

DO NOT claim:

"Detects malicious models"

unless actual tests demonstrate it.

Use:

"Detects the tested anomaly/attack class under the stated experimental conditions."

WEEK 4 — Real-World Validation

Release the prototype to real users.

Measure:

- Number of installations
- Number of real models scanned
- Number of security findings
- False positives reported
- Repeat usage
- User feedback
- Conversion intent
- Actual willingness to pay

Final decision:

GO
PIVOT
NO-GO

based on evidence collected during the 30 days.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL EVIDENCE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

At the end of the report include:

### Verified Facts

Only claims directly supported by evidence.

### Estimates

Numbers generated from assumptions or directional market research.

### Inferences

Reasoned conclusions that are not directly observed.

### Unverified Claims

Important claims that could not be independently confirmed.

### Contradicted Claims

Claims from P1-P5 that were contradicted by stronger evidence.

### Research Limitations

Explain:

- What was not checked
- What could not be verified
- Where data is incomplete
- Where competitor coverage may be incomplete
- Where market estimates are uncertain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SOURCE REGISTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Create a source table:

| ID | Source | URL | Source type | Publication date | Access/verification date | Claims supported |

Use stable URLs where possible.

Prefer:

- DOI
- Official documentation
- Official GitHub
- NVD
- Government
- Publisher
- Official company source

Do not fabricate a URL.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EVIDENCE QUALITY RULE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The final report must be less confident than the evidence, never more confident.

Example:

Evidence:
"Three audited products did not document weight-level statistical scanning."

Allowed:
"Three audited products did not document weight-level statistical scanning."

NOT allowed:
"Nobody in the industry scans model weights."

Example:

Evidence:
"One market report estimates a $3.58B AI vulnerability scanning market."

Allowed:
"One market report estimates the broader AI vulnerability scanning market at $3.58B."

NOT allowed:
"The startup's market is $3.58B."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL QUALITY GATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Before producing the final answer, run this checklist.

[ ] Every important factual claim has evidence.
[ ] Every important number has a source or is explicitly labeled an estimate.
[ ] Every competitor capability was checked.
[ ] No invented quotes exist.
[ ] No fabricated URLs exist.
[ ] Publication dates were verified.
[ ] Current information was checked.
[ ] Market size is properly scoped.
[ ] Revenue projections are labeled assumptions.
[ ] Universal claims were removed unless exhaustively proven.
[ ] Conflicting evidence is disclosed.
[ ] Unsupported claims are labeled UNVERIFIED.
[ ] Research limitations are disclosed.
[ ] GO / NO-GO / PIVOT is based on evidence, not enthusiasm.
[ ] The final language never claims guaranteed success.
[ ] The confidence level matches the evidence.

IMPORTANT FINAL RULE:

If a claim cannot be verified, DO NOT MAKE THE CLAIM.

It is better to output:

"Not verified"

than to output a precise but unsupported number.

The objective is not to make the report sound impressive.

The objective is to make the report defensible.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
OUTPUT STANDARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The final document should read like a research-backed startup diligence memo, not marketing copy.

Use precise language.

Avoid hype.

Avoid absolute statements.

Clearly distinguish:

FACT
ESTIMATE
INFERENCE
UNVERIFIED
CONTRADICTED

The final report must be reproducible by another researcher following the cited sources.

```

---

## 🗂️ How to Use

1. Compile P1-P5 exactly as before.
2. Turn **Web Search ON**.
3. Turn **Extended Thinking ON**.
4. Paste the entire P6 prompt.
5. Let Claude finish the evidence audit before generating the final report.
6. Never remove the **Final Evidence Summary**, **Source Register**, or **Quality Gate**.
7. Before sharing externally, inspect the sources for the 5–10 most important claims.

---

## ✅ What This Version Fixes

Your old P6 effectively did:

**P1 → P2 → P3 → P4 → P5 → synthesis**

The new P6 does:

**P1 → P2 → P3 → P4 → P5 → independent verification → contradiction check → evidence classification → final report**

That is the major upgrade.

Most importantly, the model is now explicitly forbidden from turning claims like:

> "500K+ repositories"

> "0/10 tools"

> "$8–12M ARR"

> "90%+ survival"

into facts unless the evidence actually supports them.

It must instead distinguish something like:

**VERIFIED:** directly supported by the source
**ESTIMATE:** calculated/modelled
**INFERENCE:** reasoned conclusion
**UNVERIFIED:** insufficient evidence
**CONTRADICTED:** stronger evidence says otherwise

That makes the report **defensible and auditable**, rather than merely convincing.
