# Racing — Metric Configuration

## Default Metrics (5)

These apply to every Racing game regardless of sub-genre.

| # | Metric | Type | Rubric |
|---|---|---|---|
| 1 | Car Roster | Quantitative | [rubric](carlist/rubric.md) |
| 2 | Track Variety | Quantitative | [rubric](track-variety/rubric.md) |
| 3 | Handling Model | Qualitative | [rubric](handling-model/rubric.md) |
| 4 | Progression | Qualitative + Quantitative | [rubric](progression/rubric.md) |
| 5 | AI Quality | Qualitative | [rubric](ai-quality/rubric.md) |

---

## Sub-genre Metric Swaps

When a sub-genre is active, one or more default metrics are replaced. The total always stays at 5.

| Sub-genre | Replaces | With | Reason |
|---|---|---|---|
| Split Screen | AI Quality | [Split Screen Performance](../../sub-genres/split-screen/performance/rubric.md) | Split screen games are played against human opponents — AI quality becomes irrelevant to the core experience |
| Free | AI Quality | [Monetisation Model](../../sub-genres/free/monetisation/rubric.md) | Free racing games are typically online or live-service focused — AI quality is secondary to whether the business model is fair |

---

## Adding a New Sub-genre

1. Create a folder under `scoring-system/metrics/sub-genres/[sub-genre-name]/`
2. Add a `rubric.md` for each new metric
3. Add a row to the swap table above, specifying which default metric it replaces and why
