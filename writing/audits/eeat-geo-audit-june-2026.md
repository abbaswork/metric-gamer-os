# EEAT & GEO Audit — June 2026

**Conducted:** June 15, 2026
**Scope:** Metric Gamer EEAT publishing framework vs. niche case studies; Google SEO and GEO (AI search) readiness
**Output:** Gap list, framework updates made, dev tasks added, additional page element recommendations

---

## Case Studies Used

### Retro Dodo
Niche retro gaming magazine. Founded June 2019 as a side project. Reached 1 million organic clicks and $50K monthly revenue within 3 years with no deliberate link-building campaign.

**What they do:**
- Topic clusters built around game systems and retro platforms — every article links to and from a cluster, so the whole cluster ranks, not individual pages in isolation
- Consistent brand voice and recognisable identity that earned organic community mentions
- Content depth over breadth within each cluster — comprehensive coverage of a narrow niche rather than thin coverage of a wide one
- No link outreach — all backlinks are earned through content quality and community trust

**Relevance to Metric Gamer:** Same scale, content-first model, niche authority over generalist coverage. Validates the genre cluster approach.

---

### Hub-and-Spoke Gaming Platform (documented case study)
A gaming platform that reorganised all content into per-game hubs — pillar pages linking to guides, tier lists, patch notes, and builds — and outranked sites 10x its size.

**What they did:**
- Restructured content so each game had a hub page with 15+ supporting articles
- Converted 200-word thin guides into 2,000+ word resources with embedded video, interactive elements, and community data
- Built a rapid-response editorial workflow for patch notes and meta changes — published within 4 hours of game updates
- Reduced LCP from 4.2s to 1.1s through image lazy-loading, video facade patterns, and CDN optimisation

**Results:** 2,300% increase in sales, 100% increase in organic clicks.

**Relevance to Metric Gamer:** Demonstrates that content architecture and page speed, not domain authority, are the primary levers for small sites competing against established publications.

---

