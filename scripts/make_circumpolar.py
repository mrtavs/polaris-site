"""Generates public/images/circumpolar.svg: a long exposure star trail chart centred on Polaris.
Deterministic (seeded) so rebuilds are identical. Run: python3 scripts/make_circumpolar.py"""
import math, random
random.seed(2026)
W = H = 1200; cx, cy = 600.0, 600.0
SPAN = 46.0          # degrees swept by every trail (same exposure for all stars)
N = 1250
out = []
def arc(r, a0, a1):
    t0, t1 = math.radians(a0), math.radians(a1)
    x0, y0 = cx + r*math.cos(t0), cy + r*math.sin(t0)
    x1, y1 = cx + r*math.cos(t1), cy + r*math.sin(t1)
    large = 1 if (a1 - a0) > 180 else 0
    return f"M{x0:.1f} {y0:.1f}A{r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f}"

out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">')
out.append('<title id="t">Star trails turning around Polaris, the fixed point navigators steer by</title>')
out.append('''<defs>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#f3e2b8" stop-opacity=".55"/><stop offset=".25" stop-color="#cfae6d" stop-opacity=".18"/><stop offset="1" stop-color="#cfae6d" stop-opacity="0"/></radialGradient>
<radialGradient id="vig" cx="50%" cy="50%" r="50%"><stop offset=".62" stop-color="#0b1626" stop-opacity="0"/><stop offset="1" stop-color="#0b1626" stop-opacity=".7"/></radialGradient>
</defs>
<style>
.sky{transform-origin:600px 600px;animation:turn 360s linear infinite}
@keyframes turn{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.sky{animation:none}}
.t{fill:none;stroke-linecap:round}
.ring{fill:none;stroke:#cfae6d}
.lab{font:500 11px "Instrument Sans",system-ui,sans-serif;fill:#cfae6d;letter-spacing:.06em}
</style>''')

# Sky: trails, each drawn as a faint tail plus a brighter head, so it reads as motion.
out.append('<g class="sky">')
cols = ['#e8eef6']*6 + ['#b9c8dc']*5 + ['#9fb3cc']*3 + ['#e9cf98']*2 + ['#f2dcae']
for i in range(N):
    # denser near the middle radii, sparse at the pole, like a real sky
    r = 16 + (random.random() ** 0.9) * 548
    mag = random.random() ** 2.6            # most stars faint, few bright
    w = 0.3 + mag * 1.9
    op = 0.08 + mag * 0.82
    a0 = random.uniform(0, 360)
    span = SPAN * random.uniform(0.97, 1.03)
    c = random.choice(cols)
    split = a0 + span * 0.55
    out.append(f'<path class="t" d="{arc(r,a0,split)}" stroke="{c}" stroke-width="{w:.2f}" stroke-opacity="{op*0.45:.2f}"/>')
    out.append(f'<path class="t" d="{arc(r,split,a0+span)}" stroke="{c}" stroke-width="{w:.2f}" stroke-opacity="{op:.2f}"/>')
out.append('</g>')
out.append(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')

# Instrument: hairline declination circles and a graduated bezel.
for r in (120, 240, 360, 480):
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" class="ring" stroke-width=".5" stroke-opacity=".16"/>')
R = 566
out.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" class="ring" stroke-width=".9" stroke-opacity=".75"/>')
out.append(f'<circle cx="{cx}" cy="{cy}" r="{R-22}" class="ring" stroke-width=".5" stroke-opacity=".3"/>')
ticks = []
for d in range(360):
    L = 14 if d % 10 == 0 else (9 if d % 5 == 0 else 5)
    t = math.radians(d - 90)
    x0, y0 = cx + R*math.cos(t), cy + R*math.sin(t)
    x1, y1 = cx + (R-L)*math.cos(t), cy + (R-L)*math.sin(t)
    ticks.append(f"M{x0:.1f} {y0:.1f}L{x1:.1f} {y1:.1f}")
out.append(f'<path d="{"".join(ticks)}" class="ring" stroke-width=".75" stroke-opacity=".8"/>')
for d in range(0, 360, 30):
    t = math.radians(d - 90); rr = R - 34
    x, y = cx + rr*math.cos(t), cy + rr*math.sin(t)
    out.append(f'<text class="lab" x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle" opacity=".95">{d:03d}</text>')
# Meridian hairline through the pole
out.append(f'<path d="M{cx} {cy-R+16}V{cy+R-16}M{cx-R+16} {cy}H{cx+R-16}" class="ring" stroke-width=".4" stroke-opacity=".14"/>')

# Polaris: the fixed point.
out.append(f'<circle cx="{cx}" cy="{cy}" r="70" fill="url(#glow)"/>')
out.append(f'<path d="M{cx} {cy-34}L{cx} {cy+34}M{cx-34} {cy}L{cx+34} {cy}" stroke="#f6e7c2" stroke-width=".7" stroke-opacity=".7"/>')
out.append(f'<path d="M{cx} {cy-9}L{cx+2.2} {cy-2.2}L{cx+9} {cy}L{cx+2.2} {cy+2.2}L{cx} {cy+9}L{cx-2.2} {cy+2.2}L{cx-9} {cy}L{cx-2.2} {cy-2.2}Z" fill="#fff6dd"/>')
out.append(f'<circle cx="{cx}" cy="{cy}" r="2.6" fill="#ffffff"/>')
out.append(f'<path d="M{cx+14} {cy-14}L{cx+44} {cy-44}H{cx+58}" fill="none" stroke="#cfae6d" stroke-width=".6" stroke-opacity=".8"/>')
out.append(f'<text class="lab" x="{cx+62}" y="{cy-40}" opacity=".95">Polaris</text>')

out.append('</svg>')
open('public/images/circumpolar.svg', 'w').write('\n'.join(out))
print(sum(len(s) for s in out), 'bytes')
