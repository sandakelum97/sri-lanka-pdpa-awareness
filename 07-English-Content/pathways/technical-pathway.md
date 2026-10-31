---
title: "PDPA for IT, security and engineering professionals"
slug: technical-pathway
language: en
type: pathway
audience: [technical, it-admin, security, developer, sysadmin]
sections_cited: "s.56; s.10; s.12; s.18; s.21; s.22; s.23; s.24; s.26; s.32"
commencement_status: "mixed"
sources: [ACT-01, ACT-02, GAZ-04, DRF-01, DRF-02, DRF-03]
content_version: 0.1
last_reviewed: 2026-10-31
reviewed_by: none
review_status: draft
---

*What the Act actually requires of systems, and what it leaves to you. Legal requirements are cited; everything else is engineering judgement.*

## 1. Definitions that drive design
- **Personal data** includes online identifiers and location data (s.56) — IP addresses, device IDs, cookies, GPS traces are in scope.
- **Anonymise** = permanent removal of identifiers so data cannot be related to a person; **pseudonymisation** = identifiers replaced, with the key kept separately under technical and organisational measures (s.56). Pseudonymised data is still personal data.
- **Processing** covers every operation including storage, retrieval, transmission, erasure and "logical or arithmetical operations" (s.56) — backups, logs, analytics and model training are processing.
- **Personal data breach** includes accidental loss and alteration, not only exfiltration (s.56).
- **Third country** = anywhere outside Sri Lanka (s.56 as amended) — every foreign region in a cloud console is a cross-border flow.

## 2. Security (s.10) — what is law and what is not
Law: "appropriate technical and organizational measures including encryption, pseudonymisation, anonymisation or access controls or such other measures as may be prescribed" to prevent unauthorised/unlawful processing and loss, destruction or damage. No standard, baseline or control set is prescribed as at 31 Oct 2026.
Not law (recommended): CIS/ISO 27001-aligned baselines; encryption at rest and in transit; MFA; least privilege; logging and monitoring; secure SDLC; patch management; backup and restore testing. On the site these are always labelled as recommendations.

## 3. Accountability records (s.12)
The DPMP must keep "duly catalogued records" demonstrating compliance with ss.5–11 and include breach-detection and complaint mechanisms. Engineering implications: data inventories and system catalogues are evidence; logging that can show access and retention is evidence; the Authority may inspect (s.32(b)) and evaluate your programme (s.32(h)).

## 4. Breach handling (s.23)
The notification form, content and deadline are reserved to rules not yet made. The 2024 draft (DRF-02) proposed 72 hours to the Authority with simultaneous notice to affected people in high-risk cases, risk-assessment factors, and a presumption of low risk where data is encrypted with uncompromised keys or recoverable from backup — useful for designing incident response, but a draft. Build: detection, triage, containment, a breach register (also a DPMP item), and notification templates to be finalised when rules issue.

## 5. DPIAs (s.24) and risk mitigation (s.25)
Triggers: systematic and extensive evaluation/profiling; systematic monitoring of publicly accessible areas or telecom networks; rule-defined activities. Re-assess on any change of "methodology, technology or process" (s.24(4)) — i.e. on major releases. Submit to the Authority on request (s.24(5) as amended). The draft template (DRF-01) maps each Part I obligation and Part II right to risks and safeguards, with a 5×5 matrix; use its structure, label it draft.

## 6. Processors, sub-processors and contracts (ss.21–22)
If you build or operate on behalf of a controller you are a processor: act only on written instructions; bind personnel to confidentiality; support audits; return or erase at exit; flow the same duties to sub-processors (s.22(3)) and carry liability for them (s.22(4)). If you decide purposes and means yourself, you become a controller (s.22(2)). Engineering: tenant isolation, instruction logs, deletion-on-termination that actually completes (including backups within a stated window).

## 7. Cross-border architecture (s.26 as amended)
Transfers permitted when the organisation keeps complying with Parts I–III for the data and adopts Authority-specified instruments (directive pending), or under s.26(3) exceptions (explicit informed consent; contract necessity; legal claims; public interest; emergency; transit). Design: a transfer register per system/region; provider data-processing terms; data residency options where offered; be ready to document a transfer impact assessment (DRF-03 structure, draft). Public authorities: watch for the Minister's prescribed categories (s.26(5)).

## 8. Automated decisions and AI (s.18)
A data subject may request human review of a decision based solely on automated processing with an "irreversible and continuous impact" on rights under the Constitution or any written law (not in force). Exceptions (law, Authority-determined manner, consent, contract) still require Authority safeguard rules, and the contract exception excludes special-category data. Design: human-in-the-loop paths for consequential decisions; logging of model inputs/outputs; ability to explain "the logic involved" (Sch V item 1(m)).

## 9. Privacy by design checklist (recommended)
- Data minimisation at schema level; retention and deletion jobs; pseudonymisation for analytics; field-level encryption for special categories; access logging; consent and preference storage with timestamps and wording; export tooling for future access requests (s.13); correction and deletion workflows (ss.15–16); region-aware storage; vendor inventory with DPA terms.

## 10. Watch list
- Rules on breach notification (s.23), DPIA form (s.24), DPO thresholds (s.20), rights procedures (s.52(1)(d)), security measures "as may be prescribed" (s.10).
- Directive on cross-border instruments (s.26(2)).
- Guidelines under s.51A (DPMP, sectoral, DPO risk categories).
- Commencement Orders for Parts II, IV, VII.
