# Skill: Write Game Page

Write a complete, publish-ready game page for Metric Gamer following the EEAT lifecycle and Writing Style Guide.

## Inputs

Parse the following from `$ARGUMENTS` if provided (format: `game_name | genre | sub_genre | author`). If any required field is missing, ask the user before proceeding.

| Input | Required | Notes |
|---|---|---|
| `game_name` | Yes | Full title exactly as it appears on the storefront |
| `genre` | Yes | e.g. Racing, Fighting, RPG, Shooter |
| `sub_genre` | No | e.g. Racing — Split Screen. Leave blank if not applicable |
| `author` | Yes | One of: ABossProductions, Metric Gamer, Lobotomy_gaming, 8-Bit Bandit |

---

## Step 1 — Load Knowledge Connectors

Before doing anything else, read all of the following files:

- `writing/Writing-style.md` — primary output standard; every paragraph must conform before submission
- `writing/eeat.md` — publishing lifecycle; defines phases 1–7
- `company/persona/persona.md` — site user personas; keep the reader audience-aware throughout
- `company/site/faq-templates.md` — FAQ question pool and format rules
- `scoring-system/overview.md` — scoring background; informs metric set selection and rubric interpretation

Then read the author persona file based on the `author` input:

| Author | File |
|---|---|
| ABossProductions | `writing/author-personas/abossgaming.md` |
| Metric Gamer | `writing/author-personas/metric-gamer.md` |
| Lobotomy_gaming | `writing/author-personas/lobotomy-gaming.md` |
| 8-Bit Bandit | `writing/author-personas/8-bit-bandit.md` |

Then read the genre metric set and all rubric files for the given genre:

| Genre | Metrics file | Rubric folder |
|---|---|---|
| Racing | `scoring-system/genres/racing/metrics.md` | `scoring-system/genres/racing/` |
| Fighting | `scoring-system/genres/fighting/metrics.md` | `scoring-system/genres/fighting/` |
| Shooter | `scoring-system/genres/shooters/metrics.md` | `scoring-system/genres/shooters/` |

If a `sub_genre` was provided, also read the relevant niche rubric files under `scoring-system/genres/{genre}/niches/{sub_genre}/`.

Do not proceed to Step 2 until all files above are read.

---

## Step 2 — Keyword & SERP Research (Phase 2)

Run before fact-checking and before drafting. Keywords must be identified first — they cannot be integrated naturally if retrofitted after the draft is done.

**Blocked domains — review opinions only:**
`ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net, polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com, trustedreviews.com, thegamer.com, screenrant.com, cbr.com`

These sites are blocked as sources for review opinions, scores, verdicts, and player voice. They may be used for factual information only (release dates, developer, platform list, feature confirmation) when no better source is available. Prefer Wikipedia, official sites, and community sources first.

**Batch 1 — SERP landscape (2 searches):**
1. `{game_name}` — what ranks top 5, what angle they take, what sections they include
2. `{game_name} review` — search intent type and competitor structure

**Batch 2 — Long-tail and intent signals (2 searches):**
1. `is {game_name} worth playing` — transactional intent query players actually search
2. `{game_name} {genre}` — secondary keyword signal and long-tail opportunities

**Batch 2.5 — Sub-genre research FAQ extraction (optional, skip if not available):**
Check for `scoring-system/genres/{genre}/sub-genres/{sub_genre}/research.md` (or `scoring-system/genres/{genre}/research.md` if no sub-genre file exists). If found, scan its Google Trends Queries and Reddit Important Factors sections for anything question-shaped or that implies a question a player would ask — player count, crossplay, tier list, patch notes, mods, meta, multiplayer, length, and similar. Add matches to the FAQ seeds list below alongside the universal templates in `faq-templates.md`. If no `research.md` exists for this genre/sub-genre, or nothing in it is FAQ-relevant, skip this step and move on — it never blocks the draft.

**Record before continuing (context only — not published):**
```
Primary keyword: [game name or "{game_name} review"]
Secondary keywords: [phrases from top results — platform, features, comparisons]
Search intent: [informational / transactional / hybrid — one sentence]
Competitor gaps: [what top pages miss that the metric breakdown uniquely covers]
FAQ seeds: [People Also Ask and community questions, plus any Batch 2.5 research.md candidates]
```

---

## Step 3 — Fact-Check Research (Phase 3)

Run web searches before drafting any copy. Do not skip this phase.

**Batch 3 — Core facts (run all 3):**
1. `{game_name} site:en.wikipedia.org` — release dates per platform, developer, publisher, genre, series
2. `{game_name} howlongtobeat` — playtime ranges (main story, completionist)
3. `{game_name} all platforms release dates` — confirm full platform list and per-platform dates

