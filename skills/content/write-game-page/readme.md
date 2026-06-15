# Skill: Write Game Page

## Purpose

Given a game name, genre, and assigned author, produce a complete, publish-ready game page for Metric Gamer. The page covers every section: SEO meta, introduction, metric descriptions with scores, pros and cons, verdict, FAQs, and game details card. All copy follows the EEAT lifecycle and the Metric Gamer Writing Style Guide. Fact-checking via live web research is mandatory before writing begins.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Writing Style Guide | writing/Writing-style.md | 5 |
| EEAT Framework | writing/eeat.md | 4 |
| Site User Personas | knoweldge/persona/persona.md | 3 |
| FAQ Templates | knoweldge/site/faq-templates.md | 3 |
| Scoring System Overview | scoring-system/overview.md | 2 |

Additionally, load the author persona file that corresponds to the `author` input:

| Author input | File |
|---|---|
| ABossProductions | writing/author-personas/abossgaming.md |
| Metric Gamer | writing/author-personas/metric-gamer.md |
| Lobotomy_gaming | writing/author-personas/lobotomy-gaming.md |
| 8-Bit Bandit | writing/author-personas/8-bit-bandit.md |

The author persona file is a required dynamic connector. Load it alongside the connector.json sources before writing.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `game_name` | string | Yes | Full title of the game exactly as it appears on the platform storefront |
| `genre` | string | Yes | Primary genre — used to select the correct metric set and rubrics |
| `sub_genre` | string | No | Sub-genre context if applicable (e.g. Shooter — Multiplayer, Racing — Split Screen). Adds sub-genre metrics where they exist. |
| `author` | enum | Yes | The Metric Gamer author writing this page: ABossProductions, Metric Gamer, Lobotomy_gaming, or 8-Bit Bandit |

---

## Execution Flow

```
Phase 1 — interface.py    Collect game_name, genre, sub_genre, author
     ↓
Phase 2 — Claude          Fact-check research: Wikipedia, HowLongToBeat, platform pages
     ↓
Phase 3 — Claude          Draft full game page following EEAT lifecycle and Writing-style.md
     ↓
Phase 4 — Claude          Validate against acceptance criteria; update tags indexes if needed
```

Do not begin drafting until Phase 2 is complete. Factual errors in the draft are harder to fix than missing copy.

---

## Interface Script

`interface.py` — collects `game_name`, `genre`, `sub_genre`, and `author`, then prints the structured input block for Claude.

---

## Web Search Strategy

All research runs via Claude web search. Two distinct search jobs run at different points.

### Blocked domains (apply to every search)

```
ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net,
polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com,
trustedreviews.com, thegamer.com, screenrant.com, cbr.com
```

---

### Phase 2 — Fact-check searches (run before drafting)

The goal here is accuracy, not player voice. Use encyclopaedic and official sources.

**Batch 1 — Core game facts (3 searches)**

- `{game_name} site:en.wikipedia.org` — release dates per platform, developer, publisher, genre, series
- `{game_name} howlongtobeat` — playtime ranges (main story, completionist)
- `{game_name} all platforms PC PS4 PS5 Xbox Switch release dates` — confirm full platform list and per-platform dates

**Batch 2 — Content details for metric descriptions (2 searches)**

Only run these if the metric descriptions will reference named content (levels, weapons, enemies, updates). Verify names before using them.

- `{game_name} wiki levels weapons enemies list` — confirm specific names before citing them
- `{game_name} patch notes update list` — if recent updates are relevant to a metric

---

### Phase 3 — Player voice for metric descriptions (run during drafting)

The goal here is raw player reaction to specific metrics — what they praised and what they complained about. Use community sources.

**Batch 3 — Community reaction (3 searches)**

- `reddit "{game_name}" {metric_name} what do you think`
- `reddit "{game_name}" best part worst part`
- `steam "{game_name}" reviews {metric_name}`

Pull **verbatim player quotes** where possible. Do not paraphrase. Each metric description must reference something specific to this game — a named level, mechanic, weapon, enemy, or update — not a generic description that could apply to the whole genre.

### What to skip

- Any result from the blocked domain list
- Press releases, launch announcements, or developer interviews
- Review aggregators
- Lists and listicle pages

---

## Page Structure

Produce all sections in this order. Every section is required.

### 1. SEO Meta

- **Meta Title** — emotive or question format, ends with ` | Metric Gamer`, under 60 characters
- **Meta Description** — primary keyword integrated naturally, frames a tension or question, closes with a CTA, under 155 characters
- **URL Slug** — `/games/{game-name-kebab-case}/`
- **Last Updated** — today's date

### 2. Reviewer Attribution

One line: `Reviewed by {author} — {one sentence on their relevant expertise for this game}.`

Draw the expertise line from the author persona file.

### 3. Game Details Card

