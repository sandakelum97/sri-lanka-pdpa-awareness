# CapCut or DaVinci Resolve — assembling a 60-second video by hand (alternative to our render.py)

1. New project 1080×1920, 30 fps.
2. Import: the B-roll clips (02-generated-drafts/video/Vxx-broll-*.mp4), the voice-over (02-generated-drafts/audio/Vxx-EN.wav or -SI.wav), and the title/caption PNGs from 09-Production/04-pipeline/cards/vxx-xx/ (these already have correct Sinhala shaping and brand colours).
3. Lay the voice-over first. Place cards and clips to match the timings in 09-Production/04-pipeline/vxx-timeline.json (or by ear: one idea per shot).
4. Captions: import 02-generated-drafts/video/Vxx-xx.vtt as a subtitle track (CapCut: Text → Captions → Import; Resolve: File → Import → Subtitle). Do NOT use auto-captions for Sinhala. Font Noto Sans Sinhala 52 px, white on #14213D at 85% opacity, bottom third.
5. End card: card-end.png for 6 s. Closing line must be visible.
6. Export H.264, 1080×1920, 30 fps, 10–12 Mbps, AAC 160 kbps. Also export the .srt/.vtt beside it.
7. Save to 02-generated-drafts/video/, add a row to 05-review/media-qa.md, then move to 03-approved-finals/video/ after review.
