# polarisglobal.io (draft)

Static Astro site for Polaris Group, replacing the Base44 build at go live.

- Build: `npm run build` (output in `dist`). Netlify project: polaris-global-draft.
- Draft protection: `netlify.toml` sends `X-Robots-Tag: noindex`, `public/robots.txt` disallows all, and pages carry a noindex meta tag unless `PUBLIC_GO_LIVE=true`. At go live: set that variable, replace `public/robots.txt`, and remove the header block in `netlify.toml`.
- Theses text: `src/content/harness.md` (V3) and `src/content/sovereignty.md` (V2), reproduced exactly from the final Google Docs of 23 October 2026 (V3 1-mjm6U7BCenOKxmr4qCbT-dXmaOPSHaUjKv0L717wNw, V2 1XNbfEBMN11OEmUwtzW6vDU4NAxQrExNlVf7uHAVL3Mg). Do not edit the text here; Marc edits the Google Doc. PDFs in `public/pdf/` are exports of those Docs.
- Old Base44 routes: `public/_redirects`.
- Research behind the refresh: `docs/`.

## Go live checklist (agreed with Marc and the SEO workstream, 23 October 2026)

Launch order: Bluesphere (live 23 October 2026), then marctaverner.com, then Polaris.

Done before go live: booking, advisory and legal links point at the live Bluesphere /book/, /services/ and /privacy/; entity spec v1.3 applied; Site Standards Checklist v1 met on the preview.

1. In Plausible, add polarisglobal.io. Goals: Book Click, Form Submit, Outbound Link: Click, File Download, plus page view goals for /fund/thanks/ and /contact/thanks/. Add the AI referrer segment (chatgpt.com, chat.openai.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai, edgeservices.bing.com). The script loads only on indexable builds.
2. In Netlify, Forms, set email notifications for fund-submission, council-interest and polaris-contact to marc@bluespheresolutions.co.uk.
3. Set PUBLIC_INDEXABLE=true in Netlify and redeploy. This switches the robots meta tag, robots.txt and X-Robots-Tag header to allow search and AI crawlers. Then remove the Netlify team login.
4. Attach polarisglobal.io and change DNS only with Marc's explicit yes, run with the SEO and AI Search workstream. Old Base44 paths already 301.
5. Do not request indexing in Search Console until a live test shows the new page rather than the old Base44 host.
