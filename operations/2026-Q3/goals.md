# Q3 2026 — Goals & Strategies
*Early start: June 2026. Full quarter: July–September 2026.*

---

## Goals

### Goal 1 — Team Accountability
Establish a team operating model where every contributor has a defined stake in the outcome — work is tied to a revenue share framework, deadlines are enforced by campaign go-live dates, and missed tasks transfer both the work and the points to whoever picks them up. The goal is not coordination for its own sake but financial accountability: contributors who deliver build their share, contributors who don't lose it. See [revenue-share.md](../../company/revenue-share.md) for the full framework.

### Goal 2 — Site Foundation
Ensure every published page communicates the rubric methodology visually and reads as human, player-sourced content — so that Google, first-time visitors, and AdSense auditors stop seeing Metric Gamer as AI spam.

### Goal 3 — Organic Growth
Grow total clicks across all channels (Search Console, social, direct) from ~15 per 28 days to 500 per 28 days by end of Q3, while increasing Domain Authority from 3 to 7–8.

---

## Starting Position

- **Domain Authority:** ~3
- **Spam Score:** ~4%
- **Total clicks / 28 days:** ~15 (Search Console only)
- **Indexed pages:** partial — some pages de-indexed by Google as duplicate/AI content
- **Content:** 100–200 pages; inconsistent SEO titles and descriptions; no rubric visible on page design
- **Author attribution:** broken on live site
- **Schema markup:** missing or unverified on most game pages
- **Core Web Vitals:** failing on mobile
- **Backlinks:** low volume, some toxic domains in profile
- **Social:** accounts exist on Reddit and Medium, inactive
- **Steam Curator:** exists, not kept current
- **Team:** dev lead (5–8 hrs/week), 2–3 content writers (1 hr each/week), SEO specialist (hired, backlinks + EEAT framework), social (no current owner)
- **Monetisation:** no ad units live; affiliate accounts not active; AdSense strategy being defined (specialist meeting week of June 16)

---

## GSC Findings — June 2026

**What the data shows:** The MG Search Console export (June 2025–June 2026) reveals a sharply concentrated traffic profile. One page — `/blog/best-free-two-player-ps4-racing-games` — accounts for the overwhelming majority of impressions site-wide. MG has established topical authority in exactly one niche.

**Topical authority map:**
- **Established:** Free 2-player PS4 games — significant impression volume, ranking around position 16 on average
- **Unestablished:** Mobile football games — pages are indexed but receiving zero clicks; no query volume attributable to this cluster

**Biggest single opportunity:** The PS4 racing ranked list sits at average position 16.1 across 37,730 impressions. Moving from page 2 to page 1 is the highest-ROI content improvement available on the site — a 10–15× click increase is realistic.

**Keyword formula at DA 2:** The only consistently winnable queries share three properties: platform-specific + free-to-play + multiplayer modifier. Queries missing any of these filters face established gaming publications that cannot be outranked at this authority level.

**November 2025 traffic drop:** Site metrics fell sharply in November 2025 — from 10–12 clicks/day to near-zero over a 2–3 week window. This coincides with known Google algorithm update periods. Cause not yet identified.

**Strategic implication for Goal 3:** The free 2-player PS4 niche is the one confirmed area where ranking uplift is achievable immediately. Mobile football ranked lists should not be published until topical authority in that niche is established — indexed pages with zero clicks are a signal that Google does not yet associate MG with that topic.

---

## Current State by Goal

**Goal 1 — Team Accountability**
The coordination problems are manageable — the team gets through work eventually. The real issue is that there is no financial stake attached to delivery. Contributors are part-time on an unmonetised project with no enforcement and no consequence for missing work. Some weeks they deliver, some weeks they don't. A revenue share framework tied to campaign go-live dates changes this: every task has a point value, every point maps to a payout, and every missed deadline is a direct financial transfer to whoever picks up the slack.

