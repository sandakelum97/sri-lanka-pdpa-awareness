# Printable PDF guides

A4, DataSavi brand, Noto fonts, bilingual where marked. Footer on every page: "Checked against the official Gazettes on <date> · datasavi.lk · Not legal advice · Not the Data Protection Authority". Version and review status on the cover.

| ID | Guide | Pages | Source | Languages |
|---|---|---|---|---|
| G01 | Small Business Guide + Checklist | 12 | pathways/small-business-guide.md, small-business-checklist.md | EN, SI |
| G02 | Your Data, Your Rights — citizen handout | 4 | pathways/citizen-pathway.md | EN, SI |
| G03 | What is in force? — the one-page status sheet | 1 | status.json, status-timeline.svg | EN, SI, TA |
| G04 | Organisational Compliance Guide | 24 | pathways/organisation-pathway.md | EN |
| G05 | Glossary | 6 | glossary | EN/SI side by side |
| G06 | The twelve scenarios — booklet | 28 | scenarios/*.md | EN, SI |
| G07 | Privacy notice template (Schedule V) | 2 | s11-transparency.md | EN, SI, TA |
| G08 | Breach response one-pager | 1 | s23 + breach-steps.svg | EN, SI |

Production: export from the website content via Pandoc/Typst or lay out in Canva/InDesign. The repo's `anthropic-skills:pdf` skill can generate G03, G07 and G08 directly from Markdown.
