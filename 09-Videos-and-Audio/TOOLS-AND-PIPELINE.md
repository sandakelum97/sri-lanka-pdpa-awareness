# Video, audio and image production — what works, what doesn't, and the pipeline

Reviewed 31 Oct 2026 against the first assets in `Generated Once (In Progress)/`.

## Verdict on the first batch
| Asset | Verdict | Why |
|---|---|---|
| `Sri_Lanka_PDPA_Implementation_Roadmap.png` (Gemini) | **Usable** after two edits | Legally correct split (2027 vs no date). Replace "Gemini Notebook" watermark area and add DataSavi footer. |
| `ශ්‍රී_ලංකා_දත්ත_ආරක්ෂණ_පනත.png` (Gemini) | **Usable** after two edits | Sinhala is correct and natural. Footer still says `magedatta.lk` and `<date>` was not replaced. |
| `Sri_Lanka_s_2027_Data_Protection_Deadline.m4a` (NotebookLM, 7 min) | Review the transcript before use | Listen for: "fully in force", "18 March 2025", "72 hours", "Rs 10 m fine for a breach". Any of these = re-generate with the guardrail text. |
| three `gemini_generated_video_*.mp4` (10 s, 720p 24 fps) | **Not usable as-is** | Every piece of on-screen text is garbled ("Bech date terd.", a fabricated handle). Generative video cannot render words reliably. Footage itself is good. |

## The rule that fixes video
**Never let the generator draw text.** Generate text-free B-roll only (prompt: "no text, no captions, no signs, no labels, no watermark"), then add every word in post with the pipeline below, which uses our own fonts and shapes Sinhala correctly.

## Pipeline (in `build/`)
1. `cards.py spec.json outdir` — renders 1080×1920 title/explainer cards and caption strips as PNGs. Uses Pillow + Raqm so Sinhala ligatures (ක්‍රි, ද්ධ…) are correct and punctuation falls back to Latin. Brand palette and status badges built in.
2. `render.py timeline.json` — assembles cards and B-roll clips (scaled/cropped to 9:16, slow push-in, dark band for captions), burns captions, concatenates with `-c copy`, muxes a voice-over if given, and writes a **WebVTT** sidecar with the same timings.
3. Output: `<name>.mp4` + `<name>.vtt`. The site's video player shows the VTT in a side panel with clickable timestamps (and as closed captions), so a Sinhala or English transcript can sit beside a video even when the video is in the other language.

First proof: `video/V02-is-the-law-in-force-EN.mp4` (56 s, cards only until text-free B-roll is regenerated) + `.vtt`.

## Recommended tools (October 2026 — verify current pricing/availability)
**Voice-over, English and Sinhala**
- ElevenLabs — best natural Sinhala TTS currently available (Sinhala is in its multilingual model); clone a consented volunteer voice for consistency. Export WAV 48 kHz.
- Google Cloud Text-to-Speech (si-LK WaveNet/Neural2 voices) — cheaper, serviceable, good for drafts.
- A real Sinhala speaker recorded on a phone in a quiet room beats both for trust. Audacity for cleanup (noise reduction, normalise to −16 LUFS).
- NotebookLM audio overviews: good for the English podcast episodes; do not use for Sinhala.

**B-roll video (text-free)**
- Google Veo via Gemini / Flow, Runway Gen-4, Kling, Pika — all fine for 5–10 s text-free clips. Prompt for Sri Lankan settings explicitly (kade, three-wheeler, tuition hall, BMICH) and "no text anywhere in frame".
- Pexels / Pixabay / Mixkit — free licensed stock footage; search "Sri Lanka street", "pharmacy counter", "classroom".
- Our own SVG infographics animated in **Canva** or **CapCut** — cleanest for the explainer sections.

**Editing and captions**
- CapCut (free, desktop/mobile): auto-captions in English; import our `.vtt`/`.srt` for Sinhala instead of auto; brand kit for colours and Noto fonts.
- DaVinci Resolve (free): for anything longer than 60 s; subtitle track import.
- This repo's `render.py` for batch, repeatable output straight from the reviewed scripts.

**Images and infographics**
- The six SVGs in `11-Website-Development/site/public/img/` are the masters — restyle in Figma or Canva rather than regenerating.
- Gemini / Nano Banana for illustrations and icon sets; always "no text", then add text in Canva with Noto Sans Sinhala.
- For charts: the dataviz skill in this repo's Claude workflow, or Datawrapper.

**Podcast**
- NotebookLM audio overview (EN) → review transcript → Audacity trim → publish via RSS (e.g. Spotify for Creators, free) and embed on the site with a transcript.
- For Sinhala episodes: script in `podcast/`, read by a human or ElevenLabs, never machine-dubbed.

## Sinhala "cover" text for every script
Each script in `scripts-60s/` gets a `## Cover (SI)` block: title, one-line hook, three on-screen lines, end-card text. See V01–V12.

## Legal QA before any asset ships
Tick in `13-Reviews-and-Approvals/media-qa.md`: (1) no "fully in force"; (2) no 18 March 2025 as a start date; (3) no "72 hours"; (4) fines described as directive-linked and not in force; (5) DataSavi footer with check date; (6) Sinhala read aloud by a native speaker once.
