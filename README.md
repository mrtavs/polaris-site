# polarisglobal.io (draft)

Static Astro site for Polaris Group, replacing the Base44 build at go live.

- Build: `npm run build` (output in `dist`). Netlify project: polaris-global-draft.
- Draft protection: `netlify.toml` sends `X-Robots-Tag: noindex`, `public/robots.txt` disallows all, and pages carry a noindex meta tag unless `PUBLIC_GO_LIVE=true`. At go live: set that variable, replace `public/robots.txt`, and remove the header block in `netlify.toml`.
- Theses text: `src/content/harness.md` (V3) and `src/content/sovereignty.md` (V2), reproduced exactly from the final Google Docs of 23 October 2026 (V3 1-mjm6U7BCenOKxmr4qCbT-dXmaOPSHaUjKv0L717wNw, V2 1XNbfEBMN11OEmUwtzW6vDU4NAxQrExNlVf7uHAVL3Mg). Do not edit the text here; Marc edits the Google Doc. PDFs in `public/pdf/` are exports of those Docs.
- Old Base44 routes: `public/_redirects`.
- Research behind the refresh: `docs/`.
