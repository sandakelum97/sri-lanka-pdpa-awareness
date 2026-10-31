"""Render text cards and caption strips as PNGs with correct Sinhala shaping (Pillow + Raqm).
Usage: python3 cards.py spec.json outdir
"""
import json, sys, os
from PIL import Image, ImageDraw, ImageFont, features
assert features.check('raqm'), 'Pillow needs Raqm for Sinhala shaping'
W, H = 1080, 1920
LAGOON, MANGO, INK, PAPER, EMBER, MIST = (15,110,107), (242,179,61), (20,33,61), (255,255,255), (166,38,57), (238,243,242)
HERE = os.path.dirname(os.path.abspath(__file__))
def font(lang, size, bold=False):
    f = ImageFont.truetype(os.path.join(HERE, 'fonts', 'sinhala.ttf' if lang == 'si' else 'latin.ttf'), size, layout_engine=ImageFont.Layout.RAQM)
    try: f.set_variation_by_axes([700 if bold else 400])
    except Exception: pass
    return f
def is_si(s): return any('඀' <= c <= '෿' for c in s)
def wrap(draw, text, f, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if draw.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines
def runs(text):
    out, cur, mode = [], '', None
    for ch in text:
        m = 'si' if '\u0d80' <= ch <= '\u0dff' or ch in '\u200c\u200d' else ('any' if ch == ' ' else 'en')
        if mode is None or m == mode or m == 'any': cur += ch; mode = mode or (m if m != 'any' else None)
        else: out.append((mode, cur)); cur, mode = ch, m
    if cur: out.append((mode or 'en', cur))
    return out
def run_width(draw, ln, size, bold):
    return sum(draw.textlength(t, font=font(m, size, bold)) for m, t in runs(ln))
def draw_mixed(draw, x, y, ln, size, bold, color):
    for m, t in runs(ln):
        f = font(m, size, bold); draw.text((x, y), t, font=f, fill=color, features=['kern','liga']); x += draw.textlength(t, font=f)
def wrap_mixed(draw, text, size, bold, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if run_width(draw, t, size, bold) <= maxw: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines
def draw_block(draw, text, y, size, color, bold=False, maxw=W-160, align='center', line_gap=1.25):
    si = is_si(text)
    lines = wrap_mixed(draw, text, size, bold, maxw)
    lh = int(size * (1.6 if si else line_gap))
    for ln in lines:
        tw = run_width(draw, ln, size, bold)
        x = (W - tw) / 2 if align == 'center' else 80
        draw_mixed(draw, x, y, ln, size, bold, color)
        y += lh
    return y
def badge(draw, status, y):
    label, bg, fg = {'IN': ('IN FORCE', (28,122,62), PAPER), '2027': ('FROM 1 JAN 2027', MANGO, INK), 'NO': ('NOT IN FORCE · NO DATE', EMBER, PAPER), 'mixed': ('PARTLY IN FORCE', MIST, INK)}[status]
    f = font('en', 40, True); tw = draw.textlength(label, font=f); pad = 36
    x0 = (W - tw) / 2 - pad
    draw.rounded_rectangle([x0, y, x0 + tw + 2*pad, y + 84], radius=42, fill=bg)
    draw.text(((W - tw)/2, y + 16), label, font=f, fill=fg)
def card(spec, out):
    bg = {'lagoon': LAGOON, 'paper': PAPER, 'ink': INK, 'ember': EMBER}[spec.get('bg', 'lagoon')]
    fg = PAPER if spec.get('bg', 'lagoon') in ('lagoon', 'ink', 'ember') else INK
    accent = MANGO if spec.get('bg', 'lagoon') != 'paper' else LAGOON
    im = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(im)
    y = spec.get('top', 520)
    if spec.get('kicker'): y = draw_block(d, spec['kicker'], y, 44, accent, True) + 24
    if spec.get('title'): y = draw_block(d, spec['title'], y, spec.get('title_size', 96), fg, True) + 30
    if spec.get('title_si'): y = draw_block(d, spec['title_si'], y, 72, accent, True) + 30
    for b in spec.get('body', []): y = draw_block(d, b, y, 52, fg) + 18
    if spec.get('badge'): badge(d, spec['badge'], y + 30); y += 150
    if spec.get('strike'):  # e.g. cancelled date
        f = font('en', 72, True); t = spec['strike']; tw = d.textlength(t, font=f); x = (W - tw)/2; yy = y + 30
        d.text((x, yy), t, font=f, fill=EMBER); d.line([x-10, yy+44, x+tw+10, yy+44], fill=EMBER, width=8); y = yy + 110
    # footer
    foot = spec.get('footer', 'Checked against the official Gazettes · 31 Oct 2026 · DataSavi · Not legal advice')
    draw_block(d, foot, H-170, 28, (fg if bg != PAPER else (90,106,120)), False, maxw=W-200)
    im.save(out)
def caption(text, out, lang=None):
    """Transparent 1080x1920 overlay with a caption strip near the bottom."""
    im = Image.new('RGBA', (W, H), (0,0,0,0)); d = ImageDraw.Draw(im)
    si = is_si(text); size = 52
    lines = wrap_mixed(d, text, size, True, W-200); lh = int(size*(1.6 if si else 1.3)); boxh = lh*len(lines) + 56
    y0 = H - 420 - boxh
    d.rounded_rectangle([60, y0, W-60, y0+boxh], radius=24, fill=(20,33,61,215))
    y = y0 + 28
    for ln in lines:
        tw = run_width(d, ln, size, True); draw_mixed(d, (W-tw)/2, y, ln, size, True, PAPER); y += lh
    im.save(out)
if __name__ == '__main__':
    spec = json.load(open(sys.argv[1])); out = sys.argv[2]; os.makedirs(out, exist_ok=True)
    for i, c in enumerate(spec['cards']): card(c, f"{out}/card-{c['id']}.png")
    for i, c in enumerate(spec['captions']): caption(c['text'], f"{out}/cap-{c['id']}.png", c.get('lang'))
    print('rendered', len(spec['cards']), 'cards and', len(spec['captions']), 'captions')
