# Feature Specifications v0.1 — the three differentiating features

Status: proposed, pending approval · 31 Oct 2026 · Build phase shown per feature. All three depend on the provision-by-provision status data in `06-Legal-Research/COMMENCEMENT-STATUS.md`, which must be a single machine-readable file (`status.json`) that every page, badge, video caption and checklist reads from.

## Shared foundation: `status.json`

```
{ "as_of": "2026-10-31",
  "provisions": [
    {"ref":"s.2",  "part":"-",   "title":"Application", "status":"2027", "date":"2027-01-01", "source":"GAZ-04"},
    {"ref":"s.13", "part":"II",  "title":"Right of access", "status":"NO", "date":null, "source":"GAZ-03"},
    ... one row per section and Schedule ...
  ],
  "status_labels": {
    "IN":   {"en":"In force", "si":"ක්‍රියාත්මකයි"},
    "2027": {"en":"In force from 1 Jan 2027", "si":"2027 ජනවාරි 1 සිට ක්‍රියාත්මක වේ"},
    "NO":   {"en":"Not yet in force — no date set", "si":"තවම ක්‍රියාත්මක නැත — දිනයක් නියම කර නැත"} } }
```
Sinhala labels above are placeholders to be confirmed against the official Sinhala Act text (OQ-15) and by the reviewer.

---

## Feature 1 — "What does this mean for me?" (occupation-based pathways)

Build phase: Phase 2 (content), Phase 3 (interface).

**Flow:** Home → "I am a…" chooser (icons, Sinhala/English) → pathway page listing 5–8 scenario cards in order of everyday relevance → each card opens a scenario explainer with its status badges and a "what you can do now" box.

**Initial pathway set (v1):** grocery/retail shop · restaurant/café · tuition class · salon · small clinic/pharmacy · online seller · school · hospital · employer/HR · website or app owner · ordinary citizen · parent · student · employee · IT/sysadmin · compliance/DPO.

**Scenario mapping (from the brief, with the sections each scenario rests on):**

| Scenario | Sections | Status today | Pathways |
|---|---|---|---|
| Collecting customer phone numbers | s.5 + Sch I(a)/(b)/(f); s.6; s.7; s.11 + Sch V | 2027 | shop, restaurant, salon, online seller |
| Loyalty cards / supermarket | s.5, 6, 7, 9; s.27 for marketing | 2027 / NO (s.27) | shop |
| Reservations | s.5, 6, 9 | 2027 | restaurant |
| Student and parent records | s.5 + Sch II (data relating to a child is a special category); s.10 | 2027 | tuition, school |
| Patient records | Sch II(g); s.10; s.20(1)(b)(ii); s.24 | 2027 | clinic, hospital |
| Employee NIC and HR files | Sch II(b); s.7; s.9 | 2027 | employer |
| Website visitor data / cookies | s.2(1)(b)(iii)–(iv); s.11; s.18 | 2027 | website owner |
| Delivery addresses | s.5, 6, 9, 21 (courier as processor) | 2027 | online seller |
| CCTV | s.24(1)(b) DPIA for systematic monitoring of public areas; s.11 signage | 2027 (form not prescribed) | shop, restaurant, school |
| Promotional SMS / WhatsApp broadcasts | s.27 + Sch III | NO | all businesses |
| Cloud services, WhatsApp, Microsoft 365, Google Workspace | s.26 (as replaced), s.21 | 2027 (instruments not specified) | all |
| Data breach | s.23 (rules not made); s.10 | 2027 | all |
| Asking a business for my data / correction / deletion | ss.13–17, 19 | NO | citizen |
| Complaint to the DPA | s.35; Part VII | IN (s.35) / NO (penalties) — see OQ-17 | citizen |

**Rules:** every scenario card carries status badges from `status.json`; "what you can do now" distinguishes "the law will require" (sections cited) from "good practice" (no section). Never states that a small shop needs a DPO; explains s.20(1)(b) thresholds are not yet prescribed.

---

## Feature 2 — "PDPA in 60 seconds" (micro-videos)

Build phase: Phase 4; scripts can be drafted in Phase 2 once content is reviewed.

**Format:** 45–60 s, 9:16 vertical master (WhatsApp/TikTok/Reels) plus 16:9 export; one concept per video; Sinhala and English versions recorded separately (not dubbed over each other); burned-in captions; end card with status badge and date ("Checked 31 Oct 2026") and the site URL.

**First 12 scripts (one concept each):** What is personal data? · What is the PDPA and is it in force? · Who is the Data Protection Authority? · "Controller" and "processor" in one minute · Why does a shop owner care? · Can a business collect my NIC? · Sinhala: පුද්ගලික දත්ත යනු කුමක්ද? · What is a data breach? · CCTV and the law · Promotional SMS — what the Act says (not yet in force) · Storing customer data in the cloud · What happens from 1 January 2027?

**Legal control:** each script has a source line (register IDs + sections) in the script file header; a video is re-recorded, not patched, when its status changes; every published video's description links to the page with the current status, because videos shared on WhatsApp cannot be recalled.

**Stored at:** `09-Videos-and-Audio/scripts-60s/<nn>-<slug>.<lang>.md` with the same metadata block used for web content.

---

## Feature 3 — Small Business Privacy Health Check

Build phase: Phase 3 (static, client-side), enhanced in Phase 4.

**Purpose:** educational self-assessment. Runs entirely in the browser; stores nothing server-side; no registration. Output is a list of "areas to look at", never a score that implies compliance.

**Mandatory disclaimer (shown before start and on results):** "This is an educational tool. It does not assess or certify compliance with the Personal Data Protection Act. It is not legal advice and is not provided by the Data Protection Authority."

**Structure (v1, ~25 questions, branching by business type from Feature 1):**
1. What you collect (names, phone, NIC, addresses, health, children, photos/CCTV)
2. Why and how you tell people (purpose, notice/signage — s.6, s.11)
3. How much and how long (s.7, s.9)
4. Where it lives (paper, phone, PC, cloud, WhatsApp — s.10, s.26)
5. Who else sees it (staff, courier, accountant, software vendors — s.21)
6. Marketing messages (s.27 — flagged "not yet in force")
7. If something goes wrong (breach readiness — s.23)
8. Handling requests from customers (ss.13–17 — flagged "not yet in force")

**Result page:** per topic, three states — "Looks reasonable", "Worth improving (good practice)", "The Act will require this from <date>" — each with the section reference, the status badge and a link to the scenario page. Printable/downloadable summary. Available in Sinhala and English.

**Technical note:** questions and logic in a JSON file reviewed by the legal reviewer; the component renders from it so the questionnaire can change without code changes.

---

## Approval needed

- [ ] Adopt `status.json` as the single source of commencement status.
- [ ] Approve the v1 pathway list and scenario mapping.
- [ ] Approve the first 12 video concepts.
- [ ] Approve the Health Check scope and disclaimer wording.
