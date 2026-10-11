---
type: project
created: 2026-10-05
updated: 2026-10-05
tags: [stream-prep, trending]
---

# 2026-10-06 - Trending docket

Stream date: Tuesday 2026-10-06 (America/Chicago). Prepared 2026-10-05 21:50-22:05 CDT by the trending-docket skill.

**Founder selection: pending.** **Founder twist: to add by Jaden.** These are recommendations, not an approved Stream Plan. Tomorrow already has a prepared breakdown, [[2026-10-06 - 13 Families Part 1 Astor]]; nothing here replaces it.

Coverage at a glance:
- X / Twitter: **US platform trends unverified (native)**. Two third-party estimates available, US-labeled, hourly snapshot.
- YouTube: **native US chart verified** (official YouTube Data API `chart=mostPopular`, regionCode US).
- TikTok: **US platform trends unverified**. Native Creative Center blocked; one partial multi-region third-party estimate.

## US platform trends

### X / Twitter

- **Status: US platform trends unverified.** x.com/explore returned HTTP 402 to an unauthenticated read (2026-10-05T21:53-05:00). No authorized read-only X trends access exists in this setup.
- **Evidence class: third-party trend estimate** (trends24.in, getdaytrends.com). Both say they mirror X's US trend list; their collection method, personalization handling and ranking logic are not documented here. No post volumes were shown on either page, so metrics are `unknown`. Ranks below are the provider's order, not X's verified rank.
- **Region:** "United States" as labeled by the providers (not independently verified).
- **Observation window:** trends24 hourly block timestamped 2026-10-06T02:28:12Z (= 2026-10-05T21:28:12-05:00). Previous block 2026-10-06T01:36:34Z. getdaytrends: current list, no timestamp shown.
- **Checked:** 2026-10-05T21:53-05:00.
- Sources: https://trends24.in/united-states/ , https://getdaytrends.com/united-states/

**trends24 US, block 21:28 CDT (rank, topic):**

| # | Trend | # | Trend | # | Trend | # | Trend | # | Trend |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Yankees | 11 | Kellen Moore | 21 | Kendre Miller | 31 | Drake London | 41 | MITB |
| 2 | Saints | 12 | McMahon | 22 | Volpe | 32 | Trombone Shorty | 42 | Sean Burke |
| 3 | #WWERaw | 13 | Penix | 23 | Slow Motion | 33 | #RiseUp | 43 | #ALDS |
| 4 | Falcons | 14 | Kyle Pitts | 24 | Lombard | 34 | ALCS | 44 | Fort Hood |
| 5 | Bijan | 15 | Shough | 25 | Mike Hughes | 35 | Richie Palacios | 45 | Brandon Staley |
| 6 | Kirk Franklin | 16 | #ATLvsNO | 26 | LA Knight | 36 | Big Cass | 46 | CJ Henderson |
| 7 | Boone | 17 | New Orleans | 27 | Bellinger | 37 | Monday Night Football | 47 | Tyree Wilson |
| 8 | Jazz | 18 | Kamara | 28 | Freddy Peralta | 38 | Knicks | 48 | Juvie |
| 9 | Rays | 19 | Schlittler | 29 | Chase Young | 39 | Sixers | 49 | Steve Gleason |
| 10 | Olave | 20 | #DirtyBirds | 30 | Jaylen Brown | 40 | Los Angeles and San Diego | 50 | Rey Fenix |

Previous block (20:36 CDT) top 10: Bijan, Falcons, Saints, #WWERaw, Jazz, McMahon, Kyle Pitts, Boone, Kendre Miller, LA Knight.

**getdaytrends US, current (top 10, no volumes/timestamp):** 1 Bijan, 2 Saints, 3 Falcons, 4 #WWERAW, 5 Jazz, 6 McMahon, 7 Penix, 8 Kyle Pitts, 9 Boone, 10 Kellen Moore. Ranks 11-50 largely overlap trends24 (adds #WhoDat, Jo Adell, Guardians, Troy Aikman, Gavin Williams, Braden Montgomery, Okorie).

