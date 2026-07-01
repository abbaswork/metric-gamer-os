# Skill: Write Game Page

## Purpose

Given a game name, genre, and assigned author, produce a complete, publish-ready game page for Metric Gamer. The page covers every section: SEO meta, introduction, metric descriptions with scores, pros and cons, verdict, FAQs, and game details card. All copy follows the EEAT lifecycle and the Metric Gamer Writing Style Guide. Fact-checking via live web research is mandatory before writing begins.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Writing Style Guide | writing/Writing-style.md | 5 |
| EEAT Framework | writing/eeat.md | 4 |
| Site User Personas | company/persona/persona.md | 3 |
| FAQ Templates | company/site/faq-templates.md | 3 |
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

## Requirements

- **[Hard]** Fact-checking (Phase 3) completes before any drafting begins — release dates, developer/publisher, platforms, and playtime are verified, never assumed.
- **[Hard]** Keyword & SERP research (Phase 2) completes before drafting — keywords are identified first, never retrofitted into a finished draft.
- **[Hard]** Every named game element used in a metric description (level, weapon, enemy, update) is verified against a live source before being cited.
- **[Soft]** The assigned author's persona voice governs phrasing choices — relaxable only where the author persona file itself defines an exception.

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
Phase 2 — Claude          Keyword & SERP research: primary keyword, secondary keywords, search intent, competitor gaps, FAQ seeds
     ↓
Phase 3 — Claude          Fact-check research: Wikipedia, HowLongToBeat, platform pages
     ↓
Phase 4 — Claude          Discovery Q&A — surface conflicting or thin facts (release
                          dates, platform list, sub-genre fit, named content used in
                          metric descriptions) as direct questions. Halt until
                          answered or explicitly waived.
     ↓
Phase 5 — Claude          Draft full game page with keywords integrated naturally
     ↓
Phase 6 — Claude          Validate against acceptance criteria; update tags indexes if needed
     ↓
