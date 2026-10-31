// Decide where the language switch should go. If the twin page doesn't exist, fall back to that section's index.
import { getCollection } from 'astro:content';
let siIds: Set<string> | null = null;
async function sinhalaIds() {
  if (siIds) return siIds;
  const p = await getCollection('pathwaysSi'); const f = await getCollection('faqSi');
  siIds = new Set([...p.map((e) => `/si/pathways/${e.id}/`), ...(f.length ? ['/si/faq/'] : []), '/si/', '/si/pathways/', '/si/scenarios/', '/si/sections/', '/si/status/', '/si/glossary/', '/si/downloads/', '/si/about/', '/si/search/']);
  return siIds;
}
export async function twinPath(path: string, lang: 'en' | 'si'): Promise<{ href: string; exact: boolean }> {
  const other = lang === 'en' ? 'si' : 'en';
  const twin = path.replace(/^\/(en|si)/, `/${other}`);
  if (other === 'en') return { href: twin, exact: true }; // every si page has an en twin
  const ids = await sinhalaIds();
  if (ids.has(twin)) return { href: twin, exact: true };
  const section = twin.split('/')[2];
  return { href: section ? `/si/${section}/` : '/si/', exact: false };
}
