# Q3 2026 — Strategies & OKRs
*Early start: June 2026. Full quarter: July–September 2026.*

Three goals. Three strategies that bind them. OKRs for each goal below.

---

## Strategies

### Strategy 1 — Fix the Floor Before Building the Tower

**The case study:** In 2019, Healthline audited their full content library and removed thousands of low-quality health articles. Traffic initially dropped, then doubled within 12 months. The mechanism runs counter to instinct — less content, more traffic — but it reflects how Google's quality signal actually works: it is domain-wide, not page-by-page. A cluster of thin or de-indexed pages drags the whole domain down, including the pages that are fine. Smaller niche sites saw the same pattern after the 2023–2024 Helpful Content Updates: sites that purged below-standard content recovered; sites that kept publishing new content on top of it got buried deeper.

**Why this is Strategy 1 for MG:** MG currently has pages de-indexed as AI spam. Author attribution is broken on the live site. There is no methodology page. The rubric system — the entire basis of MG's differentiation — is invisible in the design. Publishing new rubric-compliant reviews on top of this foundation does not fix anything; it adds more pages Google is already primed to distrust. Every other strategy depends on the floor being clean. This one comes first, and it has a hard deadline: nothing new goes live until the audit and template are done.

---

### Strategy 2 — Two Niches, Done Completely

**The case study:** HubSpot documented the Topic Cluster Model in 2017 and recorded a 55% increase in organic traffic within six months after restructuring their content into pillar-and-cluster groups — a single comprehensive pillar page supported by tightly interlinked cluster content on related subtopics. The pattern works because Google interprets the internal link structure as a signal of topical authority: a site that covers a topic deeply, with a clear hierarchy, ranks better than a site that covers many topics shallowly. At small scale, this is how niche sites consistently outrank large general publications on specific queries. ProSettings.net is the gaming-specific version: they became the definitive resource for FPS sensitivity settings by being more thorough on that one topic than anyone else, then expanding. Detailed.com (Glen Allsopp) built a respected SEO resource from zero by going depth-first on a single topic before touching the next.

**Why this is Strategy 2 for MG:** At DA 3, MG can only compete for keywords with a Semrush difficulty under 20. There is no path to 500 clicks through scattered coverage — the authority isn't there. The only viable route is to become the most complete resource on a specific gaming context and let that topical authority start lifting adjacent content. MG's scoring system is already built for this: genre rubrics exist, the write-game-page skill produces the supporting reviews, and the pillar-plus-cluster structure maps directly onto how the OS is organised. The constraint is picking two verticals and executing them completely before touching anything else. Breadth is a Q4 problem.

---

### Strategy 3 — Earn the Link, Don't Ask for It

**The case study:** ProSettings.net built its backlink profile almost entirely through community participation in FPS subreddits and gaming forums — no outreach emails, no link exchanges. The site became the resource people kept sharing because it answered a specific question better than anything else. The links followed the usefulness, not the other way around. The same pattern appears in MG's own persona research: when a poster in r/JRPG ranked 25+ games by specific metrics and explained their criteria publicly, the community engaged intensely — debating methodology, asking follow-up questions, extending the list. The format itself (metric-based, transparent, player-backed) earned organic participation that no promotional post could have generated. Reddit detects 96.4% of manipulation attempts automatically; accounts with no community history posting links are shadowbanned. The model that works is participation first, promotion never as a standalone act.

**Why this is Strategy 3 for MG:** Traditional link outreach does not work at DA 3 — nobody responds to link requests from a site with no authority. The assets MG has that are genuinely worth linking to are the rubric methodology, the scored ranked lists, and the player-sourced evidence behind every score. The strategy is to make those assets visible in the communities that would care about them, by being a genuine participant first. Developer outreach works at this stage because it is personal and relevant — you reviewed their game, you are telling them about it. Medium canonical articles cost only writing time and each one is a referring domain. Reddit links after the 30-day participation window are the most trusted links in gaming communities. The links are a byproduct of the methodology being genuinely useful — which is exactly the same value proposition as the product itself.

---

**On cadence:** Goal 1 (Team Cadence) is not a fourth strategy. It is the operating layer underneath all three. Without a consistent weekly rhythm, Strategy 1 stalls because no one is coordinating the audit. Strategy 2 stalls because content and dev are not in sync on pillar verticals. Strategy 3 stalls because social has no owner and the participation clock never starts. Cadence is what makes the three strategies execute week after week rather than once and then drift.

---

## OKRs

OKRs are organised by goal. Where a target is based on external evidence, the basis is noted inline.

---

### Goal 1 — Team Cadence

**Objective:** Build a sustainable weekly operating rhythm that keeps every role aligned and productive within 2–3 hours per person per week, without the dev lead carrying the coordination overhead alone.

