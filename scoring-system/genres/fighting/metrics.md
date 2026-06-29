# Genre: Fighting

> **Sub-genre required.** Every fighting game must be assigned a sub-genre (platform-fighter, traditional, or party) before scoring. There is no genre-level default. Rubrics live inside the sub-genre folders, not at the genre level.

## Metric Pool

Fighting uses the metric pool model: the genre defines a pool of validated metrics, and any single campaign page selects the most relevant from the pool for that context. A "Best Competitive Fighters" campaign pulls different metrics than a "Best Party Brawlers" campaign.

| # | Metric | Type | Direction | Best fit for |
|---|---|---|---|---|
| 1 | Roster Depth | Qualitative | Delight | Every fighting game — universal |
| 2 | Combat Feedback | Qualitative | Delight | Every fighting game — universal |
| 3 | Gameplay Depth | Qualitative | Delight | Competitive and skill-focused titles |
| 4 | Competitive Balance | Qualitative | Complaint | Titles with a ranked or competitive mode |
| 5 | Accessibility | Qualitative | Delight | Every fighting game — universal |
| 6 | Content & Modes | Qualitative | Delight | Every fighting game — universal |
| 7 | Presentation & Artstyle | Qualitative | Delight | Every fighting game — universal |

Roster Depth, Combat Feedback, Accessibility, and Content & Modes apply to virtually every fighting game. Gameplay Depth and Competitive Balance are essential for competitive-focused titles but less central for party fighters where depth is intentionally sacrificed for chaos. Presentation & Artstyle adds strong value for campaigns where visual identity is a key differentiator.

---

## Suggested Profiles

These are starting points, not enforced selections. Pick the 5 most relevant to what the campaign is actually evaluating.

**Competitive Fighters** (Street Fighter 6, MK11, Granblue Fantasy Versus, 2XKO): Combat Feedback, Gameplay Depth, Competitive Balance, Roster Depth, Accessibility

**Platform Fighters** (Brawlhalla, Rivals of Aether): Combat Feedback, Gameplay Depth, Roster Depth, Skill Ceiling, Presentation

**Party Fighters** (Gang Beasts, Stick Fight, ROUNDS): Roster Depth, Combat Feedback, Accessibility, Content & Modes, Gameplay, Presentation & Artstyle

---

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| platform-fighter | Platform-based brawlers with aerial combat, stock-based lives, and victory by launching opponents off stage (Brawlhalla, Rivals of Aether) | [sub-genres/platform-fighter/](sub-genres/platform-fighter/) |
| traditional | Classic 2D/2.5D one-on-one fighters with round-based health bars, motion inputs, and strong emphasis on frame data and footsies (Street Fighter 6, MK11, Dragon Ball FighterZ, Granblue Fantasy Versus) | [sub-genres/traditional/](sub-genres/traditional/) |
| party | Physics-based or casual brawlers where chaotic local multiplayer fun takes priority over competitive depth (Gang Beasts, Stick Fight, ROUNDS) | [sub-genres/party/](sub-genres/party/) |

---

## Niche: Multiplayer

Niche rubrics live in `niches/multiplayer/`. These replace pool selections when scoring a multiplayer-specific campaign.

| Metric | Rubric | Use When |
|---|---|---|
| Competitive Balance | [rubric](niches/multiplayer/competitive-balance/rubric.md) | Online ranked play with a live meta |
| Netcode & Server Quality | [rubric](niches/multiplayer/netcode/rubric.md) | Any online multiplayer mode |
| Ranked Mode | [rubric](niches/multiplayer/ranked-mode/rubric.md) | Games with a dedicated ranked queue |

---

## Niche: Free

Niche rubrics live in `niches/free/`.

| Swap Out | Swap In | Rubric |
|---|---|---|
| Presentation & Artstyle | Monetisation Model | [rubric](niches/free/monetisation/rubric.md) |
| Content & Modes | Roster Monetisation | [rubric](niches/free/roster-monetisation/rubric.md) |

For free-to-play fighting games, Monetisation Model replaces Presentation & Artstyle as the concern shifts to cost-to-play. Roster Monetisation captures the specific pain point of characters locked behind paywalls — the most common free-to-play complaint in fighting games.

---

## Other Themes Considered

- **Player Base / Longevity** — "big the current player base is, I don't have motivation to start if it seems dead" (Reddit). Cut because it's time-sensitive state, not a quality axis. The same game that had a dead player base in 2022 can be thriving in 2026. Tracked as a tag (active servers, player count estimate) rather than scored.
- **Crossplay / Connectivity** — brawlhalla crossplay (27 search interest, +30%). Cut as a standalone metric because crossplay is binary — you either have it or don't — rather than a spectrum rubric thresholds can describe. Tracked as a tag.
- **Netcode (genre-level)** — Named directly in Reddit as a top quality factor. Kept as a multiplayer niche metric only because a significant portion of fighting games are primarily local-play experiences (Gang Beasts, Stick Fight, Rivals of Aether local) where netcode is irrelevant to what's being scored.

---

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Add rubric files for any pool metrics that need sub-genre-specific scoring thresholds
3. Add a row to the sub-genres table above with a description and folder link