| Field | Source |
|---|---|
| Developer | Verified in Phase 2 |
| Publisher | Verified in Phase 2 — separate field from developer |
| Release Date(s) | Per platform if staggered |
| Platforms | Full list verified in Phase 2 |
| Playtime | From HowLongToBeat |
| Players | Single Player / Local Co-op / Online Multiplayer — all modes that exist |

### 4. Introduction

Two paragraphs only.

- **Para 1** — Factual. Developer, publisher, year, platforms, genre, series context if applicable.
- **Para 2** — Experiential. How the game feels to play. Author's voice. Sets up the core tension or loop the metrics will expand on.

Do not mention the scoring system or link to the about page.

### 5. Metric Descriptions

One paragraph per metric. Select metrics from the correct genre rubric file. If a sub-genre was provided, include sub-genre metrics where they exist.

Each paragraph follows the structure from Writing-style.md:
1. Opening judgment
2. Specific evidence (game-named)
3. Honest negative with "Unfortunately", "Unfortunately, however", or some similar phrase — only if the score warrants it
4. Practical close

Never explain the score.

### 6. Overall Score

Display the genre overall score (average of metric scores, rounded to one decimal place).

### 7. Pros and Cons

Bullet lists. Must surface things not already covered by the metric descriptions. One sentence per bullet.

### 8. Verdict

Two to three sentences. Overall experience summary and a clear recommendation. "One of the" is acceptable. No stronger superlatives.

### 9. FAQs

Use the relevant FAQ templates from `knoweldge/site/faq-templates.md`. Select universal questions plus any conditional categories that apply to this game. Second person, max 3 sentences per answer, lead with "no" in the first sentence where the answer is negative.

### 10. Tags

Include all applicable tags: developer, publisher, platforms, players (local/online), playtime range. After writing the page, check each tag index file and add any new entries that do not already appear.

---

## Acceptance Criteria

These apply at the **start** (to guide execution) and at the **end** (to validate before submitting).

### Fact-checking
- [ ] Release date(s) verified against a live source — per platform if staggered
- [ ] Developer and publisher verified as separate entities against a live source
- [ ] Full platform list verified
- [ ] All named levels, weapons, enemies, or updates cited in metric descriptions verified by name against a live source
- [ ] Playtime range sourced from HowLongToBeat or equivalent

### SEO Meta
- [ ] Meta title ends with ` | Metric Gamer`
- [ ] Meta title uses emotive or question-format language
- [ ] Meta title is under 60 characters
- [ ] Meta description integrates the primary keyword inside a natural sentence
- [ ] Meta description frames a tension or question the reader genuinely has
- [ ] Meta description closes with a CTA ("Read to find out", "We scored every metric to find out", etc.)
- [ ] Meta description is under 155 characters

### Introduction
- [ ] Introduction is exactly two paragraphs
- [ ] Para 1 is factual (developer, publisher, year, platforms, genre, series context)
- [ ] Para 2 is experiential and sets up the author's voice
- [ ] No reference to the scoring system or methodology inside the introduction

### Metric Descriptions
- [ ] Metrics are drawn from the correct genre rubric (and sub-genre if applicable)
- [ ] Each metric description is a single merged paragraph — no split between description and player experience
- [ ] Each paragraph opens with a direct judgment, not a definition of the metric
- [ ] Every named game element (level, weapon, mechanic, enemy, update) cited is verified correct
- [ ] "Unfortunately", "Unfortunately, however", or a similar phrase is used where a score warrants it, and not used where it does not
- [ ] No metric description explains the score

### Writing Style
- [ ] No em dashes anywhere in the copy
- [ ] No lists of three ("X, Y, and Z" patterns)
- [ ] No repeated comma-and chain connectors across paragraphs
- [ ] Contractions used throughout — "you'll", "it's", "you're", "haven't", "doesn't"
- [ ] "For example" uses a comma — not a semicolon or colon
- [ ] "For example" is not used in every metric paragraph — approach is varied
- [ ] No score justification language ("which is what keeps this at a 4", "this is why it scored a 3")
- [ ] No corporate qualifiers: "consistently", "genuinely", "meaningfully", "substantially"
- [ ] Author voice matches the assigned author persona — vocabulary, what they notice, how they close

### Structure
- [ ] Pros and cons are bullet points and do not repeat content from the metric descriptions
- [ ] Verdict is 2-3 sentences and ends with a clear recommendation
- [ ] Verdict does not use stronger superlatives than "one of the"
- [ ] FAQs are present, written in second person, max 3 sentences per answer
- [ ] Game details card includes developer, publisher, release date(s), platforms, playtime, and player modes

### Tags
- [ ] All applicable tags are included in the game details card
- [ ] Any new developer, publisher, platform, or player mode not previously in the tag index files has been added to the relevant index
