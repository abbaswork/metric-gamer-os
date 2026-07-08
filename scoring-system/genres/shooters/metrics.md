# Genre: Shooters
## Metric Pool (up to 10)

Shooters uses the metric pool model: the genre defines up to 10 validated metrics, and any single page (game page or ranked list) selects 5 of them — whichever are most relevant to what's actually being scored. The same game can be scored on a different 5-metric selection across different pages (e.g. a "Best Shooter Campaigns" list vs. a "Best Squad-Based Shooters" list) rather than being locked into one fixed set genre-wide.

| # | Metric | Type | Direction | Best fit for | Rubric |
|---|---|---|---|---|---|
| 1 | Gunplay | Qualitative | Delight | Every shooter — universal. Covers weapon feel, hit feedback, and arsenal variety/customization as one combined dimension. | [rubric](sub-genres/fps/gunplay/rubric.md) |
| 2 | Level Design | Qualitative | Delight | Single player / campaign | [rubric](sub-genres/fps/level-design/rubric.md) |
| 3 | Campaign Structure | Qualitative | Delight | Single player / campaign | [rubric](sub-genres/fps/campaign-structure/rubric.md) |
| 4 | Enemy Variety | Qualitative | Delight | Single player / campaign (AI-driven) | [rubric](sub-genres/fps/enemy-variety/rubric.md) |
| 5 | Squad Play & Class Design | Qualitative | Delight | Large-scale multiplayer (squad/class-based) | [rubric](niches/multiplayer/online-squads/rubric.md) |
| 6 | Maps | Qualitative | Delight | Large-scale multiplayer (route/objective design) | [rubric](niches/multiplayer/online-maps/rubric.md) |
| 7 | Movement | Qualitative | Delight | Any shooter where traversal is a skill layer, including vehicle-to-foot integration where the game has vehicles | [rubric](sub-genres/fps/movement/rubric.md) |
| 8 | Game Modes | Qualitative | Delight | Large-scale multiplayer — mode variety, design, how modes flow with maps/classes, and offline/bot playability | [rubric](niches/multiplayer/online-game-modes/rubric.md) |
| 9 | Community | Qualitative | Delight | Any active-playerbase multiplayer shooter — the actual playerbase's toxicity/friendliness and cheater prevalence, plus population/matchmaking health | [rubric](niches/multiplayer/online-community/rubric.md) |

Gunplay applies to virtually every shooter regardless of context — including what used to be a separate Weapon Variety & Customization metric, now folded in since a wide arsenal only matters in service of how it feels to fire. The other metrics split along whether the page is scoring a campaign experience or a large-scale multiplayer experience. Squad Play & Class Design, Maps, Game Modes, and Community have no separate fps pool rubric file — all four are multiplayer-only by definition, so their one definition lives directly under `niches/multiplayer/`.

## Suggested Profiles

These are starting points for picking 5 from the pool above, not enforced swaps.

**Single Player Campaign:** Gunplay, Level Design, Campaign Structure, Enemy Variety, Movement

**Large-Scale Multiplayer:** Gunplay, Squad Play & Class Design, Maps, Movement, Game Modes. This closes the previous open gap in this profile — Game Modes is the first genuinely multiplayer-native 5th metric, covering mode variety/design and whether the population is actually there to play the mode you want. Community isn't in this default 5 (a page still only picks 5), but it's an available swap for a specific page where lobby/voice culture is more central to the game's identity than one of the above — e.g. a Hell Let Loose page might swap Community in for Movement, the same way the Battlefield 5 example below swaps in Campaign Structure.

**Hybrid** (game ships both modes, page covers it holistically): pick the 5 most relevant to what the page is actually evaluating. A Battlefield 5 game page reviewed primarily for its multiplayer might use the Large-Scale Multiplayer profile with Campaign Structure swapped in for Movement if the campaign is a notable part of the game's identity — Google Trends data on Battlefield 5 shows breakout search interest in campaign-specific queries ("is battlefield 5 campaign good", "how long is battlefield 5 campaign") even though the game is primarily known for multiplayer, which is why Campaign Structure stays in the pool rather than getting swapped out entirely the way it used to be.

## Sub-genres

Shooters doesn't require a sub-genre — the pool model above is the default, and most pages just pick 5 metrics straight from the pool. A sub-genre folder exists when a named variant needs its own tailored rubric.md for a metric the pool already defines.

| Sub-genre | Description | Folder |
|---|---|---|
| fps | First-person shooters — the genre's reference point so far, spanning both campaign (Half-Life 2, Doom Eternal) and large-scale multiplayer (Battlefield, Call of Duty) titles. The 5 pool metrics not owned by a niche (Gunplay, Level Design, Campaign Structure, Enemy Variety, Movement) are written here, with FPS-specific language — iron sights, ADS, hitscan/projectile gunplay — built into the thresholds. | [sub-genres/fps/](sub-genres/fps/) |
| battle-royale | Large-lobby last-player/team-standing shooters (Warzone, Fortnite). Not yet built out — see [todo.md](sub-genres/battle-royale/todo.md). | [sub-genres/battle-royale/](sub-genres/battle-royale/) |

