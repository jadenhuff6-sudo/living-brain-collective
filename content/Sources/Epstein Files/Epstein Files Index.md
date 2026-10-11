---
type: source
created: 2026-10-07
updated: 2026-10-07
tags: [epstein, epstein-email, index, house-oversight, doj-epstein-files]
status: ingested
domains: []
source_url: https://www.justice.gov/epstein
source_kind: note
author: House Committee on Oversight and Government Reform; U.S. Department of Justice
---

# Epstein Files Index (official email releases)

Founder ask, live on stream 2026-10-07 07:59: "I need the complete Epstein emails in my Obsidian vault." Built by Mind the same morning.

**What this is:** every email-like document we could find in the two official public email sources, as searchable text, each entry tied to its official record number. **What it is not:** a guaranteed-complete inbox. No government body has released "the complete Epstein emails"; the House and the Justice Department each released a pile, and the Justice Department has kept pulling and reposting files since.

**Do not put a raw entry on stream without opening the official file first.** The Justice Department text below was copied on 2026-02-04, before the department pulled thousands of files (Feb to Mar 2026) to fix redactions that had exposed victims' names, emails and photos. Some entries here may still show details the department later redacted. Check the "official PDF" link (the live version) before quoting, and never read out a name that looks like a victim's.

## What's in

| Source | Released | Emails in vault | Where |
|---|---|---|---|
| House Oversight Committee, Epstein estate documents (20,000 pages) | 2025-11-12 | **2,319** email documents, 2008 to 2019 (55 undated) | House emails 2016 etc., folder `House Oversight 2025-11-12 estate emails` |
| DOJ Epstein Files Transparency Act, Data Sets 1 to 8 | 2025-12-19 (more added through 2025-12-23) | **2,325** (almost all in Data Set 8) | DOJ Data Set 08 index, DOJ Data Set 04 index, DOJ Data Set 01 index |
| DOJ Epstein Files Transparency Act, Data Sets 9 to 12 (the "second tranche") | 2026-01-30 (23 docs added to Set 12 around 2026-03-05) | **688,040** | DOJ Data Set 09 index (276,059), DOJ Data Set 10 index (235,161), DOJ Data Set 11 index (176,817), DOJ Data Set 12 index (63) |

Data Sets 2, 3, 5, 6 and 7 held no email documents by this method (they are mostly reports, photos and court and FBI records).

Total: **692,684 email documents** (2,319 House + 690,365 DOJ), plus 8,464 DOJ copies that repeat an email already kept, listed in DOJ near-duplicate copies so nothing is dropped.

