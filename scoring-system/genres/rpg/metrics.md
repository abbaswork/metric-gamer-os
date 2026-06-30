# Genre: RPG

> **Sub-genre not mandated.** Per `scoring-system/overview.md`, RPG allows a game to sit at the genre level with no sub-genre assigned. That said, genre-level default metrics still haven't been defined — **Cozy and JRPG are the two RPG sub-genres built out so far**, and the metric sets below are sub-genre-specific, not genre-wide defaults. Notably, the two sub-genres share zero metrics in practice even though both happen to use "Story" and "Character Development" as names — the underlying rubrics are written for entirely different contexts (farm-sim relationship mechanics vs. turn-based party narratives). Genre-level defaults are easier to abstract correctly once a third sub-genre exists to triangulate against.

## Cozy — Metric Set (6, by explicit override)

> **Deviation from the standard 5-metric cap.** `scoring-system/overview.md` specifies every page is scored on exactly 5 metrics (or 5 selected from a pool of up to 10 for pool-model genres). Research on `sub-genres/cozy/research.md` grouped cleanly into 6 distinct themes — Gameplay, Character Development, Story, World Design, Customisation, and Pacing — and merging any two would have flattened a real distinction (e.g. Character Development and Story are both narrative but track different things: relationship progression vs. plot/lore writing). The user explicitly overrode the 5-metric cap for this sub-genre rather than have two themes merged. This is a documented exception specific to Cozy, not a precedent for other RPG sub-genres.

| # | Metric | Type | Direction | Rubric |
|---|---|---|---|---|
| 1 | Gameplay | Qualitative | Delight | [rubric](sub-genres/cozy/gameplay/rubric.md) |
| 2 | Character Development | Qualitative | Delight | [rubric](sub-genres/cozy/character-development/rubric.md) |
| 3 | Story | Qualitative | Delight | [rubric](sub-genres/cozy/story/rubric.md) |
| 4 | World Design | Qualitative | Delight | [rubric](sub-genres/cozy/world-design/rubric.md) |
| 5 | Customisation | Qualitative | Delight | [rubric](sub-genres/cozy/customisation/rubric.md) |
| 6 | Pacing | Qualitative | Complaint | [rubric](sub-genres/cozy/pacing/rubric.md) |

---

## JRPG — Metric Set (5)

Research on `sub-genres/jrpg/research.md` grouped cleanly into a standard simple-5 — no override needed here, unlike Cozy. Two close calls were resolved with the user before generating: Story and Character Development stayed split (rather than merged, even though the research ties them together almost every time) for consistency with how Cozy treats them; Music/Soundtrack — named independently as a top-3 draw multiple times — was folded into World Design as shared atmosphere, also for consistency with Cozy's approach. A genre-famous complaint axis (grind/padding) was deliberately **not** added as a metric since this research file surfaced no actual grind complaints, only positive length-as-value framing — see "Other Themes Considered" below.

| # | Metric | Type | Direction | Rubric |
|---|---|---|---|---|
| 1 | Story | Qualitative | Delight | [rubric](sub-genres/jrpg/story/rubric.md) |
| 2 | Character Development | Qualitative | Delight | [rubric](sub-genres/jrpg/character-development/rubric.md) |
| 3 | Combat & Gameplay Systems | Qualitative | Delight | [rubric](sub-genres/jrpg/combat-gameplay-systems/rubric.md) |
| 4 | World Design | Qualitative | Delight | [rubric](sub-genres/jrpg/world-design/rubric.md) |
| 5 | Length & Value | Qualitative | Delight | [rubric](sub-genres/jrpg/length-value/rubric.md) |

All 5 are Delight-direction — the research file ran positive-framed queries only (no "what ruins JRPGs" pain-point factors), so no complaint metric is corroborated in this set.

---

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| cozy | Low-stakes, relaxation-focused RPGs built around farming, life-sim, and social mechanics — self-paced, with no real fail state (Stardew Valley, Animal Crossing: New Horizons, Palia, Disney Dreamlight Valley, Spiritfarer) | [sub-genres/cozy/](sub-genres/cozy/) |
| jrpg | Japanese-developed RPGs built around pre-defined protagonists, story-driven progression, and typically turn-based or menu-driven combat (Final Fantasy VII, Dragon Quest XI S, Persona 5 Royal, Chrono Trigger, Pokémon) | [sub-genres/jrpg/](sub-genres/jrpg/) |
| action | Not yet built out — see [todo.md](sub-genres/action/todo.md) |
| horror | Not yet built out — see [todo.md](sub-genres/horror/todo.md) |
| monster-hunter | Not yet built out — see [todo.md](sub-genres/monster-hunter/todo.md) |

`sub-genres/cozy/research.md` and `sub-genres/jrpg/research.md` hold the manual Reddit/Google Trends research backing each sub-genre's rubrics. Each rubric also cites at least one external source beyond research.md per the generate-metrics-rubrics skill's hard requirement.

---

## Other Themes Considered (not in either set)

**Cozy:**
- **Monetisation / No Paywall** — Palia research ("Free to play", "No content locked behind a paywall", "Constant free game updates") points at this clearly, but it's a **Free niche** concern, not a sub-genre metric. RPG's `niches/free/` isn't built out yet — revisit when that work starts.
- **Community Warmth** — Palia's "Welcoming and friendly community" is a single-source signal tied specifically to its multiplayer context; Stardew's single-player-focused research doesn't surface it, so it isn't corroborated across the sub-genre as a whole. Belongs in a future **Multiplayer niche** for RPG, not the base Cozy set.
- **Replayability via Farm Map Variety** — folded into Customisation. Choosing between multiple farm layouts is a customisation axis, not a standalone metric.
- **Content Volume / Hours-for-Price** — folded into Pacing. A loop with enough to do that you don't run out before you're ready to stop is treated as the positive end of Pacing, not a separate value metric.

**JRPG:**
- **Grind / Padding (complaint)** — the genre's most famous criticism, but no actual grind complaints showed up in this research file (only positive "long game = good value" framing). Deliberately skipped rather than invented — a future research pass specifically targeting JRPG pain points ("what ruins JRPGs", "biggest complaint about JRPGs") would be needed to source this properly before it becomes a metric.
- **Gacha / Live-Service Monetisation** — the "Free JRPGs" top-games list (Genshin Impact, Honkai: Star Rail, Zenless Zone Zero, Wuthering Waves) plus one Reddit quote about avoiding "the competitive multiplayer hamster wheel" and not falling behind "the meta" both point at this, but it's a **Free niche** concern, not a base sub-genre metric.
- **Linearity vs. Exploration** — research shows a real split (some players value JRPG linearity/strong storytelling, others value open exploration) rather than one consistent preference. Treated as a spectrum World Design accommodates rather than a separate axis — see that rubric's score bands.

## Niches

Not yet built for RPG, Cozy, or JRPG. `niches/free/` and `niches/multiplayer/` exist as empty placeholders. See "Other Themes Considered" above for candidate niche metrics once that work starts.

---

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Add a `research.md` first (Reddit + Google Trends), per `scoring-system/overview.md` and the generate-metrics-rubrics skill
3. Add a `rubric.md` for each metric — reuse a metric from an existing sub-genre (Cozy, JRPG) only where the theme genuinely transfers; introduce a new one where it doesn't
4. Add a row to the Sub-genres table above
