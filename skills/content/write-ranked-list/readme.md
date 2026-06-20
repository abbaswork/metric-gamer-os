# Skill: Write Ranked List

## Purpose

Given a list title, target search query, niche focus, author, and a set of completed game page draft paths, produce a complete publish-ready ranked list page for Metric Gamer. The ranking includes an original two-paragraph introduction, an At A Glance scores table, and an entry for each game containing metric scores, The Good, The Bad, Who Is This Game For, and a Final Verdict. All entry content is reworded from the source game pages and tailored to the list's specific niche to avoid duplicate content penalties. All prose follows the Metric Gamer Writing Style Guide.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Writing Style Guide | writing/Writing-style.md | 5 |
| EEAT Framework | writing/eeat.md | 4 |
| Site User Personas | knoweldge/persona/persona.md | 3 |
| FAQ Templates | knoweldge/site/faq-templates.md | 2 |

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

- **[Hard]** Every score in the At A Glance table and each entry matches its source game page draft exactly — scores are copied, never re-derived.
- **[Hard]** No entry content reuses sentences or matching bullet-opening words from its source game page — duplicate-content rules apply to every entry, not a sample.
- **[Hard]** Minimum 2 `draft_paths` provided and all are read before drafting begins.
- **[Soft]** Niche-irrelevant Pros/Cons are trimmed from entries — relaxable only if Discovery Q&A confirms a point is niche-relevant despite first appearance.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `list_title` | string | Yes | Full title of the ranking (e.g., "Best Free Mobile Football Games 2026") |
| `target_query` | string | Yes | The primary search query this list targets (e.g., "best free mobile football games 2026") |
| `niche_focus` | string | Yes | One sentence on what makes this list specific — platform, price point, sub-genre, or audience |
| `author` | enum | Yes | ABossProductions, Metric Gamer, Lobotomy_gaming, or 8-Bit Bandit |
| `draft_paths` | string | Yes | Comma-separated paths to completed game page draft files. Minimum 2. |

---

## Execution Flow

```
Phase 1 — interface.py    Collect list_title, target_query, niche_focus, author, draft_paths
     ↓
Phase 2 — Claude          Keyword & SERP research: primary keyword, secondary keywords,
                          search intent, competitor gaps, FAQ seeds
     ↓
Phase 3 — Claude          Load writing-style.md, eeat.md, persona.md, faq-templates.md,
                          author persona, and all source game page drafts. Extract game
                          data: scores, Pros, Cons, Who Is This Game For, Verdict.
     ↓
Phase 4 — Claude          Discovery Q&A — surface close calls (score ties, borderline
                          niche fit for a source game, refined niche_focus from SERP
                          data) as direct questions. Halt until answered or explicitly
                          waived.
     ↓
Phase 5 — Claude          Draft the ranked list: SEO meta, reviewer attribution, list
                          introduction, At A Glance table, ranked entries, FAQs.
                          Apply rewrite rules and niche tailoring to all entries.
     ↓
Phase 6 — Claude          Validate against acceptance criteria before submitting.
```

Keyword and SERP research runs first — it defines the primary keyword, niche angle, and competitor gaps before any source material is read. Do not begin drafting until Phases 2 through 4 are complete.

---

## Interface Script

`interface.py` — collects `list_title`, `target_query`, `niche_focus`, `author`, and `draft_paths`, then prints the structured input block for Claude.

---

## Web Search Strategy

All research runs via Claude web search. Research targets category and intent queries — not game-specific queries.

### Blocked domains — review opinions only

```
ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net,
polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com,
trustedreviews.com, thegamer.com, screenrant.com, cbr.com
```

### Phase 2 — Keyword & SERP research

**Batch 1 — SERP landscape (2 searches)**
- `{target_query}` — what ranks in the top 5, their structure, how deep their entries go, what angle they take, what they miss
- `{target_query} site:reddit.com` — how the community frames this category, what questions come up when players are choosing in this niche

**Batch 2 — Long-tail and intent signals (2 searches)**
- `best {niche_focus}` — alternative phrasings and secondary queries this list should also rank for
- `{niche_focus} compared` or `{niche_focus} vs` — comparison intent signals and what players weigh in this category

**Extract and record before continuing:**

