# Command: Keyword Strategy

Read `.claude/skills/keyword-strategy/readme.md`, `.claude/skills/keyword-strategy/connector.json`, and `company/site/keyword-strategy.md` before doing anything else. Every decision in this command is governed by those files.

---

## Step 1 — Load Knowledge Connectors

Read in order:
1. `company/site/keyword-strategy.md` — primary framework (importance 5)
2. `writing/eeat.md` — content quality context (importance 3)
3. `company/site/site-structure.md` — page types and URL structure (importance 3)
4. `company/persona/persona.md` — searcher intent context (importance 2)

Confirm inputs received: campaign_topic, existing_content, keyword_csv_path, gsc_csv_path, semrush_available, content_constraints (if provided).

---

## Step 2 — Read the Keyword Planner CSV

Read every row of the file at `keyword_csv_path`. Do not sample. This file may be large — read it completely before drawing conclusions.

For every row, record: keyword, avg monthly searches, 3-month change, YoY change, competition label, competition indexed value.

Surface the following before moving on:

**Structural decline flags** — keywords with YoY of -50% or worse:
List each one. These are excluded from consideration.

**Very low volume flags** — keywords with avg monthly searches under 100:
List each one. Note they may still have GSC long-tail value but cannot anchor a campaign.

**Emerging opportunity flags** — keywords with YoY of +100% or higher:
List each one. These are prioritised in the shortlist.

**Unmeasurable flags** — keywords with "Unknown" or "--" volume:
List each one. Cross-reference against GSC data in Step 3.

**High effort / low reward flags** — competition indexed value above 70 AND volume under 1,000:
List each one. These are excluded unless SERP check shows unusual openings.

**Top 10 by volume** — the 10 highest-volume terms and their YoY trend direction.

Do not proceed to Step 3 until this summary is complete and stated explicitly.

---

## Step 3 — Read the GSC Export CSV

Read the file at `gsc_csv_path`.

Cross-reference against the `existing_content` URLs provided in inputs. Identify:

**Page 2 improvement candidates** — existing MG pages with impressions but position 11–20:
These are already ranking — moving them to page 1 is higher ROI than targeting new keywords.

**Long-tail cloud signal** — queries with impressions but 0 or very few clicks (position 20+):
These reveal what Google already associates MG with in this space. Use to validate or reject keyword modifier directions.

**Topical authority signal** — query clusters where MG has consistent impression volume:
These indicate confirmed topical authority and are the safest space to expand cluster content.

If `semrush_available` is true: note that organic KD will be requested for shortlisted keywords after Step 4.

---

## Step 4 — Apply the DA 2 Filter

From the full keyword data, exclude immediately and without discussion:

- Bare game names (e.g., "rocket league", "gran turismo 4") — owned by official sites, Wikipedia, IGN, Metacritic regardless of volume
- Genre-only queries (e.g., "racing games", "football games")
- Platform-only queries (e.g., "PS4 games")
- Any keyword where the dominant modifier cluster shows -90% YoY — structural decline, excluded in full

For every remaining keyword, count modifiers: genre + platform + price point + play mode.
- Fewer than 3 modifiers → exclude
- 3 or more modifiers → carry forward to shortlist assessment

State the modifier count for each keyword carried forward.

---

## Step 5 — Build the Shortlist

From keywords passing the DA 2 filter, produce the shortlist. Each shortlisted keyword must meet:
- Avg monthly searches 100+ (or "Unknown" — flag separately, may have GSC signal)
- YoY flat or positive
- Competition indexed value under 60

If `semrush_available` is true: pause here and request the user to provide organic KD scores from Semrush for each shortlisted keyword before finalising the shortlist. Apply: KD under 30 = viable, KD 30–50 = SERP check is the deciding factor, KD above 50 = exclude.

Present the shortlist to the user in a table:

| Keyword | Volume | YoY | Competition (indexed) | Semrush KD | Modifier count |
|---|---|---|---|---|---|

---

## Step 6 — Request SERP Checks

For every keyword on the shortlist, instruct the user to:

1. Search the keyword in an incognito browser window
2. Report back:
   - Positions 1–5: site names and page types (list / review / forum / commercial / video)
   - Any featured snippets, video carousels, or knowledge panels
   - Intent signal: does page 1 directly answer the query, or is the intent split across different audiences?

**Do not proceed to Step 7 until SERP results are returned for every shortlisted keyword.**

