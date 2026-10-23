"""Subsets the self hosted fonts to the characters and weights the site uses. Run: python3 scripts/make_fonts.py"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset

ROOT = pathlib.Path(__file__).resolve().parent.parent
NM = ROOT / 'node_modules'
OUT = ROOT / 'public' / 'fonts'
OUT.mkdir(parents=True, exist_ok=True)
UNICODES = list(range(0x20, 0x7F)) + list(range(0xA0, 0x100)) + list(range(0x2010, 0x2028)) + [0x20AC, 0x2122, 0x2032, 0x2033]

def build(src, dst, wght=None):
    f = TTFont(src)
    if wght and 'fvar' in f:
        f = instancer.instantiateVariableFont(f, {'wght': wght})
    opts = subset.Options()
    opts.flavor = 'woff2'
    opts.layout_features = ['kern', 'liga', 'calt', 'onum', 'lnum', 'pnum', 'tnum']
    opts.name_IDs = ['*']
    opts.notdef_outline = True
    s = subset.Subsetter(opts)
    s.populate(unicodes=UNICODES)
    s.subset(f)
    f.flavor = 'woff2'
    f.save(OUT / dst)
    print(dst, (OUT / dst).stat().st_size)

nr = NM / '@fontsource-variable/newsreader/files'
build(nr / 'newsreader-latin-opsz-normal.woff2', 'newsreader-opsz.woff2', (400, 600))
build(nr / 'newsreader-latin-opsz-italic.woff2', 'newsreader-opsz-italic.woff2', (400, 400))
isf = NM / '@fontsource/instrument-sans/files'
for w in (400, 500, 600):
    build(isf / f'instrument-sans-latin-{w}-normal.woff2', f'instrument-sans-{w}.woff2')
