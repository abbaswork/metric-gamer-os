# Skill Schema — Format Definition

This document defines the standard structure every Metric Gamer skill must follow. It is the source of truth for building and validating skills in the portal.

A skill is a repeatable, structured task that Claude executes with defined inputs, knowledge context, research methods, and quality gates.

---

## Skill File Structure

Each skill lives in its own folder under `skills/`:

```
skills/
├── skill-schema.md              ← this file
└── [category]/
    └── [skill-name]/
        ├── readme.md            ← skill definition (human-readable)
        ├── connector.json       ← knowledge hub connectors + importance weights
        └── interface.py         ← Phase 1: collect inputs from user
```

---

## readme.md — Skill Definition

Every skill readme must contain the following sections in order:

### 1. Purpose
One paragraph. What this skill produces and why it exists.

### 2. Knowledge Connectors
Reference to `connector.json`. A summary table of which knowledge hubs are connected and their importance weight (1–5).

```markdown
| Knowledge Hub | File | Importance |
|---|---|---|
| [Hub Name] | path/to/file.md | [1–5] |
```

**Importance scale:**
| Weight | Meaning |
|---|---|
| 5 | Primary bias anchor — strongly shapes output direction |
| 4 | High influence — referenced throughout the task |
| 3 | Supporting context — used to sanity-check alignment |
| 2 | Background awareness — informs tone/framing only |
| 1 | Weak signal — referenced only if directly relevant |

### 3. Inputs
A table of all inputs the skill requires or accepts.

```markdown
| Input | Type | Required | Description |
|---|---|---|---|
| [name] | string / enum / boolean | Yes / No | What it is and how it affects the output |
```

### 4. Execution Flow

Show the two-phase flow so the skill is unambiguous to run:

```
Phase 1 — interface.py    Collect inputs from the user
     ↓
Phase 2 — Claude          Run web searches → extract raw player quotes → generate output
```

### 5. Interface Script
Reference to `interface.py`. One line on what it collects and how its output is passed to Claude.

### 6. Web Search Strategy
Define exactly how Claude should research before generating output. Must specify:
- Blocked domains (editorial, review, and aggregator sites)
- Search batches with exact query templates (use `{input}` placeholders)
- What to extract from results (verbatim quotes, source attribution, praise vs complaint)
- What to skip

The goal is raw player voice, not editorial summaries. Queries should be designed to surface community discussion threads, not review sites.

### 7. Acceptance Criteria
A checklist that applies at the **start** (to guide the task) and the **end** (to validate output before submitting). Written as `- [ ]` items.

Every item must be:
- Binary — either met or not met
- Specific to this skill's output
- Testable by re-reading the output alone

---

## connector.json — Schema

```json
{
  "skill": "[skill-id]",
  "connectors": [
    {
      "id": "[knowledge-hub-id]",
      "file": "path/to/knowledge/file.md",
      "importance": 1,
      "purpose": "One sentence — why this knowledge is connected and what it influences in the output."
    }
  ]
}
```

**Rules:**
- `importance` is an integer from 1–5
- `file` is relative to the `metric-gamer-os/` root
- `purpose` must explain the *influence*, not just describe the file
- At least one connector must have importance ≥ 4
- Maximum 5 connectors per skill (keep context focused)

---

## interface.py — Interface Script

A lightweight CLI that:
1. Prompts the user for each required (and optional) input
2. Validates inputs where appropriate
3. Prints a structured block to stdout that the portal passes to Claude

The script collects inputs only — no research, no generation.

**Standard output format:**

```
SKILL: [skill-id]
INPUTS:
  [input_name]: [value]
  [input_name]: [value]
```
