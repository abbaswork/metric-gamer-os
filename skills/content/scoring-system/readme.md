# Skill: Generate Metrics & Rubrics

## Purpose

Given a genre and optional sub-genre, research and produce a set of player-validated metrics with scoring rubrics. Each metric represents a crucial, measurable dimension of quality for games in that context. Each rubric defines what scores 1–5 mean in concrete terms, grounded in community consensus — not editorial opinion.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Research | research/*.md | 5 |
| User Personas | knowledge/persona/persona.md | 3 |
| Scoring System Overview | scoring-system/overview.md | 4 |
| Company Overview | knowledge/company/overview.md | 3 |

Research is weighted highest (5) — the manually curated `research/{genre}/readme.md` file, where one exists, is the most direct evidence of what real players care about and takes priority over live web search. Personas (3) keep outputs grounded in who is reading the score. The scoring system overview (4) defines the structural contract the output must conform to: what a metric is, what a rubric is, how genres and sub-genres relate. Company overview (3) keeps outputs aligned with the gamer-first methodology.

---

## Requirements

- **[Hard]** Every page is still scored on exactly 5 metrics. By default a genre defines one fixed set of 5 (the simple model). A genre may instead define a **metric pool of up to 10** when the research shows contexts too different to share one 5 (e.g. a campaign mode and a large-scale multiplayer mode) — see "Choosing simple vs. pool model" in the Research Strategy section. Whichever model is used, never propose more than 10 in a pool or more than 5 in a fixed set.
- **[Hard]** `research/{genre}/readme.md` must exist before metric generation proceeds. If it's missing, Claude does not substitute its own web search as the primary source — it halts and guides the user through building the file (Google Trends + Reddit research on genre-defining games), per "No research file found" in the Research Strategy section below.
- **[Hard]** Every metric has a stated direction (Delight or Complaint) with a rubric that can be applied consistently across every game — a theme with no rubric-able threshold cannot become a metric.
- **[Soft]** A sub-genre reuses a parent-genre metric wherever the theme still applies, rather than introducing an unrelated new one — relaxable only if Discovery Q&A confirms the parent metric genuinely doesn't transfer to the sub-genre context.

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
Phase 2 — Claude          Check for research/{genre}/readme.md.
                          → Missing: HALT. Guide the user through building it
                            (see "No research file found" below). Do not
                            substitute Claude's own web search for this step.
                          → Present: read it in full. This is the primary
                            research source.
     ↓
Phase 3 — Claude          Run supplementary web searches only to fill gaps the
                          research file leaves uncovered → extract raw player quotes.
     ↓
Phase 4 — Claude          Discovery Q&A — group every factor and quote by theme,
                          surface the close calls (simple 5 vs. pool-of-up-to-10,
                          which themes win a slot, where a rubric threshold sits,
                          which metric a sub-genre swap should target) as direct
                          questions. Halt until the user answers or explicitly waives.
     ↓
Phase 5 — Claude          Generate metrics + rubrics incorporating the Discovery
                          answers. If using the pool model, also write at least
                          one suggested 5-metric profile per major context.
```

Run: `python interface.py` then pass the output to Claude with this skill prompt.

---

## Interface Script

`interface.py` — collects `genre` and `sub_genre` and prints the structured input block for Claude.

---

## Research Strategy

Research runs in two steps: read the manually curated research file first, then use web search only to fill what it doesn't cover. The research file exists because Claude has no reliable live access to Reddit (its API is blocked) or Google Trends — so that data has to be gathered by the user and handed over as a file, not re-fetched on every run.

### Step 1 — Research file (primary source)

Check for `research/{genre}/readme.md` (e.g. `research/shooters/readme.md`) before doing anything else. If it exists, read it in full and treat it as ground truth — it was built from real Reddit threads and real Google Trends data the user pulled manually.

Each section feeds a different part of the output:

| Section | Use it for |
|---|---|
| Reddit Important Factors | The primary theme list. Every factor listed here is a metric candidate — carry all of them into "Identifying metrics from research" below. None get dropped without being accounted for. |
| Google Trends Queries | Search-demand evidence. Breakout terms and high-interest queries confirm which themes matter enough to players to justify a metric slot — use them to break ties when more strong themes emerge than the model in use has room for. |
| Keywords Findings | Word-choice signal only (e.g. "review" outsearches "rating", numerals outsearch spelled-out numbers, avoid abbreviations). Apply this to how metric names and rubric copy are worded. These are not metric candidates. |
| Top Games in the category | Calibration anchors. When setting a rubric's score-5 or score-1 example, check it against at least one game from this list. |

#### No research file found

If `research/{genre}/readme.md` doesn't exist for this genre, **stop here.** Do not run Claude's own web search as a stand-in — Claude has no reliable live access to Reddit (its API is blocked) or Google Trends, so a Claude-led search is not an adequate substitute for what this file is supposed to contain. Tell the user the file is required and hand them this brief:

> I don't have a research file for {genre} yet (`research/{genre}/readme.md`). Before I can generate metrics, I need you to research this manually and hand it back to me:
>
> 1. **Google Trends** — pick 2–3 genre-defining games for {genre} (the ones every other game in the genre gets compared to). Look up their trending search queries and note the query, the search interest score, and whether it's rising/breakout or declining.
> 2. **Reddit** — for those same games, search what players say makes them great (and what ruins them). List the specific recurring factors, not generic genre talk — "squad play," "netcode," "weapon customization," that level of specificity.
> 3. **Top games in the category** — list the 4–6 games that best represent {genre} right now.
>
> Use `research/shooters/readme.md` as the template for structure (Keywords Findings, Google Trends Queries, Reddit Important Factors, Top Games in the category). Save it to `research/{genre}/readme.md` and I'll pick up from there.

Halt completely until the file is provided. Step 2's web search is for closing small gaps in an existing file — it is never a replacement for a missing one.

### Step 2 — Supplementary web search (gap-filling only)

Use web search only where the research file leaves a gap — a theme backed by a single source, a sub-genre the research file doesn't cover, or a theme that needs a sharper verbatim quote to ground a rubric threshold. Don't re-search themes the research file already establishes across multiple sources. This step assumes a research file already exists — it is not a fallback for a missing one.

#### Blocked domains (apply to every search)

```
ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net,
polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com,
trustedreviews.com, thegamer.com, screenrant.com, cbr.com
```

#### Search batches

Run only the batches needed to close a gap identified in Step 1 — not all four by default. Replace `{genre}` and `{sub_genre}` with the actual inputs.

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

This applies to Step 2 search results — research-file factors arrive already synthesized, so carry them forward as-is into the grouping step below rather than re-deriving quotes for them.

Pull **verbatim quotes** from players. Do not paraphrase. For each quote note:
- The platform (Reddit, Steam, GameFAQs, NeoGAF, etc.)
- Whether it is a pain point or a delight
- The specific dimension it refers to — this becomes a metric candidate

Themes that appear across multiple independent sources are metric candidates. A single mention is not enough — unless it corroborates a factor already listed in the research file, in which case it strengthens an existing candidate rather than standing alone.

### Identifying metrics from research

Pool every research-file factor and every search-derived quote together, then group by theme. Each recurring theme is a candidate metric. For each, determine its direction before writing the rubric:

- **Complaint metric** — players hate when this exists. Score 5 = least of this, score 1 = most of this. Example: grind in JRPGs → 5 = no meaningful grind, 1 = excessive grind required.
- **Delight metric** — players love when this exists. Score 5 = most of this, score 1 = absence of it. Example: replayability in open world RPGs → 5 = highly replayable, 1 = single playthrough.

#### Choosing simple vs. pool model

Default to the simple model — every genre is scored on exactly 5 metrics (see `scoring-system/overview.md`). When more than 5 strong themes emerge, first try merging overlapping themes into one metric (e.g. two factors describing the same underlying mechanic from different angles) before assuming more slots are needed.

Escalate to the pool model (up to 10) only when, after merging, the surviving themes genuinely split along a contextual line one set of 5 can't honestly cover — most commonly a single-player/campaign context versus a large-scale multiplayer context. This is a Discovery Q&A moment: state why a single 5 doesn't fit and ask the user to confirm before building a pool.

In either model: rank candidate themes by source corroboration and Google Trends confirmation. For the simple model, select the top 5 and list the rest under an **"Other Themes Considered"** note with one line on why each was cut. For the pool model, select up to 10 for the pool, write at least one suggested 5-metric profile per major context (see existing `scoring-system/metrics/genres/shooters/metrics.md` for the format), and still list anything that didn't make the pool under "Other Themes Considered." Every factor from the research file must appear either in the final metric set (or pool) or in this note — none are silently dropped.

### What to skip

- Any result that reads like editorial content, even if it quotes players
- Aggregator or listicle pages
- Results from the blocked domain list
- Quotes that express personal taste rather than a genre-wide concern

---

## Acceptance Criteria

These apply at the **start** (to guide research) and at the **end** (to validate before submitting).

### Research
- [ ] `research/{genre}/readme.md` confirmed to exist before generation proceeded — if it was missing, the user was guided through building it (per "No research file found") instead of Claude substituting its own web search
- [ ] If present, the research file was read in full before any web search
- [ ] Every Reddit Important Factor from the research file is accounted for — selected into the final metric set (or pool) or listed under "Other Themes Considered" with a reason
- [ ] Web search was used only to close a gap in an existing research file, and that gap is stated
- [ ] Metric names and rubric wording reflect the Keywords Findings phrasing signal (e.g. preferred terms, numerals vs. spelled-out numbers), where a research file provided one
- [ ] Discovery Q&A phase run — metric-slot competition, rubric thresholds, and sub-genre swap choices surfaced as questions and answered or explicitly waived before generation

### Metrics & Rubrics
- [ ] Simple model: exactly 5 metrics generated, no more no fewer. Pool model: no more than 10 generated, with at least one suggested 5-metric profile per major context documented in `metrics.md`
- [ ] If the pool model was used, the escalation was surfaced as a Discovery Q&A question and confirmed by the user — not assumed
- [ ] Every metric is backed by at least one verbatim player quote or research-file factor
- [ ] Every metric is specific enough to have a definable rubric — it can be measured or concretely described
- [ ] Each rubric covers all 5 score levels (1–5) with clear, distinct thresholds that do not overlap
- [ ] Each rubric level is written in **second person** ("you") — not a label or summary
- [ ] At least one rubric threshold (score 1 or 5) is checked against a game from "Top Games in the category", where a research file provided one
- [ ] Each metric includes a **"Why this matters"** note and a **"Sources"** section citing which platforms or research file the evidence came from
- [ ] No metric is peripheral — it applies to the majority of games in this genre/sub-genre
- [ ] The full set covers the core player experience without significant gaps or overlaps
- [ ] If a sub-genre was provided, at least one metric specifically reflects what makes it distinct from the parent genre
