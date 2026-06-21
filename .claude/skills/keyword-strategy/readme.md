# Skill: Keyword Strategy

## Purpose

Given a campaign brief, keyword planner CSV, and GSC export, produce a validated keyword map for a Metric Gamer campaign. The output covers a confirmed campaign anchor keyword, a cluster map of ranked list targets, game page keyword assignments per cluster, and a gap list of pages that need to be written. No campaign structure is proposed until the keyword data has been fully analysed, the DA 2 filter applied, and SERP check results returned by the user for every shortlisted keyword.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Keyword Strategy | company/site/keyword-strategy.md | 5 |
| EEAT Framework | writing/eeat.md | 3 |
| Site Structure | company/site/site-structure.md | 3 |
| Site User Personas | company/persona/persona.md | 2 |

---

## Requirements

- **[Hard]** No campaign structure is proposed before SERP check results are returned for every shortlisted keyword.
- **[Hard]** The full keyword planner CSV is read row by row — never a partial sample.
- **[Hard]** The DA 2 filter is applied before shortlisting — bare game names, genre-only, and platform-only queries are excluded.
- **[Soft]** Semrush KD is requested for the shortlist only if `semrush_available` is true — if false, proceed without it but flag the gap during Discovery Q&A rather than treating SERP results alone as sufficient.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `campaign_topic` | string | Yes | One sentence — the niche with modifiers, not a genre. "Free arcade racing games on PS4/PS5" not "racing games." |
| `existing_content` | multiline string | Yes | All live MG URLs related to this campaign topic. One URL per line. |
| `keyword_csv_path` | string | Yes | Path to keyword planner CSV seeded with the campaign topic. Full export, unfiltered. |
| `gsc_csv_path` | string | Yes | Path to GSC export — last 12 months, all queries, clicks, impressions, position. |
| `semrush_available` | boolean | Yes | Whether Semrush organic KD data is available this session. If yes, KD scores will be requested for shortlisted keywords. |
| `content_constraints` | string | No | Games MG cannot authentically review, platform coverage gaps for the authors, or timeline constraints. |

---

## Execution Flow

```
Phase 1 — interface.py    Collect all inputs from the user
     ↓
Phase 2 — Claude          Read keyword planner CSV (all rows) and GSC CSV.
                          Apply YoY flags, volume filters, DA 2 modifier filter.
                          Cross-reference planner data with GSC impressions.
     ↓
Phase 3 — Claude          Build shortlist. Present to user.
                          Request SERP check results for every shortlisted keyword.
                          HALT — do not proceed until SERP results are returned.
     ↓
Phase 4 — User            Executes SERP checks. Reports back page 1 profile
                          and intent signal for each shortlisted keyword.
     ↓
Phase 5 — Claude          Discovery Q&A — surface close calls (competing anchor
                          candidates, cannibalisation tradeoffs, borderline KD
                          keywords, missing Semrush data) as direct questions.
                          Halt until answered or explicitly waived.
     ↓
Phase 6 — Claude          Incorporate SERP results and Discovery answers. Select
                          campaign anchor. Map clusters. Assign game page
                          keywords. Identify gaps.
     ↓
Phase 7 — Claude          Validate against acceptance criteria. Deliver keyword map.
```

---

## Interface Script

`interface.py` — collects `campaign_topic`, `existing_content`, `keyword_csv_path`, `gsc_csv_path`, `semrush_available`, and `content_constraints`, then prints the structured input block for Claude.

---

## Data Analysis Strategy

This skill analyses provided CSV files — it does not search for player reviews. The data sources are:

**Keyword Planner CSV**
Read every row before drawing conclusions. Extract:
- Every keyword with YoY -50% or worse → structural decline flag
- Every keyword with volume under 100 → very low volume flag
- Every keyword with +100% or higher YoY → emerging opportunity flag
- Every keyword with "Unknown" or "--" → unmeasurable, cross-reference GSC
- Competition indexed value above 70 + volume under 1,000 → high effort, low reward flag
- The 10 highest-volume terms and their trend direction

**GSC CSV**
Cross-reference against existing content URLs provided in inputs. Identify:
- Pages with high impressions but low clicks (position 11–20 — page 2 improvement candidates)
- Queries with impressions but 0 clicks (positions 20+ — existing long-tail cloud)
- Query clusters that suggest existing topical authority the campaign can build on

**Semrush (if available)**
Request organic KD score for each keyword on the shortlist after Phase 2. KD under 30 = viable at DA 2. KD 30–50 = challenging, SERP check result is the deciding factor. KD above 50 = exclude.

**SERP Check (user-executed)**
For every shortlisted keyword, user searches incognito and reports:
- Positions 1–5: site names and page types (list/review/forum/commercial/video)
- Featured snippets, video carousels, knowledge panels
- Intent signal: does page 1 directly answer the query, or is intent split?

SERP pass at DA 2: no IGN, Metacritic, Fandom, or Wikipedia in positions 1–3; at least 2 of positions 1–5 are smaller sites or forum threads; page 1 directly answers the query; no video carousels above organic results.

---

## Acceptance Criteria

### Data Analysis
- [ ] Full keyword planner CSV read — all rows, not partial
- [ ] YoY trend flag applied to every row before shortlisting
- [ ] DA filter applied — bare game names, genre-only, and platform-only queries excluded
- [ ] Modifier count stated for every shortlisted keyword (minimum 3 to proceed)
- [ ] GSC cross-reference completed — existing pages with high impressions noted
- [ ] Semrush KD incorporated for each shortlisted keyword (if semrush_available = true)

### SERP Checks
- [ ] SERP check results collected from user for every shortlisted keyword before campaign anchor is named
- [ ] Intent split identified and flagged where present
- [ ] Each keyword explicitly marked: SERP pass or SERP fail with reason

### Campaign Anchor
- [ ] Campaign anchor keyword stated explicitly
- [ ] Confirmation criteria met: 3+ modifiers, flat/positive YoY, 100+ volume or strong GSC signal, SERP pass, clean intent
- [ ] No campaign structure proposed before all confirmation criteria are met
- [ ] Discovery Q&A phase run — anchor competition, cannibalisation tradeoffs, and borderline KD keywords surfaced as questions and resolved before the anchor is named

### Cluster Map
- [ ] Each cluster has one distinct Tier 1 keyword with a clear modifier differentiating it from other clusters
- [ ] Maximum one shared game between any two clusters
- [ ] Each cluster has 3+ supporting game pages confirmed in MG's existing content library
- [ ] Cannibalisation risk flagged where clusters share more than one game

### Game Page Keywords
- [ ] One Tier 2 primary keyword assigned per game (game name + modifier — no bare game names)
- [ ] Two to three Tier 3 FAQ-level keywords assigned per game
- [ ] Game pages that already exist on MG identified and confirmed
- [ ] Gap list: game pages needed but not yet written, listed with their target keyword

### Output Format
- [ ] Campaign anchor stated with confirmation criteria
- [ ] Cluster map: each cluster has keyword, volume, competition, SERP result, game roster
- [ ] Game page assignments: primary keyword + FAQ keywords per game per cluster
- [ ] Gap list: game title, target keyword, notes
- [ ] Explicit statement of anything unconfirmed pending SERP check or Semrush data
