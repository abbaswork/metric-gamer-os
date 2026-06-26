# Genre: MOBA

> **Sub-genre required.** Every MOBA must be assigned a sub-genre (classic, hero-brawler, or third-person) before scoring. There is no genre-level default. Rubrics live inside the sub-genre folders, not at the genre level.

## Metric Pool

MOBA uses the metric pool model. The genre defines a pool of 8 validated base metrics; any single campaign selects the 5 most relevant from the pool for that context. A "Best Competitive MOBAs" campaign pulls different metrics than a "Best MOBAs for Friend Groups" campaign.

Because MOBAs are free-to-play and multiplayer by default, Monetisation Model and Matchmaking & Ranked Quality are included as base pool metrics rather than niche swap-outs.

| # | Metric | Type | Direction | Best fit for |
|---|---|---|---|---|
| 1 | Roster Depth | Qualitative | Delight | Every MOBA — universal |
| 2 | Gameplay Depth | Qualitative | Delight | Every MOBA — universal |
| 3 | Combat Feel | Qualitative | Delight | Every MOBA — universal |
| 4 | Meta Health | Qualitative | Complaint | Every MOBA — universal |
| 5 | Matchmaking & Ranked Quality | Qualitative | Complaint | Every MOBA with a ranked mode |
| 6 | Monetisation Model | Qualitative | Complaint | Every MOBA — universal (all are F2P) |
| 7 | Teamplay & Social | Qualitative | Delight | Campaigns emphasising friend-group play |
| 8 | Map Design | Qualitative | Delight | Hero-brawler and third-person most; classic MOBAs where map variety is a differentiator |

Each sub-genre folder also contains one unique metric that applies only to that sub-genre:

| Sub-genre | Unique Metric | Folder |
|---|---|---|
| classic | Itemisation & Build Depth | `itemisation/rubric.md` |
| hero-brawler | Mode & Map Variety | `mode-variety/rubric.md` |
| third-person | Aiming & Skill Expression | `aiming-skill-expression/rubric.md` |

The unique metric is added to the campaign's pool alongside the 8 base metrics, giving 9 total candidates to select 5 from.

---

## Suggested Profiles

These are starting points, not enforced selections. Pick the 5 most relevant to what the campaign is actually evaluating.

**Classic — Competitive focus** (LoL ranked, Dota 2, Predecessor): Gameplay Depth, Meta Health, Matchmaking & Ranked Quality, Itemisation & Build Depth, Roster Depth

**Classic — Onboarding / new player focus**: Roster Depth, Combat Feel, Gameplay Depth, Monetisation Model, Teamplay & Social

**Hero-brawler — General** (Brawl Stars, HotS, Battlerite): Mode & Map Variety, Roster Depth, Combat Feel, Monetisation Model, Matchmaking & Ranked Quality

**Hero-brawler — Competitive**: Meta Health, Matchmaking & Ranked Quality, Combat Feel, Roster Depth, Mode & Map Variety

**Third-person — Action MOBA focus** (Deadlock, Smite): Aiming & Skill Expression, Combat Feel, Gameplay Depth, Meta Health, Roster Depth

**Third-person — Accessibility focus**: Roster Depth, Combat Feel, Map Design, Monetisation Model, Teamplay & Social

---

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| classic | Top-down 5v5 MOBAs with three lanes, jungle, last-hitting, and a deep itemisation system (League of Legends, Dota 2, Honor of Kings, Mobile Legends: Bang Bang, Predecessor, Eternal Return) | [sub-genres/classic/](sub-genres/classic/) |
| hero-brawler | Streamlined or arena-based MOBAs that reduce or remove lanes, last-hitting, and itemisation in favour of faster matches, team objectives, and broader mode variety (Heroes of the Storm, Battlerite, Gigantic, Brawl Stars, Pokemon Unite, Awesomenauts) | [sub-genres/hero-brawler/](sub-genres/hero-brawler/) |
| third-person | MOBAs played from a third-person perspective where players aim abilities and attacks manually, adding a mechanical skill layer absent from top-down sub-genres (Smite, Deadlock, Supervive, Predecessor, Paragon) | [sub-genres/third-person/](sub-genres/third-person/) |

---

## Niche: Mobile

Niche rubric lives in `niches/mobile/`. Apply this niche when scoring a mobile MOBA — it replaces Combat Feel with Mobile Experience, since on a touchscreen the control scheme is the combat feel.

| Swap Out | Swap In | Rubric |
|---|---|---|
| Combat Feel | Mobile Experience | [rubric](niches/mobile/rubric.md) |

Mobile games scored here: Honor of Kings, Mobile Legends: Bang Bang, Pokemon Unite, Brawl Stars (mobile). These titles are typically also a sub-genre (e.g. Honor of Kings = classic + mobile niche).

> **Note:** A `niches/` folder appears inside `sub-genres/` — this is misplaced. The mobile niche lives at `scoring-system/genres/moba/niches/mobile/`, not inside the sub-genres folder.

---

## Other Themes Considered

- **Toxicity** — explicitly named in Reddit research as a downside ("sometimes leads to toxicity"). Cut as a standalone metric because toxicity is a symptom of matchmaking quality and community size, not a measurable quality axis with distinct rubric thresholds. Partially captured under Matchmaking & Ranked Quality.
- **Player Base / Longevity** — "is heroes of the storm dead" trending (+40%). Cut as time-sensitive state. The same game that had a dead base in 2022 could be thriving in 2026. Tracked as a tag (active servers, estimated player count) rather than scored.
- **Esports / Pro Scene** — mentioned in research as extra appeal. Cut because it's a downstream product of competitive quality (already captured by Meta Health and Matchmaking) not a scoreable game quality dimension. A game with no pro scene can still have excellent competitive balance.
- **Low Spec Requirements** — "runs on any PC" mentioned as a reason people love LoL. Cut because it's binary (the game either runs on your hardware or it doesn't) rather than a spectrum rubric can describe. Tracked as a tag (minimum spec).
- **New Content Updates** — "constantly changes, new champs, reworks" cited in research. Merged into Meta Health: a game that patches frequently enough to shift the meta scores higher on that metric. Standalone update cadence is a tag, not a scored axis.
