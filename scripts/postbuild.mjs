// Writes dist/robots.txt and dist/_headers. Draft builds block every crawler;
// set PUBLIC_GO_LIVE=true in Netlify at go live to open the site to search and AI crawlers.
import { writeFileSync } from 'node:fs';
const live = process.env.PUBLIC_GO_LIVE === 'true';
const site = 'https://polarisglobal.io';
const aiAndSearch = [
  'Googlebot', 'Bingbot', 'DuckDuckBot', 'Applebot', 'Applebot-Extended', 'Google-Extended',
  'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User',
  'PerplexityBot', 'Perplexity-User', 'Meta-ExternalAgent', 'MistralAI-User', 'CCBot', 'LinkedInBot',
];
const robots = live
  ? [...aiAndSearch.map((b) => `User-agent: ${b}\nAllow: /\n`), 'User-agent: *\nAllow: /\n', `Sitemap: ${site}/sitemap-index.xml`].join('\n') + '\n'
  : '# Draft build: all crawlers blocked until go live.\nUser-agent: *\nDisallow: /\n';
writeFileSync('dist/robots.txt', robots);
const headers = [
  '/*',
  live ? '  X-Robots-Tag: index, follow, max-image-preview:large' : '  X-Robots-Tag: noindex, nofollow',
  '  Referrer-Policy: strict-origin-when-cross-origin',
  '  X-Content-Type-Options: nosniff',
  '  Permissions-Policy: camera=(), microphone=(), geolocation=()',
  '',
  '/llms.txt', '  Content-Type: text/plain; charset=utf-8', '',
  '/llms-full.txt', '  Content-Type: text/plain; charset=utf-8', '',
  '/site.webmanifest', '  Content-Type: application/manifest+json', '',
  '/_astro/*', '  Cache-Control: public, max-age=31536000, immutable', '',
].join('\n');
writeFileSync('dist/_headers', headers + '\n');
console.log(`postbuild: ${live ? 'LIVE' : 'DRAFT'} robots.txt and _headers written`);
