import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://sandakelum97.github.io/sri-lanka-pdpa-awareness', // TODO: final domain (dattasaviya.lk)
  base: process.env.SITE_BASE ?? '/',
  integrations: [sitemap()],
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'si'],
    routing: { prefixDefaultLocale: true },
  },
  build: { format: 'directory' },
});
