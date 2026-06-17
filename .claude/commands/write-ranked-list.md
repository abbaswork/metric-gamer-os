# Skill: Write Ranked List

Write a complete, publish-ready ranked list page for Metric Gamer from completed game page drafts. The ranked list is a distinct content type from the individual game pages it draws from: it targets a different search query, serves a different reader intent, and must use different wording throughout to avoid duplicate content penalties. All prose must follow `writing/Writing-style.md` — consult it before drafting any section.

## Inputs

Parse the following from `$ARGUMENTS` (format: `list_title | target_query | niche_focus | author | draft_paths`). If any required field is missing, ask before proceeding.

| Input | Required | Notes |
|---|---|---|
| `list_title` | Yes | Full title of the ranking (e.g., "Best Free Mobile Football Games 2026") |
| `target_query` | Yes | The primary search query this list targets (e.g., "best free mobile football games 2026") |
| `niche_focus` | Yes | One sentence describing what makes this list specific — platform, price point, sub-genre, or audience (e.g., "free-to-play football games on iOS and Android") |
| `author` | Yes | One of: ABossProductions, Metric Gamer, Lobotomy_gaming, 8-Bit Bandit |
| `draft_paths` | Yes | Comma-separated paths to the source game page drafts. Minimum 2. |

---

## Step 1 — Keyword & SERP Research

Run this before loading any source drafts or writing anything. The target queries for a ranked list are category and intent queries — not game-specific queries. This research is entirely separate from the research done for the individual game pages.

**Blocked domains — review opinions only:**
`ign.com, gamespot.com, gamesradar.com, metacritic.com, eurogamer.net, polygon.com, kotaku.com, pcgamer.com, gameinformer.com, pushsquare.com, trustedreviews.com, thegamer.com, screenrant.com, cbr.com`

**Batch 1 — SERP landscape (run both):**
1. `{target_query}` — what ranks in the top 5, their structure, how deep their entries go, what angle they take, what they miss
2. `{target_query} site:reddit.com` — how the community frames this category, what players ask when choosing in this niche, common decision factors

**Batch 2 — Long-tail and intent signals (run both):**
1. `best {niche_focus}` — alternative phrasings and secondary queries this list should also rank for
2. `{niche_focus} compared` or `{niche_focus} vs` — comparison intent signals and what players weigh against each other in this category

**Record before continuing:**

```
Primary keyword: [the exact target_query or closest natural phrasing from SERP data]
Secondary keywords: [alternative phrasings, platform qualifiers, year variants, sub-genre terms]
Search intent: [one sentence — who is searching this and what decision they're trying to make]
Competitor gaps: [what the top-ranking lists miss that the metric breakdown uniquely covers]
Niche focus confirmed: [confirm or refine the niche_focus based on actual search behaviour]
FAQ seeds: [People Also Ask questions and community questions specific to this list's topic]
```

---

## Step 2 — Load Knowledge Connectors

Read all of the following before drafting:

- `writing/Writing-style.md` — **primary output standard for all prose in this ranking.** Every section must conform to it: no em dashes, no lists of three, contractions throughout, varied sentence length, no corporate qualifiers, no score justification language. Read this first and keep it open throughout drafting.
- `writing/eeat.md` — publishing lifecycle; this skill follows Phases 1–7
- `knoweldge/persona/persona.md` — site user personas; keep the reader's decision context in mind throughout
- `knoweldge/site/faq-templates.md` — FAQ question pool and format rules

Then read the author persona file:

| Author | File |
|---|---|
| ABossProductions | `writing/author-personas/abossgaming.md` |
| Metric Gamer | `writing/author-personas/metric-gamer.md` |
| Lobotomy_gaming | `writing/author-personas/lobotomy-gaming.md` |
| 8-Bit Bandit | `writing/author-personas/8-bit-bandit.md` |

Then read every source game page draft listed in `draft_paths`. For each draft, extract and record:

| Field | Source location in draft |
|---|---|
| Game name | Page title |
| Overall score | Overall Score section |
| Individual metric names and scores | Metric Descriptions headings |
| Pros | Pros and Cons section |
| Cons | Pros and Cons section |
| Who Is This Game For / Skip | Who Is This Game For section |
| Verdict | Verdict section |

Do not begin drafting until all files are read and game data is extracted.

