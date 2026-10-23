import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://polarisglobal.io',
  trailingSlash: 'always',
  build: { format: 'directory', inlineStylesheets: 'always' },
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/thanks/'),
      // lastmod only where page content has a real date (Site Standards Checklist v1, section 5)
      serialize: (item) => {
        const dated = {
          'https://polarisglobal.io/theses/investing-in-the-harness/': '2026-10-23',
          'https://polarisglobal.io/theses/agents-of-sovereignty/': '2026-10-23',
          'https://polarisglobal.io/fund/': '2026-10-23',
          'https://polarisglobal.io/council/': '2026-10-23',
        };
        if (dated[item.url]) item.lastmod = dated[item.url];
        return item;
      },
    }),
  ],
});
