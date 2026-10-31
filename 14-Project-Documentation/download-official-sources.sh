#!/usr/bin/env bash
# Downloads the official PDPA source documents from dpa.gov.lk / parliament.lk / documents.gov.lk
# into folders 01–05 of the repository and writes 14-Project-Documentation/CHECKSUMS.txt (SHA-256).
# Run from anywhere on a machine with normal internet access; it changes to the repo root itself.
set -u
cd "$(dirname "$0")/.."  # repo root

dl() {  # dl <target path> <url>
  local out="$1" url="$2"
  if curl -fsSL --retry 3 -o "$out" "$url"; then echo "OK   $out"; else echo "FAIL $out  <- $url"; fi
}

# A. Acts
# NOTE 31 Oct 2026: documents.gov.lk URLs below return 404 after the site's re-platforming (OQ-19). Kept for reference.
dl 01-Original-Legislation/PDPA-2022-Act-09_EN.pdf "https://www.dpa.gov.lk/acts/Data%20Protection%20Act%20SL%20-%20English%20%282%29.pdf"
dl 01-Original-Legislation/PDPA-2022-Act-09_SI.pdf "https://www.dpa.gov.lk/acts/Data%20Protection%20Act%20SL%20-%20Sinhala%20%281%29.pdf"
dl 01-Original-Legislation/PDPA-2022-Act-09_TA.pdf "https://www.dpa.gov.lk/acts/act%20tamil.pdf"
dl 01-Original-Legislation/PDPA-2022-Act-09_EN_parliament.pdf "https://www.parliament.lk/uploads/acts/gbills/english/6242.pdf"
dl 01-Original-Legislation/PDPA-2022-Act-09_EN_govprinter.pdf "http://documents.gov.lk/files/act/2022/3/09-2022_E.pdf"
dl 02-Amendments/PDPA-2025-Amendment-Act-22_EN.pdf "https://www.dpa.gov.lk/acts/22-2025_E_251104_201549%20%281%29.pdf"
dl 02-Amendments/PDPA-2025-Amendment-Act-22_SI.pdf "https://www.dpa.gov.lk/acts/22-2025_S_251104_201513%20%281%29.pdf"
dl 02-Amendments/PDPA-2025-Amendment-Act-22_TA.pdf "https://www.dpa.gov.lk/acts/6384_T.pdf"
dl 02-Amendments/PDPA-2025-Amendment-Act-22_EN_parliament.pdf "https://www.parliament.lk/uploads/acts/gbills/english/6384.pdf"
dl 02-Amendments/PDPA-2025-Amendment-Act-22_EN_govprinter.pdf "https://documents.gov.lk/view/acts/2025/10/22-2025_E.pdf"

# B. Commencement Orders
dl 03-Gazettes-and-Commencement/2023-07-21_GE-2341-59_PartV-commencement_EN.pdf "https://www.dpa.gov.lk/Gazet/2023-07-21/2341-59_E.pdf"
dl 03-Gazettes-and-Commencement/2023-07-21_GE-2341-59_PartV-commencement_SI.pdf "https://www.dpa.gov.lk/Gazet/2023-07-21/2341-59_S.pdf"
dl 03-Gazettes-and-Commencement/2023-07-21_GE-2341-59_PartV-commencement_TA.pdf "https://www.dpa.gov.lk/Gazet/2341-59_T.pdf"
dl 03-Gazettes-and-Commencement/2024-01-08_GE-2366-08_Parts-VI-VIII-IX-X_EN.pdf "https://www.dpa.gov.lk/Gazet/2024-01-08/2366-08_E.pdf"
dl 03-Gazettes-and-Commencement/2024-01-08_GE-2366-08_Parts-VI-VIII-IX-X_SI.pdf "https://www.dpa.gov.lk/Gazet/2024-01-08/2366-08_S.pdf"
dl 03-Gazettes-and-Commencement/2025-03-14_GE-2427-34_repeal-of-18Mar2025-date_EN.pdf "https://www.dpa.gov.lk/Gazet/G%2043988%20%28E%29.pdf"
dl 03-Gazettes-and-Commencement/2025-03-14_GE-2427-34_repeal-of-18Mar2025-date_SI.pdf "https://www.dpa.gov.lk/Gazet/G%2043988%20%28S%29.pdf"
dl 03-Gazettes-and-Commencement/2025-03-14_GE-2427-34_repeal-of-18Mar2025-date_TA.pdf "https://www.dpa.gov.lk/Gazet/G%2043988%20%28T%29.pdf"
dl 03-Gazettes-and-Commencement/2026-07-22_GE-2498-16_s2-s3-PartI-PartIII-1Jan2027_EN.pdf "https://www.dpa.gov.lk/Gazet/2498-16_E.pdf"
dl 03-Gazettes-and-Commencement/2026-07-22_GE-2498-16_s2-s3-PartI-PartIII-1Jan2027_SI.pdf "https://www.dpa.gov.lk/Gazet/2498-16_S.pdf"
dl 03-Gazettes-and-Commencement/2026-07-22_GE-2498-16_s2-s3-PartI-PartIII-1Jan2027_TA.pdf "https://www.dpa.gov.lk/Gazet/2498-16_T.pdf"

