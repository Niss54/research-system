# Phase 1: Problem Space Validation (Grounded Audit)

## Problem Hypothesis
**Stated Problem:** Families struggle to identify, claim, and transfer a deceased person's financial and physical assets because succession procedures are fragmented across multiple institutions, each requiring different documentation, verification, and follow-up processes. These complexities can delay access to legitimate inheritance, particularly when nominations are missing, asset records are incomplete, or legal disputes arise.

**Target Audience (ICP):** Surviving adult heirs, nominees, surviving spouses, and appointed estate executors in urban India.
**Geographic Scope:** India-first (expanding to common-law jurisdictions).

---

## 🔍 Critical Dimensionality Check: Pre-Death vs Post-Death
> **CRITICAL ARCHITECTURAL BOUNDARY:**
> We explicitly separate **Pre-Death Estate Planning** (Will generation, trust formation, pre-death asset cataloging) from **Post-Death Succession & Asset Transfer** (bereavement claim submission, institution-by-institution transfer, legal heir certificates, court probate).
> This research is **100% focused on Post-Death Estate Settlement**. It does NOT pivot to an AI Will generator.

---

## 📊 Evaluation Across Core Dimensions

### 1. Frequency: Life-Event / Episodic with Extreme Duration
- **Individual User Level:** Infrequent / Once in 5–15 years per family.
- **Duration of Pain:** Very High (6 to 18 months of recurring administrative friction, branch visits, and notary paperwork).
- **Macro Market Inflow:** Approximately **9.5 Million deaths annually in India**, of which an estimated **2.5–3 Million urban families** hold formal financial assets (bank deposits, demat shares, mutual funds, EPF, life insurance, and real estate).

### 2. Severity: 7.5 / 10 (Direct Financial Lockup)
- **Financial Paralysis:** When the sole earner or family patriarch passes away, bank accounts without survivorship clauses ('Either or Survivor') are frozen immediately upon notification.
- **Unclaimed Assets Scale:** Over **₹1,00,000 Crore ($12B+)** in unclaimed bank deposits, insurance proceeds, and dividends lie with RBI's UDGAM portal and the Investor Education and Protection Fund (IEPF), heavily driven by heirs being unaware of assets or giving up due to procedural complexity.

### 3. Willingness to Pay: PARTIAL (Unproven for Pure DIY Software)
- Families routinely pay ₹25,000 to ₹1,50,000 to offline estate lawyers and touts for obtaining Legal Heir Certificates and Succession Certificates.
- However, consumer willingness to pay for a standalone automated digital checklist without human execution is unproven. **Yellow SMART** offers an entry tier at ₹500/year remote, scaling to premium on-ground legal assistance.

---

## 🏛️ Evidence Ledger

<!-- BEGIN P1_HANDOFF -->
PROBLEM_STATEMENT: Families struggle to identify, claim, and transfer a deceased person's financial and physical assets because succession procedures are fragmented across multiple institutions, each requiring different documentation, verification, and follow-up processes.
TARGET_AUDIENCE: Surviving heirs, nominees, and executors in urban India handling deceased estates with financial assets.
FREQUENCY: Episodic (Once in 5-15 years per family; 2.5M+ urban deaths annually in India with 6-18 months active case duration)
FREQUENCY_EVIDENCE: SBI deceased claim guidelines, RBI annual banking complaints reports, Registrar of Deaths data.
SEVERITY: 7.5/10 — direct capital freeze of Rs 5L to 50L per household for 6-18 months.
SEVERITY_EVIDENCE: Over Rs 1,00,000 Crore lying in unclaimed deposits (RBI UDGAM) and IEPF due to succession procedural abandonment.
WILLINGNESS_TO_PAY: Partial — proven spend on offline lawyers (Rs 25k-1.5L), but digital SaaS payment intent remains unvalidated.
WTP_EVIDENCE: Commercial adoption of Yellow SMART (Rs 500/yr remote plan + on-ground legal fees) and WillJini estate services.

KEY_SOURCES:
- https://sbi.bank.in/en/web/personal-banking/information-services/deceased-settlement — SBI Deceased Settlement Policy
- https://www.sebi.gov.in/legal/circulars/sep-2025/ease-of-doing-investment-smooth-transmission-of-securities-from-nominee-to-legal-heir_96711.html — SEBI Securities Transmission Circular
- https://rbikehtahai.rbi.org.in/nomination-and-settlement.html — RBI Nomination & Deceased Claim Guidance
- https://www.getyellow.in/yellow-smart — Yellow SMART Post-Demise Services

VERDICT: CONTINUE DISCOVERY 🟡 (MAYBE ⚠️)
VERDICT_REASONING: Problem existence and regulatory friction are conclusively verified by official circulars. However, customer willingness to pay for software vs offline legal assistance is not yet proven. Do NOT declare GO yet.
KEY_PAIN_SIGNALS:
- Nominee status does NOT confer absolute ownership; banks require extensive indemnities and legal heir consents.
- Mutual funds (CAMS/KFintech), demat (CDSL/NSDL), EPF, and banks require separate physical stamp papers and notarized affidavits.
- Severe emotional vulnerability makes navigating bureaucratic branch managers traumatic.
<!-- END P1_HANDOFF -->
