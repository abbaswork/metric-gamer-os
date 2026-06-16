# Sports — Metric Configuration

## Default Metrics (5)

These apply to every Sports game regardless of sub-genre.

| # | Metric | Type | Rubric |
|---|---|---|---|
| 1 | Gameplay | Qualitative | [rubric](gameplay/rubric.md) |
| 2 | Game Modes | Qualitative + Quantitative | [rubric](game-modes/rubric.md) |
| 3 | Roster Depth | Quantitative + Qualitative | [rubric](roster-depth/rubric.md) |
| 4 | Progression | Qualitative + Quantitative | [rubric](progression/rubric.md) |
| 5 | Presentation | Qualitative | [rubric](presentation/rubric.md) |

---

## Sub-genre Metric Swaps

When a sub-genre is active, one or more default metrics are replaced. The total always stays at 5.

| Sub-genre | Replaces | With | Reason |
|---|---|---|---|
| Co-op / Multiplayer | Progression | [Multiplayer Quality](../../sub-genres/sports-multiplayer/multiplayer-quality/rubric.md) | Multiplayer sports games are primarily evaluated on the quality of the competitive and co-op experience — Progression is a single-player metric and is the correct swap out |
| Free | Presentation | [Monetisation Model](../../sub-genres/free/monetisation/rubric.md) | F2P sports games rarely deliver broadcast-quality presentation — the defining question is whether the monetisation model is fair, making Presentation the correct swap out |

---

## Adding a New Sub-genre

1. Create a folder under `scoring-system/metrics/sub-genres/[sub-genre-name]/`
2. Add a `rubric.md` for each new metric
3. Add a row to the swap table above, specifying which default metric it replaces and why