### GEO Research Sources
- [GEO White Paper v3.0, August 2025](https://medium.com/@shaneht/the-geo-white-paper-optimizing-brand-discoverability-in-models-like-chatgpt-perplexity-and-ee741613dfb3) — Tepper
- [Google AI Optimisation Guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — Google Search Central, 2026
- [Frase.io GEO Guide 2026](https://www.frase.io/blog/what-is-generative-engine-optimization-geo)
- Previsible 2025 AI Traffic Report — AI-referred sessions up 527% YoY in first 5 months of 2025
- Content featuring quotes, expert opinions, or proprietary data shows 30–40% higher visibility in AI-generated answers (GEO White Paper)
- Median CTR lift of +34% across 17 gaming sites after implementing Organisation, BreadcrumbList, FAQPage, and Article schemas (redclawey.com iGaming schema study, 2025–2026)

---

## EEAT Framework Audit

### What the framework covers well

| Area | Assessment |
|---|---|
| First-hand experience signals | Reviewer attribution with specific persona expertise — ahead of most niche sites that use generic "Editorial Team" bylines |
| Content updating | Phase 7 content refresh is explicit and built into the lifecycle |
| FAQ structure | Real user questions, conversational phrasing, PAA intent awareness |
| Schema awareness | Article, Review, FAQ, Breadcrumb all listed in Phase 4 |
| Human voice signals | Writing style guide enforces contractions, sentence variety, no corporate language — all EEAT trust signals |
| Keyword research before writing | Phase 2 keyword + SERP research is mandatory before drafting |
| Topical authority planning | Phase 1 and Phase 7 both address cluster building and semantic relevance |

---
### Gaps Identified

#### GEO Gaps

**Gap 1 — Scores not positioned as citable data**
The Metric Gamer overall score is a genuinely proprietary data point, but it appears as a number without source attribution in the body copy. AI engines need "Metric Gamer rates [game] X/5 on the [genre] rubric" framing to attribute the score to the site when generating answers. Without it, the score is treated as an opinion, not a citable fact.

*Status: Identified. Recommended fix — short framing paragraph in the Overall Score section of each game page. Pending approval before updating write-game-page spec.*

**Gap 2 — No brand entity signals in the framework**
AI engines cite brands they've encountered referenced elsewhere — Wikipedia, consistent external mentions, Google Knowledge Panels. The framework had no coverage of monitoring or building brand entity presence.

*Status: Fixed. Brand Entity Monitoring step added to Phase 7 of eeat.md.*

**Gap 3 — Digital PR and external citation strategy**
No strategy for earning mentions from external sources (Reddit threads, gaming communities, other sites). GEO citation probability increases when other sources reference the brand. Confirmed by user that this is handled by the social strategy, not the EEAT framework.

*Status: Out of scope for EEAT framework — covered in social strategy.*

**Gap 4 — Author authority on-site only**
Author bios exist on the site but no cross-platform presence linking to social or YouTube channels. Confirmed by user that this is handled by the social strategy.

*Status: Out of scope for EEAT framework — covered in social strategy.*

---

#### Google SEO Gaps

**Gap 5 — No VideoGame schema specification**
The schema section listed Article, FAQ, Review, and Breadcrumb but did not specify the VideoGame schema type or the AggregateRating properties required to generate star ratings in Google SERPs. This is the highest-impact schema addition for a gaming review site.

*Status: Fixed. VideoGame schema section added to Phase 4 of eeat.md. AggregateRating task added to dev to-do.md (Development Priority 2, Schema markup section).*

Required schema properties:
- Schema type: `VideoGame`
- Nested: `Review` → `reviewRating` → `ratingValue` (the Metric Gamer score), `bestRating: 5`, `worstRating: 1`
- `ratingCount: 1` (the reviewer)
- `gamePlatform` — from the Game Details Card
- `genre` — from the scoring rubric genre
- `author` — reviewer name

**Gap 6 — Core Web Vitals targets undefined**
Phase 6 Pre-Publish QA said "test page speed basics" without specific targets. The hub-and-spoke case study specifically cited reducing LCP from 4.2s to 1.1s as a key competitive factor.

*Status: Fixed. CWV targets added to Phase 6 of eeat.md: LCP under 2.5s, INP under 200ms, CLS under 0.1.*

**Gap 7 — No systematic PAA sourcing**
The framework mentioned People Also Ask as a general concept but had no step for capturing live PAA boxes as FAQ seeds during SERP research. This meant FAQs were written from generic templates rather than from questions Google already knows users are asking.

*Status: Fixed. PAA capture step added to Phase 1 SERP Research in eeat.md.*

**Gap 8 — Content cluster architecture**
The framework references topical authority and pillar-cluster systems in Phase 7 but only as a scaling concept. At current scale, Metric Gamer's cluster structure (genre → game reviews within that genre) is the right approach. Per-game hub-and-spoke content (guides, car lists, comparisons per game) requires new content types and is a phase 2 decision when review volume justifies it.

*Status: No change required. Genre-level cluster is the correct current architecture. Per-game hub architecture is a future expansion.*

---

## Updates Made to the Framework

| File | Change |
|---|---|
| `writing/eeat.md` | VideoGame schema section added to Phase 4 — specifies type, AggregateRating properties, gamePlatform, genre, author, and why this is the critical schema for game pages |
| `writing/eeat.md` | Core Web Vitals targets added to Phase 6 Pre-Publish QA — LCP under 2.5s, INP under 200ms, CLS under 0.1, PageSpeed Insights as the tool |
| `writing/eeat.md` | Brand Entity Monitoring step added to Phase 7 — monitoring-only, tracks external citations as a GEO readiness signal over time |
| `writing/eeat.md` | PAA capture step added to Phase 1 SERP Research — captures People Also Ask questions as high-priority FAQ seeds |
| `content/2026/Q3/to-do.md` | AggregateRating added to schema markup task in Development Priority 2 — specifies ratingValue, bestRating, worstRating, ratingCount, and author properties |

---

## Scoring Scale Analysis — /5 vs /10

**Conclusion: Keep /5.**

The rubric system is the core of Metric Gamer's differentiation. Each /5 score corresponds to a defined rubric level with specific criteria for what earns a 1, 2, 3, 4, or 5. This only works cleanly with 5 levels. Switching to /10 requires either:
- Rewriting every rubric to define 10 meaningful, distinguishable levels per metric (levels 6, 7, and 8 on a car roster are nearly impossible to separate meaningfully), or
- Multiplying /5 scores by 2, which creates the appearance of precision without rubric backing

Every major site uses /10 or /100. A rubric-backed /5 with a documented methodology is a genuine differentiator and makes the "how we score" story cleaner to explain.

For schema and GEO: `bestRating: 5` is a valid and correctly interpreted value. AI engines read the scale from structured data, not from convention.

**Recommended addition:** Add a label alongside the score on the page — **4.0 / 5 — Strong** — so readers get familiar "good/great/average" context without changing the scale or the rubric.

---

## Additional Page Elements — SEO & GEO

Elements not currently in the framework or write-game-page spec that the case studies support adding. Ranked by evidence strength.

### High priority

**Table of contents with jump links**
Every game page should open with a ToC linking to each section. The hub-and-spoke case study cited this explicitly for dwell time and featured snippet competition. AI engines also use heading structure to determine what topics a page covers — a ToC makes that structure immediately parseable.

**"Who is this game for?" targeting block**
A short section (not a scored metric, not the verdict) that directly identifies the player type. Example: "Play this if you want the deepest single-player career on PS2. Skip it if you're looking for online multiplayer or realistic rally physics." GEO citation rates are significantly higher for content that answers audience-specific "is X for me?" queries. This addresses a real search intent gap — current game pages have the information but spread across metrics and verdict rather than in one scannable block.

**Methodology link on every game page template**
The /how-we-score/ page is in the dev to-do list. Every individual game page should link to it — either in the reviewer attribution line or near the score. This is a direct EEAT trust signal: it demonstrates the score is backed by a documented process, not arbitrary opinion. AI engines weight this type of sourced methodology reference.

### Medium priority

**Related games section**
Every game page should link to 2-3 other pages within the same genre cluster. GT4 should link to other racing game pages when they exist. This is the primary mechanism by which individual page authority flows through the cluster and builds collective topical authority.

**Developer and publisher entity links**
Link developer and publisher names in the Game Details Card to their Wikipedia or official pages. Google uses entity relationships to understand topical relevance. One line of work per page, done at publish time.

**Game-specific image alt text**
Not "screenshot1.webp" but "gran-turismo-4-career-mode-ps2-license-test.webp". Image search is a secondary traffic source. Descriptive alt text also feeds entity signals about page content.

### Lower priority (larger effort)

**YouTube embed**
Embedding a relevant gameplay video (not necessarily MG-produced) improves dwell time and signals content depth. Sites with video content consistently outperform text-only pages on both engagement and AI citation metrics. This becomes more relevant once the MG YouTube presence is established.

**User score / community rating prompt**
A simple "agree with our score?" interaction that captures user votes creates a fresh content signal and social proof layer. Lower priority at current scale — needs minimum traffic volume to be meaningful.

---

## Open Items

| Item | Status |
|---|---|
| Score framing paragraph in Overall Score section | Pending format approval before updating write-game-page spec and GT4 draft |
| "Who is this game for?" block — add to write-game-page spec | Not yet added — requires format decision first |
| Table of contents — add to write-game-page spec | Not yet added |
| /5 score label ("Strong", "Good", etc.) — define label scale | Not yet defined |
| Methodology page — /how-we-score/ | In dev to-do, Priority 1 |
| VideoGame schema with AggregateRating | In dev to-do, Priority 2 |