Phase 7 — Claude          If game is on Steam: write Steam curator review (conditional)
```

Do not begin drafting until Phases 2 through 4 are complete. Keywords must be identified before writing begins — they cannot be integrated naturally if they are retrofitted after the draft is done.

---

## Interface Script

`interface.py` — collects `game_name`, `genre`, `sub_genre`, and `author`, then prints the structured input block for Claude.

---

## Web Search Strategy

All research runs via Claude web search. Three distinct search jobs run at different points.

### Blocked domains — review opinions only

The following sites are blocked as sources for review opinions, scores, verdicts, player voice, and analysis. They may be used for factual information only (release dates, developer/publisher, platform lists, feature confirmation, patch notes) when no better source is available.

```
ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net,
polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com,
trustedreviews.com, thegamer.com, screenrant.com, cbr.com
```

Prefer Wikipedia, official developer/publisher sites, and community sources (Reddit, Steam, GTPlanet, etc.) even for factual lookups. Fall back to the above sites only when they are the clearest available source for a specific fact.

---

### Phase 2 — Keyword & SERP research (run before fact-checking)

The goal here is to identify the primary keyword, secondary keywords, search intent, and what existing pages are missing. Keywords must be known before writing begins.

**Batch 1 — SERP landscape (2 searches)**

- `{game_name}` — see what ranks in the top 5, what angle they take, what sections they include
- `{game_name} review` — identify search intent type and competitor structure

**Batch 2 — Long-tail and intent signals (2 searches)**

- `is {game_name} worth playing` — captures the transactional intent query players actually search
- `{game_name} {genre}` — secondary keyword signal and niche long-tail opportunities

**Batch 2.5 — Sub-genre research FAQ extraction (optional, skip if not available)**

Check for `scoring-system/genres/{genre}/sub-genres/{sub_genre}/research.md` (or `scoring-system/genres/{genre}/research.md` if no sub-genre file exists). If found, scan its Google Trends Queries and Reddit Important Factors sections for anything question-shaped or that implies a question a player would ask — player count, crossplay, tier list, patch notes, mods, meta, multiplayer, length, and similar. Add matches to the FAQ seeds list below alongside the universal templates in `faq-templates.md`. If no `research.md` exists for this genre/sub-genre, or nothing in it is FAQ-relevant, skip this step and move on — it never blocks the draft.

**Extract and record before continuing:**

```
Primary keyword: [usually the game name, sometimes "{game_name} review"]
Secondary keywords: [phrases appearing across top results — platform names, notable features, comparisons]
Search intent: [informational / transactional / hybrid — one sentence on what the player is looking for]
Competitor gaps: [what top-ranking pages don't cover that our metric breakdown uniquely addresses]
FAQ seeds: [People Also Ask questions and community questions, plus any Batch 2.5 research.md candidates]
```

This output stays in context only. It is not a published section of the page. Use it to guide where secondary keywords are placed naturally in the intro, metric descriptions, and FAQs.

---

### Phase 3 — Fact-check searches (run before drafting)

The goal here is accuracy, not player voice. Use encyclopaedic and official sources.

**Batch 3 — Core game facts (3 searches)**

- `{game_name} site:en.wikipedia.org` — release dates per platform, developer, publisher, genre, series
- `{game_name} howlongtobeat` — playtime ranges (main story, completionist)
- `{game_name} all platforms PC PS4 PS5 Xbox Switch release dates` — confirm full platform list and per-platform dates

**Batch 4 — Content details for metric descriptions (2 searches)**

Only run these if the metric descriptions will reference named content (levels, weapons, enemies, updates). Verify names before using them.

- `{game_name} wiki levels weapons enemies list` — confirm specific names before citing them
- `{game_name} patch notes update list` — if recent updates are relevant to a metric

---

### Phase 4 — Player voice for metric descriptions (run during drafting)

The goal here is raw player reaction to specific metrics — what they praised and what they complained about. Use community sources.

**Batch 5 — Community reaction (3 searches)**

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

- **Para 1** — The game's reputation and what it's known for. Lead with how the community or genre positions the game, then back it up with key numbers: series position, release era, car/track/content count, approximate playtime scale, platform. Do not include developer and publisher here — they are in the Game Details Card. The paragraph should be keyword-rich but read naturally, not like a press release.

- **Para 2** — Reader framing, not a verdict. Tell the reader what the page covers and why it's useful to them. Do not summarise the game's strengths and weaknesses or pre-answer whether it's worth playing — that is the Verdict's job. A paragraph that delivers conclusions before the metrics makes the rest of the page redundant. Close by pointing the reader forward into the metric breakdown.

Do not mention the scoring system or link to the about page.

See `writing/Writing-style.md` for the reference example (Gran Turismo 4).

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

### 8. Who Is This Game For?

Two parts. Who should play it and who should skip it. 2–3 specific reasons each, tied directly to the game's scored metrics and verified features. Do not repeat content already covered in the Pros/Cons or Verdict. Second person throughout.

Format:
**Play this if** you [specific reason tied to a strength]
**Skip this if** you [specific reason tied to a weakness or gap]

### 9. Verdict

Two to three sentences. Overall experience summary and a clear recommendation. "One of the" is acceptable. No stronger superlatives.

### 10. FAQs

Use the relevant FAQ templates from `company/site/faq-templates.md`. Select universal questions plus any conditional categories that apply to this game. Second person, max 3 sentences per answer, lead with "no" in the first sentence where the answer is negative.

### 11. Tags

Include all applicable tags: developer, publisher, platforms, players (local/online), playtime range. After writing the page, check each tag index file and add any new entries that do not already appear.

### 12. Steam Curator Review (conditional — only if the game is available on Steam)

Confirmed during Phase 3 when the platform list is verified. If Steam is not in the platform list, skip this section entirely.

Use the following template. Pull scores directly from the scored metrics above. The Good and The Bad must be tied to specific high and low scoring metrics respectively — not generic praise or criticism.

```
[Metric 1] [Score] | [Metric 2] [Score] | [Metric 3] [Score] | [Metric 4] [Score] | [Metric 5] [Score]

[Overall Score] / 5 — [One sentence verdict]

The Good: [Specific positive tied to a high-scoring metric or standout feature]
The Bad: [Specific negative tied to a low-scoring metric]

[CTA — rotate from approved list, do not use the same one twice in a row]
```

**Approved CTAs (rotate between these — do not repeat the same one on consecutive reviews):**
- `Full breakdown at metricgamer.com`
- `See the full scored breakdown at metricgamer.com`
- `Find out if it's worth your time at metricgamer.com`
- `More scored breakdowns on our curator page`

**Rules:**
- Total review text must fit within 500 characters
- No em dashes anywhere in the review
- The verdict line must be one sentence only
- The Good and The Bad must each be one sentence, specific to this game — not genre generalisations
- Do not explain what Metric Gamer is inside the review text — the CTA handles that

---

## Acceptance Criteria

These apply at the **start** (to guide execution) and at the **end** (to validate before submitting).

### Fact-checking
- [ ] Release date(s) verified against a live source — per platform if staggered
- [ ] Developer and publisher verified as separate entities against a live source
- [ ] Full platform list verified
- [ ] All named levels, weapons, enemies, or updates cited in metric descriptions verified by name against a live source
- [ ] Playtime range sourced from HowLongToBeat or equivalent
- [ ] Discovery Q&A phase run — conflicting or thin facts and sub-genre fit surfaced as questions and resolved before drafting begins

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
- [ ] Para 1 leads with the game's reputation or community positioning, backed by key numbers (series position, release era, content count, playtime scale, platform) — no developer or publisher in the intro body
- [ ] Para 2 frames what the page covers and why it's useful — does not pre-answer whether the game is worth playing
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
- [ ] "Who Is This Game For?" section is present with both Play this if and Skip this if parts
- [ ] "Who Is This Game For?" reasons are game-specific and do not repeat content from Pros/Cons or Verdict
- [ ] Verdict is 2-3 sentences and ends with a clear recommendation
- [ ] Verdict does not use stronger superlatives than "one of the"
- [ ] FAQs are present, written in second person, max 3 sentences per answer
- [ ] Game details card includes developer, publisher, release date(s), platforms, playtime, and player modes

### Tags
- [ ] All applicable tags are included in the game details card
- [ ] Any new developer, publisher, platform, or player mode not previously in the tag index files has been added to the relevant index

### Steam Curator Review (conditional)
- [ ] Confirmed whether game is available on Steam during Phase 3 platform verification
- [ ] If on Steam: review written and included in the draft under section 12
- [ ] Review fits within 500 characters
- [ ] The Good ties to a high-scoring metric with game-specific detail
- [ ] The Bad ties to a low-scoring metric with game-specific detail
- [ ] CTA selected from the approved list
- [ ] No em dashes in the review text
- [ ] If not on Steam: section 12 marked as not applicable
