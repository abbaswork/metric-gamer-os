# Skill: Write Checklist

## Purpose

Given a genre (and optionally a sub-genre) and metric name, produce a 5-band metric score checklist following the Checklist Writing Guide. The checklist is derived entirely from the existing rubric — no web research required. The skill supports two process modes: review (draft shown for user approval before writing to file) and direct (written to file immediately after generation).

**Knowledge connectors:** see `connector.json`

| Knowledge Hub | File | Importance |
|---|---|---|
| Checklist Writing Guide | scoring-system/checklist-writing-guide.md | 5 |
| Scoring System Overview | scoring-system/overview.md | 2 |

---

## Requirements

- **[Hard]** The rubric.md for the target metric must exist before the skill runs — if the file is not found at the expected path, stop and report the path checked.
- **[Hard]** The Checklist Writing Guide must be loaded and read in full before any checklist is generated.
- **[Soft]** In review mode, the draft must be explicitly approved by the user before being written to file — never write without approval in review mode.

---

## Inputs

| Input | Type | Required | Description |
|---|---|---|---|
| `genre` | string | Yes | The genre folder name (e.g. fighting, shooters, rpg) |
| `sub_genre` | string | No | The sub-genre folder name (e.g. fps, cozy, party). Leave blank if the metric sits at genre level. |
| `metric` | string | Yes | The metric folder name (e.g. gunplay, campaign-structure, character-development) |
| `process` | enum | Yes | `review` = show draft for approval before writing; `direct` = write to file immediately |

---

## Execution Flow

```
Phase 1 — interface.py    Collect sub_genre (optional), genre, metric, process

     ↓

Phase 2 — Claude          Load checklist-writing-guide.md in full.
                          Locate and read the rubric at:
                            With sub-genre:    scoring-system/genres/{genre}/sub-genres/{sub_genre}/{metric}/rubric.md
                            Without sub-genre: scoring-system/genres/{genre}/{metric}/rubric.md
                          If rubric not found, stop and report the path checked.

     ↓

Phase 3 — Claude          Identify the thread — the single core dimension all five bands
                          measure. State it internally before writing.

     ↓

Phase 4 — Claude          Generate the 5-band checklist following the writing guide.

     ↓

Phase 5a (review mode)    Present draft to user. Wait for explicit approval or revision
                          instructions. Do not write to file until approved.

Phase 5b (direct mode)    Write checklist directly to:
                            With sub-genre:    scoring-system/genres/{genre}/sub-genres/{sub_genre}/{metric}/checklist.md
                            Without sub-genre: scoring-system/genres/{genre}/{metric}/checklist.md

     ↓

Phase 6 — Claude          Validate against Acceptance Criteria.
                          In review mode: validate after user approval, before writing.
```

---

## Interface Script

`interface.py` — collects `sub_genre` (optional), `genre`, `metric`, and `process`, then prints the structured input block for Claude.

---

## Web Search Strategy

Not applicable. Checklists are derived entirely from the existing rubric — no web research is required or permitted.

---

## Acceptance Criteria

- [ ] Checklist Writing Guide was loaded before generating the checklist
- [ ] The rubric was read in full before generating the checklist
- [ ] The thread (single core dimension) was identified from the rubric before writing any band
- [ ] Each band is a single, complete, grammatically correct sentence
- [ ] No band uses jargon (throughline, competent, overarching, consistently engaging, archetypes, routing choices, accessible routes, or similar)
- [ ] No band is a comma splice — two independent clauses joined by a comma is not a sentence
- [ ] No em-dashes anywhere in the checklist
- [ ] All five bands measure the same core dimension at decreasing intensity
- [ ] The defining characteristic of each rubric band is faithfully captured in the checklist sentence
- [ ] The checklist reads like a human game reviewer wrote it, not a rubric paraphrase
- [ ] In review mode: user explicitly approved the draft before it was written to file
- [ ] Checklist written to the correct path relative to the rubric
