# Genre: Racing

> **Sub-genre required.** Every racing game must be assigned a sub-genre before scoring. There is no genre-level default. Rubrics live inside the sub-genre folders, not at the genre level.

## Metric Pool

Racing uses the metric pool model: the genre defines a pool of validated metrics, and any single campaign page selects the most relevant from the pool for that context. A "Best Open-World Arcade Racers" campaign pulls different metrics than a "Best Crash & Combat Racers" campaign.

| # | Metric | Type | Direction | Best fit for |
|---|---|---|---|---|
| 1 | Car Roster | Qualitative | Delight | Every racing game — universal |
| 2 | Track Variety & Design | Qualitative | Delight | Every racing game — universal |
| 3 | Handling Model | Qualitative | Delight | Every racing game — universal |
| 4 | Customization & Progression | Qualitative | Delight | Every racing game — universal |
| 5 | AI Quality | Qualitative | Complaint | Single-player / vs-AI race contexts |

Car Roster, Track Variety & Design, Handling Model, and Customization & Progression apply to virtually every racing game regardless of sub-genre — though the rubric thresholds for Handling Model differ sharply between an arcade racer and a sim racer, which is why each sub-genre writes its own version. AI Quality is essential for any race context with computer-controlled opponents but gets swapped for Online Race Integrity once the context is fully competitive online play (see Niche: Multiplayer below).

Each sub-genre folder also contains one unique metric that applies only to that sub-genre:

| Sub-genre | Unique Metric | Folder |
|---|---|---|
| Arcade Racing | Spectacle & Crashes | `spectacle-crashes/rubric.md` |

The unique metric is added to the campaign's pool alongside the 5 base metrics, giving 6 total candidates to select 5 from for an Arcade Racing campaign.

---

## Suggested Profiles

These are starting points, not enforced selections. Pick the 5 most relevant to what the campaign is actually evaluating.

**Arcade Racing — Open World / Street Racing** (Need for Speed Most Wanted, Need for Speed Underground, Midnight Club 3): Handling Model, Car Roster, Customization & Progression, Track Variety & Design, AI Quality

**Arcade Racing — Crash & Combat Focus** (Burnout 3: Takedown, Crazy Taxi, Sega Rally): Handling Model, Spectacle & Crashes, Track Variety & Design, AI Quality, Car Roster

---

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| Arcade Racing | Accessible, exaggerated-physics racing that prioritizes fun and spectacle over simulation — drifting, takedowns, and open-world street racing (Need for Speed, Burnout, Crazy Taxi, Midnight Club) | [sub-genres/arcade-racing/](sub-genres/arcade-racing/) |

---

## Niche: Multiplayer

Niche rubrics live in `niches/multiplayer/`. These replace pool selections when scoring a multiplayer-specific campaign.

| Metric | Rubric | Use When |
|---|---|---|
| Online Race Integrity | [rubric](niches/multiplayer/online-race-integrity/rubric.md) | Online races — replaces AI Quality, since there is no computer-controlled opponent to score |
| Split-Screen Quality | [rubric](niches/multiplayer/split-screen/rubric.md) | Games offering local split-screen multiplayer |
| Matchmaking & Lobby Quality | [rubric](niches/multiplayer/matchmaking/rubric.md) | Games with an online ranked or quick-match queue |

---

## Niche: Free

Niche rubrics live in `niches/free/`.

| Swap Out | Swap In | Rubric |
|---|---|---|
| Customization & Progression | Monetisation Model | [rubric](niches/free/monetisation/rubric.md) |
| Car Roster | Car Access | [rubric](niches/free/car-access/rubric.md) |

For free-to-play racing games, Monetisation Model replaces Customization & Progression since the concern shifts to cost-to-progress. Car Access captures the specific pain point of cars locked behind paywalls or grind walls — distinct from Car Roster's measure of total roster breadth.

---

## Other Themes Considered

- **Realism** — Named in Reddit research as a factor in "what makes a good arcade racing game," but kept out of the pool as a standalone metric. Arcade racing's identity is built on exaggerated, accessible handling rather than physical accuracy; the few mentions likely reflect sim-racing crossover responses bleeding into the same threads rather than arcade-specific sentiment. Realism is the right axis for a future Sim Racing sub-genre, not this one.
- **Mastery / Skill Ceiling** — "tactile action and a sense of accomplishment from mastery," "take genuine effort to get good at" (Reddit). Cut as a standalone metric because it's a property of the Handling Model, not a separate axis — a handling model that rewards mastery scores higher on Handling Model directly.
- **Goofy / Chaotic Moments** — "get to do really goofy things" (Reddit). Folded into Spectacle & Crashes rather than kept separate, since the appeal is the same spectacle-over-realism payoff as a good crash or takedown.

---

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Add rubric files for any pool metrics that need sub-genre-specific scoring thresholds, plus the sub-genre's own unique metric
3. Add a row to the sub-genres table above with a description and folder link
