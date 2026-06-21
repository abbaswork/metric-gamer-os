# Metric Gamer — Site Structure & Entry

## Site Structure

```
metricgamer.com/
├── Home  /
│   └── Find Games search bar (primary CTA)
│
├── Game Page  /games/[game-slug]
│   ├── Introduction & overview
│   ├── Metric scores (per-metric breakdown)
│   ├── Pros & cons
│   ├── Verdict
│   ├── FAQs
│   ├── Where to play
│   └── Similar games → links to Ranked List Page
│
├── Ranked List Page  /rankings/[list-slug]
│   ├── List introduction
│   ├── All games ranked by combined metric score
│   ├── Per-game metric breakdown
│   └── Metric toggle (remove metrics → score recalculates dynamically)
│
├── Find Ranked Lists  /rankings
│   └── Browse all curated ranking campaigns
│
└── About  /about  (accessed via ? icon)
    ├── What is Metric Gamer
    ├── Methodology explanation
    └── Author profiles
```

## Full Journey Map into Site

```
                    ┌─────────────────────────────────────────┐
                    │            ENTRY POINTS                 │
                    └───────┬──────────────┬──────────────────┘
                            │              │              │
              Social Media  │    Google /  │   Google /   │  Backlinks
              (IG/YT/TT)    │    Backlinks │   Organic    │  
                            ▼              ▼              ▼
                        HOME PAGE     GAME PAGE    RANKED LIST PAGE
                        (search)      (cold)         (cold)
                            │              │              │
                            └──────────────┴──────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │       GAME PAGE         │
                              │  intro → metrics →      │
                              │  pros/cons → verdict →  │
                              │  FAQs → where to play   │
                              └────────────┬────────────┘
                                           │
                              ┌────────────▼────────────┐
                              │    RANKED LIST PAGE     │
                              │  ranked comparison →    │
                              │  metric toggle →        │
                              │  dynamic score          │
                              └──────┬──────────┬───────┘
                                     │          │
                          Browse all lists   About / Methodology
                          (/rankings)        (/about via ? icon)
```

---

## Page-Level Entry Point Summary

| Traffic Source | Landing Page | User Intent |
|---|---|---|
| Instagram / TikTok | Home | Brand-aware, browsing |
| YouTube | Home or Game Page | Game-curious, some intent |
| Google (game name) | Game Page | Evaluating a specific game |
| Google (list query) | Ranked List Page | Seeking a ranked recommendation |
| Guest post backlink | Game Page | Referred, evaluating specific game |
| Direct / brand | Home | Returning or brand-aware user |
