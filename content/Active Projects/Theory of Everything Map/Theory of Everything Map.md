---
type: project
created: 2026-10-01
updated: 2026-10-01
tags: [higher-self, mind, knowledge-map, disclosure, research, plan]
domains: [self-mastery]
status: pilot-built
---

# Theory of Everything Map

**Founder's ask, live on stream 2026-10-01 08:42 (exact words):** "my goal with this is how can we get as much AI in as much different databases, different topics, and create a big theory of everything all the way from how the world works, so it's different families, but also we have spirituality, and everything in between transnational capital, geopolitics. All of these big important topics are all interrelated to some extent. So I would love to craft a clean, as clean as we can get in terms of just having all of it in one place, all of it, be able to explain it all, because I think the biggest reason why we haven't unlocked a lot of this information is it's been safeguarded, one, but it's also been siloed and not communicating back and forth. So that would be my challenge to you guys is to make sure we can do this at a high level."

Trigger: David Grusch on JRE 2560 saying AI could reveal hidden truths by correlating siloed databases. Today's crew work on that challenge, used as the starting material: [[2026-10-01 - AI cross-check challenge - what public data shows about UAP]], [[Mind Intelligence Agencies and Child Trafficking]], [[2026-10-01 - Grusch JRE 2560 live finds]].

**Status (2026-10-01, 10:33):** the founder said go at 10:17 ("yeah, we can build a trial run"). The **pilot is built**; results are in . Start with the dashboard, How It All Connects, [[Is this knowledge safeguarded, siloed, or neither]], [[Live map cards]] and [[Bridges]].

## In one breath

One map in the vault where every person, institution, program, place, text and teaching is a page, and every connection between them is its own small page that says **how we know it** (documented, testimony, statistical, or speculation) and **where it came from**. Several AI models read across all seven topic areas **and outside public databases**, looking for the same names, money, dates and ideas showing up in different silos; they propose connections, a second model checks them, and each is marked honestly. Above the map sits the "explain it all" layer: a readable account of how each area works and a master **How It All Connects** page, every sentence traceable to its evidence, with competing explanations side by side.

## Scope against his words

| His words | How the plan answers | Where it is still narrower |
|---|---|---|
| "as much AI in as much different databases" | Several models (extract, verify, critique); one outside connector per area, starting in the pilot | The pilot touches two outside databases, not all of them |
| "different topics... families, spirituality, transnational capital, geopolitics" | Seven areas below, one map | Areas can be added; seven is the start |
| "all of it in one place" | One project hub, one dashboard, one master explanation | Big raw datasets sit on the T7 drive, pointed to from the vault |
| "be able to explain it all" | Explanation layer, starting with one cross-area explanation in the pilot | The full seven-area account comes after back-fill |
| "safeguarded... siloed" | Joining silos is the method. Safeguarding is tested as a hypothesis on its own Question page; information we cannot reach is written as **unknown**, never as proof of a cover-up | |
| "at a high level" | Proven methods from investigative journalism and intelligence analysis, second-model checks, planted-control tests | |

## The seven topic areas

| Area | Already in the vault | Outside databases to join |
|---|---|---|
| Families and institutions | [[Bloodlines of the Illuminati - Breakdown]] (attributed allegation map only), [[2026-09-28 - Steelman - secret societies hold the most power]], [[Mind Giza Gatekeepers]] | Wikidata, LittleSis (elite power mapping), OpenCorporates, foundation filings (IRS 990s) |
| Transnational capital and banking rails | Simon Dixon's three videos in the Creator Library | OpenSanctions, ICIJ Offshore Leaks, GLEIF "who owns whom", SEC EDGAR, BIS and central-bank data |
| Geopolitics | Simon Dixon war coverage; today's treaty finds | GDELT news events, ACLED conflict data, SIPRI arms transfers, UN votes |
| Intelligence and black programs | [[Mind Intelligence Agencies and Child Trafficking]], CIA catalogs | CIA Reading Room (CREST), National Security Archive, The Black Vault FOIA sets, Pentagon budget books |
| UAP and non-human intelligence disclosure | [[Mind Disclosure Context]], CIA 713-record and Greer catalogs, today's cross-check | NARA UAP Records Collection, AARO reports, Project Blue Book, NUFORC, VASCO plate data |
| Ancient history and texts | [[Younger Dryas source guide]], [[Mind Giza Radar Project]], [[Mind Engle Context]], [[Mind Vedas Context]] | sacred-texts, Perseus, cuneiform archive (CDLI), Open Context |
| Consciousness and spirituality | Law of One Library (106 sessions), Knowledge Foundation, [[Mind Dispenza Context]], Rupert Spira | Corpus Hermeticum, the CIA's 1983 Gateway Process report (not yet ingested), PubMed meditation studies |

