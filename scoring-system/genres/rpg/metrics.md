# Genre: RPG

> **Sub-genre not mandated.** Per `scoring-system/overview.md`, RPG allows a game to sit at the genre level with no sub-genre assigned. That said, genre-level default metrics haven't been defined yet — **Cozy is the first RPG sub-genre built out**, so the 6 metrics below are Cozy-specific, not genre-wide defaults. Genre-level defaults are easier to abstract correctly once a second sub-genre exists to compare against, rather than generalising from one data point now.

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

## Sub-genres

| Sub-genre | Description | Folder |
|---|---|---|
| cozy | Low-stakes, relaxation-focused RPGs built around farming, life-sim, and social mechanics — self-paced, with no real fail state (Stardew Valley, Animal Crossing: New Horizons, Palia, Disney Dreamlight Valley, Spiritfarer) | [sub-genres/cozy/](sub-genres/cozy/) |
| action | Not yet built out — see [todo.md](sub-genres/action/todo.md) |
| horror | Not yet built out — see [todo.md](sub-genres/horror/todo.md) |
| monster-hunter | Not yet built out — see [todo.md](sub-genres/monster-hunter/todo.md) |

`sub-genres/cozy/research.md` holds the manual Reddit/Google Trends research backing these 6 rubrics, scoped to Stardew Valley and Palia — the two games with dedicated research in that file. Each rubric also cites at least one external source beyond research.md per the generate-metrics-rubrics skill's hard requirement.

---

## Other Themes Considered (not in the 6)

- **Monetisation / No Paywall** — Palia research ("Free to play", "No content locked behind a paywall", "Constant free game updates") points at this clearly, but it's a **Free niche** concern, not a sub-genre metric. RPG's `niches/free/` isn't built out yet — revisit when that work starts.
- **Community Warmth** — Palia's "Welcoming and friendly community" is a single-source signal tied specifically to its multiplayer context; Stardew's single-player-focused research doesn't surface it, so it isn't corroborated across the sub-genre as a whole. Belongs in a future **Multiplayer niche** for RPG, not the base Cozy set.
- **Replayability via Farm Map Variety** — folded into Customisation. Choosing between multiple farm layouts is a customisation axis, not a standalone metric.
- **Content Volume / Hours-for-Price** — folded into Pacing. A loop with enough to do that you don't run out before you're ready to stop is treated as the positive end of Pacing, not a separate value metric.

## Niches

Not yet built for RPG or Cozy. `niches/free/` and `niches/multiplayer/` exist as empty placeholders. See "Other Themes Considered" above for candidate niche metrics once that work starts — both candidates come directly from Palia, the one multiplayer/free-to-play game in the current research.

---

## Adding a New Sub-genre

1. Create a folder under `sub-genres/[sub-genre-name]/` inside this genre folder
2. Add a `research.md` first (Reddit + Google Trends), per `scoring-system/overview.md` and the generate-metrics-rubrics skill
3. Add a `rubric.md` for each metric — reuse a Cozy metric only where the theme genuinely transfers; introduce a new one where it doesn't
4. Add a row to the Sub-genres table above
