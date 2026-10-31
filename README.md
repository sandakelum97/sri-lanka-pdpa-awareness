# Sri Lanka PDPA Awareness Project — Research Repository

Independent public-interest education initiative explaining the Personal Data Protection Act, No. 9 of 2022 (as amended by Act No. 22 of 2025). Not affiliated with the Government of Sri Lanka or the Data Protection Authority.

Goal of Phase 1: the most trustworthy, understandable and accessible independent educational resource on the Act — built on a complete, verified legal source library before any website design.

## Folder structure

```
Sri-Lanka-PDPA-Awareness-Project/
├── 01-Original-Legislation/          Act No. 9 of 2022 (EN, SI, TA; DPA + Parliament + Govt Printer copies). Never edited.
├── 02-Amendments/                    Act No. 22 of 2025 (EN, SI, TA)
├── 03-Gazettes-and-Commencement/     Extraordinary Gazettes 2341/59, 2366/08, 2427/34, 2498/16 (EN, SI, TA)
├── 04-Regulations-and-Rules/
│   ├── drafts-2024/                  Seven consultation drafts — NOT LAW
│   └── final/                        (empty — nothing gazetted as at 31 Oct 2026)
├── 05-DPA-Guidelines-and-Circulars/  Circulars 01/2024 (superseded) and 01/2026
├── 06-Legal-Research/
│   ├── LEGAL-DOCUMENT-REGISTER.md    Master register (IDs ACT-, GAZ-, CIR-, DRF-, WEB-)
│   ├── COMMENCEMENT-STATUS.md        Provision-by-provision status tracker (IN / 2027 / NO)
│   ├── SECTION-REFERENCE-MATRIX.md   Every section: title, amendment, status, priority, audience, research tasks
│   ├── draft-instrument-summaries.md What each 2024 draft says and how the 2025 amendment affects it
│   ├── OPEN-QUESTIONS.md             Verification backlog (OQ-xx)
│   ├── secondary-sources/            Law-firm notes, news — for locating, never for citing
│   └── related-laws/                 RTI Act, Online Safety Act, CBSL regulations etc. (to collect)
├── 07-English-Content/               glossary/ scenarios/ faq/ pathways/ health-check/
├── 08-Sinhala-Content/               same slugs as 07, Sinhala text
├── 09-Videos-and-Audio/              scripts-60s/ audio/ subtitles/
├── 10-Infographics-and-Presentations/
├── 11-Website-Development/           design/ src/ cms/ feature-specs/ (FEATURE-SPECS-v0.1.md)
├── 12-AI-Knowledge-Base/             chunks/ (versioned, citation-bearing) evaluation/
├── 13-Reviews-and-Approvals/         Legal and Sinhala review sign-offs, one file per content release
└── 14-Project-Documentation/         PROJECT-TRACKER.md, download scripts, CHECKSUMS.txt, monitoring/legal-update-log.md
```

## Getting the official documents

Run `14-Project-Documentation/download-official-sources.sh` (Linux/macOS) or `.ps1` (Windows). It fetches all 33 official PDFs into folders 01–05 and writes SHA-256 checksums.

## Content metadata (required on every published item)

```
title, slug, language, audience, sections_cited, amendment_refs, commencement_status (IN | 2027 | NO),
sources (register IDs), content_version, last_reviewed, reviewed_by, review_status (draft | legal-reviewed | published)
```

## Ground rules

1. Official sources first (dpa.gov.lk, parliament.lk, documents.gov.lk). Secondary sources only to find them.
2. Every legal statement carries a section number, amendment reference and register ID.
3. Commencement status is shown on every page, from one `status.json`; "in the Act" is not "in force".
4. Drafts are always labelled as drafts.
5. Sinhala text prevails over Tamil; the English text is not the authoritative text — contested wording is checked against the Sinhala Act.
6. No AI-generated legal content or update is published without human review recorded in 13-Reviews-and-Approvals.
7. The site itself collects no unnecessary visitor data (no accounts, no third-party trackers, self-hosted privacy-respecting analytics at most).