`sub-genres/fps/research.md` holds the manual Reddit/Google Trends research backing these rubrics; it's scoped to FPS titles (Battlefield, Call of Duty) and is the primary source for the metrics where it has a matching theme — Gunplay (the weapon variety + customization angle, plus the aim-assist fairness note), Movement, Campaign Structure (the OP's own 5/5 definitions from the 2026-07-06 r/fps thread cover these three directly, in their own words — see research.md), and (via `niches/multiplayer/`) Squad Play & Class Design, Maps, Game Modes, and Community. Enemy Variety and Level Design still lean on web-confirmed sources, since research.md has no Reddit/Trends line item for those two themes. A future sub-genre with different community research — battle-royale, once it's built out — would get its own `research.md` rather than sharing this one.

A non-FPS sub-genre that needs different scoring language for an existing pool metric (e.g. a top-down shooter where "iron sights" doesn't map cleanly onto Gunplay) gets its own `rubric.md` for that metric under its sub-genre folder, rather than editing the fps version.

---

## Other Themes Considered (not in the pool)

- **Atmosphere** (setting — WW2, futuristic, etc.) — a taste signal, not a quality axis. The gradable part of this is execution, which overlaps too heavily with Immersion to stand alone.
- **Immersion** (sound design) — Gunplay's rubric already covers audiovisual and sound feedback explicitly. Keeping this separate would score the same thing twice.
- **Cosmetics** — weakest research support (single mention, no Google Trends signal). The real complaints in this space are about monetization, which the Free niche's Monetisation Model metric already owns.
- **Vehicle Variety & Customization** — folded into Movement as a traversal consideration rather than kept as a standalone metric or a Maps consideration. Whether a vehicle is good is inseparable from whether it actually extends what a player can do with movement — that's a Movement question, not a question of route/objective layout (Maps) or of how the vehicle itself handles in isolation.
- **Netcode & Server Quality** — previously a Multiplayer niche metric; removed. No fps pool equivalent exists, so there's nothing for a multiplayer page to fall back on for this dimension right now.
- **Team Size** — raised once (50v50) in r/fps research, 2026-07-06. Folded into Game Modes as a sub-consideration rather than a standalone metric — scale shapes what a mode's front line/objective flow means, but on its own it's a single mention, not enough signal for its own axis.
- **Input Parity / Aim Assist** — raised in the same research pass (necessary for controller players, but a dealbreaker when it crosses into overpowered/aim-botty). Folded into Gunplay's rubric as a fairness dimension of weapon handling rather than a standalone metric — single thread of agreement, and conceptually closer to "is the gunplay fair" than to a new independent axis.
- **HUD/UI Clarity** — raised once ("really readable in-world" HUD). Single mention, no Google Trends or repeated Reddit signal — logged here, no action taken.

## Niche: Multiplayer

Niche rubrics live in `niches/multiplayer/`. These replace or supplement the pool selections when scoring a multiplayer-specific page.

| Metric | Rubric | Use When |
|---|---|---|
| Maps | [rubric](niches/multiplayer/online-maps/rubric.md) | Large-scale or tactical multiplayer with multiple map options |
| Squad Play & Class Design | [rubric](niches/multiplayer/online-squads/rubric.md) | Team-based or squad-focused multiplayer (Battlefield, Apex, Planetside) |
| Game Modes | [rubric](niches/multiplayer/online-game-modes/rubric.md) | Any multiplayer shooter with more than one mode, to score mode design and offline/bot playability |
| Community | [rubric](niches/multiplayer/online-community/rubric.md) | Any multiplayer shooter with an active playerbase, to score actual community toxicity/friendliness, cheating prevalence, and population/matchmaking health |

None of these are a swap against an fps pool rubric — all four metrics are multiplayer-only by definition, so the niche file is their only definition, not a replacement for a campaign-flavoured version.

---

## Niche: Free

Niche rubrics live in `niches/free/`.

| Swap Out | Swap In | Rubric |
|---|---|---|
| Enemy Variety | Monetisation Model | [rubric](niches/free/monetisation/rubric.md) |

Free-to-play shooters swap Enemy Variety for Monetisation Model, which covers battle pass fairness, operator cosmetic advantages, and weapon access/pay-to-win concerns as one combined metric.

---

## Adding a New Niche

1. Create a folder under `niches/[niche-name]/` inside this genre folder
2. Add a `rubric.md` for each new metric
3. Add a row to the relevant swap table above, specifying which default metric it replaces and why

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Add a `rubric.md` for any pool metrics that need sub-genre-specific scoring thresholds — only add a file when the thresholds actually need to differ from the fps version, not as a blanket copy
3. Add a row to the Sub-genres table above with a description and folder link
