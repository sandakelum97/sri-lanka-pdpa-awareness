# Production pack — videos, podcast audio, infographics

For use with Gemini (image and video generation), NotebookLM (audio overviews / podcast-style explainers) and similar tools. Everything here was written from the research repository; nothing in it may be changed by a generator without a human re-checking it against `06-Legal-Research/COMMENCEMENT-STATUS.md`.

## Brand to use in every asset
- Name: **දත්ත සවිය · DataSavi** — "an independent public-education initiative".
- Colours: lagoon green #0F6E6B, mango yellow #F2B33D, ink #14213D, white. Never Sri Lankan flag colours or any government emblem.
- Type: Noto Sans / Noto Sans Sinhala.
- Every video and infographic ends with: "Checked against the official Gazettes on <date> · datasavi.lk (placeholder) · Not legal advice · Not the Data Protection Authority".

## Legal guardrails (paste these into every generation prompt)
1. The Act is only partly in force. Duties on businesses start 1 January 2027. Individuals' rights (Part II), marketing-message rules (Part IV) and penalties (Part VII) have no start date. Never say or imply the Act is fully in force.
2. Never say "18 March 2025" as a start date; it was repealed.
3. Never state "72 hours" for breach reporting as law; no deadline exists yet.
4. Never say "Rs 10 million fine for a data breach"; the penalty is for ignoring an Authority directive, and Part VII is not in force.
5. Do not invent rights, deadlines, exemptions or thresholds. If a figure is not in the script, do not add one.
6. Do not use the DPA's logo, the national emblem, or the word "official".
7. Sinhala: natural spoken Sinhala, not machine translation; use the terms in `07-English-Content/glossary/GLOSSARY-bilingual-v0.1.md`.

## Hard rule for video generators
Generate **text-free** footage only — add every word in post (see TOOLS-AND-PIPELINE.md). Prompt suffix: "no text, no captions, no signs, no labels, no logos, no watermark".

## Workflow
1. Generate from the script/brief.
2. A human checks the output against the script and the guardrails (tick the box in `13-Reviews-and-Approvals/`).
3. Save finals under `09-Videos-and-Audio/audio|video/` or `10-Infographics-and-Presentations/` with the script ID in the file name.
4. Re-record, don't patch, when the legal status changes — shared WhatsApp videos cannot be recalled, so every video carries its check date.

## What to upload to NotebookLM as sources
- `06-Legal-Research/COMMENCEMENT-STATUS.md`
- `06-Legal-Research/draft-instrument-summaries.md`
- `07-English-Content/faq/faq.md`, `pathways/small-business-guide.md`, `pathways/citizen-pathway.md`
- The relevant `07-English-Content/scenarios/*.md` for the episode
- The official Act PDFs from `01-Original-Legislation/` and `02-Amendments/` (English)
Do **not** upload third-party law-firm articles; they contain the errors the guardrails exist to prevent.
