# Website prototype (Phase 3)

Static site built with [Astro](https://astro.build). Content is **not** stored here — the pages render the Markdown in `07-English-Content/` and the status data in `06-Legal-Research/data/status.json` directly, so content review stays a Git/PR process and the site never drifts from the research repository.

## Stack and why
| Need (brief §10) | Choice | Reason |
|---|---|---|
| Responsive frontend | Astro, plain CSS | Static HTML, no JS framework needed for content pages; fast on low-end phones |
| Backend / CMS | Git + pull requests (optionally Decap CMS later) | Human review gate before publish, full change history, free |
| Search | Pagefind | Client-side, works offline, no query ever leaves the browser |
| Bilingual | Astro i18n routing (`/en/`, `/si/`), Tamil-ready (`/ta/`) | Same slug per language; language switch keeps you on the same page |
| Multimedia hosting | Static assets + an external video host (to decide in Phase 4) | |
| Database | None | Nothing to breach; health-check tool will run client-side |
| SEO | Static HTML, per-page meta, sitemap (to add) | |
| Analytics | None by default; self-hosted Umami if ever needed | No cookies, no third-party trackers |
| Accessibility | Semantic HTML, skip link, contrast-checked palette, keyboard nav | Audit in Phase 6 |
| Backup / DR | The Git repository is the backup; rebuild from source anywhere | |
| Security monitoring | No server to monitor; dependency updates via Dependabot | |
| Hosting | GitHub Pages or Cloudflare Pages (free) | Workflow included for GitHub Pages |

## Run locally
```
cd 11-Website-Development/site
npm install
npm run dev        # http://localhost:4321
npm run build      # outputs dist/ and runs Pagefind
```

## Status badges
`src/lib/status.ts` reads `06-Legal-Research/data/status.json`. Every badge, the home-page notice and the `/status/` tracker render from it. When a new Gazette is published, update that file first.

## Fonts
Self-host Noto Sans and Noto Sans Sinhala under `public/fonts/` before launch (do not load from Google Fonts — avoids a third-party request on every page view).

## Not yet built
Sinhala content pages (blocked on review), sitemap/robots, self-hosted fonts, the small-business health-check tool, video embeds, the AI assistant (Phase 5).
