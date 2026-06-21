# Scoring System — Overview

## Purpose

The scoring system is how Metric Gamer turns real player sentiment into structured, comparable scores. Every score a user sees on a Game Page or Ranked List Page is the product of this system.

---

## Core Concepts

### Genres

A genre is the top-level category a game belongs to — e.g., **Racing**, **Fighting**.

Each genre has its own set of **metrics** that reflect what players in that genre actually care about. A racing game is not scored on the same things as a fighting game.

### Sub-genres and Niches

Every genre has three layers of specificity:

1. **Genre** — the top-level category (Racing, Fighting, RPG, Sports, Shooters). Genre-level metrics apply to all games in that genre by default. A game can sit at this level with no sub-genre assigned.
2. **Sub-genre** — a named variant within a genre (e.g., JRPG, Cozy, Monster Hunter within RPG). Not every game needs a sub-genre. Sub-genres have their own metrics that reflect what makes that variant distinct.
3. **Niche** — context modifiers that apply at either genre or sub-genre level: **Multiplayer** and **Free**. A niche can exist without a sub-genre.

A niche does not add extra metrics on top — it **swaps** one or more metrics for niche-specific ones. The total is always 5.

Niche rubrics live inside the genre or sub-genre folder under `niches/multiplayer/` or `niches/free/`. They are not shared across genres — each genre's niche rubrics are written specifically for that genre's context. Multiplayer for shooters scores squad play and netcode. Multiplayer for racing scores split-screen performance and online race integrity. The theme is the same; the criteria are different.

**Example:** Racing defaults to AI Quality as its 5th metric. When the niche is Multiplayer (online), AI Quality is swapped for Online Race Integrity — because online races are evaluated on penalty systems and fair play, not AI behaviour.

Each genre's `metrics.md` documents the default metrics and the swap tables for both niches — or, for a genre using the metric pool model (see Metrics below), the full pool and its suggested 5-metric profiles.

### Metrics

A metric is a single, named dimension of quality for a specific genre or sub-genre context — e.g., **Car Roster** (the breadth of cars in a racing game).

- Every campaign is scored on exactly **5 metrics**
- By default, each genre defines one fixed set of 5 — this is the simple model most genres use
- A genre may instead define a **metric pool of up to 10**, when one fixed 5 can't honestly cover contexts as different as a campaign and a large-scale multiplayer mode. When a genre uses a pool, individual pages select 5 from it — the ones most relevant to what that specific page is evaluating — instead of every game in the genre using one shared default. The same game can be scored on a different 5-metric selection across different pages (e.g. a campaign-focused list and a multiplayer-focused list pulling different profiles from the same genre's pool)
- Niches swap one or more metrics for context-specific ones. In the pool model, a niche's "swap" can also just mean picking a different 5 directly from the pool rather than a forced 1-for-1 substitution
- The same metric is never counted twice within a single page's 5 (no overlaps)

### Rubrics

A rubric is the scoring guide for a single metric. It defines what each score (1–5) means in concrete, measurable terms — grounded in real player expectations for that genre.

A rubric is defined **once** per metric and applied consistently to every game scored against it. This is what makes scores comparable across games on the same ranked list.

### Metric Direction

Every metric has a direction that determines how the rubric scales. Direction is set at the time the metric is created and comes from the type of player sentiment that identified it:

- **Delight metric** — players love when this exists. Discovered through positive queries ("favourite part of", "what makes addictive"). Score 5 = maximum of the feature, score 1 = absence of it. Example: Car Roster → 5 = 200+ cars, 1 = under 20.

- **Complaint metric** — players hate when this problem exists. Discovered through pain point queries ("most annoying part of", "what ruins"). Score 5 = absence or minimum of the problem, score 1 = worst case. Example: AI rubber banding → 5 = no rubber banding, 1 = severely broken AI.

Direction is recorded in every rubric file as:
```
**Direction:** Delight — 5 = [best case], 1 = [worst case]
**Direction:** Complaint — 5 = [problem absent], 1 = [problem at its worst]
```

