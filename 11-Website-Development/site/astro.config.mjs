import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://example.org', // TODO: set final domain
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'si'],
    routing: { prefixDefaultLocale: true },
  },
  build: { format: 'directory' },
});