**Batch 4 — Content details (run only if metric descriptions will cite named content):**
1. `{game_name} wiki levels tracks cars list` — confirm specific names before using them
2. `{game_name} patch notes update list` — if recent updates are relevant to a metric

Do not begin drafting until Steps 2 through 4 are complete.

---

## Step 4 — Discovery Q&A (Phase 4)

Before drafting, surface any close call from Steps 2–3 as a direct question rather than assuming silently:
- Sources disagree on a release date, developer/publisher, or platform list — state the conflict and ask which to use, or which source takes precedence.
- The sub-genre's relevance to this specific game is unclear — ask whether to apply sub-genre metrics or the genre baseline.
- A named element needed for a metric description (a level, weapon, or update) couldn't be verified — ask whether to omit it or use a more general description instead.

State the assumption you would otherwise make alongside each question. Do not begin drafting until the user answers or explicitly says to use your judgement.

---

## Step 5 — Score Each Metric (Phase 5)

Run before drafting. Every metric must have a confirmed score before any copy is written.

For each metric in the game's rubric set, run the following player voice searches:

1. `reddit "{game_name}" {metric_name} what do you think`
2. `reddit "{game_name}" best part worst part`
3. `steam "{game_name}" reviews {metric_name}`

Pull verbatim player quotes where possible.

**Scoring process:**
Read the rubric Description column for the metric. Work top-down from band 5:
- Does the community's experience match this description?
- If yes — assign that score with the supporting evidence
- If no — move to band 4 and repeat
- Continue until you find the highest band the game fully satisfies

**Tiebreaker rule:** if the game sits between two bands, assign the upper band only if the gap is minor and does not affect the core of what that band describes. Otherwise assign the lower band.

Once all metrics are scored, present a scored summary to the user before proceeding:

```
{Metric}: {Score} — {one line of key evidence}
{Metric}: {Score} — {one line of key evidence}
Overall: {average rounded to one decimal}
```

Wait for the user to confirm or push back on any score. Do not begin drafting until all scores are confirmed.

---

## Step 6 — Draft the Full Game Page (Phase 6)

Draft from the confirmed scores. Each metric description explains how the game earned its score — it does not arrive at the score mid-paragraph or re-evaluate during writing. Each metric description must reference something specific — a named track, mechanic, car, update — not generic genre description.

Produce all sections in this order. Every section is required.

### 1. SEO Meta
- **Meta Title** — emotive or question format, ends with ` | Metric Gamer`, under 60 characters
- **Meta Description** — primary keyword integrated naturally, frames a tension or question, closes with a CTA, under 155 characters
- **URL Slug** — `/games/{game-name-kebab-case}/`
- **Last Updated** — today's date

### 2. Reviewer Attribution
`Reviewed by {author} — {one sentence on their relevant expertise for this game}.`
Draw the expertise line from the author persona file.

### 3. Game Details Card
| Field | Source |
|---|---|
| Developer | Verified in Phase 3 |
| Publisher | Verified in Phase 3 — separate field |
| Release Date(s) | Per platform if staggered |
| Platforms | Full list verified in Phase 3 |
| Playtime | From HowLongToBeat |
| Players | All modes that exist (Single / Local Co-op / Online) |

### 4. Introduction
Two paragraphs only.
- **Para 1** — The game's reputation and what it's known for. Lead with how the community or genre positions the game, then back it up with key numbers: series position, release era, content count, approximate playtime scale, platform. Do not include developer and publisher — they are in the Game Details Card already.
- **Para 2** — Reader framing, not a verdict. Tell the reader what the page covers and why it's useful. Do not summarise strengths and weaknesses or pre-answer whether the game is worth playing — that is the Verdict's job. Close by pointing the reader into the metric breakdown.

Do not mention the scoring system or link to the about page.

### 5. Metric Descriptions
One paragraph per metric. Select from the correct genre rubric. If a sub-genre was provided, include sub-genre metrics where they exist.

Each paragraph structure:
1. Opening judgment
2. Specific named evidence (track, car, mechanic, update)
3. Honest negative with "Unfortunately" or similar — only if the score warrants it
4. Practical close

Never explain the score.

### 6. Overall Score
Average of metric scores, rounded to one decimal place.

### 7. Pros and Cons
Bullet lists. Must surface things not already covered by the metric descriptions. One sentence per bullet.

### 8. Who Is This Game For?
Two parts. Who should play it and who should skip it. 2–3 specific reasons each, tied directly to the game's scored metrics and verified features — not genre generalisations. Do not repeat content already in the Pros/Cons or Verdict. Second person throughout.

