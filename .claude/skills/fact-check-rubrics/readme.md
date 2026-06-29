# Skill: Fact-Check Rubrics

## Purpose

Given a genre and sub-genre, audit every rubric in that sub-genre for claims that are not grounded in cited sources. Every claim in a rubric — in scoring criteria, observable signals, checklist items, and Why This Matters prose — must trace back to a real source. Claims that are Claude's own logical inferences, however plausible, undermine the credibility of the scoring system and the validity of every game score derived from it.

The skill reads all rubric files in the target sub-genre, cross-references every claim against cited sources, classifies each claim into one of four categories (backed, partially backed, not backed, contradicted), runs web research on all non-fully-backed claims, and delivers a structured report in chat. The user decides what to do with every finding through a guided Q&A flow. The skill never modifies rubric files.

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Genre Research | scoring-system/genres/{genre}/research.md | 5 |
| Genre Metrics | scoring-system/genres/{genre}/metrics.md | 3 |
| Scoring System Overview | scoring-system/overview.md | 3 |
| Company Overview | company/overview.md | 2 |

The genre research file (importance 5) is the primary source of truth — it contains the manually curated Reddit and Google Trends data that rubric claims should trace back to. If a claim is not in the research file and has no external source cited, it is a candidate for scrutiny. Genre metrics (3) provides context on what the sub-genre is scoring and helps identify when a claim is outside the intended scope. Scoring system overview (3) defines the structural contract rubrics must conform to.

---

## Requirements

- **[Hard]** Never modify any rubric file during this skill run. Report findings in chat only. Every decision about what to change, remove, or research further belongs to the user.
- **[Hard]** Every claim must be classified into exactly one of four categories — backed, partially backed, not backed, or contradicted — before the report is delivered. No claim is left unclassified.
- **[Hard]** Web research must be completed on all partially backed and not-backed claims before the report is delivered. The report arrives with research already done, not with a list of things still to check.
- **[Hard]** Do NOT apply a domain blocklist to web searches. Use editorial judgment to filter results by reading them — not by URL.
- **[Hard]** Claims in scoring criteria, observable signals, and checklist items are flagged as **Critical** — they directly affect how games are scored. Claims in Why This Matters prose are flagged as **Advisory** — they affect credibility but not scores directly. Both are reported, but Critical flags take priority in the report.
- **[Hard]** If the target sub-genre folder does not exist, halt immediately and tell the user — do not attempt to audit a path that is not there.
- **[Soft]** The research.md for the genre is read before any rubric files — relaxable only if the file does not exist, in which case the audit proceeds on external sources only and the missing research file is flagged in the report.

---

## Claim Classification

Every claim found in a rubric is assigned one of four classifications:

| Classification | Definition |
|---|---|
| **Backed** | Directly supported by a source cited in the rubric's Sources section, or by the genre research file. No action needed. |
| **Partially backed** | Supported by general research or a neighbouring domain but not specifically for this genre or sub-genre. Needs targeted research before it can be confirmed or flagged. |
| **Not backed** | No source cited or traceable. Appears to be Claude's own inference. Needs research — if nothing is found, flagged for user decision. |
| **Contradicted** | A source (cited in the rubric or found during research) directly contradicts the claim. Flagged prominently for user decision. |

**What counts as a "claim":** Any statement in a rubric that asserts something is true about player preferences, game design principles, or genre characteristics. This includes: signals and criteria in the Observable Signals or Checklist table, score-band descriptions that reference specific design features, and explanatory assertions in Why This Matters. It does not include structural prose (e.g. "this rubric scores X") or direct verbatim quotes from cited sources.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `genre` | string | Yes | The genre folder name (e.g. `fighting`, `racing`, `moba`) |
| `sub_genre` | string | Yes | The sub-genre folder name within that genre (e.g. `platform-fighter`, `party`, `traditional`) |

---

## Execution Flow

```
Phase 1 — interface.py    Collect genre and sub_genre from user

Phase 2 — Claude          Verify the sub-genre folder exists.
                          → Missing: HALT. Report the path that was not found.
                          → Present: read research.md for the genre (if it exists),
                            then read every rubric.md in the sub-genre folder in full.

Phase 3 — Claude          For each rubric, identify every claim and classify it.
                          Separate Critical claims (scoring criteria, signals,
                          checklist items) from Advisory claims (Why This Matters prose).

Phase 4 — Claude          Run web research on all partially backed and not-backed
                          claims. Batch searches to cover all claims before reporting.
                          Note what was found, what backed the claim further, and
                          what contradicted or failed to support it.

Phase 5 — Claude          Discovery Q&A — surface any genuine ambiguity before
                          delivering the report. The only ambiguity that warrants a
                          question is whether a claim falls under a different rubric's
                          scope (e.g. a signal that belongs in a different metric).
                          If no genuine ambiguity exists, proceed directly to the report.

Phase 6 — Claude          Deliver the per-rubric report in chat (see Report Format).
                          Then deliver the "Held for Decision" summary table.
                          Then ask Q1 and Q2.

Phase 7 — Claude          If the user answers Yes to Q2, run deeper research on all
                          partially backed and not-backed claims. Update classifications
                          where research changes the finding.
                          Then deliver an updated "Held for Decision" summary table.
                          Then ask Q1, Q2, and Q3.

Phase 8 — Claude          Await final user answers. Make no changes to any file
                          until the user has answered all three questions and given
                          explicit instruction to proceed.
```

