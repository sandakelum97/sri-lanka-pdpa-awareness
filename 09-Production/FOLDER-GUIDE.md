# 09-Production — where every production asset lives

One tree for everything that is not website code or legal research. Flow: **brief/script → generated draft → review → approved final**. Nothing is published from `02-generated-drafts/`.

```
09-Production/
├── README.md                 Brand rules + legal guardrails (paste into every generation prompt)
├── TOOLS-AND-PIPELINE.md     Which tools for what; the video pipeline; why text-free footage
├── FOLDER-GUIDE.md           This file
├── 00-brand/                 Logo set (mark, light, dark), name decision
├── 01-scripts-and-briefs/    Everything a human or tool needs BEFORE generating
│   ├── video-60s/            V01–V12: VO (EN + SI draft), on-screen text, shot list, Sinhala cover block
│   ├── podcast/              Episode briefs for NotebookLM / human recording
│   ├── infographics/         Briefs I07–I14
│   ├── presentations/        Deck outlines (slide-by-slide)
│   ├── pdf-guides/           Printable guide specs
│   ├── posters/              Counter cards, awareness posters
│   ├── photos-and-drawings/  Shot lists for photography; illustration briefs
│   └── tables-and-charts/    Data tables and chart specs (source: status.json, section matrix)
├── 02-generated-drafts/      Raw output from Gemini, NotebookLM, Veo, Canva, cameras — by type, dated
│   └── video | audio | images | infographics | presentations | pdf | photos | drawings | tables
├── 03-approved-finals/       Only files that passed 05-review; same sub-folders; these feed the website
├── 04-pipeline/              cards.py, render.py, fonts, rendered cards/captions, timeline JSONs
└── 05-review/                media-qa.md — one row per asset, six checks, reviewer, result
```

## File naming
`YYYY-MM-DD_<tool>_<slug>-<LANG>.<ext>` for drafts (e.g. `2026-10-31_gemini_roadmap-EN.png`).
`<ID>-<slug>-<LANG>.<ext>` for finals, where ID is the script/brief ID (e.g. `V02-is-the-law-in-force-EN.mp4`, `I08-special-categories-SI.png`).

## Rules
1. Never delete from `02-generated-drafts/`; move to `03-approved-finals/` or leave with a note in `05-review/`.
2. Every final has a row in `05-review/media-qa.md` with the six legal checks ticked.
3. Sinhala text in any asset comes from the glossary or a reviewed script — never from the generator's own translation.
4. Git tracks everything here (large binaries included for now; move to Git LFS if the repo passes ~500 MB).
