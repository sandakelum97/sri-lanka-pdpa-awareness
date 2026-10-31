import status from '../../../../06-Legal-Research/data/status.json';
export type StatusKey = 'IN' | '2027' | 'NO' | 'mixed';
export const asOf: string = status.as_of;
export const labels = status.status_labels as Record<string, { en: string; si: string }>;
export const provisions = status.provisions as { ref: string; status: string; date: string | null; source: string }[];
export const parts = status.parts as { part: string; title: string; sections: (string | number)[] }[];
export const instruments = status.instruments as Record<string, { title: string; published: string; effect: string }>;
export function label(key: string | undefined, lang: 'en' | 'si' = 'en'): string {
  if (!key) return '';
  if (key === 'mixed') return lang === 'en' ? 'Mixed — see each provision' : 'මිශ්‍ර — එක් එක් විධිවිධානය බලන්න';
  return labels[key]?.[lang] ?? key;
}
export function statusForPart(part: string): string {
  const p = provisions.find((x) => x.ref === `Part ${part}`);
  return p?.status ?? '';
}
