import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const base = '../../07-English-Content';
const meta = z.object({
  title: z.string(),
  slug: z.string().optional(),
  language: z.string().default('en'),
  commencement_status: z.string().optional(),
  sections_cited: z.string().optional(),
  amendment_refs: z.string().optional(),
  sources: z.array(z.string()).optional(),
  content_version: z.union([z.string(), z.number()]).optional(),
  last_reviewed: z.union([z.string(), z.date()]).optional(),
  reviewed_by: z.string().optional(),
  review_status: z.string().optional(),
  audience: z.array(z.string()).optional(),
  pathways: z.array(z.string()).optional(),
  part: z.union([z.string(), z.number()]).optional(),
  section: z.union([z.string(), z.number()]).optional(),
  type: z.string().optional(),
}).passthrough();

export const collections = {
  sections: defineCollection({ loader: glob({ pattern: ['s*.md'], base: `${base}/sections` }), schema: meta }),
  scenarios: defineCollection({ loader: glob({ pattern: ['[0-9]*.md'], base: `${base}/scenarios` }), schema: meta }),
  pathways: defineCollection({ loader: glob({ pattern: ['*.md', '!README.md'], base: `${base}/pathways` }), schema: meta }),
  faq: defineCollection({ loader: glob({ pattern: ['faq.md'], base: `${base}/faq` }), schema: meta }),
  glossary: defineCollection({ loader: glob({ pattern: ['*.md'], base: `${base}/glossary` }), schema: z.object({}).passthrough() }),
};
