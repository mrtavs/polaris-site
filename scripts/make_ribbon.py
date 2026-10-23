"""Generates public/images/ribbon.svg: an abstract ribbon of hairline strands sweeping up and to the right,
twisting once, cool silver warming to brass. Deterministic. Run: python3 scripts/make_ribbon.py"""
import math
W, H = 1600, 1000
def lerp(a, b, t): return a + (b - a) * t
out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">',
'''<defs>
<linearGradient id="g" gradientUnits="userSpaceOnUse" x1="300" y1="1000" x2="1600" y2="200">
<stop offset="0" stop-color="#4f6584" stop-opacity="0"/>
<stop offset=".22" stop-color="#7f95b2"/>
<stop offset=".55" stop-color="#c9d4e2"/>
<stop offset=".82" stop-color="#e6cc93"/>
<stop offset="1" stop-color="#cfae6d" stop-opacity=".2"/>
</linearGradient>
<linearGradient id="g2" gradientUnits="userSpaceOnUse" x1="200" y1="1000" x2="1600" y2="150">
<stop offset="0" stop-color="#4f6584" stop-opacity="0"/>
<stop offset=".4" stop-color="#6f86a5"/>
<stop offset="1" stop-color="#b89a5e" stop-opacity="0"/>
</linearGradient>
<radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#cfae6d" stop-opacity=".18"/><stop offset="1" stop-color="#cfae6d" stop-opacity="0"/></radialGradient>
</defs>''']

def ribbon(n, p0, c1, c2, p3, grad, width, op_lo, op_hi):
    g = [f'<g fill="none" stroke="url(#{grad})" stroke-width="{width}">']
    for i in range(n):
        u = i / (n - 1)
        e = 0.5 - 0.5 * math.cos(math.pi * u)        # ease so strands bunch at the edges like a lit fabric
        P0 = (lerp(*p0[0], e), lerp(*p0[1], e)); C1 = (lerp(*c1[0], e), lerp(*c1[1], e))
        C2 = (lerp(*c2[0], e), lerp(*c2[1], e)); P3 = (lerp(*p3[0], e), lerp(*p3[1], e))
        op = op_lo + (op_hi - op_lo) * (0.5 + 0.5 * math.cos(2 * math.pi * u))   # brighter at the edges
        g.append(f'<path d="M{P0[0]:.1f} {P0[1]:.1f}C{C1[0]:.1f} {C1[1]:.1f} {C2[0]:.1f} {C2[1]:.1f} {P3[0]:.1f} {P3[1]:.1f}" stroke-opacity="{op:.2f}"/>')
    g.append('</g>')
    return g

# a faint wide ribbon behind for depth
out += ribbon(80, ((180, 620), (1120, 1060)), ((620, 760), (980, 520)), ((1000, 1180), (300, 120)), ((1820, 1700), (60, 260)), 'g2', 0.6, 0.05, 0.15)
# main ribbon: control points cross over, so the strands twist once mid-flight
out += ribbon(200, ((300, 760), (1100, 1060)), ((760, 880), (1020, 660)), ((1060, 1240), (300, 520)), ((1800, 1760), (120, 330)), 'g', 0.7, 0.14, 0.55)
# a quiet point of light where the ribbon leaves, the only nod to Polaris
out.append('</svg>')
open('public/images/ribbon.svg', 'w').write('\n'.join(out))
print(sum(map(len, out)), 'bytes')
