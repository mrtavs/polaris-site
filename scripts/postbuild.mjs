// Writes dist/robots.txt, dist/_headers and Markdown twins of every content page.
// Draft builds block every crawler. At go live set PUBLIC_INDEXABLE=true in Netlify
// (Site Standards Checklist v1, section 3). PUBLIC_GO_LIVE=true is still accepted.
import { writeFileSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative, dirname } from 'node:path';
import { NodeHtmlMarkdown } from 'node-html-markdown';

const live = process.env.PUBLIC_INDEXABLE === 'true' || process.env.PUBLIC_GO_LIVE === 'true';
const site = 'https://polarisglobal.io';
const DIST = 'dist';

// robots.txt, per the checklist template
const named = [
  'Googlebot', 'Google-Extended', 'Bingbot', 'OAI-SearchBot', 'ChatGPT-User', 'GPTBot',
  'Claude-SearchBot', 'Claude-User', 'ClaudeBot', 'PerplexityBot', 'Perplexity-User',
  'Applebot', 'Applebot-Extended',
];
const robots = live
  ? [
      named.map((b) => `User-agent: ${b}`).join('\n'),
      'Allow: /',
      '',
      'User-agent: *',
      'Allow: /',
      '',
      `Sitemap: ${site}/sitemap-index.xml`,
      '',
    ].join('\n')
  : '# Draft build: all crawlers blocked until go live.\nUser-agent: *\nDisallow: /\n';
writeFileSync(join(DIST, 'robots.txt'), robots);

// Headers
const headers = [
  '/*',
  ...(live ? [] : ['  X-Robots-Tag: noindex, nofollow']),
  '  Referrer-Policy: strict-origin-when-cross-origin',
  '  X-Content-Type-Options: nosniff',
  '  Permissions-Policy: camera=(), microphone=(), geolocation=()',
  '',
  // Thank you pages carry a noindex meta; the header covers crawlers that skip HTML.
  '/contact/thanks/*', '  X-Robots-Tag: noindex', '',
  '/fund/thanks/*', '  X-Robots-Tag: noindex', '',
  '/*.md', '  Content-Type: text/markdown; charset=utf-8', '',
  '/llms.txt', '  Content-Type: text/plain; charset=utf-8', '',
  '/llms-full.txt', '  Content-Type: text/plain; charset=utf-8', '',
  '/site.webmanifest', '  Content-Type: application/manifest+json', '',
  '/_astro/*', '  Cache-Control: public, max-age=31536000, immutable', '',
  '/fonts/*', '  Cache-Control: public, max-age=31536000, immutable', '',
].join('\n');
writeFileSync(join(DIST, '_headers'), headers + '\n');

// IndexNow key file (the deploy-succeeded function pings api.indexnow.org with every sitemap URL).
const INDEXNOW_KEY = 'd225142c66ac2deb313c58cfabb8f555';
if (live) writeFileSync(join(DIST, `${INDEXNOW_KEY}.txt`), INDEXNOW_KEY);

// Markdown twins: /x/y/ -> /x/y.md, / -> /index.md (main content only)
const walk = (d) => readdirSync(d).flatMap((f) => {
  const p = join(d, f);
  return statSync(p).isDirectory() ? walk(p) : [p];
});
const pages = walk(DIST).filter((f) => f.endsWith('index.html') && !f.includes('/thanks/'));
let n = 0;
for (const f of pages) {
  const html = readFileSync(f, 'utf8');
  const main = html.match(/<main[^>]*>([\s\S]*?)<\/main>/)?.[1];
  if (!main) continue;
  const title = html.match(/<title>([\s\S]*?)<\/title>/)?.[1] ?? '';
  const canonical = html.match(/<link rel="canonical" href="([^"]+)"/)?.[1] ?? '';
  const cleaned = main.replace(/<svg[\s\S]*?<\/svg>/g, '').replace(/<img[^>]*>/g, '').replace(/<form[\s\S]*?<\/form>/g, '').replace(/<style[\s\S]*?<\/style>/g, '');
  const md = `# ${title}\n\nSource: ${canonical}\n\n` + NodeHtmlMarkdown.translate(cleaned).trim() + '\n';
  const rel = relative(DIST, dirname(f));
  const out = rel === '' ? join(DIST, 'index.md') : join(DIST, `${rel}.md`);
  writeFileSync(out, md);
  n++;
}
console.log(`postbuild: ${live ? 'LIVE' : 'DRAFT'} robots.txt, _headers and ${n} Markdown twins written`);
