# Command: Keyword Research

## Purpose
Validates keyword opportunities for a new campaign before any content structure is planned or written. No campaign structure is proposed until every step in this command is complete.

---

## What the User Must Provide Before This Command Runs

### 1. Campaign Brief
One paragraph covering:
- **Campaign topic:** What is the niche? Not a genre — a niche with modifiers. "Free arcade racing games" not "racing games."
- **Target audience:** Who is searching? What platform? What price sensitivity?
- **Content constraints:** Which games is MG unable to review? Any platform coverage gaps for the authors?
- **Existing MG content in this space:** Full list of every live URL related to the campaign topic

### 2. Keyword Planner CSV
- Seeded with the **campaign TOPIC** (broad term — not specific keywords, not game names)
- Date range: last 12 months
- Full export — not filtered by volume or competition
- Required columns: keyword, avg monthly searches, 3-month change, YoY change, competition, competition indexed value

### 3. GSC Export
- Last 12 months
- All queries, clicks, impressions, CTR, average position
- Filtered to campaign genre/topic where possible

### 4. SEO Tool Access (upgrades analysis quality)
If Semrush or Ahrefs access is available, provide organic keyword difficulty for shortlisted terms. Without this, the planner competition index is used as a proxy — which is imperfect and increases the importance of SERP checks.

### 5. SERP Check Results (user executes, reports back)
For every keyword that passes the initial filters, the user searches it in an incognito window and reports:
- Positions 1–5: site names and page types (list/review/forum/commercial/video)
- Any featured snippets, video carousels, or knowledge panels
- Intent signal: is page 1 directly answering the query, or is the intent mixed?

**This check cannot be skipped. Claude cannot access live SERPs reliably. No keyword is confirmed without a SERP result.**

---

## Execution Flow

### Step 1 — Read the complete CSV
Read every row before drawing any conclusions. Do not sample. Surface and state explicitly:

- Every keyword with YoY of -50% or worse → flag as structural decline
- Every keyword with avg monthly searches under 100 → flag as very low volume
- Every keyword showing +100% or higher YoY → flag as emerging opportunity
- Every keyword showing "Unknown" or "--" → flag as unmeasurable, note for GSC cross-reference
- Every keyword with competition index above 70 AND volume under 1,000 → flag as high effort, low reward
- The 10 highest-volume terms and their trend direction

Do not proceed until this summary is complete.

### Step 2 — Apply the DA filter
Exclude without discussion:
- Bare game names
- Genre-only queries
- Platform-only queries
- Any keyword cluster where the dominant modifier shows -90% YoY

Flag each remaining keyword with its modifier count. Remove any with fewer than 3 modifiers.

### Step 3 — Build the shortlist
Produce a shortlist of keywords that:
- Pass the modifier filter (3+ modifiers)
- Have avg monthly searches of 100+ (or "Unknown" — flag separately)
- Have flat or positive YoY
- Have competition indexed value under 60

Present the shortlist to the user before moving forward.

### Step 4 — SERP check (user executes)
Instruct the user to search every shortlisted keyword incognito and report back the format above. Wait for results before proceeding.

### Step 5 — Discovery Q&A
Before selecting the anchor, surface any close call as a direct question and wait for the user's answer rather than deciding silently:
- Two or more keywords are both SERP-PASS and close in volume/YoY — which should anchor the campaign?
- A cluster would share more than one game with another cluster — proceed with the cannibalisation risk, or drop one keyword?
- A keyword sits in the "Unknown" volume or borderline competition range — include on GSC signal alone, or exclude?

Do not proceed to Step 6 until these are resolved or the user explicitly says to use your judgement.

### Step 6 — Campaign anchor selection
From SERP-validated keywords, select the campaign anchor:
- Highest volume that passes the SERP check
- Flat or growing YoY
- Clean intent (no split between different searcher types)

State the anchor keyword and the reasoning explicitly.

### Step 7 — Cluster map
Map remaining validated keywords to clusters (ranked lists). Flag any cannibalisation risks (more than one shared game between clusters). Confirm each cluster has at least 3 supporting game pages in MG's content library.

### Step 8 — Game page keyword assignments
For each game in each cluster, assign:
- One primary Tier 2 keyword (game name + modifier — not bare game name)
- Two to three Tier 3 FAQ-level keywords
Note which game pages already exist on MG and which need to be written.

---

## Output Format
A validated keyword map covering:
- Campaign anchor + confirmation criteria met
- Cluster list: primary keyword, volume, competition, SERP result, game roster
- Game page keyword assignments per cluster
- Gap list: game pages needed but not yet written
- Explicit note on anything unconfirmed pending SERP check