- House notes: one note per email, with sender, recipient, date, subject and Bates number (`HOUSE_OVERSIGHT_######`) in the frontmatter. Year tables: House emails 2008, House emails 2009, House emails 2010, House emails 2011, House emails 2012, House emails 2013, House emails 2014, House emails 2015, House emails 2016, House emails 2017, House emails 2018, House emails 2019, House emails Undated.
- DOJ notes: 2,767 batch notes of up to 250 emails each, sorted by record number (`EFTA########`). Every entry has date, sender, recipient, subject and a link to the official PDF on justice.gov (the site asks you to confirm you are 18 or older).
- Search tip: Obsidian search works across all of it, for example a name, an email address (`[email removed]` is Epstein's main account), or a Bates/EFTA number.

## Official sources (URL and date)

- House Oversight, 2025-11-12, additional estate documents: https://oversight.house.gov/release/oversight-committee-releases-additional-epstein-estate-documents/ (files: [Google Drive](https://drive.google.com/drive/folders/1hTNH5woIRio578onLGElkTWofUSWRoH_), now returning "not found"; [Dropbox backup](https://www.dropbox.com/scl/fo/9bq6uj0pnycpa4gxqiuzs/ABBA-BoYUAT7627MBeLiVYg?rlkey=3s6ggcjihou9nt8srsn2qt1n7&dl=0), browsable but too big to download as one file).
- House Oversight Democrats, 2025-11-12, the three emails released that morning: https://oversightdemocrats.house.gov/news/press-releases/house-oversight-committee-releases-jeffrey-epstein-email-correspondence-raising (all three are inside the House set above).
- DOJ Epstein Library: https://www.justice.gov/epstein ; data set list: https://www.justice.gov/epstein/doj-disclosures ; Jan 30 2026 press release: https://www.justice.gov/opa/pr/department-justice-publishes-35-million-responsive-pages-compliance-epstein-files
- Law: Epstein Files Transparency Act, Public Law 119-38, signed 2025-11-19: https://www.congress.gov/119/plaws/publ38/PLAW-119publ38.pdf

## How the text was obtained (provenance)

The official files are page images and PDFs: about 300 GB for the DOJ sets and a Drive folder that no longer serves. So the text came from public full-text copies of those exact official files, keeping the official record numbers so every entry can be traced back:

- House: the release's own `TEXT` folder (native text) plus OCR of its page images, via the public mirror https://huggingface.co/datasets/teyler/epstein-files-20k (re-upload of `tensonaut/EPSTEIN_FILES_20K`). 2,317 emails come from native text, 2 from page OCR.
- DOJ: machine OCR of all 1,380,932 PDFs in Data Sets 1 to 12, from https://huggingface.co/datasets/ishumilin/epstein-files-ocr-complete (CC0; built from a 2026-02-04 copy of the official files).
- Emails were picked out by their header lines (From plus at least two of Sent, To, Subject, Date). Each DOJ entry's data set comes from the official data set pages' starting record numbers.

## Checks run (2026-10-07)

- House: three widely reported emails found word for word at their reported records: the 2011-04-02 "dog that hasn't barked" email (HOUSE_OVERSIGHT_031326), the 2019-01-31 Wolff email (HOUSE_OVERSIGHT_030411), and the 2011-03-04 Oscar diary thread. The official House PDF of the three Democrat-released emails is image-only, so no automated word match was possible.
- DOJ: 40 random entries checked against the live official PDFs. **All 40 are still online at the exact linked address.** 27 matched near word for word (80%+ of words), 9 mostly (50 to 80%), 4 less (short calendar alerts where OCR read a few words differently). Median overlap 84%. OCR misreads letters, so check the PDF before quoting names or numbers.

## Redactions

- House set: 121 of 2,319 emails contain a redaction marker. The House release otherwise left names visible (including Virginia Giuffre's).
- DOJ set: 2,732 entries contain a visible redaction or hidden-text marker in the OCR (6,814 markers); many more redactions are black boxes OCR can't see. DOJ says it redacted victim names and identifying details ("DOJ Redaction"), plus grand-jury and court-ordered material, and withheld about 200,000 pages for privilege. Public figures' names were not redacted.
- After this copy was made, DOJ took down and re-redacted roughly 9,500 to 47,635 files (Feb to Mar 2026) and later added 23 documents to Data Set 12. In June 2026 a federal judge ordered the department to lift or justify redactions on eight emails; whether the less-redacted copies were posted is unconfirmed.

## What's missing

- Emails whose header lines were blacked out, cut off or unreadable by OCR, and emails that only exist as attachments or photos.
- Anything DOJ added or changed after 2026-02-04 (including the 23 later Data Set 12 documents and the re-redacted reposts). The DOJ library says it was last updated 2026-09-11; what changed is unknown.
- The raw page images and PDFs themselves (about 300 GB; no room on this Mac or the T7).
- Other House releases (Sept 2 2025 DOJ records, 33,295 pages; Sept 8 2025 birthday book, will and address book, 358 pages; Sept 26 2025 phone and flight logs, ledgers and schedules; Oct 17 2025 records). These are not email sets. The estate also handed over about 23,000 more documents the committee had not released as of 2025-11-12.
- Deliberately excluded: the leaked Yahoo mailbox (Bloomberg and DDoSecrets, never an official release) and Jmail (a useful search site that mixes official and unofficial mail).

## Related

- 2026-10-07 - Julian Dorey Simon Dixon highlights (the episode that prompted this)
- [[Mind Intelligence Agencies and Child Trafficking]]