```
Primary keyword: [exact target_query or closest natural phrasing from SERP data]
Secondary keywords: [alternative phrasings, platform qualifiers, year variants, sub-genre terms]
Search intent: [one sentence — who is searching this and what decision they're trying to make]
Competitor gaps: [what top-ranking lists miss that the metric breakdown uniquely covers]
Niche focus confirmed: [confirm or refine the niche_focus based on actual search behaviour]
FAQ seeds: [People Also Ask questions and community questions for this list's topic]
```

### What to skip
- Any result from the blocked domain list
- Press releases, launch announcements, developer interviews
- Review aggregators
- Generic listicle pages with no scoring or structured comparison

---

## Page Structure

Produce all sections in this order. Every section is required.

### 1. SEO Meta
- **Meta Title** — statement or question format, ends with ` | Metric Gamer`, under 60 characters, leads with a list signal ("Best", "Top", "Ranked")
- **Meta Description** — primary keyword integrated naturally, tells the reader what they'll find and what decision the list helps them make, closes with a CTA, under 155 characters
- **URL Slug** — `/ranking/{list-slug-kebab-case}/`
- **Last Updated** — today's date

### 2. Reviewer Attribution
One line: `Reviewed by {author} — {one sentence on their expertise relevant to this list's niche}.`

### 3. List Introduction
Two paragraphs. Original copy — no sentences from any source game page.

Following `writing/Writing-style.md`: reads like advice from a knowledgeable player surveying the options, not a directory listing or AI summary.

- **Para 1** — The category, why it matters to players, what the landscape looks like. Primary keyword appears naturally here. No developer or publisher names.
- **Para 2** — Reader framing. How the ranking works, what they'll find in the entries, what decision this helps them make. Does not pre-answer which game is best.

### 4. At A Glance Table
All games with overall scores and individual metric scores, copied directly from source game page drafts. Ranked highest overall score first. Tie-breaks documented in a note beneath the table.

### 5. Ranked Entries
One section per game in rank order. Each entry: metric scores table, The Good (2–4 bullets), The Bad (2–4 bullets), Who Is This Game For (2 Play this if, 2 Skip this if), Final Verdict (1–2 sentences).

All entry content reworded from source game pages following the rewrite rules in the command file: no bullet opens with the same word as its source counterpart, no Verdict opens with the same phrase as the source game page Verdict, all points niche-tailored to the list's focus.

### 6. FAQs
List-level questions about the category or how to choose — not game-specific questions. Second person, max 3 sentences per answer, lead with "no" where the answer is negative.

---

## Acceptance Criteria

### Scores and Sources
- [ ] Every overall score matches the source game page exactly
- [ ] Every individual metric score matches the source game page exactly
- [ ] Ranking order is correct (highest overall score first)
- [ ] Any tie-break is documented beneath the At A Glance table
- [ ] Discovery Q&A phase run — score ties, borderline niche fit, and refined niche_focus surfaced as questions and resolved before drafting begins

### Duplicate Content
- [ ] List introduction contains no sentences or phrases from any source game page
- [ ] No The Good bullet opens with the same word(s) as its source Pro counterpart
- [ ] No The Bad bullet opens with the same word(s) as its source Con counterpart
- [ ] No Final Verdict opens with the same phrase as the source game page Verdict
- [ ] No Who Is This Game For entry uses the same phrasing as the source game page entry

### Niche Alignment
- [ ] Niche-irrelevant Pros/Cons omitted from entries
- [ ] The Good bullets lead with the most niche-relevant points
- [ ] Final Verdicts open from a comparative or ranking context angle
- [ ] Who Is This Game For trimmed to 2 most niche-relevant per side

### SEO Meta
- [ ] Meta title ends with ` | Metric Gamer`, under 60 characters, uses a list signal
- [ ] Meta description integrates primary keyword naturally, under 155 characters, closes with a CTA
- [ ] URL slug follows `/ranking/{list-slug-kebab-case}/` format

### Writing Style (writing-style.md)
- [ ] No em dashes anywhere in the copy
- [ ] No lists of three in any prose
- [ ] No corporate qualifiers
- [ ] Contractions used throughout
- [ ] Sentence length is varied — no run of short sentences
- [ ] No score justification language
- [ ] List introduction reads as original, knowledgeable copy
- [ ] Final Verdicts read like advice from a knowledgeable player, not an AI summary

### Structure
- [ ] List introduction is exactly two paragraphs
- [ ] At A Glance table is present and complete
- [ ] Every game has an entry with all required elements
- [ ] FAQs present, second person, max 3 sentences each, list-level questions only
