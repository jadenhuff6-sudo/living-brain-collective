---
type: project
created: 2026-10-06
updated: 2026-10-06
tags: [stream-prep, trending]
---

# 2026-10-07 - Trending docket

Stream date: Wednesday 2026-10-07 (America/Chicago). Prepared 2026-10-06 19:30-19:55 CDT by the trending-docket skill.

**Founder selection: pending.** **Founder twist: to add by Jaden.** These are recommendations, not an approved Stream Plan. Tomorrow already has a prepared breakdown, 2026-10-07 - Julian Dorey Simon Dixon highlights; nothing here replaces it.

Coverage at a glance:
- X / Twitter: **US platform trends unverified (native)**. Two third-party estimates, US-labeled, hourly snapshots. Sports-heavy (MLB postseason Dodgers/Braves).
- YouTube: **native US chart verified** (official YouTube Data API `chart=mostPopular`, regionCode US). Gaming/music-heavy.
- TikTok: **US platform trends unverified**. Creative Center blocked; one global third-party sound estimate.

## US platform trends

### X / Twitter

- **Status: US platform trends unverified.** x.com/explore returned only the logged-out app shell (HTTP 200, no trend data) at 2026-10-06T19:31:17-05:00. No authorized read-only X trends access exists in this setup.
- **Evidence class: third-party trend estimate** (trends24.in, getdaytrends.com). Both say they mirror X's US trend list; collection method and ranking logic are not documented. No post volumes were shown (empty count fields), so metrics are `unknown`. Ranks are the provider's order, not X's verified rank.
- **Region:** "United States" as labeled by the providers (not independently verified).
- **Observation window:** trends24 hourly blocks at 2026-10-06T18:58:01-05:00 (latest), 18:03:55 and 17:12:42. getdaytrends: current list, no timestamp shown.
- **Checked:** 2026-10-06T19:31:17-05:00.
- Sources: https://trends24.in/united-states/ , https://getdaytrends.com/united-states/

**trends24 US, block 18:58 CDT (rank, topic):**

| # | Trend | # | Trend | # | Trend | # | Trend | # | Trend |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Freddie | 11 | Dubon | 21 | Mookie | 31 | Soares | 41 | E 234x |
| 2 | Chris Sale | 12 | Eva Marie Saint | 22 | Better Call Saul | 32 | 26 P | 42 | Dear Canada |
| 3 | Messi | 13 | San Diego | 23 | Dylan Larkin | 33 | Boomers | 43 | Ha-Seong Kim |
| 4 | Yamamoto | 14 | North by Northwest | 24 | Rowdy Tellez | 34 | #LADvsATL | 44 | Maradona |
| 5 | Acuna | 15 | Mr. October | 25 | Bierley | 35 | Abstract | 45 | Anduril |
| 6 | #Dodgers | 16 | #ElUltimoTango | 26 | Baldwin | 36 | Scaloni | 46 | Merino |
| 7 | Lane Johnson | 17 | On the Waterfront | 27 | Tropical Depression Nine | 37 | #NLDS | 47 | Pelé |
| 8 | #DWCS | 18 | Bussi | 28 | Onley | 38 | Kenny Albert | 48 | Benin |
| 9 | Ohtani | 19 | Andrew Tate | 29 | 2x PEG | 39 | Ponzi | 49 | Social Security |
| 10 | Kike Hernandez | 20 | Baba | 30 | 45% EPS | 40 | Chet Hanks | 50 | Eric Andre |