---

## Interface Script

`interface.py` — collects `genre` and `sub_genre`, validates that neither is empty, and prints the structured input block for Claude.

---

## Web Search Strategy

Research runs only on partially backed and not-backed claims. Backed claims are not re-searched. Contradicted claims use the contradicting source already found — no additional search needed unless the user requests it.

Do NOT apply a domain blocklist. Filter results by reading them, not by URL.

### Search approach per claim

For each claim requiring research, run two searches:

1. **Supporting evidence search** — look for research, game design writing, or community discussion that confirms the claim is true for this genre or sub-genre specifically.
   - Query template: `{sub_genre} game {claim_topic} player preference design`
   - Query template: `{claim_topic} game design research evidence`

2. **Contradicting evidence search** — look for anything that directly contradicts the claim.
   - Query template: `{claim_topic} game design contradicted OR myth OR debunked`
   - Query template: `{genre} {sub_genre} {claim_topic} players don't care OR doesn't matter`

### Batching

Group claims by theme before searching — multiple claims about the same topic (e.g. match length, character variety) can be covered by a single well-formed search. Run searches in parallel where claims are independent.

### What to extract

- Verbatim quotes that directly address the claim
- Whether the evidence is genre/sub-genre-specific or general (this determines whether it fully backs or only partially backs the claim)
- Source URL and publication for attribution

### What to skip

- Editorial opinion pieces without specific evidence
- Aggregator or listicle pages
- Quotes that address a related topic but do not directly speak to the claim being checked

---

## Report Format

### Per-rubric tables

Each rubric is reported as a table with four columns: Claim | Type | Classification | Finding.

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

After all rubrics:

```
## Summary

| Rubric | Backed | Partially Backed | Not Backed | Contradicted |
|---|---|---|---|---|
| [rubric name] | # | # | # | # |
| **Total** | # | # | # | # |
```

### Held for Decision table

After the summary count table, a consolidated table of every non-backed finding:

```
## Held for Your Decision

| Rubric | Claim | Type | Classification |
|---|---|---|---|
| [rubric] | [claim text] | Critical / Advisory | Partially Backed / Not Backed / Contradicted ⚠️ |
```

### Q&A flow

Immediately after the Held for Decision table, ask:

> **Q1.** Should I retain all backed points?
> **Q2.** Shall I conduct more research into the partially backed, contradicted, and not-backed points?

If the user answers Yes to Q2, conduct deeper research, update the Held for Decision table, then ask:

> **Q1.** Should I retain all backed points?
> **Q2.** Shall I conduct more research into any remaining partially backed, contradicted, or not-backed points?
> **Q3.** Shall I remove the not-backed points and inferences?

Once all three questions are answered, the fact-check is complete. Make no rubric file changes until the user has given explicit instruction based on their Q3 answer.

---

## Acceptance Criteria

- [ ] Sub-genre folder existence verified before proceeding — if missing, skill halted with path reported
- [ ] Genre research.md read before any rubric files, where it exists
- [ ] Every rubric.md in the target sub-genre folder read in full
- [ ] Every claim in every rubric classified into exactly one of: backed, partially backed, not backed, contradicted
- [ ] Critical claims (scoring criteria, signals, checklist items) distinguished from Advisory claims (Why This Matters prose) in the report
- [ ] Per-rubric findings delivered as tables (Claim | Type | Classification | Finding)
- [ ] Web research completed on all partially backed and not-backed claims before report delivered — report does not flag claims as "needs research" without having done it
- [ ] No domain blocklist applied to searches
- [ ] No rubric file modified during the skill run
- [ ] All non-backed findings explicitly marked "held for your decision"
- [ ] Summary count table present after all rubric tables
- [ ] Held for Decision consolidated table present after the summary count table
- [ ] Q1 and Q2 asked after the Held for Decision table
- [ ] If user answers Yes to Q2: deeper research run, updated Held for Decision table delivered, Q1 + Q2 + Q3 asked
- [ ] Discovery Q&A phase ran — any genuine ambiguity surfaced and resolved or waived before report delivered
