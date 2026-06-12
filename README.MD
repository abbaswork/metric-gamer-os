# 📊 Metric Gamer OS — Project Proposal

## 1. Overview

Metric Gamer OS is an AI-assisted content + SEO operating system designed to unify:

* Game review generation
* SEO keyword research
* Content planning and scheduling
* Community-driven ranking systems
* Editorial workflows
* Data-backed content production

The system treats **GitHub as the source of truth**, where structured knowledge, workflows (“skills”), and templates are stored, while execution is handled through Claude + MCP integrations and optional tooling layers.

The core principle:

> Workflows matter more than tools. Tools are interchangeable execution layers.

---

## 2. Core Design Principles

### 2.1 GitHub = Source of Truth

All stable system knowledge lives in:

* `/skills` → AI execution workflows
* `/knoweldge` → context around metric gamer
* `/templates` → content structures
* `/seo` → keyword rules and models
* `/content` → editorial systems
* `/metrics` → scoring logic
* `/community` → aggregation logic

Format constraints:

* `.md` → logic + human readable workflows
* `.json` → structured schemas
* `.csv` → dataset snapshots

---

### 2.2 Claude = Execution Engine (not UI)

Claude is used for:

* interpreting “skills”
* generating structured outputs
* transforming data
* executing workflows via MCP tools
* updating GitHub + data sources

---

### 2.3 MCP = Integration Layer

MCP tools provide controlled access to:

* GitHub (read/write repo)
* WordPress (content publishing)
* Google Sheets (optional Phase 3)
* External SEO APIs (future)

---

### 2.4 No premature abstraction

No portal, backend, or UI layer is introduced until workflows are validated in real usage.

---

## 3. System Architecture (Phase 1–3 Model)

```text
          Claude (Execution Layer)
                   ↓
        MCP Tooling / API Layer
     ┌─────────────┴─────────────┐
     ↓                           ↓
   GitHub                    Data Sources
 (source of truth)     (Sheets / CSV / APIs)
     ↓
Markdown / JSON / CSV workflow definitions
```

---

# 4. Phased Execution Roadmap

---

## 🟢 Phase 1 — Local GitHub Operating System (Foundation)

### Goal:

Establish all workflows, structures, and AI execution patterns locally.

### Scope:

* Everything stored in GitHub:

  * Markdown (skills, templates, processes)
  * CSV (datasets, keyword exports)
  * JSON (structured configs)

* Execution via:

  * VS Code + Claude Code
  * MCP GitHub integration

* No backend

* No portal

* No shared orchestration layer

---

### Deliverables:

* `/skills` framework defined
* Review generation workflow
* Keyword research workflow
* Content templates
* Metric scoring system (v1)
* Basic AI execution patterns validated

---

### Constraints:

* No centralized UI
* Manual execution per user
* No automation layer yet

---

## 🟡 Phase 2 — Skills & Workflow Formalization

### Goal:

Standardize all AI operations into reusable “skills”.

---

### Definition: Skill

A skill is a structured workflow definition containing:

* Inputs
* Outputs
* Required datasets
* Step-by-step reasoning process
* Validation rules
* Data update targets

---

### Example Skill Structure:

```text
/skills/keyword-research.md

Inputs:
- topic
- region
- intent type

Process:
1. Load keyword dataset
2. Cluster by intent
3. Score by relevance model
4. Filter duplicates
5. Output structured table

Outputs:
- keyword clusters (CSV/Sheet format)
- content opportunities
- priority score list
```

---

### Deliverables:

* Standard skill schema
* Skill registry
* Execution conventions for Claude
* Input/output validation rules
* Reusable workflow templates

---

## 🟠 Phase 3 — Integration Layer (Tools vs Workflows Separation)

### Goal:

Introduce external data systems only when workflow needs exceed GitHub capabilities.

---

### Decision principle:

> If structured human interaction is needed → use Google Sheets
> If structured system logic is needed → use GitHub
> If automation is needed → use MCP/API layer

---

### Options:

#### Option A — Google Sheets Integration

Used for:

* keyword databases
* content calendars
* editorial tracking

Via:

* MCP Google Sheets API integration

---

