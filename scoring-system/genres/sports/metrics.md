# Genre: Sports

> **Sub-genre required.** Every sports game must be assigned a sub-genre before scoring. There is no genre-level default. Football is the first sub-genre built out — others (e.g. basketball, tennis) follow the same pattern when added.

## Metric Pool — Football

Football uses the metric pool model, not a fixed simple-5. The sub-genre spans two genuinely different play experiences — **on-pitch action sims** (EA Sports FC, eFootball, PES) where the player controls real-time matches, and **pure management/tactics sims** (Football Manager, Championship Manager, Top Eleven) with zero on-pitch control. A single fixed 5 can't honestly score both: on-pitch shooting feel means nothing for Football Manager, and transfer-market depth means nothing for EA Sports FC. This mirrors how Shooters handles single-player campaign vs. large-scale multiplayer with one pool and per-page profiles, rather than splitting into separate sub-genres.

| # | Metric | Type | Direction | Best fit for | Rubric |
|---|---|---|---|---|---|
| 1 | On-Pitch Match Feel | Qualitative | Delight | Action sims only — no equivalent in management sims | [rubric](sub-genres/football/on-pitch-feel/rubric.md) |
| 2 | Tactical Depth & AI | Qualitative | Delight | Both — formations/instructions in-match (action) or full tactical systems across a season (management) | [rubric](sub-genres/football/tactical-depth/rubric.md) |
| 3 | Squad & Player Progression | Qualitative | Delight | Both — Career Mode/Ultimate Team progression (action) or youth academy/player development (management) | [rubric](sub-genres/football/squad-progression/rubric.md) |
| 4 | Chemistry & Cohesion | Qualitative | Delight | Both — chemistry links (action) or team dynamics/morale (management) | [rubric](sub-genres/football/chemistry-cohesion/rubric.md) |
| 5 | License Authenticity | Qualitative | Delight | Both — universal driver of "feels real" | [rubric](sub-genres/football/license-authenticity/rubric.md) |
| 6 | Competitive Balance | Qualitative | Complaint | Both — AI scripting/rubber-banding (action) or match-engine fairness (management) | [rubric](sub-genres/football/competitive-balance/rubric.md) |
| 7 | Content & Game Modes | Qualitative | Delight | Both — universal, but most visible in action sims (Career Mode, Ultimate Team, World Cup modes) | [rubric](sub-genres/football/content-modes/rubric.md) |
| 8 | Transfer Market & Squad Building | Qualitative | Delight | Management sims only — no equivalent in action sims | [rubric](sub-genres/football/transfer-market/rubric.md) |
| 9 | Presentation & Atmosphere | Qualitative | Delight | Action sims primarily — broadcast presentation, commentary, crowd | [rubric](sub-genres/football/presentation-atmosphere/rubric.md) |

All 9 rubrics live in the single `sub-genres/football/` folder — there's only one sub-genre, so unlike Fighting's per-sub-genre rewrites, each rubric is written once to work across whichever profile selects it (same approach as Shooters' `sub-genres/fps/` holding pool rubrics for both its campaign and multiplayer profiles).

---

## Suggested Profiles

Starting points, not enforced selections. Pick the 5 most relevant to what the page is actually evaluating.

**Action Sim** (EA Sports FC 26, eFootball, PES + mods like Football Life 25 / Smokepatch): On-Pitch Match Feel, License Authenticity, Content & Game Modes, Competitive Balance, Presentation & Atmosphere

**Management Sim** (Football Manager, Championship Manager, Top Eleven): Tactical Depth & AI, Transfer Market & Squad Building, Squad & Player Progression, Chemistry & Cohesion, License Authenticity

License Authenticity is the one metric both profiles share — it's the rare theme that's equally load-bearing whether you're controlling the match or just managing from the touchline.

---

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| football | Spans both on-pitch action sims and management/tactics sims — see profiles above. Research grounded in `research.md` (Reddit + Google Trends, pulled during the June 2026 World Cup window — tournament-only noise filtered out). | [sub-genres/football/](sub-genres/football/) |

---

## Other Themes Considered (not in the pool)

- **Player base / longevity** — relevant ("how big the current player base is") but it's time-sensitive state, not a quality axis fixable in a rubric. Tracked as a tag (player count, active servers), not a metric — same reasoning Fighting used to cut this theme.
- **Crossplay** — binary (has it or doesn't), not a spectrum a rubric can describe across 5 levels. Tracked as a tag.
- **PC/platform availability** — relevant to the keyword/campaign side (see `operations/2026-Q3/campaigns/pc-football/`) but not a quality axis. Tracked as a tag.

---

## Niche: Multiplayer

Niche rubric lives in `niches/multiplayer/`. Replaces a pool selection when scoring a multiplayer-specific page.

| Swap Out | Swap In | Rubric | Use When |
|---|---|---|---|
| Presentation & Atmosphere | Multiplayer Quality | [rubric](niches/multiplayer/multiplayer-quality/rubric.md) | Online head-to-head or Ultimate-Team-style online play (action sims), or FM's online leagues (management) |

---

## Niche: Free

Niche rubric lives in `niches/free/`. Replaces a pool selection when scoring a free-to-play page.

| Swap Out | Swap In | Rubric | Use When |
|---|---|---|---|
| Content & Game Modes (action) or Transfer Market & Squad Building (management, e.g. Top Eleven) | Monetisation | [rubric](niches/free/monetisation/rubric.md) | Free-to-play football games where pack/gacha economy is a primary concern (eFootball, FC Ultimate Team-centric pages, Top Eleven) |

---

## Adding a New Niche

1. Create a folder under `niches/[niche-name]/` inside this genre folder
2. Add a `rubric.md` for each new metric
3. Add a row to the relevant swap table above, specifying which pool metric it replaces and why

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Decide simple-5 vs. pool model based on how much internal variation the sub-genre has — don't default to copying football's pool model if a simple-5 fits
3. Add a row to the Sub-genres table above with a description and folder link