Reading the list (agent note, not provider categories): the snapshot is dominated by live sports during the observation hour, Monday Night Football (#ATLvsNO, Falcons at Saints), MLB postseason (Yankees, Rays, #ALDS, ALCS), and WWE Raw. Non-sports items: **Kirk Franklin** (driver not confirmed; he released a GloRilla single 2026-09-28 and announced the album *I Am What I Am* for 2026-10-30, per Rapzilla, but nothing ties that to tonight's spike), **Fort Hood** (likely the 2026-10-05 Pentagon announcement on Nidal Hasan, see below; driver inferred from same-day news, not shown by the provider), **Juvie**, **Slow Motion** (drivers unknown). Momentum/velocity: unknown (one snapshot pair, no volumes).

### YouTube

- **Status: native US chart verified.** Evidence class: **native platform trend** (YouTube's own "most popular" chart via the official YouTube Data API v3, `videos.list chart=mostPopular regionCode=US`, read-only, existing channel credentials).
- **Region:** US (API parameter). **Window:** YouTube does not publish the chart's window or ranking formula; it is all-category, not personalized. Caveat: YouTube retired the public Trending page in 2025; this API chart is what remains, and its ranking is clearly not raw views (rank 1 has 81,651 views).
- **Checked:** 2026-10-05T21:52:19-05:00. Views/likes are cumulative at check time; no velocity measured.
- Category = the uploader's YouTube category.

| # | Title | Channel | Category | Published (UTC) | Views at check | Link |
|---|---|---|---|---|---|---|
| 1 | Bow | FOB Huncho - Topic | Music | 2026-09-29 | 81,651 | https://www.youtube.com/watch?v=guYIc9Ves5E |
| 2 | Season 5: A Grim Doctrine Launch Trailer \| Overwatch | PlayOverwatch | Gaming | 2026-10-05 | 468,600 | https://www.youtube.com/watch?v=Ih6DVdyQn3I |
| 3 | GRIEF (VERIFIED) // TOP 1 | Doggie | Gaming | 2026-10-05 | 1,054,566 | https://www.youtube.com/watch?v=gB8slBPlOjc |
| 4 | Bjorn Bonebreaker - Mama, Don't Close Your Eyes [Official Lyrics Video] | Bjorn Bonebreaker | Music | 2026-09-14 | 397,997 | https://www.youtube.com/watch?v=r8h8Kee_PYU |
| 5 | JAILER 2 - Official Trailer \| Superstar Rajinikanth | Sun TV | Entertainment | 2026-10-05 | 10,035,366 | https://www.youtube.com/watch?v=FW_PPcr1sPE |
| 6 | Surviving in a Maze isn't Easy... | SMii7Y | Gaming | 2026-10-05 | 827,360 | https://www.youtube.com/watch?v=AsGh9FojXbM |
| 7 | Yu Les – Jarahn ft. SHLD, Nene Morus & Rich Antony | Jarahn | Music | 2026-09-25 | 104,558 | https://www.youtube.com/watch?v=6pm4s82cMuA |
| 8 | Southern Charm \| Season 12 Official Trailer | Entertainment Tonight | Entertainment | 2026-10-05 | 30,901 | https://www.youtube.com/watch?v=rRIe0y8tcnw |
| 9 | Evolving from POOR to MILLIONAIRE Island! | TechyCraft | Gaming | 2026-10-05 | 432,943 | https://www.youtube.com/watch?v=Kr9_nECiPt0 |
| 10 | El Gigante de Hierro | Grupo Sonador - Topic | Music | 2026-10-01 | 193,586 | https://www.youtube.com/watch?v=cPIMvQvvSLM |
| 11 | MechWarrior 5 Mercenaries - Ashes & Ascension - Launch Trailer | MechWarrior 5 Mercenaries | Gaming | 2026-10-05 | 99,000 | https://www.youtube.com/watch?v=-XtLCjzIjn4 |
| 12 | This Card Game is Cursed... | SMii7Yplus | Gaming | 2026-10-04 | 1,618,071 | https://www.youtube.com/watch?v=_geP6kSwIfY |
| 13 | Rammstein - Live in Mexico City - Sonne | Rammstein Official | Music | 2026-10-05 | 1,037,319 | https://www.youtube.com/watch?v=UxmdCABl1EY |
| 14 | AVENGERS DOOMSDAY Marvel Officially Reveals Deadpool, Castle Doomstadt, Doombots | Everything Always | Film & Animation | 2026-10-05 | 74,160 | https://www.youtube.com/watch?v=CHul6mHnPMI |
| 15 | Where Did Grandmas House Lead Me… | CaseOh | Gaming | 2026-10-05 | 118,220 | https://www.youtube.com/watch?v=W4kW0L9zzbo |
| 16 | Stand By Me | Ben E. King - Topic | Music | 2026-09-29 | 391,155 | https://www.youtube.com/watch?v=n1PEyqySLjM |
| 17 | Garividi Lakshmi Trailer | T-Series Telugu | Music | 2026-10-05 | 250,384 | https://www.youtube.com/watch?v=GiSqnQhWI80 |
| 18 | GTA5 - Okay, NOW It's the Final Game Session! | VanossGaming | Gaming | 2026-10-05 | 840,304 | https://www.youtube.com/watch?v=ofgPZp3-WEg |
| 19 | Algarete (Neoperreo) | Nobdy - Topic | Music | 2026-09-29 | 1,311,817 | https://www.youtube.com/watch?v=GPB30bWHMTs |
| 20 | Hanuman Ansh Telugu Trailer | Hombale Films | Entertainment | 2026-10-05 | 1,044,300 | https://www.youtube.com/watch?v=DDyZq1QEybI |
| 21 | Try Not To Get AGE-RESTRICTED Challenge #2 | Markiplier | Gaming | 2026-10-04 | 1,765,545 | https://www.youtube.com/watch?v=o2JkhCiOQBY |
| 22 | YFG Fatso - "Bougie Hoes Pt 2 [Official Music Video] | YFG Fatso | People & Blogs | 2026-10-03 | 273,390 | https://www.youtube.com/watch?v=Ge2xeRJAHv8 |
| 23 | All New Skins, Solo Leveling Collab, Doctrine, & MORE! - Overwatch Season 5 Trailer Breakdown | Master Ian Gamer | Gaming | 2026-10-05 | 54,745 | https://www.youtube.com/watch?v=54syvsGJH1E |
| 24 | Gaming will never be the same.. | Asmongold TV | Gaming | 2026-10-05 | 807,873 | https://www.youtube.com/watch?v=5HpRIOvo5Jk |
| 25 | Creeré | Tercer Cielo - Topic | Music | 2026-10-01 | 209,900 | https://www.youtube.com/watch?v=yZY-PhVxQzo |
| 26 | The Standard - (Official Trailer) \| Chris Bumstead Documentary | Chris Bumstead | Sports | 2026-10-05 | 303,227 | https://www.youtube.com/watch?v=IYlR70uPrWU |
| 27 | GRIEF - STREAM 1 | Trick | Gaming | 2026-10-06 | 579,418 | https://www.youtube.com/watch?v=rDeYgmWMYJ8 |
| 28 | All The Things She Said | Septemberry - Topic | Music | 2026-09-29 | 1,159,748 | https://www.youtube.com/watch?v=04l5nCVrAGI |
| 29 | Hell Week 666 Trailer \| Sam and Colby | XPLR Highlights | People & Blogs | 2026-10-03 | 183,299 | https://www.youtube.com/watch?v=H36rDvDG4ZM |
| 30 | We Automate Infinite Netherite - Sky Factory Season 7 EP 4 | SSundeePlus | People & Blogs | 2026-10-04 | 940,120 | https://www.youtube.com/watch?v=RqagxX1-dP8 |
| 31 | Saii Kay, Dabz Wills - Maris Talaigu | SaiiKayVEVO | Music | 2026-09-09 | 318,471 | https://www.youtube.com/watch?v=RcU67qwHf4w |
| 32 | Episode 4: Angels Among Us Trailer \| Victoria's Secret | Victoria's Secret | Entertainment | 2026-10-04 | 135,390 | https://www.youtube.com/watch?v=ruh9yJWJX2M |
| 33 | GUESS THE YOUTUBER w/ Foltyn | CaylusBlox | Gaming | 2026-10-05 | 159,630 | https://www.youtube.com/watch?v=oeuGc8mfKsw |
| 34 | Ambe-Saii kay(Da-rock Localremix) | Da-rock Music - Topic | Music | 2026-09-07 | 83,994 | https://www.youtube.com/watch?v=F4BCYKpWwf4 |
| 35 | I Hate Clips... | Jynxzi | Gaming | 2026-10-04 | 1,208,859 | https://www.youtube.com/watch?v=m2kVV-COOno |
| 36 | KAROL G, Judeline, rusowsky - BbY WOW \| Letra | sunday | Music | 2026-10-02 | 1,992,195 | https://www.youtube.com/watch?v=O9rLu25w95s |
| 37 | ROBLOX BALL vs BALL... | More Techy | Gaming | 2026-10-05 | 184,184 | https://www.youtube.com/watch?v=ZwJsq4am-_E |
| 38 | MIX NGI (feat. Jarahn & Dabz wills) | Cammy B - Topic | Music | 2026-10-01 | 11,228 | https://www.youtube.com/watch?v=Dodw0r5pmQ4 |
| 39 | Slowly Becoming Cat in the Hat in Murder Mystery 2... | Techy Plays | Gaming | 2026-10-05 | 249,655 | https://www.youtube.com/watch?v=GeUJxh2Suk8 |
| 40 | THERE HASN'T BEEN A CROSSOVER THIS COLD SINCE JIMMY AND TIMMY! | RDC Live | Gaming | 2026-10-05 | 113,148 | https://www.youtube.com/watch?v=N-AN3o_hkpM |
| 41 | This is Going To Get Me Banned... | SSundee | Gaming | 2026-10-05 | 137,189 | https://www.youtube.com/watch?v=DtWW9wbIsAQ |
| 42 | Our New QB Is UNSTOPPABLE! Wheel of MUT! Ep. #4 | MMG | Sports | 2026-10-04 | 452,119 | https://www.youtube.com/watch?v=gHZ1vTOC2ng |
| 43 | GTA 6: NEW INFO - Money, Lucia's Backstory, New Screenshot, NPCs & More... | TGG | Gaming | 2026-10-05 | 639,270 | https://www.youtube.com/watch?v=0VhNvKNUcuc |
| 44 | I'm A Robot Vacuum In A Horror Game. | Joe Bart Games | Gaming | 2026-10-05 | 312,364 | https://www.youtube.com/watch?v=Zv1dVeV4nPw |
| 45 | The Dark Truth Behind Roblox LETHAL APE... | Techys | Gaming | 2026-10-05 | 177,506 | https://www.youtube.com/watch?v=KQvvKHsm7K8 |
| 46 | im back (live) | Ludwig | Gaming | 2026-10-06 | 299,243 | https://www.youtube.com/watch?v=5vRiQ9o2aqI |
| 47 | Week 8 Teaser | FridayNightFunkin | Gaming | 2026-10-06 | 38,024 | https://www.youtube.com/watch?v=NpkgrxZWJhs |
| 48 | ESL Pro League Season 24 - Day 3 - Stream A - Full show | ESL Counter-Strike | Gaming | 2026-10-05 | 2,408,968 | https://www.youtube.com/watch?v=GWkVaZlFFRU |
| 49 | Hermitcraft 11: Episode 29 - HAUNTING HERMITS! | Grian | Gaming | 2026-10-04 | 885,207 | https://www.youtube.com/watch?v=jKeTyuj1xPc |
| 50 | DR DISRESPECT - DOCTOBER 2026 CONTEST ANNOUNCED (live) | DrDisRespect | Gaming | 2026-10-06 | 345,846 | https://www.youtube.com/watch?v=LNQuOwZjt0s |

Shape of the list: 27 of 50 are Gaming, 13 Music, the rest trailers and entertainment. A new game called GRIEF shows up twice (ranks 3 and 27). No news/commentary video made the top 50.

### TikTok

- **Status: US platform trends unverified.** TikTok's native trend surface (Creative Center, Trends > Hashtags, US, 7 days) rendered only a navigation shell to an unauthenticated read, and its public JSON endpoint returned `{"code":40101,"msg":"no permission"}` (checked 2026-10-05T21:54-05:00). No authorized logged-in browser session was available to this run.
- **Third-party trend estimate (partial, not US-only):** Tokchart "Top Trending TikTok Sounds", page dated 2026-10-06, checked 2026-10-05T21:55-05:00, https://tokchart.com/ . Ranked by Tokchart's proprietary 1-1000 score; regions are multi-country; only rows 1-5 are free (rest paywalled). Only items with a US region label are relevant to this docket:

| Tokchart # | Sound | Score | Videos | Daily videos | Views | Regions listed | Sound origin |
|---|---|---|---|---|---|---|---|
| 1 | "Dont Forget October 3rd" (uploader name is a profanity) | 992 | 1.1M | +1.1M/day (provider figure) | 447M+ | US, UK, +17 | provider says Sep 2009 (likely the original audio clip date; unverified) |
| 3 | "Zany Emote Fortnite" (CsCrafty) | 980 | 246K | +48.6K/day | 365M+ | US, JM, +22 | about 5 years old |

  Rows 2, 4, 5 are Nigeria-, Thailand- and Indonesia/Malaysia-led sounds (not US).
- **Excluded as stale/unverified:** socialcal.app "trending TikTok songs" (says it mirrors Creative Center, but last update shown was 2026-05-12); publisher blog roundups of "October TikTok trends" (editorial, no rank/metrics).

## Neutral source context and optional trending-lesson candidate

Only one candidate is supported by the observed platform evidence and has a teachable question. It is offered, not selected.

### Candidate: Fort Hood shooter Nidal Hasan, firing squad approved

**Platform link:** "Fort Hood" at #44 on the trends24 X estimate (21:28 CDT block). Third-party estimate, not native X verification; the provider does not show why it trended. Not on the YouTube native chart. TikTok unverified. Fresh YouTube coverage exists but is small (top result at check: Ben Dykes, "Trump Just Approved a Firing Squad for Nidal Hasan", 11:17, 1,208 views, published 2026-10-06T02:02Z, https://www.youtube.com/watch?v=vXdngxfSgTE). Momentum unknown.

**What happened.** On 2026-10-05 the Pentagon's chief spokesman said the Secretary of War recommended, and President Trump approved, execution by Army firing squad for Nidal Malik Hasan. Hasan, a former Army psychiatrist, killed 13 people and wounded 32 at Fort Hood, Texas, on 2009-11-05, and a military jury convicted him and sentenced him to death in August 2013. Under military law the President must approve a death sentence before it can be carried out; the Secretary of the Army is to set the time and place. If it happens it would be the first US military execution since 1961, and the first by Army firing squad since 1945.

**Fact sheet, questioned not trusted**

Documented (checkable records):
- Attack date 2009-11-05; 13 killed, 32 wounded; court-martial conviction and death sentence August 2013 (military court record; reported consistently since 2013).
- The approval announcement itself: a post on X by Chief Pentagon Spokesman Sean Parnell, quoted by Army Times as: "Secretary of War Pete Hegseth has recommended — and President Donald J. Trump has approved — death by U.S. Army firing squad for convicted terrorist Nidal Malik Hasan." (Army Times, J.D. Simkins, published 2026-10-06 01:01). The original X post URL was not retrieved in this run (X blocked unauthenticated reads); pull it up live.
- Last US military execution: 1961 (Army Pvt. John Bennett, hanging); last Army firing-squad execution: Pvt. Eddie Slovik, 1945-01-31 (Army Times; matches the historical record).

Claimed (who says it, how they would know, what they gain):
- "Hasan said his attack was in defense of Taliban leadership" (Army Times summarizing his court statements; he represented himself at trial, so the record exists, but the exact wording should be checked against trial transcripts before quoting).
- Hasan's death sentence was upheld by the Court of Appeals for the Armed Forces (secondary sources online, one dating it 2023; date and ruling not verified here). Gain: settles whether appeals are really exhausted.
- Framing differs by outlet: Washington Times, Fox, PJ Media and RedState (all 2026-10-05) lead with "terrorist"/"jihadi" and the firing squad as justice; critics of the death penalty were not quoted in the coverage checked. Each side gains an audience that already agrees with it.

Unknown (as of 2026-10-05 22:00 CDT):
- Execution date and place (Secretary of the Army has not announced).
- Whether Hasan has any pending Supreme Court petition or federal habeas challenge, and whether any court will pause it.
- Why a firing squad rather than lethal injection, in the Pentagon's own words beyond the one-line announcement.
- What the victims' families think of this decision (none quoted in the sources checked).

**Founder twist:** to add by Jaden. Neutral open questions if useful: who should decide how a convicted killer dies, and does method matter; why did this take 17 years; is justice delayed still justice.

**Receipts to pull up on screen (in order):**
1. Sean Parnell's X post announcing the approval (find live on x.com; not retrieved here).
2. Army Times straight report: https://www.armytimes.com/news/your-military/2026/10/06/fort-hood-mass-shooter-nidal-malik-hasan-to-die-by-us-army-firing-squad/
3. Washington Times (2026-10-05): https://www.washingtontimes.com/news/2026/oct/5/trump-oks-firing-squad-execution-fort-hood-shooter-nidal-hasan/
4. Fox News: https://www.foxnews.com/politics/trump-clears-way-fort-hood-terrorist-face-army-firing-squad-nearly-17-years-after-massacre
5. Background on the 2009 attack and trial: https://en.wikipedia.org/wiki/2009_Fort_Hood_shooting (secondary; use for dates only).

**Guardrails:** 13 people died; lead with respect for them and their families, never put victims on the thumbnail, no replaying attack footage as the draw. Hasan's conviction is a court record, so "convicted" is fair; motives beyond his own trial statements stay "claimed". Debate the policy, not anyone's grief.

**Title idea:** "The Fort Hood Shooter and the Firing Squad: What Does Justice Look Like 17 Years Later?"

**Crew cues, if useful (neutral):**
- Higher Self: The approval is documented by the Pentagon's own post. The date, place and any last appeals are still unknown.
- Researcher: The last US military execution was 1961; the last Army firing squad, 1945. Ask who decided the method and why.
- Skeptic: Every outlet checked framed it one way; no opponents were quoted. Ask who is missing from the story.

## Recent news, not verified platform trends

- **Kirk Franklin** (on the X estimate at #6, driver unknown): released a single with GloRilla 2026-09-28 and announced the album *I Am What I Am* for 2026-10-30 (Rapzilla, Sept 2026, https://rapzilla.com/2026-09-kirk-franklin-reveals-new-album-i-am-what-i-am-song-glorilla/). Nothing found explains a spike tonight; do not present as the reason he trended.
- No other recent news story was added; same-day headline roundups seen in search (2026-10-05) were not independently verified in this run.

## Optional reaction videos

Coverage: the 50 matched YouTube channels in Creator Library Sources were scanned through the official YouTube Data API at 2026-10-05T21:55-05:00 (49 reachable; robdyrdek uploads list unreachable). Long-form uploads (10+ min) from the last 21 days were ranked by views versus that channel's recent long-form median, then by show fit. Excluded as already covered: JRE #2560 David Grusch, Jesse Michels Aztec, Acid for Squares Kip Andersen, the DOAC/Shawn Ryan prep. None of these catalog videos appear on the YouTube native chart above, so **none is a verified platform trend**; they are show-fit picks with measured relative performance. Playback and captions were not checked.

### Recommended main video
- **The theory of time that proves your past self still exists**, Aperture. https://www.youtube.com/watch?v=Hv7f1bedXOE
- Published 2026-09-27 (8.5 days old at check). Full video 29:41.
- Evidence checked: 2026-10-05T21:56:02-05:00, YouTube Data API metadata (public, embeddable). 753,187 views, about 5.2x the channel's recent long-form median. Status: verified metadata; playback, captions and content claims not checked.
- Neutral context: a produced philosophy/physics explainer on time (block universe style ideas). Good pause points will be wherever it moves from physics to "your past self still exists". Strongest counterpoint: block-universe interpretations are one reading of relativity, not an experimental result; many physicists hold other views. Founder twist: to add by Jaden.

### Alternative 1
- **Global Meet-Up #6 (Montreal): The Supremacy of Sin**, Predictive History. https://www.youtube.com/watch?v=YyUl1QerHjA
- Published 2026-10-04 (1.6 days old). Full video 3:06:58 (would need an excerpt; none chosen).
- Evidence checked: 2026-10-05T21:56:02-05:00, API metadata. 307,218 views, about 10.4x the channel's recent long-form median. Verified metadata only; live meet-up format, audio/caption quality unchecked.
- Neutral context: Predictive History's live talk to an audience. Counterpoint: its forecasts are one lecturer's model of history; check any specific prediction against what happened. Founder twist: to add by Jaden.

### Alternative 2
- **Dusty Slay - Moon Landing Conspiracies, Flat Earth, Aliens and the Nephilim | SRS #344**, Shawn Ryan Show. https://www.youtube.com/watch?v=X9aAQw9mxg4
- Published 2026-10-01 (4.4 days old). Full video 2:49:16 (excerpt needed).
- Evidence checked: 2026-10-05T21:56:02-05:00, API metadata. 1,078,149 views, about 2.6x the channel's recent long-form median. Verified metadata only.
- Neutral context: a comedian talking through popular conspiracy theories. Counterpoint: moon-landing and flat-earth claims have strong public counter-evidence (retroreflectors, independent tracking, returned samples); attribute every claim to the speaker. Founder twist: to add by Jaden.

## Daily ritual (Tuesday)

**Yoga (Tuesday, 40-minute cap applies):**
- **Do This When Your Whole Body Feels Tight**, Breathe and Flow (original channel, UCbfPq-uRqonJQli41muSLeQ). https://www.youtube.com/watch?v=8lkJi4ldZ90
- Runtime 29:58 (API duration, full video), so it **meets the 40-minute cap**. Published 2021-04-09.
- Evidence checked: 2026-10-05T21:55:37-05:00, YouTube Data API (public, embeddable). Playback not checked.
- Context: Tuesday follows Monday's upper-body workout. Proposed fit: full-body deep stretch, moderate.
- Gentler alternative if worn: **Do This Before Bed When Your Body Won't Let Go**, Breathe and Flow, https://www.youtube.com/watch?v=RI5gOBeTqyE , 14:08, published 2019-07-10 (same check).

**Frequency audio (The Power Of You, founder-confirmed channel https://www.youtube.com/@ThePowerOfYou):**
- **The Inner Temple - 10 Hz Deep Alpha Binaural Beats - Enter The Kingdom of Your Higher Self**. https://www.youtube.com/watch?v=KZZiMIMQNPI
- Labeled 10 Hz (publisher's label, alpha binaural beat; not measured). Full runtime 6:00:23; published 2026-10-05 (newest upload). 5,336 views at check.
- Evidence checked: 2026-10-05T21:55:37-05:00, YouTube Data API (public, embeddable). Playback not checked.
- Proposed use: background during meditation and the I Am God mantra; binaural tracks are made for headphones, so on stream it plays as an ambient bed. No specific effect is promised.
- Not a repeat: no prior use found in the vault log. (Yesterday's docket file was offline in iCloud and could not be read to confirm its frequency pick.)

## Optional evergreen fallbacks

None added tonight. Older relevance picks from earlier dockets remain in those dockets.

## Run notes

- Light run, 2026-10-05 21:50-22:05 CDT, after the protected window; OBS was not running. Read-only web and official YouTube API only; no downloads, renders, uploads, paid calls or account changes.
- Access gaps for the founder: X native trends and TikTok Creative Center both need a logged-in browser session this run did not have.
