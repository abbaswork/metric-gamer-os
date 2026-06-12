# Skill: Generate Metrics & Rubrics

## Purpose

Given a genre and optional sub-genre, research and produce a set of player-validated metrics with scoring rubrics. Each metric represents a crucial, measurable dimension of quality for games in that context. Each rubric defines what scores 1–5 mean in concrete terms, grounded in community consensus — not editorial opinion.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| User Personas | knowledge/persona/persona.md | 5 |
| Scoring System Overview | scoring-system/overview.md | 4 |
| Company Overview | knowledge/company/overview.md | 3 |

Personas are weighted highest (5) — every metric must reflect what real players care about. The scoring system overview (4) defines the structural contract the output must conform to: what a metric is, what a rubric is, how genres and sub-genres relate. Company overview (3) keeps outputs aligned with the gamer-first methodology.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `genre` | string | Yes | The primary game genre (e.g., Racing, Fighting, RPG) |
| `sub_genre` | string | No | A more specific context within the genre (e.g., Split Screen, Kart Racing, Beat 'em Up). If provided, metrics should reflect the sub-genre context on top of the genre baseline. |

---

## Execution Flow

```
Phase 1 — interface.py    Collect genre and sub_genre from the user
     ↓
Phase 2 — Claude          Run web searches → extract raw player quotes → generate metrics + rubrics
```

Run: `python interface.py` then pass the output to Claude with this skill prompt.

---

## Interface Script

`interface.py` — collects `genre` and `sub_genre` and prints the structured input block for Claude.

---

## Web Search Strategy

Research runs entirely through Claude web search. The goal is raw player voice — verbatim quotes from actual community discussions. Queries are designed around what players actually search when they have strong feelings about a genre, not generic discovery language.

### Blocked domains (apply to every search)

```
ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net,
polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com,
trustedreviews.com, thegamer.com, screenrant.com, cbr.com
```

### Search batches

Run all four batches. Replace `{genre}` and `{sub_genre}` with the actual inputs.

**Batch 1 — Pain points (4 searches)**

Complaint queries surface what players genuinely hate. Answers become **complaint metrics** where 5 = absence or minimum of the problem, 1 = worst case.

- `reddit "most annoying part of {genre} games"`
- `reddit "what ruins {genre} games"`
- `reddit "biggest complaint about {genre} games"`
- `reddit "why do people quit {genre} games"`

**Batch 2 — Delights (4 searches)**

Positive queries surface what players genuinely love. Answers become **delight metrics** where 5 = maximum of the feature, 1 = absence of it.

- `reddit "favourite part of {genre} games"`
- `reddit "what makes {genre} games addictive"`
- `reddit "best thing about {genre} games"`
- `reddit "what keeps you playing {genre} games"`

**Batch 3 — Discovery intent (3 searches)**

These match what players search when choosing a game — the same intent as Metric Gamer users. Results often validate which dimensions matter most to purchase decisions.

- `reddit "what to look for in a {genre} game"`
- `reddit "what should a good {genre} game have"`
- `gamefaqs "{genre}" forum what matters recommend`

**Batch 4 — Sub-genre specific (2 searches, only if sub_genre was provided)**

- `reddit "{sub_genre}" "{genre}" what matters players`
- `reddit "{sub_genre}" "{genre}" complaint OR hate OR love`

### What to extract

Pull **verbatim quotes** from players. Do not paraphrase. For each quote note:
- The platform (Reddit, Steam, GameFAQs, NeoGAF, etc.)
- Whether it is a pain point or a delight
- The specific dimension it refers to — this becomes a metric candidate

Themes that appear across multiple independent sources are metric candidates. A single mention is not enough.

### Identifying metrics from research

After collecting quotes, group them by theme. Each recurring theme is a candidate metric. For each, determine its direction before writing the rubric:

- **Complaint metric** — players hate when this exists. Score 5 = least of this, score 1 = most of this. Example: grind in JRPGs → 5 = no meaningful grind, 1 = excessive grind required.
- **Delight metric** — players love when this exists. Score 5 = most of this, score 1 = absence of it. Example: replayability in open world RPGs → 5 = highly replayable, 1 = single playthrough.

### What to skip

- Any result that reads like editorial content, even if it quotes players
- Aggregator or listicle pages
- Results from the blocked domain list
- Quotes that express personal taste rather than a genre-wide concern

---

## Acceptance Criteria

These apply at the **start** (to guide research) and at the **end** (to validate before submitting).

- [ ] Exactly 5 metrics are generated — no more, no fewer
- [ ] Every metric is backed by at least one verbatim player quote from the web search
- [ ] Every metric is specific enough to have a definable rubric — it can be measured or concretely described
- [ ] Each rubric covers all 5 score levels (1–5) with clear, distinct thresholds that do not overlap
- [ ] Each rubric level is written in **second person** ("you") — not a label or summary
- [ ] Each metric includes a **"Why this matters"** note and a **"Sources"** section citing which platforms the quotes came from
- [ ] No metric is peripheral — it applies to the majority of games in this genre/sub-genre
- [ ] The full set covers the core player experience without significant gaps or overlaps
- [ ] If a sub-genre was provided, at least one metric specifically reflects what makes it distinct from the parent genre
