# Project Tracker — Sri Lanka PDPA Awareness & Education Platform

Last updated: 31 Oct 2026 (v1.2) · Current phase: Phase 1 (Legal Research and Foundation)

## Milestone 1 — Verified Legal Research Repository

Target: close all P1-related open questions and have every official document stored locally with checksums.

| # | Task | Status | Output |
|---|---|---|---|
| 1.1 | Identify principal Act and all amendments | Done | LEGAL-DOCUMENT-REGISTER.md §A |
| 1.2 | Identify all commencement Orders | Done | Register §B |
| 1.3 | Identify circulars, drafts, official pages | Done | Register §C–E |
| 1.4 | Establish commencement position at research date | Done | COMMENCEMENT-STATUS.md |
| 1.5 | Section-by-section reference matrix | Done (v1.0) | SECTION-REFERENCE-MATRIX.md |
| 1.6 | Download and preserve all official PDFs (EN/SI/TA) with SHA-256 | Done 31 Oct 2026 — 30 PDFs fetched and content-checked; the two documents.gov.lk duplicate copies failed (host not allow-listed at the time) — re-run the script after allow-listing | folders 01–05 + 14-Project-Documentation/CHECKSUMS.txt |
| 1.7 | Read GAZ-01, CIR-01, all seven drafts in full; record summaries | Done for GAZ-01 and DRF-01–07 (31 Oct 2026); CIR-01 archive-only, not read | 06-Legal-Research/draft-instrument-summaries.md |
| 1.8 | Sinhala-text verification of all P1 sections | Pending (needs bilingual legal reviewer) | text-discrepancies.md |
| 1.9 | Close open questions OQ-01 to OQ-15 | Pending | OPEN-QUESTIONS.md |
| 1.10 | Human legal review sign-off of Phase 1 | Pending | sign-off note in this file |

## Decisions log

| Date | Decision | Rationale |
|---|---|---|
| 2026-10-31 | Owner deferred legal review to a later stage; content continues as 'draft / unreviewed' and nothing is published until review. | Owner instruction. |
| 2026-10-31 | **Provisionally adopted by default, pending owner confirmation:** (a) three-value commencement status model IN / 2027 / NO rendered from one `status.json`; (b) FEATURE-SPECS-v0.1 treated as approved for planning; (c) all Sinhala content carries 'unverified' status until a bilingual legal reviewer signs off. | Owner asked to proceed; no objection raised. |

### Earlier decisions

| Date | Decision | Rationale |
|---|---|---|
| 2026-10-31 | Only documents on dpa.gov.lk, parliament.lk or documents.gov.lk count as official. | Project brief §2. |
| 2026-10-31 | Commencement status is a mandatory field on every content item; statuses: IN / 2027 / NO. | Avoid describing unenforceable provisions as binding. |
| 2026-10-31 | Draft instruments are stored under `draft-instruments/` and always labelled "DRAFT — not law". | Project brief §2. |
| 2026-10-31 | The DPA's own outdated pages (est.php, Background.php) are not used as authority for dates. | Superseded by GAZ-03/GAZ-04. |
| 2026-10-31 | Adopted the 14-folder structure proposed by the project owner; three differentiating features ('What does this mean for me?', 'PDPA in 60 seconds', 'Small Business Privacy Health Check') specified in 11-Website-Development/feature-specs/FEATURE-SPECS-v0.1.md, pending approval. | Owner's recommendation, 31 Oct 2026. |
| 2026-10-31 | Section numbering on the site follows the Act as amended; original text shown in a collapsible "Before the 2025 amendment" block where changed. | Project brief §2 (distinguish Act from amendments). |

## Issues / risks

| ID | Issue | Impact | Mitigation |
|---|---|---|---|
| R-01 | Parts II, IV, VII have no date; a further Order could issue at any time. | Content may go stale overnight. | Monitoring process (14-Project-Documentation/monitoring); commencement badges rendered from a single data file. |
| R-02 | Draft rules may be re-issued with different numbers/content. | Compliance guide may mislead. | Never state draft numbers (e.g. 72 h) as requirements. |
| R-03 | Sinhala text prevails; English-only research. | Legal inaccuracy in Sinhala content. | OQ-03; bilingual reviewer before Phase 2 sign-off. |
| R-04 | Workspace cannot download from dpa.gov.lk. | Resolved 31 Oct 2026 — script run natively on Windows. | documents.gov.lk still to be allow-listed for the two duplicate copies. |
| R-05 | Sinhala/Tamil 2022 Act PDFs are legacy-font, not Unicode (OQ-18). | Sinhala glossary and EN/SI verification cannot be done by text extraction. | Legacy→Unicode conversion or OCR, reviewer spot-check. |

## Phase 2 — started 31 Oct 2026

| # | Task | Status | Output |
|---|---|---|---|
| 2.1 | Bilingual glossary from s.56 definitions | v0.1 drafted — 20 Sinhala terms read from official Unicode texts, 12 pending OQ-18; reviewer sign-off pending | 07-English-Content/glossary/GLOSSARY-bilingual-v0.1.md |
| 2.2 | Plain-English explanations for Part I and Part III (status 2027) | v0.1 drafted 31 Oct 2026 — 16 section files + index, unreviewed | 07-English-Content/sections/ |
| 2.2b | ss.2–3 and the not-in-force Parts II, IV, VII | v0.1 drafted 31 Oct 2026 — 13 section files, unreviewed | 07-English-Content/sections/ |
| 2.3a | Twelve everyday scenarios | v0.1 drafted 31 Oct 2026, unreviewed | 07-English-Content/scenarios/ |
| 2.3b | 'Who is the DPA' page (Part V) | v0.1 drafted 31 Oct 2026 | 07-English-Content/sections/s28-35-who-is-the-dpa.md |
| 2.3c | Small-business pathway and guide | Not started | 07-English-Content/pathways/ |
| 2.4 | FAQ | Not started | 07-English-Content/faq/ |
| 2.5 | Sinhala explanations | Blocked on reviewer + OQ-18 | 08-Sinhala-Content/ |

## Next steps (proposed)

1. Run the download script and commit the PDFs + checksums.
2. Read the seven drafts and GAZ-01; fill in draft-instrument-summaries.md.
3. Resolve OQ-01, OQ-04, OQ-05, OQ-08 online; park OQ-02/03/06/11 for the legal reviewer.
4. Present Milestone 1 for review, then start Phase 2 with the glossary (s.56 definitions, EN/SI) and the small-business pathway built on Part I + Part III (2027) with Part II/IV/VII clearly marked "not yet in force".
