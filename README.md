# polarisglobal.io (draft)

Static Astro site for Polaris Group, replacing the Base44 build at go live.

- Build: `npm run build` (output in `dist`). Netlify project: polaris-global-draft.
- Draft protection: `netlify.toml` sends `X-Robots-Tag: noindex`, `public/robots.txt` disallows all, and pages carry a noindex meta tag unless `PUBLIC_GO_LIVE=true`. At go live: set that variable, replace `public/robots.txt`, and remove the header block in `netlify.toml`.
- Theses text: `src/content/harness.md` (V3) and `src/content/sovereignty.md` (V2). PDFs in `public/pdf/` are generated from the built pages; regenerate them after any text change.
- Old Base44 routes: `public/_redirects`.
- Research behind the refresh: `docs/`.
