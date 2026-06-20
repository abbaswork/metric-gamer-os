# Scoring System — Overview

## Purpose

The scoring system is how Metric Gamer turns real player sentiment into structured, comparable scores. Every score a user sees on a Game Page or Ranked List Page is the product of this system.

---

## Core Concepts

### Genres

A genre is the top-level category a game belongs to — e.g., **Racing**, **Fighting**.

Each genre has its own set of **metrics** that reflect what players in that genre actually care about. A racing game is not scored on the same things as a fighting game.

### Sub-genres

A sub-genre is a more specific context within a genre — e.g., **Split Screen Racing** within Racing.

A sub-genre does not add extra metrics on top of the genre — it **swaps** one or more genre metrics for sub-genre-specific ones. The total is always 5.

**Example:** Racing defaults to AI Quality as its 5th metric. When the sub-genre is Split Screen, AI Quality is swapped for Split Screen Performance — because split screen games are played against human opponents, making AI quality irrelevant to that experience.

Each genre's `metrics.md` documents the default 5 and the swap table for all its sub-genres — or, for a genre using the metric pool model (see Metrics below), the full pool and its suggested 5-metric profiles instead of a single default and swap table.

### Metrics

A metric is a single, named dimension of quality for a specific genre or sub-genre context — e.g., **Car Roster** (the breadth of cars in a racing game).

- Every campaign is scored on exactly **5 metrics**
- By default, each genre defines one fixed set of 5 — this is the simple model most genres use
- A genre may instead define a **metric pool of up to 10**, when one fixed 5 can't honestly cover contexts as different as a campaign and a large-scale multiplayer mode. When a genre uses a pool, individual pages select 5 from it — the ones most relevant to what that specific page is evaluating — instead of every game in the genre using one shared default. The same game can be scored on a different 5-metric selection across different pages (e.g. a campaign-focused list and a multiplayer-focused list pulling different profiles from the same genre's pool)
- Sub-genres swap one or more metrics for context-specific ones. In the pool model, a sub-genre's "swap" can also just mean picking a different 5 directly from the pool rather than a forced 1-for-1 substitution
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
2. The campaign maps to a **genre** (Racing) and optionally a **sub-genre** (Split Screen Racing)
3. The relevant **metrics** for that genre + sub-genre are identified — for a pool-model genre, this means selecting the 5 most relevant from the pool rather than reading off one fixed default
4. Each metric has a pre-defined **rubric** — the scoring thresholds do not change per campaign
5. Each game in the campaign is researched against player sources (Steam, Reddit, forums) and scored per metric using the rubric
6. The per-metric scores combine into an overall score for that game within that campaign
7. **Tags** are applied separately to support filtering and discovery — they do not alter scores

---

## Folder Structure

```
scoring-system/
├── overview.md                           ← this file
├── metrics/
│   ├── genres/
│   │   ├── racing/
│   │   │   ├── metrics.md               ← default 5 metrics + sub-genre swap table
│   │   │   ├── carlist/rubric.md
│   │   │   ├── track-variety/rubric.md
│   │   │   ├── handling-model/rubric.md
│   │   │   ├── progression/rubric.md
│   │   │   └── ai-quality/rubric.md     ← default 5th; swapped out for split screen
│   │   ├── fighting/
│   │   └── shooters/
│   │       ├── metrics.md               ← pool model: up to 10 metrics + suggested profiles
│   │       ├── gunplay/rubric.md
│   │       ├── weapon-variety/rubric.md
│   │       ├── level-design/rubric.md
│   │       ├── campaign-structure/rubric.md
│   │       ├── enemy-variety/rubric.md
│   │       ├── squad-play/rubric.md
│   │       ├── maps/rubric.md
│   │       └── movement/rubric.md
│   └── sub-genres/
│       └── split-screen/
│           └── performance/rubric.md    ← replaces ai-quality for split screen campaigns
└── tags/
    ├── platforms/
    ├── players/
    ├── playtime/
    ├── release-dates/
    └── developer/
```

Each metric lives inside its genre (or sub-genre) folder. The `rubric.md` inside each metric folder is the single source of truth for how that metric is scored. A pool-model genre keeps every pool metric directly under its own `genres/{genre}/` folder rather than splitting context-specific ones into a separate `sub-genres/` folder — the pool already covers what swapping used to handle.
