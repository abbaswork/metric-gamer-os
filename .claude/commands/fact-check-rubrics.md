# Command: Fact-Check Rubrics

Read `.claude/skills/fact-check-rubrics/readme.md` and `.claude/skills/fact-check-rubrics/connector.json` before doing anything else. Every decision in this command is governed by those files.

---

## Inputs

Parse the following from `$ARGUMENTS` if provided (format: `genre | sub_genre`). If either is missing, ask before proceeding.

| Input | Required | Notes |
|---|---|---|
| `genre` | Yes | The genre folder name (e.g. `fighting`, `racing`, `moba`) |
| `sub_genre` | Yes | The sub-genre folder name within that genre (e.g. `platform-fighter`, `party`, `traditional`) |

---

## Step 1 — Verify Sub-genre Folder

Check that `scoring-system/genres/{genre}/sub-genres/{sub_genre}/` exists.

- If it does **not** exist: HALT. Report the exact path that was not found. Do not proceed.
- If it exists: proceed to Step 2.

---

## Step 2 — Load Research and Rubrics

Read in this order:

1. `scoring-system/genres/{genre}/research.md` — primary source of truth for claim classification. If this file does not exist, note it in the report and proceed on external sources only.
2. Every `rubric.md` file found inside `scoring-system/genres/{genre}/sub-genres/{sub_genre}/` — read each one in full.

Do not proceed to Step 3 until all files are read.

---

## Step 3 — Classify Every Claim

For each rubric, identify every claim and assign it exactly one classification:

| Classification | Definition |
|---|---|
| **Backed** | Directly supported by a source cited in the rubric's Sources section, or by the genre research file. No action needed. |
| **Partially Backed** | Supported by general research or a neighbouring domain but not specifically for this genre or sub-genre. Needs targeted research before it can be confirmed or flagged. |
| **Not Backed** | No source cited or traceable. Appears to be an inference. Needs research — if nothing found, flagged for user decision. |
| **Contradicted** | A source directly contradicts the claim. Flagged prominently for user decision. |

**What counts as a claim:** any statement that asserts something is true about player preferences, game design principles, or genre characteristics. This includes: signals and criteria in Observable Signals or Checklist tables, score-band descriptions that reference specific design features, and explanatory assertions in Why This Matters. It does not include structural prose (e.g. "this rubric scores X") or direct verbatim quotes from cited sources.

Label every claim as **Critical** (scoring criteria, observable signals, checklist items) or **Advisory** (Why This Matters prose). Both are reported — Critical flags take priority.

---

## Step 4 — Web Research on Non-Backed Claims

Run web research on every Partially Backed and Not Backed claim before delivering any report. The report must arrive with research already done — never flag claims as "needs research" without having run it.

**Do not apply a domain blocklist.** Filter results by reading them, not by URL.

For each claim requiring research, run two searches:

1. **Supporting search** — look for research, game design writing, or community discussion that confirms the claim for this genre or sub-genre specifically.
   - `{sub_genre} game {claim_topic} player preference design`
   - `{claim_topic} game design research evidence`

2. **Contradicting search** — look for anything that directly contradicts the claim.
   - `{claim_topic} game design contradicted OR myth OR debunked`
   - `{genre} {sub_genre} {claim_topic} players don't care OR doesn't matter`

Group claims by theme before searching — multiple claims about the same topic can be covered by a single well-formed search. Run independent searches in parallel.

Extract: verbatim quotes that directly address the claim, whether evidence is genre-specific or general, source URL and publication.

Skip: editorial opinion without specific evidence, aggregator or listicle pages, quotes that address a related topic but do not directly speak to the claim.

Update each classification based on what was found:
- Evidence backs the claim specifically → upgrade to Backed
- Evidence partially backs it → remains Partially Backed, note what was found
- Nothing found → remains Not Backed, note that searches returned nothing
- Contradicting evidence found → reclassify as Contradicted

---

## Step 5 — Discovery Q&A

Surface any genuine ambiguity before delivering the report. The only ambiguity that warrants a question is whether a claim falls under a different rubric's scope (e.g. a signal that belongs in a different metric). If no genuine ambiguity exists, proceed directly to Step 6.

---

## Step 6 — Deliver the Report

### Per-rubric tables

Report each rubric as a table with four columns:

```
## {Rubric Name} — {metric-folder-name}/rubric.md

| Claim | Type | Classification | Finding |
|---|---|---|---|
| [claim text] | Critical | Backed | [source] |
| [claim text] | Critical | Contradicted ⚠️ | contradicted by [source]: "[quote]" — held for your decision |
| [claim text] | Critical | Partially Backed | partially supported by [source]: "[quote]" — not {sub_genre}-specific — held for your decision |
| [claim text] | Critical | Not Backed | research finding: [what was found / nothing found] — held for your decision |
| [claim text] | Advisory | Backed | [source] |
| [claim text] | Advisory | Not Backed | [what was found / nothing found] — held for your decision |
```

### Summary count table

After all rubric tables:

```
## Summary

| Rubric | Backed | Partially Backed | Not Backed | Contradicted |
|---|---|---|---|---|
| [rubric name] | # | # | # | # |
| **Total** | # | # | # | # |
```

### Held for Decision table

After the summary:

```
## Held for Your Decision

| Rubric | Claim | Type | Classification |
|---|---|---|---|
| [rubric] | [claim text] | Critical / Advisory | Partially Backed / Not Backed / Contradicted ⚠️ |
```

### Q&A

Immediately after the Held for Decision table, ask:

> **Q1.** Should I retain all backed points?
> **Q2.** Shall I conduct more research into the partially backed, contradicted, and not-backed points?

---

## Step 7 — Deeper Research (if Q2 = Yes)

Run deeper research on all remaining Partially Backed, Contradicted, and Not Backed claims. Update classifications where research changes the finding. Deliver an updated Held for Decision table. Then ask:

> **Q1.** Should I retain all backed points?
> **Q2.** Shall I conduct more research into any remaining partially backed, contradicted, or not-backed points?
> **Q3.** Shall I remove the not-backed points and inferences?

---

## Step 8 — Await Final Instructions

Make no changes to any rubric file until the user has answered all three questions and given explicit instruction to proceed.

---

## Hard Rules

- Never modify any rubric file during this command. Report findings in chat only.
- Every claim must be classified before the report is delivered. No claim left unclassified.
- Web research must be completed on all Partially Backed and Not Backed claims before the report is delivered.
- Do not apply a domain blocklist to searches.
- Critical and Advisory labels must appear on every row of every per-rubric table.
- All non-backed findings must be explicitly marked "held for your decision."