| # | Key Result | Target | Basis |
|---|---|---|---|
| T1 | Weekly sync running with a fixed agenda agreed by all roles | Running by end of week 1; 0 missed syncs across Q3 | No current meeting cadence exists — coordination happens ad hoc, which means work blocks go unresolved until someone notices |
| T2 | Every role submitting an async written update (shipped / blocked / next) before each weekly sync | 100% compliance for 8 consecutive weeks by end of Q3 | Written updates replace status questions in the meeting; they also create a record of what was actually done, which is the minimum data needed to improve execution over time |
| T3 | Role-specific checklists (dev publish checklist, content acceptance criteria, SEO keyword sign-off, social participation log) created and in active use | In use from week 1; 0 pages published without checklist sign-off | Checklists are the accountability mechanism that doesn't require a manager — each role self-certifies before handoff, which is the only model that scales at 2–3 hrs/week per person |
| T4 | Total active coordination time per person confirmed at or under 2.5 hours per week | Verified via async update log review at the 8-week mark | The dev lead currently runs 5–8 hrs/week; the target requires shifting accountability to role owners, not just working faster |

---

### Goal 2 — Site Foundation

**Objective:** Ensure every published page communicates the rubric methodology visually and reads as human, player-sourced content — so Google, first-time visitors, and AdSense auditors stop reading MG as AI spam.

**Hard rule:** No new game pages are published until F1 through F4 are complete. Publishing new content on top of a broken foundation compounds the de-indexing problem.

| # | Key Result | Target | Basis |
|---|---|---|---|
| F1 | Full EEAT audit of all existing published pages complete — every page categorised as Pass / Rewrite / Remove | Complete by end of week 4 | At DA 3, low-quality content suppresses the whole domain, not just the individual page — removing or fixing the floor is higher-ROI than publishing new content at this volume |
| F2 | Every de-indexed page in Google Search Console either rewritten to EEAT standard and resubmitted, or removed with a 301 redirect | 0 de-indexed pages remaining by end of week 6 | De-indexed content drags DA without contributing traffic; this is the single biggest anchor on MG's organic performance |
| F3 | Every broken internal link and 404 resolved — broken pages either restored or redirected | 0 broken links verified via Screaming Frog or equivalent; complete before any new content is published | Dead links waste crawl budget; at this content volume, crawl budget is a real constraint |
| F4 | Core Web Vitals passing on mobile — LCP under 2.5s, CLS under 0.1 | Verified via PageSpeed Insights before any new content is added | Google uses Core Web Vitals as a ranking signal; failing mobile CWV suppresses rankings regardless of content quality |
| F5 | Rubric score component live on 100% of published pages — metric score bars or radar chart, rubric level descriptions accessible on hover or expand, "how we scored this" transparency panel | Retrofitted to all existing pages that survive the audit; live on all new pages from week 6 onward | The rubric is the entire basis of MG's differentiation from every other review site — it is currently invisible in the design, which means there is no visible reason for a visitor to trust MG's scores over a generic list |
| F6 | Methodology page live at a stable URL explaining the rubric system, player evidence sourcing, and author assignment — linked from the site footer and every game page | Published and indexed in Google Search Console by end of week 4 | The methodology page does not exist on the live site; for a metrics-based review platform, a public, plain-language explanation of how scores are derived is the most direct available signal of legitimacy |
| F7 | Author attribution correct on 100% of live pages; one author profile page per active author live and linked from every byline | 100% of live pages showing correct author verified on the published site; 1 profile page per active author | WordPress author attribution is currently broken on the live site — every other EEAT improvement made this quarter is undermined until this is fixed |

---

### Goal 3 — Organic Growth

**Objective:** Grow total clicks across all channels from ~15 per 28 days to 500 per 28 days by end of Q3, while growing Domain Authority from 3 to 7–8.

**Note on keyword targeting:** At DA 3, MG can only compete for keywords with a Semrush difficulty of 0–20. IGN, Metacritic, and OpenCritic own rankings above that threshold regardless of content quality. Every new piece published this quarter must have keyword difficulty confirmed below 20 before writing begins. DA movement from Q3 work will begin to show in data within the quarter but will compound most visibly in Q4 — new backlinks take time to be crawled and reflected.

**Growth model:** 8–10 indexed pages ranking for KD 0–10 keywords can each drive 30–50 clicks/month from Search Console. Medium and Reddit referrals add a further 50–100 clicks/month from week 6 onward once the participation period is complete. Social and direct build from week 6 as sharing begins. 500 clicks/28 days by end of Q3 is achievable if Goal 2 is complete by week 6 and both genre clusters are live by week 10.