**Goal 2 — Site Foundation**
The website visually communicates nothing about the rubric system. Author attribution is broken on the live site. Methodology page does not exist. Broken links waste crawl budget. Some pages are de-indexed as AI spam. New content published on top of this foundation compounds the problem.

**Goal 3 — Organic Growth**
At DA 3, only KD 0–20 keywords are winnable. Social channels are dormant and generate no referral traffic. No genre clusters exist — pages are isolated without pillar-to-supporting-review internal link structure. Backlink profile is thin and has some toxic domains pulling spam score to 4%.

---

## Strategies

### Goal 1 — Team Accountability

**Core bet:** Money-driven contributors respond to financial stake, not schedules or social pressure. The mechanism that makes a part-time team on an unmonetised project deliver consistently is the knowledge that incomplete work transfers their payout to someone else.

**What we're doing:**

1. **Revenue share tied to child OKRs.** Every contributor has a base 10% share of the contributor pool (30% of net revenue), earned through points assigned per child OKR. Maximum 20% if they absorb others' incomplete work. Full framework in [revenue-share.md](../../company/revenue-share.md).

2. **Campaign go-live dates as the enforcement mechanism.** All work is tied to a campaign with a fixed go-live date. Contributors submit 1–2 days before. At go-live, owners publish what is done — incomplete tasks have their points transferred to whoever picked them up, or back to the owners by default. No extensions.

3. **Points assigned before campaigns begin.** Each child OKR carries a defined point value published before any work starts. Contributors know exactly what they are earning before they agree to the task.

4. **Tier 1 payout at the 500-click milestone.** A flat $30 pool ($10 per contributor slot) funded by the owners, distributed by points earned. This makes the framework financially real from the first milestone.

5. **One weekly sync (30 min max).** Agenda is fixed: what shipped, what's blocked, OKR progress. Not a strategy meeting — a checkpoint.

6. **Async written update per role before each sync.** Three lines: shipped / blocked / next. This is the record that point claims are verified against.

**What we're not doing:** Gamification, leaderboards, social pressure, or anything that treats the team like they are playing a game rather than building a business.

---

### Goal 2 — Site Foundation

**Core bet:** Google's view of Metric Gamer is determined by its worst pages, not its best. The fastest path to being indexed and trusted is fixing the floor before adding anything new on top of it. Every new page published before the audit is done makes the problem bigger.

**Hard rule:** No new game pages published until the EEAT audit is complete and the page template is fixed with rubric scores visible.

**Sequencing:**

**Weeks 1–3 — Dev fixes first.**
Technical blockers throttle everything else. Fix in this order: broken links and 404s → author attribution on live site → Core Web Vitals (LCP, CLS on mobile) → schema markup (VideoGame + Review JSON-LD) → static category pages for the 2 pillar verticals. These are the structural issues that prevent any SEO gains regardless of content quality.

**Weeks 2–4 — Content audit.**
Audit every existing published page against the EEAT framework. Three outcomes per page: Pass / Rewrite / Remove with 301 redirect. Prioritise rewrites for pages that already have impressions in Search Console. Remove pages that would fail a Google quality evaluation — low-quality content at this volume suppresses the entire domain. Coordinate with S1 (de-indexed pages in GSC) so the same pages are addressed in both audits at once.

**Weeks 3–6 — Rubric visible on every page.**
Build the visual score component into the page template: metric score bars or radar chart, rubric level descriptions accessible on hover, "how we scored this" transparency panel. Publish the methodology page at /how-we-score/ and link it from every game page footer. Retrofit the new template to all existing pages that survived the audit.

**Milestone check (end of week 6):** Zero de-indexed pages remaining. Zero broken internal links. 100% of live pages showing correct author attribution. Rubric scores visible on 100% of published pages. Methodology page indexed.

---

### Goal 3 — Organic Growth