# C. Circulars
dl 05-DPA-Guidelines-and-Circulars/2024-09-13_DPA-Circular-01-2024_EN.pdf "https://www.dpa.gov.lk/media/DPA%20Circular%2001-2024%20English%20-%2013%20Sep2024.pdf"
dl 05-DPA-Guidelines-and-Circulars/2026-08_DPA-Circular-01-2026_EN.pdf "https://dpa.gov.lk/media/DPA_Circular_012026_E.pdf"
dl 05-DPA-Guidelines-and-Circulars/2026-08_DPA-Circular-01-2026_SI.pdf "https://www.dpa.gov.lk/media/DPA_Circular_012026_S%20%281%29.pdf"
dl 05-DPA-Guidelines-and-Circulars/2026-08_DPA-Circular-01-2026_TA.pdf "https://www.dpa.gov.lk/media/012026-DPA_Circular_T.pdf"

# D. Draft instruments (NOT law)
dl 04-Regulations-and-Rules/drafts-2024/2024-10-01_DRAFT-DPIA-Regulations_v1.0.pdf "https://www.dpa.gov.lk/guid/DPA%20Final%20Draft_PDPIA%20Regulations-for%20Public%20ConsultationV%201.0.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-01_DRAFT-Breach-Notification-Rules_v1.0.pdf "https://www.dpa.gov.lk/guid/DPA%20-%20%20PC%20Draft_Data%20Breach%20Notification%20Rules%20-%20V%201.0.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-02_DRAFT-Cross-Border-Instruments-Directive_v1.0.pdf "https://www.dpa.gov.lk/guid/DPA%20-%20Instruments%20for%20Processing%20Data%20Outside%20SL-%20Draft%20Directive%20V%201.0.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-03_DRAFT-DPO-Regulations_v1.0.pdf "https://www.dpa.gov.lk/guid/DPA%20PC_Regulations%20on%20DPO%20V%201.0.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-05_DRAFT-Rights-and-Appeals-Regulations.pdf "https://www.dpa.gov.lk/guid/DPA%20-%20%20Draft_Appeals%20Regulation.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-05_DRAFT-Inquiry-Procedure-Regulations.pdf "https://www.dpa.gov.lk/guid/DPA%20-%20Draft%20Regulations%20on%20Inquiry%20Procedure%20-%20for%20Public%20Consultation%20%2805%20Oct%202024%29.pdf"
dl 04-Regulations-and-Rules/drafts-2024/2024-10-12_DRAFT-Fees-Regulation_v1.0.pdf "https://www.dpa.gov.lk/guid/9%20DPA%20-%20Draft%20Regulation%20on%20Personal%20Data%20%28Fees%29%20-%20V%201.0%20-%2012%20Oct%202024.pdf"

# E. Snapshot of the official index page (for change detection)
dl 06-Legal-Research/secondary-sources/dpa-downloads-page_$(date +%Y-%m-%d).html "https://www.dpa.gov.lk/guidelines.php"

echo "Writing CHECKSUMS.txt"
find 01-Original-Legislation 02-Amendments 03-Gazettes-and-Commencement 04-Regulations-and-Rules 05-DPA-Guidelines-and-Circulars -type f -name '*.pdf' -print0 | sort -z | xargs -0 sha256sum > 14-Project-Documentation/CHECKSUMS.txt
echo "Done. Retrieved on $(date -u +%Y-%m-%dT%H:%MZ)" >> 14-Project-Documentation/CHECKSUMS.txt
