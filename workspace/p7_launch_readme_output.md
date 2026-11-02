# InheritFlow — The Cross-Institution Estate Settlement Copilot

> Navigating the loss of a loved one is devastating. Navigating bank bureaucracy shouldn't make it unbearable.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-10b981?style=for-the-badge)](LICENSE)
[![Built by Nisha](https://img.shields.io/badge/Research%20by-Nisha%20(Nissh)-6366f1?style=for-the-badge)](https://nissh.info)
[![Status: Discovery Phase](https://img.shields.io/badge/Status-Continue%20Discovery%20(MAYBE)-f59e0b?style=for-the-badge)](workspace/COMPLETE_RESEARCH_DOSSIER.md)

---

## 🎯 What is InheritFlow?
**InheritFlow** is an evidence-backed estate settlement and asset transfer platform designed for families in India. Instead of making 25 trips to 8 different bank branches, depositories, and registrar offices, InheritFlow consolidates deceased claims into a unified, verified workflow.

---

## 📊 Post-Launch Validation & PostHog Telemetry Spec
Upon launching the MVP pilot, track real user behavior to validate if the product solves the core administrative bottleneck:

| Event Name | Trigger Condition | Validation Metric |
|---|---|---|
| `estate_created` | User initiates a new deceased estate case | Inflow demand |
| `asset_inventoried` | User logs a bank account, mutual fund, or property | Average assets per family (Benchmark: 4.5) |
| `claim_packet_generated` | Pre-filled bank claim form and indemnity bond downloaded | Core product utility |
| `branch_friction_reported` | User flags that a branch manager rejected a valid nominee form | Regulatory friction heat-map |
| `lawyer_escalation_requested` | User requests legal help for Succession Certificate or Probate | Monetization conversion trigger |
| `asset_settled_completed` | Funds successfully credited to legal heir's account | Ultimate North Star Metric (Days to Settlement) |

---

## 📋 30-Day Discovery & Pilot Roadmap
- [x] Phase 1–6 Grounded Market Research & Competitor Audit Complete (Yellow SMART, EstateExec benchmarked)
- [ ] Conduct 15 interviews with heirs who settled estates in 2025–2026
- [ ] Build bank form generator for top 5 banks (SBI, HDFC, ICICI, Axis, Zerodha)
- [ ] Pilot with 10 bereaved families in Bangalore & Delhi NCR
- [ ] Establish lawyer escalation network for Succession Certificates
