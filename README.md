# polarisglobal.io (draft)

Static Astro site for Polaris Group, replacing the Base44 build at go live.

- Build: `npm run build` (output in `dist`). Netlify project: polaris-global-draft.
- Draft protection: `netlify.toml` sends `X-Robots-Tag: noindex`, `public/robots.txt` disallows all, and pages carry a noindex meta tag unless `PUBLIC_GO_LIVE=true`. At go live: set that variable, replace `public/robots.txt`, and remove the header block in `netlify.toml`.
- Theses text: `src/content/harness.md` (V3) and `src/content/sovereignty.md` (V2), reproduced exactly from the final Google Docs of 23 October 2026 (V3 1-mjm6U7BCenOKxmr4qCbT-dXmaOPSHaUjKv0L717wNw, V2 1XNbfEBMN11OEmUwtzW6vDU4NAxQrExNlVf7uHAVL3Mg). Do not edit the text here; Marc edits the Google Doc. PDFs in `public/pdf/` are exports of those Docs.
- Old Base44 routes: `public/_redirects`.
- Research behind the refresh: `docs/`.

## Go live checklist (agreed with Marc, 23 October 2026)

Polaris goes live only after the new Bluesphere site is live, because the legal and privacy link points to bluespheresolutions.co.uk/privacy/.

1. Check bluespheresolutions.co.uk/privacy/, /book/ and /services/ load on the live Bluesphere site.
2. In src/config/legal.ts set BOOKING_URL to https://bluespheresolutions.co.uk/book/ and ADVISORY_URL to https://bluespheresolutions.co.uk/services/. Update the same two links in public/llms.txt.
3. In Plausible, add the site polarisglobal.io and create goals: Booking Click, Fund Submission, Contact Submission, Council Interest, Outbound Link: Click, File Download. The script loads only on live builds.
4. In Netlify, Forms, set email notifications for fund-submission, council-interest and polaris-contact to marc@bluespheresolutions.co.uk.
5. Set PUBLIC_GO_LIVE=true in Netlify. This switches the robots meta tag, robots.txt and X-Robots-Tag header to allow search and AI crawlers.
6. Attach the polarisglobal.io domain and change DNS only with Marc's explicit yes, together with the SEO and AI Search workstream.
