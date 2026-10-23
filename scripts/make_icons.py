"""Builds the Polaris icon set and per page share cards. Run: python3 scripts/make_icons.py (needs playwright)."""
import base64, io, pathlib
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / 'public'
NAVY, BRASS = '#13233a', '#cfae6d'
STAR = 'M12 2.6 13.55 10.45 21.4 12 13.55 13.55 12 21.4 10.45 13.55 2.6 12 10.45 10.45Z'

def svg(rounded=True, pad=0.0):
    s = 1 - 2 * pad
    t = 12 * (1 - s)
    rect = f'<rect width="24" height="24" rx="{5 if rounded else 0}" fill="{NAVY}"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">{rect}'
            f'<path transform="translate({t} {t}) scale({s})" d="{STAR}" fill="{BRASS}"/></svg>')

(PUB / 'favicon.svg').write_text(svg())

font = lambda p: base64.b64encode((ROOT / 'node_modules' / p).read_bytes()).decode()
NEWS = font('@fontsource-variable/newsreader/files/newsreader-latin-opsz-normal.woff2')
SANS = font('@fontsource/instrument-sans/files/instrument-sans-latin-500-normal.woff2')
RIBBON = base64.b64encode((PUB / 'images' / 'ribbon.svg').read_bytes()).decode()

def card(kicker, title, sub):
    return f'''<html><head><style>
@font-face{{font-family:N;src:url(data:font/woff2;base64,{NEWS})}}
@font-face{{font-family:S;src:url(data:font/woff2;base64,{SANS})}}
body{{margin:0;width:1200px;height:630px;background:#0b1626;overflow:hidden;position:relative;font-family:S}}
.r{{position:absolute;inset:0;background:url(data:image/svg+xml;base64,{RIBBON}) left 270px top -10px/1000px auto no-repeat}}
.s{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(11,22,38,.92) 0%,rgba(11,22,38,.75) 50%,rgba(11,22,38,0) 72%)}}
.c{{position:absolute;left:72px;top:64px;bottom:60px;width:700px;display:flex;flex-direction:column}}
.b{{display:flex;align-items:center;gap:14px;color:#e6eaf0;font-size:26px;letter-spacing:.01em}}
.k{{margin-top:auto;color:{BRASS};font-size:22px;letter-spacing:.14em;text-transform:uppercase}}
h1{{font-family:N;font-weight:400;color:#f3f5f8;font-size:76px;line-height:1.02;margin:18px 0 0;letter-spacing:-.01em}}
p{{color:#c3ccd7;font-size:25px;line-height:1.4;margin:22px 0 0;max-width:600px}}
</style></head><body><div class="r"></div><div class="s"></div><div class="c">
<div class="b"><svg width="30" height="30" viewBox="0 0 24 24"><path d="{STAR}" fill="{BRASS}"/></svg>Polaris Group</div>
<div class="k">{kicker}</div><h1>{title}</h1><p>{sub}</p></div></body></html>'''

CARDS = {
  'og.png': ('Applied AI', 'Where value is moving in applied AI', 'Theses, private angel investment and the Polaris Council. Founded by Marc Taverner.'),
  'og-harness.png': ('Investment thesis', 'Investing in the Harness', 'Own the harness, not the weights. Sell to an obligation, not a preference. By Marc Taverner.'),
  'og-sovereignty.png': ('Essay, 2026 to 2031', 'Agents of Sovereignty', 'Earning and owning value in an economy reshaped by AI. By Marc Taverner.'),
  'og-fund.png': ('Polaris Fund', 'Private angel investment', 'For start ups that make the harness portable, provable or protected.'),
  'og-council.png': ('Polaris Council', 'The private and public sectors, in one room', "Convened at Speaker's House, Westminster, 23 April 2026."),
  'og-archive.png': ('Archive', 'The 2025 thesis and papers', 'Kept on record, with a note on what changed.'),
}

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1200, 'height': 630})
    for name, (k, t, s) in CARDS.items():
        pg.set_content(card(k, t, s)); pg.wait_for_timeout(300)
        pg.screenshot(path=str(PUB / name))
    def png(svgtext, size):
        q = b.new_page(viewport={'width': size, 'height': size})
        q.set_content(f'<html><body style="margin:0">{svgtext.replace("<svg ", f"<svg width={size} height={size} ", 1)}</body></html>')
        data = q.screenshot(omit_background=True); q.close()
        return Image.open(io.BytesIO(data)).convert('RGBA')
    png(svg(rounded=False, pad=0.08), 180).save(PUB / 'apple-touch-icon.png')
    png(svg(), 192).save(PUB / 'icon-192.png')
    png(svg(), 512).save(PUB / 'icon-512.png')
    png(svg(rounded=False, pad=0.2), 512).save(PUB / 'icon-maskable-512.png')
    png(svg(), 96).save(PUB / 'favicon-96.png')
    big = png(svg(), 256)
    big.save(PUB / 'favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    b.close()
print('done')
