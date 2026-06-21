# Metric Gamer OS

The operating system for [metricgamer.com](https://www.metricgamer.com) — a structured, AI-assisted system for producing game pages, ranked lists, and SEO campaigns grounded in real player research.

---

## What This Is

Metric Gamer scores games using a rubric system built from community research (Reddit, Google Trends, player forums). Every score on the site traces back to a genre-specific metric, and every metric traces back to what players actually say makes a game good or bad in that context.

This repo holds the full operating system: the company context, the scoring system, the writing rules, the skills that run each workflow, and the campaign records that track what's been produced.

---

## Folder Structure

```
metric-gamer-os/
│
├── .claude/
│   ├── commands/          ← slash command entry points (run these in Claude Code)
│   └── skills/            ← full skill packages: readme + interface.py + connector.json
│
├── company/               ← context about Metric Gamer as a business
│   ├── overview.md        ← what MG is, UVP, how the system works
│   ├── pillars.md         ← editorial and brand principles
│   ├── revenue-share.md   ← contributor point and revenue model
│   ├── persona/
│   │   └── persona.md     ← reader audience profiles
│   └── site/
│       ├── keyword-strategy.md   ← keyword tier system, DA filter, cluster rules
│       ├── site-structure.md     ← page types and URL conventions
│       └── faq-templates.md      ← FAQ question pool and format rules
│
├── operations/            ← milestone and campaign tracking
│   └── 2026-Q3/
│       ├── okrs.md
│       ├── goals.md
│       ├── projects.md    ← quarter-wide task list with point allocations
│       ├── retrospective.md
│       ├── to-do.md
│       └── campaigns/     ← one folder per active campaign
│           └── {campaign}/
│               ├── keywords/   ← keyword planner exports + keywords.md strategy
│               └── drafts/     ← game page and ranked list drafts
│
├── scoring-system/
│   ├── overview.md        ← how genres, sub-genres, niches, and rubrics relate
│   ├── genres/
│   │   └── {genre}/
│   │       ├── research.md          ← genre research (Reddit + Google Trends)
│   │       ├── sub-genres/
│   │       │   └── {sub-genre}/
│   │       │       ├── {metric}/rubric.md   ← one folder per metric, rubric inside
│   │       │       └── niches/
│   │       │           ├── multiplayer/
│   │       │           │   └── {metric}/rubric.md
│   │       │           └── free/
│   │       │               └── {metric}/rubric.md
│   │       └── niches/              ← genre-level niches (no sub-genre required)
│   │           ├── multiplayer/
│   │           └── free/
│   └── tags/              ← metadata only, not scoring inputs
│       ├── platforms/
│       ├── players/
│       ├── playtime/
│       └── developer/
│
├── writing/
│   ├── eeat.md            ← EEAT framework and 7-phase publishing lifecycle
│   ├── Writing-style.md   ← prose rules: tone, structure, what to avoid
│   ├── author-personas/   ← voice file per author contributor
│   └── audits/            ← site and content quality audits
│
├── roles.json             ← team access permissions
└── README.md              ← this file
```

**Current genres:** Racing, Fighting, Shooters (sub-genres: fps, battle-royale), Sports (sub-genre: football), RPG (sub-genres: cozy, monster-hunter, horror, action)

---

## The Content Workflow

Every piece of content follows this sequence. Skills handle the AI-heavy steps.

### 1. Set campaign direction
Start in `operations/{milestone}/`. OKRs and goals set what the quarter is targeting. Create a campaign folder under `campaigns/` for the topic you're working on.

### 2. Keyword research → campaign strategy
Run `/keyword-research` to pull data from Google Keyword Planner. Export CSVs into `campaigns/{campaign}/keywords/`. Then run `/keyword-strategy` to produce Tier 2 (game page) and Tier 3 (FAQ/H2) keyword assignments for the campaign.

### 3. Build the scoring system
Run the scoring-system skill (`python .claude/skills/scoring-system/interface.py`) for your genre and sub-genre. This reads the genre's `research.md` file and produces metrics and rubrics. Rubrics land in `scoring-system/genres/{genre}/sub-genres/{sub-genre}/{metric}/rubric.md`.

Before running: `research.md` must exist for the genre. If it doesn't, the skill will halt and guide you through building it first (Google Trends + Reddit research — no AI substitution).

### 4. Write game pages
Run `/write-game-page` with `game_name | genre | sub_genre | author`. The skill reads writing rules, author persona, genre rubrics, and keyword assignment — then produces a full publish-ready draft. Save to `campaigns/{campaign}/drafts/`.

### 5. Write ranked lists
Run `/write-ranked-list` once enough game page drafts exist for the campaign. The skill pulls scores and metadata from the drafts and produces a ranked list with intro, entries, and FAQs.

---

## Skills Reference

Skills live in `.claude/skills/`. Each skill has three files:
- `readme.md` — full execution instructions Claude follows
- `interface.py` — collects inputs and prints the structured prompt block
- `connector.json` — declares which knowledge files the skill must read before starting

| Skill | Trigger | What it does |
|---|---|---|
| keyword-strategy | `/keyword-strategy` | Produces Tier 2 + Tier 3 keyword assignments for a campaign |
| scoring-system | `python .claude/skills/scoring-system/interface.py` | Generates metrics and rubrics for a genre/sub-genre |
| write-game-page | `/write-game-page` | Writes a complete game page with scores, FAQs, and meta |
| write-ranked-list | `/write-ranked-list` | Writes a ranked list from existing game page drafts |

---

## Scoring System

Every game is scored on exactly 5 metrics. Metrics are specific to the genre and sub-genre — a racing game is not scored on the same things as an RPG.

**Three levels of specificity:**

1. **Genre** — top-level category (Racing, Fighting, RPG, Sports, Shooters)
2. **Sub-genre** — named variant within a genre (e.g. FPS within Shooters, Football within Sports). Not every game requires one.
3. **Niche** — context modifier: **Multiplayer** or **Free**. Can apply at genre or sub-genre level.

Metrics live as `rubric.md` files inside their sub-genre or niche folder. A rubric defines what scores 1–5 mean in concrete, measurable terms for that specific context. The same rubric is applied to every game scored against it — that's what makes scores comparable within a ranked list.

See `scoring-system/overview.md` for the full structural reference.

---

## For AI Reading This

Before any content task, read:
- `writing/eeat.md` — the 7-phase publishing lifecycle every page follows
- `writing/Writing-style.md` — prose rules that override default writing behaviour
- `company/overview.md` — what Metric Gamer is and who it's for
- `company/persona/persona.md` — who the reader is

Before any scoring or research task, read:
- `scoring-system/overview.md` — structural rules for metrics, rubrics, and genres

Connector files (`connector.json`) in each skill declare exactly which files to load and in what priority order. Always read the connector before starting a skill.

Research for genre metrics comes from `scoring-system/genres/{genre}/research.md` — built from real Reddit threads and Google Trends data, not AI inference. Do not substitute your own web search for a missing research file.