Earlier blocks, top 10:
- 18:03 CDT: Lane Johnson, Chris Sale, Dubon, Eva Marie Saint, San Diego, Ohtani, Messi, North by Northwest, On the Waterfront, Yamamoto. (Also in that block: Andrew Tate #12, Russ Vought #34, Sally Yates #47, Macron #48, Rod Stewart #44.)
- 17:12 CDT: Lane Johnson, San Diego, Better Call Saul, Eva Marie Saint, Baba, Tropical Depression Nine, Messi, Freddie Jackson, Andrew Tate, 2x PEG.

**getdaytrends US, current (top 20, no volumes/timestamp):** 1 Freddie, 2 Chris Sale, 3 Messi, 4 acuña, 5 Yamamoto, 6 #Dodgers, 7 Lane Johnson, 8 #DWCS, 9 Kike Hernandez, 10 Ohtani, 11 Dubon, 12 Eva Marie Saint, 13 san diego, 14 #ElUltimoTango, 15 North by Northwest, 16 Mr. October, 17 On the Waterfront, 18 Bussi, 19 Andrew Tate, 20 Baldwin. Ranks 21-50 essentially match trends24.

Reading the list (agent note, not provider categories): the evening is dominated by the MLB postseason (#LADvsATL, #NLDS: Freddie, Chris Sale, Yamamoto, Acuna, Ohtani, Mookie) and football (Lane Johnson). Non-sports items, drivers checked where possible:
- **Eva Marie Saint / North by Northwest / On the Waterfront** (#12/#14/#17, in the top 10 of the two earlier blocks): driver confirmed by same-day news, her death at 102 (see candidate below).
- **Andrew Tate** (#19; #12 and #9 earlier): **driver not identified.** Background from prior reporting: he and Tristan Tate are fighting UK extradition from a Miami federal detention center (bail denied, NPR 2026-09-09); they deny all allegations. Nothing found tonight shows what new development, if any, drove today's spike.
- **Lane Johnson**: background only; Eagles tackle who said 2026 is "probably" his last season (philadelphiaeagles.com). Today's specific driver not confirmed.
- **Tropical Depression Nine, Social Security, Ponzi, Better Call Saul, Russ Vought, Sally Yates, Anduril, Boomers, 2x PEG / 45% EPS / 26 P** (finance-tweet fragments): drivers not checked or unknown.
- Momentum/velocity: unknown (three hourly snapshots, no volumes).

### YouTube

- **Status: native US chart verified.** Evidence class: **native platform trend** (YouTube's own "most popular" chart via the official YouTube Data API v3, `videos.list chart=mostPopular regionCode=US`, read-only, existing channel credentials).
- **Region:** US (API parameter). **Window:** YouTube does not publish the chart's window or formula; all-category, not personalized. Caveat: the public Trending page was retired in 2025; ranking is clearly not raw views (rank 1 has 112,635 views).
- **Checked:** 2026-10-06T19:30:41-05:00. Views are cumulative at check time; no velocity measured.
- Category = the uploader's YouTube category.

| # | Title | Channel | Category | Published (UTC) | Length | Views at check | Link |
|---|---|---|---|---|---|---|---|
| 1 | Yu Les – Jarahn ft. SHLD, Nene Morus & Rich Antony (Official Music Video) | Jarahn | Music | 2026-09-25 | 4:02 | 112,635 | https://www.youtube.com/watch?v=6pm4s82cMuA |
| 2 | Frozen Trail Launch Trailer \| ARC Raiders | ARC Raiders | Gaming | 2026-10-06 | 1:56 | 348,442 | https://www.youtube.com/watch?v=KjiJDylLdZA |
| 3 | Escaping Terminus: The Deadliest Minecraft Prison | FlameFrags | Gaming | 2026-10-06 | 1:58:47 | 1,964,141 | https://www.youtube.com/watch?v=8t8YBu7bdT0 |
| 4 | Bow | FOB Huncho - Topic | Music | 2026-09-29 | 2:16 | 131,732 | https://www.youtube.com/watch?v=guYIc9Ves5E |
| 5 | Season 5: A Grim Doctrine Launch Trailer \| Overwatch | PlayOverwatch | Gaming | 2026-10-05 | 2:21 | 586,815 | https://www.youtube.com/watch?v=Ih6DVdyQn3I |
| 6 | INFINITE MONEY GLITCH FOUND \| Bills Must Be Paid | Markiplier | Gaming | 2026-10-06 | 1:19:22 | 662,214 | https://www.youtube.com/watch?v=FUW8BCRH9FM |
| 7 | Bjorn Bonebreaker - Mama, Don't Close Your Eyes [Official Lyrics Video] | Bjorn Bonebreaker | Music | 2026-09-14 | 2:39 | 762,457 | https://www.youtube.com/watch?v=r8h8Kee_PYU |
| 8 | JAILER 2 - Official Trailer \| Superstar Rajinikanth \| Sun Pictures \| Anirudh \| Nelson | Sun TV | Entertainment | 2026-10-05 | 2:25 | 14,520,619 | https://www.youtube.com/watch?v=FW_PPcr1sPE |
| 9 | Season 10.5: New Modes and Halloween // Dev Vision Vol. 22 \| Marvel Rivals | Marvel Rivals | Gaming | 2026-10-06 | 4:39 | 578,779 | https://www.youtube.com/watch?v=MHqiMvdtrYY |
| 10 | 👯‍♀️🏔️ANDEAN NIGHTS / LATIN URBAN🪘 / SLAP HOUSE 🎶/ MELODIC TECHNO HOUSE🎉👯 | MelodiZenith | Music | 2026-09-24 | 4:06 | 3,861,331 | https://www.youtube.com/watch?v=_BLmo7NhDJk |
| 11 | Honest Trailers \| Master and Commander: The Far Side of the World | Screen Junkies | People & Blogs | 2026-10-06 | 7:27 | 224,449 | https://www.youtube.com/watch?v=cPjW_ESwKXU |
| 12 | PLAYING HARDCORE MINECRAFT UNTIL WE BEAT IT DAY 1 | Jynxzi | Entertainment | 2026-10-06 | 6:15:27 | 1,460,057 | https://www.youtube.com/watch?v=LPztP1mrKkw |
| 13 | Money On The Dash | LUCØ - Topic | Music | 2026-10-01 | 2:00 | 458,343 | https://www.youtube.com/watch?v=fv0ebPWwtVg |
| 14 | Gods Don't Give Gifts - Official Trailer (2026) | Gossip Goblin | Film & Animation | 2026-10-06 | 1:49 | 276,286 | https://www.youtube.com/watch?v=1G5LArU7tmE |
| 15 | Surviving in a Maze isn't Easy... | SMii7Y | Gaming | 2026-10-05 | 36:01 | 1,969,040 | https://www.youtube.com/watch?v=AsGh9FojXbM |
| 16 | We fell in love in October (Gravagerz REMIX) | SHLL. - Topic | Music | 2026-09-29 | 2:47 | 829,670 | https://www.youtube.com/watch?v=U_m6o1g_JAg |
| 17 | TDS: Halloween 2026 Trailer | Paradoxum Games | Film & Animation | 2026-10-06 | 1:17 | 114,931 | https://www.youtube.com/watch?v=ISMNK4Jr9Fs |
| 18 | Gears of War is worse than woke.. | Asmongold TV | Gaming | 2026-10-06 | 2:57:39 | 982,805 | https://www.youtube.com/watch?v=5iqD_WcY5jg |
| 19 | El Gigante de Hierro | Grupo Sonador - Topic | Music | 2026-10-01 | 3:37 | 322,150 | https://www.youtube.com/watch?v=cPIMvQvvSLM |
| 20 | Dead by Daylight \| NieR:Automata Collection \| Reveal Trailer | Dead by Daylight | Gaming | 2026-10-06 | 1:03 | 108,006 | https://www.youtube.com/watch?v=NoEBBp789WU |
| 21 | 30 Seconds to Detonation 💣 | Clash Royale | Gaming | 2026-10-06 | 0:45 | 415,470 | https://www.youtube.com/watch?v=icsvRE68MxA |
| 22 | EON, Neton Vega, De La Rose, L Prince - NI TAN SANTX (Video Oficial) | Warner Música | Music | 2026-10-02 | 3:20 | 488,728 | https://www.youtube.com/watch?v=xspyQqNlkZY |
| 23 | I Kill The Bear \| Official Series Trailer | Letterkenny Problems | Comedy | 2026-10-06 | 2:49 | 65,293 | https://www.youtube.com/watch?v=3JWEGVpNIiQ |
| 24 | GRIEF (VERIFIED) // TOP 1 | Doggie | Gaming | 2026-10-05 | 8:40 | 2,217,447 | https://www.youtube.com/watch?v=gB8slBPlOjc |
| 25 | Moving To The Sun | quitjob - Topic | Music | 2026-09-29 | 2:32 | 1,388,492 | https://www.youtube.com/watch?v=Huj-UJ8LKhI |
| 26 | Battlefield 6 - Official Season 5 Las Vegas Gameplay Trailer | IGN | Gaming | 2026-10-06 | 2:06 | 201,880 | https://www.youtube.com/watch?v=jIa8BGPhtxE |
| 27 | Learn The Skill, Win $1,000 (Minecraft) | Cash | Entertainment | 2026-10-06 | 20:51 | 275,252 | https://www.youtube.com/watch?v=g4viqmRp6V0 |
| 28 | Rammstein - Live in Mexico City - Sonne (Official Video) | Rammstein Official | Music | 2026-10-05 | 4:59 | 1,668,264 | https://www.youtube.com/watch?v=UxmdCABl1EY |
| 29 | True Damage: Know My Name \| Skins Trailer - League of Legends | League of Legends | Gaming | 2026-10-06 | 1:41 | 296,518 | https://www.youtube.com/watch?v=l-AeX7nZIm0 |
| 30 | The Ultimate Peggle Challenge, but I programmed a frog | DougDougDoug | Gaming | 2026-10-06 | 28:57 | 192,766 | https://www.youtube.com/watch?v=0UjMRq3UHH0 |
| 31 | I Want to Know What Love Is (1999 Remaster) | Foreigner - Topic | Music | 2026-09-30 | 5:05 | 122,552 | https://www.youtube.com/watch?v=lWFCmtc2YFQ |
| 32 | Comrade Kalyan - Official Trailer \| Sree Vishnu \| Mahima Nambiar \| Janakiram Marella | Saregama Telugu | Entertainment | 2026-10-06 | 2:31 | 1,482,978 | https://www.youtube.com/watch?v=QTz5PqZspEs |
| 33 | 🔴LIVE \| DAWSON OAKS TRAILER PARK \| GIMMICK X JOHN \| MANY MEN MONDAY \| #BUNGULATE | TheBurntPeanut | Gaming | 2026-10-06 | 7:11:48 | 792,934 | https://www.youtube.com/watch?v=07MQ-kscC7I |
| 34 | Mili - Rendezvous [Limbus Company] | Mili | Music | 2026-10-04 | 3:46 | 1,673,002 | https://www.youtube.com/watch?v=3gkSzjp-aoY |
| 35 | Disney Epic Mickey: Rebrushed – Launch Trailer – Nintendo Switch 2 | Nintendo of America | Gaming | 2026-10-06 | 0:43 | 258,445 | https://www.youtube.com/watch?v=VeV7U7104GE |
| 36 | I’m the LAST DEMON! | Aphmau | Gaming | 2026-10-06 | 21:02 | 147,312 | https://www.youtube.com/watch?v=tLxWVtOEYGQ |
| 37 | MIX NGI (feat. Jarahn & Dabz wills) | Cammy B - Topic | Music | 2026-10-01 | 3:19 | 13,697 | https://www.youtube.com/watch?v=Dodw0r5pmQ4 |
| 38 | Spider-Man: Brand New Day Extended Preview (2026) | Fandango (Stream) | Film & Animation | 2026-10-06 | 9:28 | 151,764 | https://www.youtube.com/watch?v=YRqKt-aYPqM |
| 39 | Everything Is Everything Now | Big A | People & Blogs | 2026-10-06 | 23:51 | 673,407 | https://www.youtube.com/watch?v=jp7hM1vKRpY |
| 40 | Saii Kay, Dabz Wills - Maris Talaigu (Official Music Video) | SaiiKayVEVO | Music | 2026-09-09 | 3:37 | 327,145 | https://www.youtube.com/watch?v=RcU67qwHf4w |
| 41 | Heartland \| Official Trailer \| Netflix | Netflix | Entertainment | 2026-10-06 | 2:08 | 141,825 | https://www.youtube.com/watch?v=ziIz59enN1c |
| 42 | Where Did Grandmas House Lead Me… | CaseOh | Gaming | 2026-10-05 | 1:09:30 | 459,418 | https://www.youtube.com/watch?v=W4kW0L9zzbo |
| 43 | Ambe-Saii kay(Da-rock Localremix) | Da-rock Music - Topic | Music | 2026-09-07 | 4:04 | 88,424 | https://www.youtube.com/watch?v=F4BCYKpWwf4 |
| 44 | The New Terrance and Phillip Movie Trailer | Comedy Central | Entertainment | 2026-10-06 | 31:05 | hidden | https://www.youtube.com/watch?v=q89IgW_NKFA |
| 45 | Using Glitches To Cheat In Steal an Egg Hide & Seek… | Techy Plays | Gaming | 2026-10-06 | 10:53 | 177,298 | https://www.youtube.com/watch?v=gN1IXbLUXZY |
| 46 | Romeo Santos - La Diabla \| Letra | Malaver Lyrics | Music | 2026-09-30 | 4:00 | 502,095 | https://www.youtube.com/watch?v=jWrj0UIojhc |
| 47 | Star Wars: Galactic Racer™ \| Official Launch Trailer | Star Wars | Entertainment | 2026-10-06 | 2:14 | 130,719 | https://www.youtube.com/watch?v=pR-V3j-sc7s |
| 48 | POOR vs RICH TRAIN Build Challenge! (Minecraft) | TechyCraft | Gaming | 2026-10-06 | 14:58 | 224,127 | https://www.youtube.com/watch?v=TqS53IRD3zs |
| 49 | Stand By Me | Ben E. King - Topic | Music | 2026-09-29 | 2:58 | 398,796 | https://www.youtube.com/watch?v=n1PEyqySLjM |
| 50 | Southern Charm \| Season 12 Official Trailer (Bravo, 2026) | Entertainment Tonight | Entertainment | 2026-10-05 | 2:31 | 59,773 | https://www.youtube.com/watch?v=rRIe0y8tcnw |

Shape of the list: 19 of 50 Gaming, 17 Music, 8 Entertainment, 3 Film & Animation, 2 People & Blogs, 1 Comedy. Mostly game trailers, long gaming streams and music. Cross-platform note: "We fell in love in October" appears here as a remix (#16) and the girl in red original is #3 on the Tokchart TikTok estimate below; seasonal, not news. No news or commentary video made the top 50 (closest: Asmongold "Gears of War is worse than woke.." at #18, a gaming-culture stream).

### TikTok

- **Status: US platform trends unverified.** TikTok's native trend surface (Creative Center, Trends > Hashtags, US, 7 days) returned only a page shell ("TikTok One Creative Suite") to an unauthenticated read, and its public JSON endpoint returned `{"code":40101,"msg":"no permission"}` (checked 2026-10-06T19:31:17-05:00). No authorized logged-in session was available to this run.
- **Third-party trend estimate (global, not US-only):** Tokchart "Top Trending Audios on TikTok Today", page "Last updated: October 6, 2026", checked 2026-10-06T19:31:17-05:00, https://tokchart.com/ . Tokchart's own note: its 1-1000 score "only represent[s] global trendiness", not country trends. Views/likes are the provider's sampled minimums. Only rows 1-5 are free; later rows are paywalled. Shown in the provider's order; the US column shows whether the provider lists the US among trending countries:

| Tokchart # | Sound (author) | Type | Score | UGC videos | Videos/day (7-day avg, provider) | Min. views | US listed? | First uploaded |
|---|---|---|---|---|---|---|---|---|
| 1 | "sauti asilia - deefleek1" (MR FLEEK), matched song "AkpakO Bum Bum" | UGC contains music | 984 | 597,800 | +40,600 | 177M+ | yes, among 19 countries; led by NG/KE | 3 weeks ago |
| 2 | Original audio, Green Screen Memes | UGC original audio | 980 | 480,900 | +37,800 | 623M+ | yes, US listed first | 1 week ago |
| 3 | "we fell in love in october", girl in red | Catalog sound | 978 | 1,834,457 | +31,218 | 4B+ | yes, among 23 | 7 years ago (2018 song) |
| 4 | "Zany Emote Fortnite", CsCrafty | UGC contains music | 975 | 266,200 | +20,200 | 419M+ | yes, US listed first | 5 years ago |
| 5 | Original audio, N.N. Aung | UGC original audio | 974 | 332,300 | +20,000 | 79M+ | no (TH/MY/SG/MM/JP) | 2 weeks ago |

- No US hashtag or topic list was available from any source this run; the TikTok picture is sounds only.

## Neutral source context and optional trending-lesson candidate

One candidate is supported by the observed platform evidence (third-party X estimate, driver confirmed by same-day news). Offered, not selected. Andrew Tate was also on the X estimate, but no driver was found, so it is not prepped.

### Candidate: Eva Marie Saint dies at 102

**Platform link:** "Eva Marie Saint" #12, "North by Northwest" #14, "On the Waterfront" #17 on the trends24 US estimate (18:58 CDT block); she was #4 in the 18:03 and 17:12 blocks. Third-party estimate, not native X verification; volumes unknown. Not on the YouTube native chart. TikTok unverified. Momentum unknown.

**What happened.** Eva Marie Saint, the actress who won the 1955 Academy Award for Best Supporting Actress for *On the Waterfront* (1954) and starred in Hitchcock's *North by Northwest* (1959), died on Tuesday 2026-10-06 at 102. Reports say she died of natural causes at her home in Los Angeles. She was widely described as the oldest living Oscar winner. She famously stepped back from stardom to raise her family.

**Fact sheet, questioned not trusted**

Documented (checkable records):
- Birth date 1924-07-04 and the Oscar win for *On the Waterfront* (Academy awards database, public record).
- Her film credits, including *North by Northwest* (1959) and *Exodus* (1960) (the films themselves).
- Her own words, as quoted by the Santa Barbara Independent: "I don't want to be a superstar. I was having children." (original interview source not traced in this run; check before quoting on air).

Claimed (who says it, how they would know, what they gain):
- Death on 2026-10-06, natural causes, at home in Los Angeles: reported by the Santa Barbara Independent (Jean Yamamura, 2026-10-06 16:33; the article notes her grandson works at the paper), NPR, the Washington Post, Newsweek and Deadline, all 2026-10-06. No family or representative statement was retrieved in this run; outlets likely sourced the family or a rep. Gain: none obvious; it is a routine obituary.
- "Oldest living Oscar winner" until today: widely repeated by outlets; not checked against the Academy's own records.
- Health/longevity habits (walks, watching the Dodgers, family): from her own 2024 interviews as retold by People and Hello! magazine; secondhand.

Unknown (as of 2026-10-06 19:55 CDT):
- Any statement from her family (none retrieved).
- Memorial or service plans.

**Founder twist:** to add by Jaden. Neutral open questions if useful: what does a 102-year life that chose family over fame say about success; what made the Golden Age films last; does anyone become a legend now the way she did.

**Receipts to pull up on screen (in order):**
1. NPR obituary (2026-10-06): https://www.npr.org/2026/10/06/462030457/eva-marie-saint-on-the-waterfront-dead-102
2. Santa Barbara Independent (2026-10-06): https://www.independent.com/2026/10/06/eva-marie-saint-hollywood-legend-and-montecito-resident-dies-at-102/
3. Washington Post (2026-10-06): https://www.washingtonpost.com/entertainment/2026/10/06/eva-marie-saint-dies/e09c31a8-c1d0-11f1-8170-681419af1cc9_story.html
4. A clip from *North by Northwest* or *On the Waterfront* (find an official studio/Academy clip live; short, for context only).

**Guardrails:** a death of a real person; lead with respect for her and her family. Natural death at 102, so no speculation about cause. No obituary photo or deathbed framing as thumbnail bait. Keep film clips short (fair-use context).

**Title idea:** "Eva Marie Saint Lived to 102 and Chose Family Over Fame: What Did She Know?"

**Crew cues, if useful (neutral):**
- Higher Self: Her death is reported by NPR, the Post and her hometown paper. No family statement has been read on air yet.
- Researcher: She won her Oscar for *On the Waterfront* and starred in *North by Northwest*. She was 102.
- Skeptic: The "oldest living Oscar winner" line is repeated everywhere. Check who held it next.

## Recent news, not verified platform trends

- **Andrew Tate extradition case** (on the X estimate, driver unknown): NPR reported 2026-09-09 that a Miami federal judge denied the Tates bail during their UK extradition fight; they deny all allegations. https://www.npr.org/2026/09/09/nx-s1-5954174/andrew-tate-bail-extradition-jail . Not prepped; if chosen, it falls under the accusations guardrail (alleged/claimed only, both sides' own words).
- No other recent news story was added.

## Optional reaction videos

Coverage: the 50 matched YouTube channels in Creator Library Sources were scanned through the official YouTube Data API at 2026-10-06T19:30:41-05:00 (49 reachable; channel UC0fKsf2yjvE-qQEI4pYba6Q returned an API error). Long-form uploads (10+ min) from the last 21 days were ranked by views versus that channel's recent long-form median, then by show fit. Excluded as already covered: JRE #2560 David Grusch, Acid for Squares Kip Andersen (E113) and Darryl Anka (E112, in mtm58-EPISODE-RECORD), Jesse Michels alien-bodies, the Shawn Ryan and Simon Dixon preps. **None of these appear on the YouTube native chart above, so none is a verified platform trend**; they are show-fit picks with measured relative performance. Playback and captions were not checked.

### Recommended main video
- **Emergency Discussion #3: Xi Visits Trump**, Predictive History. https://www.youtube.com/watch?v=q7GdLK1xwAo
- Published 2026-09-25 (11.2 days old at check). Full video 3:01:21 (would need an excerpt; none chosen).
- Evidence checked: 2026-10-06T19:30:41-05:00, YouTube Data API metadata (public, embeddable). 525,194 views, about 17.4x the channel's recent long-form median (highest relative performance in the catalog tonight). Status: verified metadata; playback, captions and content claims not checked.
- Neutral context: Professor Jiang's lecture-style discussion of a Xi-Trump meeting. Natural link to the Simon Dixon breakdown's "currency war before military war" chapter, if he wants it. Strongest counterpoint: his forecasts are one lecturer's model of history; check any specific prediction against what has actually happened, and confirm the meeting details against official readouts. Founder twist: to add by Jaden.

### Alternative 1
- **Naomi Klein Warns Trump's 'End Times Fascism' Is Already Here**, Zeteo. https://www.youtube.com/watch?v=oS-6Hd6seK4
- Published 2026-10-03 (3.3 days old). Full video 49:06.
- Evidence checked: 2026-10-06T19:30:41-05:00, API metadata. 368,773 views, about 12.0x the channel's recent long-form median. Verified metadata only.
- Neutral context: political commentary interview; one side of a partisan argument. Counterpoint: "fascism" is a contested label; ask for the specific actions and sources behind each claim, and give the administration's own stated reasons. Founder twist: to add by Jaden.

### Alternative 2
- **The theory of time that proves your past self still exists**, Aperture. https://www.youtube.com/watch?v=Hv7f1bedXOE
- Published 2026-09-27 (9.4 days old). Full video 29:41.
- Evidence checked: 2026-10-06T19:30:41-05:00, API metadata. 802,340 views, about 5.4x the channel's recent long-form median. Verified metadata only.
- **Intentional carryover:** recommended in [[2026-10-06 - Trending docket]] but not used (MTM69 reacted to the Astor material). Counterpoint: block-universe ideas are one reading of relativity, not an experimental result. Founder twist: to add by Jaden.

## Daily ritual (Wednesday, abs day)

**Yoga (Wednesday; no 40-minute cap, gentler recommended on abs day):**
- **Do This Before Bed When Your Body Won't Let Go**, Breathe and Flow (original channel, UCbfPq-uRqonJQli41muSLeQ). https://www.youtube.com/watch?v=RI5gOBeTqyE
- Runtime 14:08 (API duration, full video). Published 2019-07-10.
- Evidence checked: 2026-10-06T19:30:41-05:00, YouTube Data API (public, embeddable). Playback not checked.
- Context: abs workout day. Proposed fit: gentle, short. Note it is a bedtime-style flow; fine for a calm morning but not energizing.
- Longer alternative if he wants more: **Do This When Your Whole Body Feels Tight**, Breathe and Flow, https://www.youtube.com/watch?v=8lkJi4ldZ90 , 29:58, published 2021-04-09 (same check; also yesterday's proposal).

**Frequency audio (The Power Of You, founder-confirmed channel https://www.youtube.com/@ThePowerOfYou):**
- **Bridge To The Beyond - 6 Hz Theta Binaural Beats - Align Your Mind With Higher Realms**. https://www.youtube.com/watch?v=jL06YO_PgSo
- Labeled 6 Hz theta (publisher's label, binaural; not measured). Full runtime 4:37:38; published 2026-06-01. 77,743 views at check.
- Evidence checked: 2026-10-06T19:30:41-05:00, YouTube Data API (public, embeddable, channel UCzEFv0Rjl-a0gBMCsvbgEEw). Playback not checked.
- Proposed use: background bed during meditation and the I Am God mantra; binaural tracks are made for headphones, so on stream it plays as ambience. No specific effect is promised.
- Not a repeat: not found in episode records. Yesterday's proposal (The Inner Temple, 10 Hz) was not used on MTM69 (it used a 417 Hz guided meditation) and remains an option.

## Optional evergreen fallbacks

None added tonight. Older relevance picks remain in earlier dockets.

## Run notes

- Light run, 2026-10-06 19:30-19:55 CDT, outside the protected window; launched by the 19:30 job after its OBS check. Read-only web and official YouTube API only; no downloads, renders, uploads, paid calls or account changes. Deadline's article redirected to a paid-access gateway and was not read.
- Access gaps for the founder: X native trends and TikTok Creative Center both need a logged-in browser session this run did not have.