---

## Step 3 — Draft the Ranked List

Produce all sections in this order. Every section is required. Save the output to `writing/drafts/ranked/{list-slug}.md`.

### 1. SEO Meta

- **Meta Title** — statement or question format, ends with ` | Metric Gamer`, under 60 characters. Lead with the list signal ("Best", "Top", "Ranked"). Include the niche qualifier (platform, price point, year) where it fits naturally within the character limit.
- **Meta Description** — integrate the primary keyword naturally inside a real sentence. Tell the reader what they'll find and what decision the list helps them make. Close with a CTA. Under 155 characters.
- **URL Slug** — `/ranking/{list-slug-kebab-case}/`
- **Last Updated** — today's date

### 2. Reviewer Attribution

`Reviewed by {author} — {one sentence on their expertise relevant to this specific list's niche}.`

Draw the expertise line from the author persona file, angled toward the list's niche rather than a generic bio.

### 3. List Introduction

Two paragraphs. Entirely original copy — no sentences, clauses, or phrases from any source game page draft.

Before writing, re-read `writing/Writing-style.md`. The introduction must read like advice from a knowledgeable friend surveying the options — not a directory listing or an AI-generated category summary.

- **Para 1** — Sets up the category. Why this niche matters to players, what the landscape looks like, what the best games in this category tend to do well. The primary keyword should appear naturally in this paragraph. No developer or publisher names here.
- **Para 2** — Reader framing. Tell the reader how the ranking works (scored across the same metrics from each game page), what they'll find in the entries, and what decision this helps them make. Point them into the breakdown. Do not pre-answer which game is best or summarise the ranking outcome.

The introduction is the primary SEO surface for this page. Integrate the primary keyword and at least two secondary keywords naturally across both paragraphs.

### 4. At A Glance Table

A summary table with every game, its overall score, and its individual metric scores. Values copied directly from source game page drafts — do not alter any scores.

```markdown
| Rank | Game | Score | [Metric 1] | [Metric 2] | [Metric 3] | [Metric 4] | [Metric 5] |
|---|---|---|---|---|---|---|---|
| 1 | [Game] | [Score]/5 | [Score] | [Score] | [Score] | [Score] | [Score] |
```

Rank order: highest overall score first. For tied overall scores, the higher rank goes to the game with the stronger score in the metric most relevant to the list's `niche_focus`. Document any tie-break reason in a note beneath the table.

### 5. Ranked Entries

One section per game in rank order. Every entry contains exactly these elements — no more, no fewer.

---

**#[Rank] [Game Name]**

**Score: [Overall]/5**

| Metric | Score |
|---|---|
| [Metric Name] | [Score]/5 |
| [Metric Name] | [Score]/5 |
| [Metric Name] | [Score]/5 |
| [Metric Name] | [Score]/5 |
| [Metric Name] | [Score]/5 |

**The Good**
- [bullet]
- [bullet]
- [bullet]

**The Bad**
- [bullet]
- [bullet]

**Who Is This Game For?**
**Play this if** [specific reason — niche-aligned]
**Play this if** [specific reason — niche-aligned]
**Skip this if** [specific reason — niche-aligned]
**Skip this if** [specific reason — niche-aligned]

**Final Verdict**
[1–2 sentences]

---

### 6. FAQs

Use templates from `knoweldge/site/faq-templates.md`. Select questions appropriate to the list's niche — these should be list-level questions about the category or how to choose, not game-specific questions (those belong on the individual game pages). Second person, max 3 sentences per answer, lead with "no" where the answer is negative.

---

## Rewrite Rules

These rules apply to every ranked entry. They exist to ensure the ranked list content is substantively different from the game page content it draws from. Before applying any rule, re-read `writing/Writing-style.md`. The style guide governs all prose here the same way it governs game pages.

**Writing style — non-negotiable across every element:**
- No em dashes anywhere. Use commas, full stops, or "however" to restructure.
- No lists of three ("X, Y, and Z" patterns). Use two items or break into separate sentences.
- Contractions throughout — "you'll", "it's", "you're", "doesn't", "haven't"
- Vary sentence length. A long sentence followed by a short one reads naturally. A run of short sentences signals AI writing.
- No corporate qualifiers: "genuinely", "consistently", "meaningfully", "substantially"
- No score justification language