| # | Key Result | Target | Owner | Basis |
|---|---|---|---|---|
| G1 | Total clicks across all channels in the final 28-day window of Q3 | 500 (Search Console + social referrals + direct, tracked in GA4) | All | Baseline is ~15 clicks/28 days; 500 is achievable across three channels firing together — no single channel gets there at DA 3 |
| G2 | Domain Authority | 7–8 verified in Moz by end of Q3 | SEO | DA 7–8 unlocks higher-KD keyword competition in Q4; movement at this stage is driven by quality referring domains, not volume |
| G3 | Spam score reduced to under 2% | Disavow file submitted by week 2; spam score re-checked at 60 days post-submission | SEO | Current 4% spam score at DA 3 means toxic links represent a higher share of the backlink profile than at higher DA; Moz disavow results take a minimum of 60 days to reflect |
| G4 | 2 fully built pillar verticals — pillar page + 4 supporting game reviews per vertical, all targeting KD 0–20, all interlinked with no orphan pages | Both clusters live by week 10; pillar pages updated to link to all supporting reviews within 48 hours of each review going live | Content + Dev | HubSpot's topic cluster model produced a 55% organic traffic increase in 6 months — the mechanism is Google interpreting internal link depth as a topical authority signal |
| G5 | Schema markup (VideoGame + Review JSON-LD) live and verified on 100% of game pages | 0 pages published without schema confirmed via Google Rich Results Test | Dev | SearchPilot controlled test: adding review schema increased organic traffic by 20% — the mechanism is CTR improvement from star rating rich results appearing in SERPs |
| G6 | 3 buyer-intent pieces published — 1 curated list, 1 "is [game] worth it in 2026" verdict, 1 comparison — each with Humble Bundle affiliate links | 3 pieces live by end of Q3, each targeting a confirmed KD 0–20 keyword and internally linked to the relevant pillar page | Content | Buyer-intent content converts at 2–5× the rate of general reviews (Siege Media research); these pieces attract purchase-stage traffic and carry affiliate links directly |
| G7 | Humble Bundle and Amazon Associates affiliate accounts active; affiliate link in 100% of new reviews | Both accounts active; 0 new reviews published without at least one Humble Bundle link | Content | Humble Bundle: 4–8% commission, 30-day cookie; Amazon games: 1% commission, 24-hour cookie — Humble Bundle is the primary CTA; Amazon closes accounts without 3 qualifying sales in 180 days |
| G8 | 10 new referring domains from topically relevant gaming sources | 10 confirmed live by end of Q3 | SEO + Social | Referring domain quality at this DA level matters more than volume — 10 relevant gaming sources outperform 50 generic directory links; developer outreach and Medium canonicals are the two highest-conversion sources at MG's current scale |
| G9 | Reddit participation — 3 substantive comments per week across 3 subreddits (r/patientgamers, r/ShouldIBuyThisGame, and one genre sub matching the first pillar vertical) | 30-day participation clock starts week 1; 0 MG links shared in the first 30 days; link sharing eligible from week 5, only in direct response to relevant questions | Social | Reddit detects 96.4% of manipulation attempts automatically; accounts with no community history are shadowbanned; the 95/5 rule applies — 19 genuine interactions for every 1 promotional mention is the minimum threshold for community tolerance |
| G10 | Medium — 1 opinion or explainer article per week published under an MG author byline, canonical tag set to metricgamer.com, submitted to a gaming publication | 1 article per week from week 1; minimum 1,200 words per article | Social + Content | Correct canonical tags mean Google indexes MG as the source, not Medium; each article is simultaneously a referring domain, a backlink, and a referral traffic source — the highest ROI social channel available at this DA |
| G11 | 1 external byline on a third-party gaming platform with a backlink to MG | Confirmed live by end of Q3 | Social | A single byline on a third-party platform does more for author EEAT than publishing exclusively on a DA 3 domain — it is the fastest available off-site credibility signal for the authors |
| G12 | Steam Curator feed updated for every new game page within 7 days of publish | 0 new reviews missing a Steam Curator entry after 7 days | Social | Steam Curator reviews appear on individual game store pages and build topically relevant brand presence with no traffic or DA requirement |

---

## Priority & Sequencing

| Weeks | Focus |
|---|---|
| 1 | Cadence live (T1–T3). Reddit clock starts (G9). Medium articles start (G10). Disavow file submitted (G3). Pillar verticals decided and locked. |
| 2–4 | EEAT audit complete (F1). Broken links fixed (F3). CWV fixed (F4). Methodology page live (F6). Keyword research for both clusters confirmed. |
| 4–6 | De-indexed pages cleared (F2). Author attribution fixed (F7). Schema on all existing pages (G5). Affiliate accounts active (G7). |
| 6 | Foundation milestone check: F1–F7 all green. New content publishing resumes. |
| 6–10 | Rubric component live (F5). Both genre clusters written and published (G4). Developer outreach begins (G8). |
| 6–13 | Reddit sharing eligible (G9 post-30 days). Social amplifying published clusters. External byline pursued (G11). Buyer-intent pieces published (G6). |
| End of Q3 | G1 (500 clicks/28 days) and G2 (DA 7–8) measured and reported at team sync. |

**AdSense:** Parked until specialist meeting week of June 16. Outcomes from that meeting will be added as a sub-goal under Goal 2 once the blockers are defined.