#### Option B — Code-based Data Layer

Replace Sheets where needed:

* JSON datasets
* CSV pipelines
* GitHub-based structured tables

---

### Deliverables:

* Sheet integration decision per workflow
* MCP-based read/write connectors
* Hybrid data model validation

---

## 🔵 Phase 4 — Portal + Orchestration Layer (Conditional)

### Trigger condition:

Only implemented if:

* multiple non-technical users require access
* workflow standardization becomes critical
* cross-tool execution complexity increases
* operational scaling requires central control

---

### Architecture:

```text
os.metricgamer.com (Frontend UI)
          ↓
Backend Orchestrator (Node/Python)
          ↓
Claude API + MCP tools
          ↓
GitHub + Sheets + WordPress
```

---

### Portal Responsibilities:

* Trigger skills
* Display outputs
* Show workflow status
* Provide single entry point for non-technical users
* NOT replace Sheets or GitHub UI

---

### Deliverables:

* Skill execution API (`runSkill`)
* Authentication layer
* Workflow dashboard
* Integration routing layer

---

## 🔴 Phase 5 — Automation Layer (Scheduled Intelligence)

### Goal:

Move from manual execution → autonomous execution.

---

### Features:

* Scheduled keyword research updates
* Weekly content generation
* Automated SEO audits
* Content performance updates
* Community ranking recalculations

---

### Architecture:

```text
Scheduler (cron / queue system)
          ↓
Orchestrator
          ↓
Claude execution
          ↓
GitHub + Sheets updates
```

---

# 5. Metric Gamer Use Cases (AI Workflows)

---

## 5.1 Game Review Generation Workflow

### Objective:

Generate structured, metric-based game reviews.

---

### Input:

* Game title
* Platform
* Genre
* Community data sources

---

### Process:

1. Load review template from GitHub

2. Fetch community sentiment (Reddit, forums, etc.)

3. Break game into metric categories:

   * Gameplay mechanics
   * Story depth
   * Replayability
   * Performance
   * Innovation
   * Value for money

4. Score each category (0–10)

5. Generate weighted final score

6. Produce structured review output

---

### Output:

```text
- Structured review (Markdown)
- Score breakdown table
- Pros / cons summary
- SEO-optimized article version
- Rank placement eligibility
```

---

## 5.2 Ranked List Generation Workflow

### Objective:

Generate ranked game lists using metric aggregation.

---

### Process:

1. Pull multiple game reviews
2. Normalize scoring weights
3. Apply ranking algorithm
4. Integrate community sentiment weighting
5. Produce ranked list with explanations

---

### Output:

* Top 10 lists
* Weighted ranking table
* Justification per rank
* SEO-ready article format

---

## 5.3 Keyword Research Workflow

### Objective:

Generate SEO-optimized keyword clusters for gaming content.

---

### Process:

1. Input topic (e.g. “best RPG games”)
2. Fetch keyword dataset (Sheets or CSV)
3. Cluster by intent:

   * informational
   * transactional
   * comparison
4. Score by:

   * volume
   * competition
   * relevance
5. Output structured clusters

---

### Output:

* Keyword clusters
* Priority list
* Content ideas mapped to clusters

---

## 5.4 Community Sentiment Aggregation

### Objective:

Incorporate external community opinions into scoring system.

---

### Sources:

* Reddit discussions
* Steam reviews
* Gaming forums
* YouTube sentiment summaries

---

### Process:

1. Scrape or API ingest sentiment data
2. Normalize sentiment scoring
3. Map sentiment to review metrics
4. Adjust final ranking weights

---

# 6. Key Architectural Decision Rule

At every stage:

> Prefer workflow clarity over tool complexity

---

# 7. Success Criteria

* All core workflows executable via Claude + GitHub (Phase 1–2)
* Skills are reusable and deterministic
* No dependency on UI for execution
* Clear separation between:

  * knowledge (GitHub)
  * data (Sheets/CSV)
  * execution (Claude)

---

If you want next, I can convert this into:

* a **real GitHub repo structure (folders + example files)**
* a **skill schema template you can immediately implement**
* or a **minimal MCP + Claude execution spec (actual API flow + pseudocode)**