Format:
**Play this if** you [specific reason tied to a strength]
**Skip this if** you [specific reason tied to a weakness or gap]

### 9. Verdict
2–3 sentences. Overall experience summary and a clear recommendation. "One of the" is acceptable. No stronger superlatives.

### 10. FAQs
Use templates from `company/site/faq-templates.md`. Universal questions plus any conditional categories that apply. Second person, max 3 sentences per answer, lead with "no" where the answer is negative.

### 11. Tags
All applicable tags: developer, publisher, platforms, players, playtime range. After writing the page, check each tag index file and add any new entries not already present.

### 12. Steam Curator Review (conditional)
Only write this if the game is available on Steam — confirmed during Step 3 when the platform list is verified. If not on Steam, mark as not applicable.

```
[Metric 1] [Score] | [Metric 2] [Score] | [Metric 3] [Score] | [Metric 4] [Score] | [Metric 5] [Score]

[Overall Score] / 5 — [One sentence verdict]

The Good: [Specific positive tied to a high-scoring metric]
The Bad: [Specific negative tied to a low-scoring metric]

[CTA]
```

Approved CTAs — rotate between these, do not use the same one on consecutive reviews:
- `Full breakdown at metricgamer.com`
- `See the full scored breakdown at metricgamer.com`
- `Find out if it's worth your time at metricgamer.com`
- `More scored breakdowns on our curator page`

Rules: 500 character limit total. No em dashes. The Good and The Bad must be game-specific, not genre generalisations.

---

## Step 7 — Validate (Phase 7)

Before submitting, verify every item below is met.

### Scoring
- [ ] All metrics scored against the rubric Description column before drafting began
- [ ] Each score supported by verbatim player quotes or named game-specific evidence
- [ ] Tiebreaker rule applied where a game sat between two bands
- [ ] Scored summary presented to user and confirmed before drafting began

### Fact-checking
- [ ] Release date(s) verified per platform against a live source
- [ ] Developer and publisher verified as separate entities
- [ ] Full platform list verified
- [ ] All named elements cited in metric descriptions verified correct
- [ ] Playtime sourced from HowLongToBeat or equivalent

### SEO Meta
- [ ] Meta title ends with ` | Metric Gamer`
- [ ] Meta title uses emotive or question-format language
- [ ] Meta title is under 60 characters
- [ ] Meta description integrates primary keyword naturally
- [ ] Meta description frames a tension or question
- [ ] Meta description closes with a CTA
- [ ] Meta description is under 155 characters

### Introduction
- [ ] Exactly two paragraphs
- [ ] Para 1 leads with the game's reputation or community positioning, backed by key numbers — no developer or publisher in the intro body
- [ ] Para 2 frames what the page covers and why it's useful — does not pre-answer whether the game is worth playing
- [ ] No reference to the scoring system

### Metric Descriptions
- [ ] Metrics drawn from the correct genre rubric
- [ ] Single merged paragraph per metric — no split
- [ ] Opens with a direct judgment, not a definition
- [ ] All named game elements verified correct
- [ ] "Unfortunately" used where score warrants it, absent where it doesn't
- [ ] No metric explains the score

### Writing Style
- [ ] No em dashes anywhere in the copy
- [ ] No lists of three ("X, Y, and Z" patterns)
- [ ] No repeated comma-and chain connectors across paragraphs
- [ ] Contractions used throughout
- [ ] "For example" uses a comma — not a semicolon or colon
- [ ] "For example" not used in every metric paragraph
- [ ] No score justification language
- [ ] No corporate qualifiers: "consistently", "genuinely", "meaningfully", "substantially"
- [ ] Author voice matches the assigned author persona

### Structure
- [ ] Pros and cons don't repeat metric description content
- [ ] "Who Is This Game For?" section present with both Play this if and Skip this if parts
- [ ] "Who Is This Game For?" reasons are game-specific — not genre generalisations — and don't repeat Pros/Cons or Verdict content
- [ ] Verdict is 2–3 sentences with a clear recommendation
- [ ] Verdict uses no superlatives stronger than "one of the"
- [ ] FAQs present, second person, max 3 sentences each
- [ ] Game details card is complete with all fields

### Tags
- [ ] All applicable tags included
- [ ] Tag index files updated with any new entries not already present

### Steam Curator Review (conditional)
- [ ] Confirmed whether game is on Steam during Step 3 platform verification
- [ ] If on Steam: review written in section 12 of the draft, within 500 characters, The Good and The Bad are game-specific, CTA from approved list, no em dashes
- [ ] If not on Steam: section 12 marked as not applicable
