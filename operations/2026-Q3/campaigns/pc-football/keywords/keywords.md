# Q3 2026 — Keyword Research Log

---

## PC Football Campaign — Status: Awaiting Keyword Planner CSV

### Campaign Brief

**Topic:** Best PC football games 2026 — broad roundup angle, no single narrative tying the roster together.

**Game roster (user-provided, 2026-06-27):**
| Game | Type | Notes |
|---|---|---|
| eFootball | Free-to-play sim | Multi-platform — also covered on mobile in the `mobile-football` campaign. Keyword targeting here must stay PC/console-specific to avoid cannibalising that campaign. |
| Football Manager 24 | Management sim | PC/console |
| Football Life 25 | PES mod/patch | Fan-made patch for PES 2021 (Konami's last full release before pivoting to eFootball). PC only. Enthusiast/niche audience. |
| Smokepatch | PES mod/patch | Same category as Football Life 25 — competing/alternative patch. PC only. |
| FC 26 | Mainstream sim (EA) | PC/console |

**Target audience:** TBD — needs confirmation. Likely PC football/soccer gamers, including a sub-audience of former PES players looking for what replaced it (mods + eFootball + FC).

**Content constraints:** TBD — need to confirm which of these 5 MG can actually review (PES mods require owning PES 2021 + manually installing a patch — confirm access before committing to those two pages).

**Existing MG content in this space:**
- `mobile-football` campaign already has a draft for `efootball-2026-mobile.md` — mobile-specific. This campaign must target PC/console modifiers only for eFootball to avoid keyword overlap.
- No other existing football content found in `operations/2026-Q3/campaigns/`.

**Open flag:** Per `operations/2026-Q3/to-do.md`, "Vertical 2" for the keyword-formula-mandatory new content track has not been locked at team sync yet. This campaign has not been confirmed as Vertical 2 — treat as exploratory until decided.

---

### Step 1 — CSV Read
**Not yet performed.** No Keyword Planner CSV provided for this campaign yet.

**2026-06-27 — Google Trends file received, not usable for Step 1:** User shared `searched_with_top-searches_Worldwide_20260527-0702_20260627-0702.csv` — worldwide Google Trends relative interest (0-100) + trend %, not a Keyword Planner export. No monthly volume or competition columns, so it cannot feed the DA filter or shortlist.
- Dataset dominated by World Cup 2026 tournament intent-split: "world cup" (100, +650%), "fifa world cup" (51), national team queries (Portugal, Argentina, Mexico, Spain, etc.), "ronaldo," "messi" — real-world tournament searches, not football video games.
- Only relevant signal for this roster: "football manager" / "best football manager games" cluster (19, **-20%**) — declining, relevant to Football Manager 24 only.
- "best football games android/mobile" cluster present but mobile-specific — belongs to `mobile-football` campaign, not this one.
- Nothing present for eFootball, FC 26, Football Life 25, Smokepatch, or "pc football games."
- Still waiting on the actual Keyword Planner CSV seeded with `pc football games` to perform Step 1.

**Seed term needed:** `pc football games` (broad campaign topic — not a game name, not pre-filtered). This is genre + platform only (2 of the 4 required modifiers) — the planner export should be scanned for related queries carrying a 3rd modifier (free-to-play, career mode, multiplayer, management, simulation, 2026, etc.) per the Modifier Formula in `company/site/keyword-strategy.md`.

**Export spec (per `.claude/commands/keyword-research.md`):**
- Date range: last 12 months
- Full export, not filtered by volume or competition
- Required columns: keyword, avg monthly searches, 3-month change, YoY change, competition, competition indexed value
- Save to `operations/2026-Q3/campaigns/pc-football/keywords/`

### Next Steps
- [ ] Confirm target audience framing
- [ ] Confirm content constraints (can MG review Football Life 25 / Smokepatch — PES 2021 + patch install required?)
- [ ] User exports Keyword Planner CSV seeded with "pc football games" → place in this folder
- [ ] Run Step 1 (full CSV read + flags) once CSV is provided
- [ ] Apply DA filter (Step 2) and build shortlist (Step 3)
- [ ] User runs SERP checks on shortlist (Step 4)
- [ ] Resolve any close calls (Step 5)
- [ ] Confirm campaign anchor (Step 6)
- [ ] Build cluster map (Step 7)
- [ ] Assign game page keywords for each of the 5 games (Step 8)