State this explicitly: "I need SERP check results for the above keywords before selecting the campaign anchor. Please search each one incognito and report back what's on page 1."

---

## Step 7 — Discovery Q&A

Before selecting the campaign anchor, surface every close call as a direct question rather than deciding silently. Typical close calls at this point:

- Two or more SERP-PASS keywords are close enough in volume/YoY that either could anchor the campaign — ask which to prioritise.
- A cluster would share more than one game with another cluster — ask whether to accept the cannibalisation risk or drop one of the competing keywords.
- A keyword sits in the KD 30–50 range with a SERP-PASS result — ask whether the SERP result alone is enough to include it.
- `semrush_available` was false — flag that KD data is missing for the shortlist and ask whether to proceed on SERP/GSC signal alone.

State the assumption you would otherwise make alongside each question. Do not proceed to Step 8 until the user answers or explicitly says to use your judgement.

---

## Step 8 — Evaluate SERP Results and Select Campaign Anchor

Apply the SERP pass criteria from `company/site/keyword-strategy.md` to each returned result.

Mark each keyword explicitly:
- **SERP PASS** — no IGN/Metacritic/Fandom/Wikipedia in positions 1–3; at least 2 smaller/medium sites or forum threads in top 5; intent is clean
- **SERP FAIL** — reason stated (e.g., "IGN and Metacritic hold positions 1 and 2", "intent split: physical products + video games")

From SERP-passing keywords, select the campaign anchor:
- Highest volume that passes the SERP check
- Flat or growing YoY
- Clean intent (no audience split)

State the campaign anchor and all confirmation criteria explicitly before building the cluster map.

---

## Step 9 — Map Clusters

From remaining SERP-passing keywords (excluding the anchor), build the cluster map.

Each cluster = one ranked list targeting one Tier 1 keyword with a distinct modifier from the anchor and from other clusters.

For each cluster:
- State the primary keyword, volume, competition, SERP result
- List which MG game pages from `existing_content` support this cluster
- Flag if fewer than 3 supporting game pages exist (cluster may not be viable yet)
- Flag cannibalisation risk if more than one game is shared with another cluster

---

## Step 10 — Assign Game Page Keywords

For each game appearing in each cluster, assign:

**Tier 2 primary keyword** — game name + campaign modifier. Not the bare game name.
Examples:
- "rocket league free ps4" (not "rocket league")
- "burnout 3 takedown review ps2" (not "burnout 3")
- "is asphalt legends worth it" (not "asphalt legends")

Niche game exception: for smaller titles with low major publication coverage, targeting closer to the bare game name may be viable. Note which games qualify and confirm via SERP check if not already done.

**Tier 3 FAQ keywords** — 2–3 question-format long-tails per game. These go in FAQ sections and H2s. Often zero volume in the planner — that is expected.

For each game note: existing MG page (yes / no / URL).

---

## Step 11 — Gap List

List every game needed by the cluster map that does not have an existing MG page. For each:
- Game title
- Which cluster(s) it supports
- Target Tier 2 primary keyword
- Priority (High / Medium) — High if its absence leaves a cluster with fewer than 3 supporting pages

---

## Step 12 — Validate and Deliver

Check every item in the acceptance criteria in `.claude/skills/keyword-strategy/readme.md` before delivering the keyword map.

**Output format:**

```
CAMPAIGN ANCHOR
Keyword: [keyword]
Volume: [monthly]  YoY: [trend]  Competition: [index]  KD: [if available]
SERP: PASS — [one sentence on what's ranking]
Confirmation criteria: [list all 5 — modifier count, YoY, volume, SERP, intent]

CLUSTER MAP
Cluster 1: [keyword]
  Volume / Competition / SERP result
  Games: [list with existing page status]
  Cannibalisation risk: [yes/no — shared games with other clusters]

[repeat per cluster]

GAME PAGE KEYWORD ASSIGNMENTS
[Game] — Cluster [N]
  Tier 2: [primary keyword]
  Tier 3: [FAQ keyword 1], [FAQ keyword 2], [FAQ keyword 3]
  MG page: [exists at URL / needs to be written]

[repeat per game]

GAP LIST
[Game] — supports Cluster [N] — Priority [High/Medium]
  Target keyword: [Tier 2 keyword]

[repeat per gap]

UNCONFIRMED
[Anything not confirmed due to missing SERP data, no Semrush KD, or Unknown volume]
```