Built inside this project folder (Entities, Claims, Questions, Views, Changelog) so no new top-level folder is created and the Nexus app's six domain tags stay untouched; the map uses its own `area:` field. People or organizations that already have a Hive Mind entity page are linked, not duplicated.

## The pieces (schema)

Borrowed, not invented: entity types follow **FollowTheMoney**, the model investigative journalists (OCCRP Aleph, OpenSanctions) use for people, companies, ownership and payments; source grading follows the intelligence **Admiralty grade**; big contested questions use **Analysis of Competing Hypotheses** (Heuer, CIA). All fields are flat (Obsidian properties cannot nest).

1. **Entity page** (one per named person, organization, company, program, place, event, text or teaching). Required: `entity_id`, `kind`, `area`, `aliases`, `identifiers` (Wikidata ID, company number, archive ID), `subject_kind` (public figure / private person / organization / text). **"Family" is never an entity that receives claims**: family pages only list named members, and every claim is about a named person or organization. No ethnic or religious group is ever the subject of a funding or cause claim.
2. **Claim page** (one atomic connection: "X funded Y", "Document Z says W", "the Ra transcript says V").
   - Required (every claim): `claim_id` (built from subject + relation + object + event date + amount where there is one, so repeat passes cannot create duplicates and two separate payments between the same parties stay two claims), `event_date`, `amount` (when financial), `subject`, `relation` (from a fixed list), `object`, **`evidence`** (the founder's four: documented / testimony / statistical / speculation, meaning *how we know*, not whether it is true), `source_kind` (original record / derivative / channeled), `sources` (wikilinks plus exact locator: page, timestamp, document ID), `status` (proposed / checked / contested / refuted), `found_by`, `checked_by`, `created`, `last_checked`, `live_ok` (yes / no).
   - Added for high-impact claims only (`critical: true`): `source_grade` A to F, the strongest competing explanation, and **what record would change the picture**.
   - `relation_kind`: causal / financial / organizational / chronological / **parallel**. Parallel is resemblance across traditions (a Mahabharata flying city and a modern UAP report); parallels are never ranked as bridges and never promoted to causal without their own evidence.
   - Channeled material: "Ra says V" is documented as a statement in the transcript; the content is testimony with `source_kind: channeled`. Truth of the content and identity of the speaker are separate questions.
   - **Evidence lines** (in the page body, one line per source, since properties cannot nest): source link, exact locator, source kind, grade A to F, **upstream** (which original it ultimately rests on), and whether it **supports or challenges** the claim. Confidence counts distinct upstreams among supporting lines, weighted by grade, and is lowered by any challenging line.
   - Worked example, claim "The 1976 US-Soviet protocol uses code ATOM 222 for unidentified objects on missile-warning systems" (evidence: documented on the code system; the 222 pairing is contested):
     - National Security Archive Document 3, Carter Library NLC-12-17-9-2-9, scan p. 2 | original record | grade B | upstream: itself | supports the ATOM code system; OCR scrambled on the 222 line
     - [[2026-10-01 - AI cross-check challenge - what public data shows about UAP]] | derivative | grade C | upstream: Document 3 | supports, adds no independence
     - Grusch, JRE 2560 | testimony | grade D | upstream: unknown | supports the gist, challenges the details (he says "ADAM", "2013 annex")
     - Result before the pilot: one independent chain at grade B on the code system; the 222 pairing was only "likely". **Pilot update:** the original scan's page 6 shows ATOM 222 directly after the "detection by missile warning systems of unidentified objects" situation, so the pairing is now its own checked claim at 0.85 (see the table below). The exact JRE timestamp of Grusch's "ADAM" wording is not yet located.
   - Confidence is **computed**, not typed: from the number of independent source chains (two stories copying one upstream source count as one) and the source grades. A claim with no `source_grade` is scored as grade F (cannot be judged) until someone grades it, so a missing grade can only lower confidence, never raise it.
   - **Confidence decision table** (this is exactly what the pilot code computes):

     | Step | Rule |
     |---|---|
     | 1. Status first | Only `checked` claims get a number. `proposed`, `contested` and `refuted` show the status word instead, never a number. |
     | 2. Grade each evidence line | A 1.0, B 0.85, C 0.6, D 0.4, E 0.2, F 0.1. **Missing grade = F.** The per-line grades control; the claim's `source_grade` just shows the best line. |
     | 3. Count independence | Lines with the same upstream count once, at their best grade. Unknown upstream counts as its own line at grade F. |
     | 4. Add and cap | Sum the distinct upstreams, cap at 1.0. |
     | 5. Weight by how we know | documented or statistical x1.0, testimony x0.4, speculation x0.1. |
     | 6. Conflicts | Any line that challenges the claim (or a checker "partly") sets status `contested`, so step 1 removes the number until it is resolved. |

     Pilot results from the table: ATOM 222 read on the original scan (one upstream NLC-12-17-9-2-9, grade B, documented) = **0.85**; the crew's earlier derivative page on the same point (ungraded, so F) = **0.1**; a Wikidata membership listing (grade C) = **0.6**; Robert Salas's UFO testimony (ungraded F, testimony) = **0.04**.
3. **Source pages**: the existing `Sources/` convention, never edited after ingest. **AI-written vault pages (live finds, Mind research) are `derivative`**: a claim backed only by them stays testimony/proposed until its locator points to the original record. Big raw datasets live on the T7 drive with a pointer page and checksum in the vault.
4. **Question pages** (competing hypotheses): every explanation in a column, including the plain mundane one, every piece of evidence in a row, consistent or inconsistent, plus the predictions that would tell them apart. First three: "Is there a non-human presence?", "Do a small number of networks steer global capital?", and the founder's own premise: **"Is this knowledge safeguarded, siloed, or neither?"**
5. **Explanation pages** in `Generated/`, dated: per-area accounts and the master How It All Connects. Written only from checked claims; a script confirms every sentence links a claim; competing explanations are shown, not one tidy story.
6. **Changelog**: one dated note per batch ("12 claims promoted after source check"); refuted or replaced claims move to Archive with `superseded_by`, never deleted.
7. **Corrections ripple out immediately**: when a claim is refuted, contested or replaced, every map card that used it is withdrawn and regenerated, and every explanation or Question page that cites it is marked `stale` with a banner until it is rechecked. Each card and explanation lists the claim IDs it was built from, so the ripple is a lookup, not a guess.

## How sources get in

1. **What we already have**: an extraction pass reads the ~25 research pages above and writes candidate claims (`proposed`). Every claim must carry a quote that a script finds word for word at its locator. Nothing from memory.
2. **Stream-fed**: each stream's live-finds page feeds the same extractor after the stream.
3. **Outside databases**: one small connector per database, pulling records that match map entities **plus one hop out** (their direct links), so discovery is not limited to names we already know. Each pull logs its query, date, record count and the database's license terms. Being listed in a database (an offshore leak, a sanctions list) is not wrongdoing; ICIJ says so explicitly, and the map records it that way.
4. **Checking before promotion**: a different model from the extractor checks every claim tagged documented, every claim naming a living person, and a random sample: does the source actually **support** the claim in context (not just contain the quote), is the archive host confused with the author, are two sources really independent.
5. **Identity**: aliases only *suggest* a match; two people merge only on a shared identifier (Wikidata ID, birth date plus role). Merges are recorded and reversible. A wrong merge is the fastest way to a fake bridge.

## How cross-links are found (AI correlation passes)

Run after a stream, never in the live window (05:30 to 11:00).

1. **Same-entity pass** (suggest merges, under the identity rule above).
2. **Bridge pass**: entities touching two or more areas. **Bridge strength** = checked documented or statistical claims on both sides, divided down for big hubs that touch everything (CIA, "the US government", Egypt). Before any bridge is shown, it must beat a **shuffled-data baseline** (same network, with the topic areas each claim carries shuffled across claims); with many combinations tested, the bar rises accordingly.
3. **Money and custody trace**: ownership, funding, board seats, contracts. A missing payment link is written **unknown**.
4. **Timeline pass**: dated events across areas, compared against shuffled dates and against reporting bias (more reports where more people live). Today's null result on sighting reports near missile bases, once population was counted, is the model.
5. **Cluster summaries** (the Microsoft GraphRAG method for whole-corpus questions), built from checked claims only. Adopted only if it beats plain search on the same test questions.
6. **Contradiction pass**: disagreeing claims open a Question page.
7. **Model disagreement** is a signal: when the extractor and checker models disagree, the claim stays proposed and is flagged.

"No strong bridges found" is a valid, reportable result.

## How the crew uses it live

The co-host's local lookup has about 7,000 characters for everything it retrieves, and its coaching loader caps near 1,400. So the build adds a **map card** per entity, at most about 600 characters, generated from checked claims: one-line summary, the top three claims with their evidence tags and dates, the strongest counter-point, and at most one bridge to another area. Name lookup tolerates speech-to-text misspellings ("Grush", "Gru sh"). Mind says the tag aloud ("that's documented", "that's his testimony").

When the map cannot answer cleanly, it says so instead of guessing:
- **Two possible matches** (two people with the same name): the card names both and asks which one; it never blends them.
- **Nothing checked on the question**: the card says "the map has nothing checked on that yet" and Mind opens a research job.
- **Stale or contested claims**: shown only with the word "contested" or "being rechecked", never as settled.

**Saying it on stream counts as publishing**, so only claims with `live_ok: yes` reach the card. Never live: crime or abuse claims about a living person without a court or official record; claims about private individuals; any group-level claim. The guest-breakdown rule (play the guest's claims as true) stays separate; the map is always on the record. Wiring the cards into the co-host app is a later step, tested on the dry-run replay first, and never touches the running app while he is live.

## The dashboard

1. **Inside Obsidian** (ships with the pilot): Obsidian Bases tables: claims by area and evidence tag; proposed claims waiting for a check; ranked bridges; possible duplicates; open Question pages.
2. **Later, a local page in Chrome** like his other dashboards: the seven areas as colored regions, the strongest bridges drawn between them, a search box, every link colored by documented / testimony / statistical / speculation.

## Who owns what

Mind extracts and researches; Ego (a different model) checks claims and argues the competing explanation; Body builds connectors, scripts and dashboards; Higher Self approves promotions in batches and owns the explanation layer; **the founder approves anything that goes live or public**. Cost and time caps: subscription models only for passes, no paid fan-out, at most one connector added per week, queue of unchecked claims capped at 200 before new extraction pauses.

## Phased build

| Phase | What | Done when |
|---|---|---|
| 1 | This plan (council + acceptance) | His go |
| 2 | **Pilot** (below) | Pilot test passes |
| 3 | Back-fill every Mind Library page; stream-fed ingest on | Every Mind Library page mapped and checked |
| 4 | Outside connectors, one area at a time | Each logged and spot-checked |
| 5 | Live map cards + Chrome dashboard | Passed dry-run replay, then on stream |
| 6 | Full explanation layer | Every sentence traces to checked claims |
| Scale trigger | At 5,000 claims the master copy moves to a graph database, with the vault pages generated from it; one master copy at a time, never two | Export round-trips without loss |

## Recommended first build step: the pilot

**Map today's Grusch material across three or more areas and test it against two outside databases.**

- Write the templates and the Obsidian Bases dashboard.
- Map 25 to 30 claims from today's live finds, the UAP cross-check, the intelligence-agencies audit, the secret-societies steelman, the Giza gatekeepers page and today's Law of One passage, spanning at least three areas.
- Join two outside databases for those entities: **Wikidata** (identities and family/organization links) and the **CIA Reading Room or National Security Archive** (original records behind today's claims, such as the 1976 ATOM protocol).
- Run the bridge pass once and write **one cross-area explanation** and the "safeguarded, siloed, or neither?" Question page.

**Pass/fail** (no quota of bridges; "no strong bridges" can pass):
1. Every claim has an evidence tag, a source kind and an exact locator; a script finds every quote word for word.
2. A second model checks **every** pilot claim for real support in context; zero misquotes or unsupported "documented" tags remain.
3. **Planted controls**: three true links and three false ones (plus two look-alike names) are slipped in; the passes must keep the true ones and reject the false ones and the false merges.
4. The outside databases are scored: did they add any checked link the vault did not already have?
5. Five live-style questions get map cards under 600 characters that the crew judges better than today's lookup: three ordinary ("What's Grusch's evidence trail from intelligence to UAP?"), one with an ambiguous name (must ask which one), and one the map cannot answer (must say so plainly).
7. **Correction test**: refute one pilot claim on purpose; its card must be withdrawn and the explanation marked stale in the same run.
6. The explanation's sentences all trace to checked claims.

It costs almost nothing (subscription models, free public databases), changes nothing outside the vault, and runs after the stream.

## Pilot results (2026-10-01)

Built after the founder's go, inside the morning window, with light compute only (text scripts, two free public databases, cloud model checks; no local models, renders or builds).

**What is in it:** 53 claims (46 real plus 7 planted test controls) and 44 real entities (plus 4 planted look-alikes) across all seven areas (geopolitics 23, intelligence 19, UAP 18, capital 16, ancient 11, families and institutions 9, consciousness 1), plus two new source pages: the original 1976 protocol record and a Wikidata snapshot.

**Pass/fail against the plan's six tests:**

| Test | Result |
|---|---|
| 1. Every claim tagged, sourced, quote found word for word | **Pass.** All 51 tagged and located; the script caught the one fabricated quote (a planted fake). |
| 2. A second model checks every claim | **Pass.** Codex, blind, checked all 51: 45 checked, 2 contested (both were Body's own Wikidata claims that overreached), 4 refuted (all four planted fakes). It retagged one claim (the Mahabharata line is a documented text, not testimony). |
| 3. Planted controls | **Pass.** 3 of 3 true plants kept; 4 of 4 false plants rejected (fake quote, real quote twisted into a false conclusion, wrong signer, look-alike photographer). Both look-alike name pairs (Robert/Roberto Salas, Peter Lindberg/Lindbergh) were flagged and **not** merged. |
| 4. Did outside databases add anything new? | **Yes, measured.** A novelty check (`novelty.py`) compares each checked connector claim with the vault pages the pilot read: **5 of 13 are new** (both 1976 signers, Graybeal and Ustinov; Epstein's Council on Foreign Relations and Trilateral Commission memberships; the protocol file sitting in Zbigniew Brzezinski's papers), confirmed by a search of all 1,095 vault pages after downloading them from iCloud (the first search could not read 1,087 of them), plus one upgrade (ATOM 222 went from "most likely" on the crew's page to read on the original scan, page 6). The other 8 (Gelli heading P2, Calvi chairing Ambrosiano, Pinochet founding DINA, and others) confirm what the vault already had, from a second source. Wikidata also confirmed identities for 32 of the 44 real map entities (five searched had no Wikidata match, recorded as unknown). CIA ownership of Crypto AG came back contested (needs the 2020 reporting). |
| 5. Live cards beat today's lookup | **Pass, 5 of 5, twice** (rerun after the P2 card learned to include a second named topic, the Vatican Bank) in a blind comparison against the crew's current keyword search over the same pages (judge: Codex; the baseline is a close approximation of the live search, not the live app itself). All cards under 600 characters; the "Salas" question asks which person; the Rothschild question says the map has nothing checked. |
| 6. Explanation traces to checked claims | **Pass.** Every sentence in 2026-10-01 - How It All Connects - pilot cites a checked claim, and the build now **refuses to publish** an explanation with any uncited sentence. Citation proves traceability, not that each sentence is a fair summary; Higher Self read each sentence against its claims and tightened two. |
| 7. Correction ripple | **Pass.** Refuting the ATOM 222 claim on a test copy pulled it from its live card and stamped both the explanation and the Question page STALE. |

**Bridges:** only checked documented or statistical claims count, parallels excluded. The baseline keeps every entity's number of links and randomly reassigns which claims (with their areas) attach to which entity, 2,000 times. **First cross-silo lead:** the 1976 protocol file sits in Brzezinski's papers, and the vault's secret-societies research names him the Trilateral Commission's founding director, so one person's records join the UAP, geopolitics and institutions silos. It is a lead to follow, not evidence he handled UAP matters. None beat the bar yet (strongest candidates: BCCI and First American, the Council on Foreign Relations and the Trilateral Commission). Epstein touches four areas but scores as noise because he is a hub. That is the expected honest result at 51 claims.

**The premise test:** on the pilot's evidence, "safeguarded first, then siloed" and "siloed" fit best, and "nothing hidden" fits worst. That's nine pieces of evidence, so it's a direction, not a finding.

**Fixes after Astra's pilot review (round 1):** the confidence code now caps before weighting and treats an unknown origin as grade F, matching the table; testimony can no longer form a bridge; a quote must sit in the page section its locator names; an explanation with an uncited sentence is blocked; 12 fixed-example tests cover these (`test_toe.py`, all pass). Run order receipts (file times): Astra round 3 on the plan finished 10:19:51, before extraction (10:20:34), Wikidata (10:24:19) and the blind check (10:27:48).

**Astra's pilot reviews (two rounds, the limit):** round 1 found real bugs (confidence math, testimony counting toward bridges, quotes not tied to their page, uncited sentences not blocked), all fixed. Round 2: **4 of 16 met, 11 partly, 1 not met; verdict GAPS.** Fixed after round 2, not re-reviewed: the overstated "reached the public only in 2022" sentence; a quote citing a page that doesn't exist now fails; a correction also marks related claims on the same point as contested; merged duplicate claims keep all their evidence; the dashboard gained Open questions, Look-alike names and Checked-only-against-summaries views; the novelty claim was re-verified against the whole vault. 14 fixed-example tests pass. The "not met" item (the changelog note) was blank only in the review copy because iCloud had evicted it.

**Known gaps:** **33 of the 44 checked real claims were checked against the crew's summary pages, not the original records**, which falls short of the plan's own rule. They carry `verified_against: crew summary (original not yet read)` and grade F (confidence 0.1 or less) until Phase 3 reads the originals. consciousness has only one claim (the Law of One line); Grusch's own testimony claims were thin in the source pages; the card test compared against a close copy of the crew's keyword search, not the live app; the bridge baseline keeps the network fixed and shuffles which topic areas each claim carries (Astra asked that this be described plainly; it is not a full rewiring of links); the T7 failed its storage check, so raw data sits at `[local path removed]` for now. Code: `[local path removed]` (`toe_build.py`, `wikidata_connector.py`, `novelty.py`, `test_toe.py`, `sync_to_vault.sh`). The live crew does **not** use the cards yet; wiring them in is Phase 5.

**Next step (recommended):** Phase 3 back-fill: map the rest of the Mind Research Library (Law of One, Vedas, Dispenza, Engle, Giza radar, Younger Dryas, CIA and Greer catalogs) so consciousness and ancient history get real weight, then rerun the bridge pass at a few hundred claims.

## Risks and guardrails

- **Profound-feeling but empty correlations**: shuffled baselines, hub down-weighting, parallels excluded from bridges, Question pages, planted controls, model-disagreement flags.
- **People and families**: named individuals only, live/publication gate, allegation versus finding kept apart, listing is not wrongdoing, no ancestry-based or group blame.
- **Derivative sources**: AI summaries never count as originals.
- **Vault health**: the vault is iCloud-evicted at high disk use (internal disk at 9.3 GB free today, below the 30 GB target); big data stays on the T7 and the scale trigger moves the master copy before page counts hurt sync.

## Research and work receipts

- **Read first (2026-10-01, 08:42 to 08:55, before drafting):** the vault manual (`CLAUDE.md`), today's live-finds page, [[Mind Research Library]], [[Mind Disclosure Context]], Knowledge Foundation, Creator Library Sources (Simon Dixon entries), the crew task list (today's UAP cross-check and intelligence-agencies jobs), and the co-host's knowledge-bridge lookup code (its ~7,000-character retrieval budget).
- **Outside research before drafting:** FollowTheMoney / OpenSanctions / OCCRP Aleph entity and ownership model (opensanctions.org/docs/entities, followthemoney.readthedocs.io, docs.aleph.occrp.org); Microsoft GraphRAG community summaries for whole-corpus questions (arxiv.org/abs/2404.16130, microsoft.github.io/graphrag); the Admiralty grading code (NATO STANAG 2511) and Heuer's Analysis of Competing Hypotheses. The council added the ICIJ Offshore Leaks disclaimer and Obsidian's no-nested-properties limit.
- **Receipts:** the exact reads, searches and timestamps for this phase are in this session's own run log (Claude Code session transcript for task `claude-mupl3751-p3ie`, started 08:42 CDT) and the raw council outputs; beyond that log, the order of research and the compute footprint are self-reported.
- **Light compute while he was live:** this phase used only file reads, web searches and cloud model reviews (Codex, Claude, Perplexity at about 2 cents, Astra). No local transcription, rendering, model loading or builds ran.

## Council and acceptance results

**Council (2026-10-01, round 1):** Codex, Claude and Perplexity reviewed; all three returned findings, no seat failed. Gemini, Kimi and Grok were not run, under the cost policy's default of two subscription seats plus the mandatory Perplexity seat. Folded in: outside databases in the pilot (Claude P1); bridge quota replaced by planted controls and "zero bridges can pass" (Claude, Codex P1); defined bridge strength with hub down-weighting and shuffled baselines (all three); AI pages marked derivative (Claude P1); quote-plus-support checks by a second model (Codex P1); live use treated as publishing, with a live gate (all three); required versus high-impact fields and computed confidence (Claude, Perplexity); claim IDs, reversible merges, changelog, supersede-not-delete (all three); 600-character map cards with misheard-name lookup (all three); one explanation and the "safeguarded, siloed, or neither" question in the pilot (Codex, Claude); scope table, owners and caps, scale trigger (Perplexity, Codex). Not adopted: putting the vault folder under git (the vault sits in iCloud; changelog plus Archive covers history for now). Raw reviews: `/tmp/plan-council-toe/`.

**Acceptance (Astra, GPT-6, read-only), two rounds as the rules allow:** Round 1: 10 of 16 asks met; gaps were stale answers after corrections, confidence with missing grades, live handling of unknowns, research receipts and the go question, all fixed. Round 2: 13 of 16 met, verdict GAPS on three items: auditable per-source evidence (fixed after round 2 with evidence lines and the worked example, not re-reviewed), the vault copy missing the go question (fixed and verified identical), and research order and light compute being self-reported (receipts now point to the session log; still self-reported beyond it). Raw verdicts: `/tmp/toe-astra/astra1.txt`, `astra2.txt`.