**Core bet:** 500 clicks/28 days from DA 3 requires all three channels — SEO, social, and backlinks — moving together. No single channel gets there at this authority level. The sequencing matters: SEO wins first, then social amplifies what's already ranking, then backlinks push DA up so the next quarter's content competes higher.

**Three parallel tracks:**

**Track 1 — SEO (primary growth driver)**
Win two genre niches completely before expanding. **Vertical 1 is confirmed by GSC data: free 2-player PS4 games.** MG already ranks in this niche — the priority is moving the existing ranked list from position 16 to page 1, then building the supporting game page cluster around it. Vertical 2 to be decided at the first team sync. For each vertical: complete the genre rubric, publish a pillar page, publish 4 supporting game reviews. Every page targets KD 0–20 only — confirmed in Semrush before writing begins. The keyword formula to follow at DA 2: platform-specific + free-to-play + multiplayer modifier. Queries missing any of these filters are not winnable. Internal linking: every supporting review links to its pillar; pillar links back to all supporting reviews. No orphan pages.

Buyer-intent pieces alongside the genre clusters: one curated list, one "is [game] worth it in 2026" verdict, one comparison. These carry Humble Bundle affiliate links and convert at 2–5× the rate of straight reviews.

**Track 2 — Social (amplification + referral traffic)**
Start the Reddit 30-day participation clock immediately — this is time-gated and cannot be compressed. Participate in r/patientgamers, r/ShouldIBuyThisGame, and the genre sub for the first pillar vertical. Minimum 3 substantive comments per subreddit per week. No MG links for 30 days. After 30 days: share only in direct response to relevant questions, never as a standalone post.

Medium: one opinion or explainer article per week from week 1, minimum 1,200 words, canonical tag set to metricgamer.com before publish, submitted to a gaming publication. Each article is both a backlink and a referral traffic source.

Steam Curator: every new game page added within 7 days of publish. Update existing feed for all unrepresented MG pages. One external byline on a third-party gaming platform — pitched in week 2, written once accepted.

**Track 3 — Backlinks (DA growth)**
Target: 10 new referring domains this quarter. Sources in priority order: Medium articles with correct canonical tags (2–3 domains), Reddit links post-30 days in direct response to questions (3–4 domains), indie developer outreach for every game MG has reviewed — personalised 3–4 sentence email linking to their review page (3–4 domains). Toxic backlink disavow file submitted in week 1 to bring spam score below 2%.

**Sequencing across the quarter:**

| Weeks | Priority |
|---|---|
| 1–6 | Foundation fixed (Goal 2). Reddit clock running. Medium articles start. Disavow file submitted. |
| 4–10 | Genre clusters published. Developer outreach. Schema live. Affiliate links in all new reviews. |
| 6–13 | Reddit sharing begins. External byline live. Social amplifying ranked pages. Full channel measurement. |

**Growth model:** 8–10 indexed pages ranking for KD 0–10 keywords can each drive 30–50 clicks/month. Medium + Reddit referrals add 50–100 clicks/month. Social and direct build from week 6 onward. 500/28 days by end of Q3 is achievable if Goal 2 is complete by week 6 and both genre clusters are live by week 10.

---

## Priority Order

Goals are sequenced — not parallel from day one.

1. **Goal 1 first** (week 1): Revenue share framework and point allocations must be agreed and published before any campaign work is assigned. Without it, there is no accountability mechanism for anything below.
2. **Goal 2 is locked as highest priority through week 6**: Foundation work gates everything. Content writers on audit and rewrites. Dev on technical fixes. No new pages until the template is done.
3. **Goal 3 scales from week 4 onward**: SEO work can begin on keyword research and rubric sets while dev finishes the template. Social and backlink tracks start immediately (Reddit clock, Medium articles, disavow).

**AdSense strategy:** Parked until specialist meeting (week of June 16). Outcomes from that meeting will be added as a sub-strategy under Goal 2 once the blockers are defined.
