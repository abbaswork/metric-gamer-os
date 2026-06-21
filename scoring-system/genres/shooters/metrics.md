# Genre: Shooters
## Metric Pool (up to 10)

Shooters uses the metric pool model: the genre defines up to 10 validated metrics, and any single page (game page or ranked list) selects 5 of them — whichever are most relevant to what's actually being scored. The same game can be scored on a different 5-metric selection across different pages (e.g. a "Best Shooter Campaigns" list vs. a "Best Squad-Based Shooters" list) rather than being locked into one fixed set genre-wide.

| # | Metric | Type | Direction | Best fit for |
|---|---|---|---|---|
| 1 | Gunplay | Qualitative | Delight | Every shooter — universal |
| 2 | Weapon Variety & Customization | Qualitative | Delight | Every shooter — universal |
| 3 | Level Design | Qualitative | Delight | Single player / campaign |
| 4 | Campaign Structure | Qualitative | Delight | Single player / campaign |
| 5 | Enemy Variety | Qualitative | Delight | Single player / campaign (AI-driven) |
| 6 | Squad Play & Class Design | Qualitative | Delight | Large-scale multiplayer (squad/class-based) |
| 7 | Maps | Qualitative | Delight | Large-scale multiplayer (vehicle + infantry play) |
| 8 | Movement | Qualitative | Delight | Any shooter where traversal is a skill layer |

Gunplay and Weapon Variety & Customization apply to virtually every shooter regardless of context — they're the two metrics most pages will keep. The other 6 split along whether the page is scoring a campaign experience or a large-scale multiplayer experience.

## Suggested Profiles

These are starting points for picking 5 from the pool above, not enforced swaps.

**Single Player Campaign:** Gunplay, Weapon Variety & Customization, Level Design, Campaign Structure, Enemy Variety

**Large-Scale Multiplayer:** Gunplay, Weapon Variety & Customization, Squad Play & Class Design, Maps, Movement

**Hybrid** (game ships both modes, page covers it holistically): pick the 5 most relevant to what the page is actually evaluating. A Battlefield 5 game page reviewed primarily for its multiplayer might use the Large-Scale Multiplayer profile with Campaign Structure swapped in for Movement if the campaign is a notable part of the game's identity — Google Trends data on Battlefield 5 shows breakout search interest in campaign-specific queries ("is battlefield 5 campaign good", "how long is battlefield 5 campaign") even though the game is primarily known for multiplayer, which is why Campaign Structure stays in the pool rather than getting swapped out entirely the way it used to be.

## Other Themes Considered (not in the pool)

- **Atmosphere** (setting — WW2, futuristic, etc.) — a taste signal, not a quality axis. The gradable part of this is execution, which overlaps too heavily with Immersion to stand alone.
- **Immersion** (sound design) — Gunplay's rubric already covers audiovisual and sound feedback explicitly. Keeping this separate would score the same thing twice.
- **Cosmetics** — weakest research support (single mention, no Google Trends signal). The real complaints in this space are about monetization, which the Free sub-genre's Monetisation Model metric already owns.
- **Vehicle Variety & Customization** — folded into Maps as a traversal consideration rather than kept as a standalone metric. Vehicle quality on a bad map and vehicle quality on a good map read very differently — the map is what actually determines whether vehicles work, so it made more sense as one dimension of Maps than a competing metric.

## Sub-genre: Multiplayer

Sub-genre rubrics live in `niches/multiplayer/`. These replace or supplement the pool selections when scoring a multiplayer-specific page.

| Metric | Rubric | Use When |
|---|---|---|
| Map Design | [rubric](niches/multiplayer/map-design/rubric.md) | Large-scale or tactical multiplayer with multiple map options |
| Netcode & Server Quality | [rubric](niches/multiplayer/netcode/rubric.md) | Any online multiplayer mode |
| Squad Play & Class Design | [rubric](niches/multiplayer/squad-play/rubric.md) | Team-based or squad-focused multiplayer (Battlefield, Apex, Planetside) |

For a Large-Scale Multiplayer profile, Map Design and Squad Play & Class Design from the sub-genre folder replace the pool selections of the same names — the sub-genre rubrics have more targeted multiplayer-specific thresholds than the pool metrics. Netcode & Server Quality is always included as one of the 5 for any online multiplayer page.

---

## Sub-genre: Free

Sub-genre rubrics live in `niches/free/`.

| Swap Out | Swap In | Rubric |
|---|---|---|
| Enemy Variety | Monetisation Model | [rubric](niches/free/monetisation/rubric.md) |
| Level Design | Weapon Access | [rubric](niches/free/weapon-access/rubric.md) |

Free-to-play shooters swap Enemy Variety for Monetisation Model. When weapon pay-to-win is a specific documented concern for the title being scored, Weapon Access replaces Level Design as the second free sub-genre metric. For a free multiplayer shooter, apply both the Free and Multiplayer sub-genre rubrics — they address different dimensions and do not overlap.

---

## Adding a New Sub-genre

1. Create a folder under `niches/[sub-genre-name]/` inside this genre folder
2. Add a `rubric.md` for each new metric
3. Add a row to the relevant swap table above, specifying which default metric it replaces and why