### Tags

Tags are **metadata**, not scoring inputs. They do not affect a game's score.

Tags exist to help users search, filter, and contextualise games — e.g., platform, number of players, developer, release date, estimated playtime.

Tags are defined separately under `/tags/` and are attached to games and lists at the campaign level.

---

## How It Comes Together

1. A **campaign** is created around a specific gaming context (e.g., *Best Split Screen Racing Games on PS2*)
2. The campaign maps to a **genre** (Racing), optionally a **sub-genre** (e.g., JRPG for RPG), and optionally a **niche** (Multiplayer or Free)
3. The relevant **metrics** for that genre + sub-genre + niche combination are identified — for a pool-model genre, this means selecting the 5 most relevant from the pool rather than reading off one fixed default
4. Each metric has a pre-defined **rubric** — the scoring thresholds do not change per campaign
5. Each game in the campaign is researched against player sources (Steam, Reddit, forums) and scored per metric using the rubric
6. The per-metric scores combine into an overall score for that game within that campaign
7. **Tags** are applied separately to support filtering and discovery — they do not alter scores

---

## Folder Structure

```
scoring-system/
├── overview.md                               ← this file
├── genres/
│   ├── racing/
│   │   ├── metrics.md                        ← default metrics + niche swap tables
│   │   ├── research.md                       ← genre research (Reddit, Google Trends)
│   │   ├── carlist/rubric.md
│   │   ├── track-variety/rubric.md
│   │   ├── handling-model/rubric.md
│   │   ├── progression/rubric.md
│   │   ├── ai-quality/rubric.md
│   │   └── niches/
│   │       ├── multiplayer/
│   │       │   ├── split-screen/rubric.md
│   │       │   ├── online-race-integrity/rubric.md
│   │       │   └── matchmaking/rubric.md
│   │       └── free/
│   │           ├── monetisation/rubric.md
│   │           └── car-access/rubric.md
│   ├── fighting/
│   │   ├── metrics.md
│   │   ├── [genre rubrics]/
│   │   └── niches/
│   │       ├── multiplayer/
│   │       │   ├── competitive-balance/rubric.md
│   │       │   ├── netcode/rubric.md
│   │       │   └── ranked-mode/rubric.md
│   │       └── free/
│   │           ├── monetisation/rubric.md
│   │           └── roster-monetisation/rubric.md
│   ├── shooters/
│   │   ├── metrics.md                        ← pool model: up to 10 metrics + profiles
│   │   ├── research.md
│   │   ├── [genre rubrics]/
│   │   └── niches/
│   │       ├── multiplayer/
│   │       │   ├── map-design/rubric.md
│   │       │   ├── netcode/rubric.md
│   │       │   └── squad-play/rubric.md
│   │       └── free/
│   │           ├── monetisation/rubric.md
│   │           └── weapon-access/rubric.md
│   ├── sports/
│   │   ├── metrics.md
│   │   ├── [genre rubrics]/
│   │   └── niches/
│   │       ├── multiplayer/
│   │       │   └── multiplayer-quality/rubric.md
│   │       └── free/
│   │           └── monetisation/rubric.md
│   └── rpg/
│       ├── metrics.md                        ← genre-level defaults
│       ├── niches/                           ← genre-level niches (no sub-genre required)
│       │   ├── multiplayer/
│       │   └── free/
│       └── sub-genres/                       ← RPG has named sub-genres
│           ├── cozy/
│           ├── monster-hunter/
│           ├── horror/
│           └── action/
│               └── niches/                   ← sub-genre-level niches
│                   ├── multiplayer/
│                   └── free/
└── tags/
    ├── platforms/
    ├── players/
    ├── playtime/
    └── developer/
```

Genre rubrics live inside their genre folder. Niche rubrics live inside `{genre}/niches/{multiplayer|free}/` or inside `{genre}/sub-genres/{sub-genre}/niches/{multiplayer|free}/`. Nothing is shared across genres. The `rubric.md` inside each metric folder is the single source of truth for how that metric is scored.