### The Good and The Bad

- **Source:** Pros and Cons from the source game page
- **No bullet may open with the same word or phrase as its source counterpart.** If a source Pro starts with "The live events calendar follows real UEFA Champions League fixtures", the Good bullet must open differently.
- **Restructure the information within each bullet.** Lead with the payoff, not the feature. "VS Attack leagues hold up to 100 members" becomes "Leagues that hold up to 100 members give VS Attack more social depth than competing apps."
- **Niche filter:** If a Pro or Con has no bearing on the list's `niche_focus` or target platform, omit it. A console-specific feature note has no place in a mobile-only list entry.
- **Target:** 2–4 bullets each. Prioritise the most niche-relevant points.

### Who Is This Game For?

- **Source:** Who Is This Game For section from the source game page
- **Reframe every point from the list's niche angle.** The entry version is shorter and more pointed than the game page version — it speaks to a reader who found this via the list's search query.
- **Trim to 2 "Play this if" and 2 "Skip this if" entries.** Choose the 2 most relevant to the list's `niche_focus` from each side.
- **No entry may use the same phrasing as the source game page.** Reword from a different angle while preserving the same underlying fact or judgment.

### Final Verdict

- **Source:** Verdict from the source game page
- **1–2 sentences maximum.** The game page Verdict is 2–3 sentences; the ranked entry Verdict is tighter.
- **Must open from a comparative or niche angle**, not the same opener as the game page Verdict. The entry Verdict should situate the game within the ranking — where it sits relative to the other options, or why it earns its rank for this specific audience.
- **Example (wrong):** "Gran Turismo 4 is still one of the best PS2 racing games you can go back to" — this mirrors the game page voice and makes no comparative claim.
- **Example (right):** "Nothing else in this ranking matches GT4 for single-player depth. The credit grind and the cancelled online mode are real limitations, but they're the problems of a game that's already given you more structured content than most players finish." — opens from the ranking's perspective, uses contractions, no em dashes, closes with something a knowledgeable player would say.

---

## Step 4 — Validate

Before submitting, verify every item below.

### Scores and Sources
- [ ] Every overall score matches the source game page exactly
- [ ] Every individual metric score matches the source game page exactly
- [ ] Ranking order is correct (highest overall score first)
- [ ] Any tie-break is documented in a note beneath the At A Glance table

### Duplicate Content
- [ ] List introduction contains no sentences or phrases from any source game page
- [ ] No The Good bullet opens with the same word(s) as its source Pro counterpart
- [ ] No The Bad bullet opens with the same word(s) as its source Con counterpart
- [ ] No Final Verdict opens with the same phrase as the source game page Verdict
- [ ] No Who Is This Game For entry uses the same phrasing as the source game page entry

### Niche Alignment
- [ ] Niche-irrelevant Pros/Cons have been omitted from entries
- [ ] The Good bullets lead with the most niche-relevant points
- [ ] Final Verdicts open from a comparative or ranking context angle
- [ ] Who Is This Game For entries are trimmed to the 2 most niche-relevant per side

### SEO Meta
- [ ] Meta title ends with ` | Metric Gamer`
- [ ] Meta title under 60 characters
- [ ] Meta title uses a list signal ("Best", "Top", "Ranked")
- [ ] Meta description integrates primary keyword naturally
- [ ] Meta description under 155 characters
- [ ] Meta description closes with a CTA
- [ ] URL slug follows `/ranking/{list-slug-kebab-case}/` format

### Writing Style (writing-style.md)
- [ ] No em dashes anywhere in the copy
- [ ] No lists of three in any prose
- [ ] No corporate qualifiers ("genuinely", "consistently", "meaningfully", "substantially")
- [ ] Contractions used throughout
- [ ] Sentence length is varied — no run of short sentences anywhere
- [ ] No score justification language
- [ ] List introduction reads as original, knowledgeable copy — not a generic category summary
- [ ] Final Verdicts read like advice from a knowledgeable player — not an AI summary paragraph

### Structure
- [ ] List introduction is exactly two paragraphs
- [ ] At A Glance table is present and complete
- [ ] Every game has an entry with all required elements: metric scores, The Good, The Bad, Who Is This Game For, Final Verdict
- [ ] FAQs present, second person, max 3 sentences each, list-level questions only