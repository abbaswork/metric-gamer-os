# Ranking Page Duplicate Content & SEO Audit — June 2026

**Conducted:** June 25, 2026
**Scope:** Live audit of `/ranking/best-free-two-player-shooter-games-on-pc/` — why ranking pages cause game pages to drop out of the index, and why ranking pages themselves carry little independent SEO value.
**Method:** curl-only static HTML audit against the local dev server (no browser automation, per `metric-gamer-headless-app` project convention), cross-referenced against `company/site/keyword-strategy.md`, `.claude/skills/write-ranked-list/readme.md`, and the `metric-gamer-headless-app` codebase.
**Output:** Confirmed root cause, quantified scope, four supporting gaps, fix directions for dev + content-ops follow-up.

---

## Finding 1 — Duplicate content is a schema gap, not an authoring gap

The Ranking GraphQL query has no field of its own for a game entry's Pros/Cons/Verdict — it reads straight into the **Game post's own ACF fields**.

- `RankingBySlugQuery.ts` (`metric-gamer-headless-app/src/queries/ranking/RankingBySlugQuery.ts:14-37`) queries `... on Game { propertiesGame { theBad, theGood, verdict } }` — the identical shape `GameBySlugQuery.ts` uses for the standalone game page.
- `app/ranking/[slug]/page.tsx:92-96` maps that directly into `analysis.pros/cons/verdict`, which `DetailedBreakdown.tsx:196-224` renders as-is.

There is no ranking-entry-level text field anywhere in the schema to hold unique copy. Even a perfectly rewritten entry has nowhere to be saved today. This also means `write-ranked-list`'s rewrite output (the skill already requires no-shared-sentence rewriting) has no destination on the live site — the skill spec and the live schema are out of sync.

**Confirmed duplication:** Valorant's Pros, Cons, and Final Verdict are word-for-word identical across its game page and two separate ranking pages it appears on (`/ranking/best-free-two-player-shooter-games-on-pc/` and `/ranking/best-free-to-play-shooter-games-on-pc/`).

*Status: Root cause confirmed. Fix requires a schema change (new ACF sub-fields on the ranking's game-entry repeater) before any content fix is possible.*

---

## Finding 2 — Quantified scope

On the audited page, the duplicated "Detailed Breakdown" block (Pros/Cons/Verdict for all 4 games) is **3,923 of 7,171 characters of body text — 54.7%** of the page's visible copy. Only a 309-character, 2-sentence intro is unique to the page itself; the rest is nav/footer/related-rankings boilerplate.

*Status: Quantifies "not much SEO value being delivered through the content itself" — over half the page is someone else's page, and most of the remainder is site chrome.*

---

## Finding 3 — Hardcoded placeholder genre/year tags

`app/ranking/[slug]/page.tsx:88-89` hardcodes `tags: ["RPG", "Action"]` and `releaseDate: "2024"` for every game on every ranking, regardless of the game's real genre or release year. Counter-Strike 2 (released 2023) shows "2024" and "RPG Action" on the audited page.

This is a direct instance of the anti-pattern `error-states-checklist.md` already names as technical debt to phase out (silent placeholder fallbacks masking missing/unmapped data instead of pulling the real field). The real data already exists and is already queried elsewhere — `GameBySlugQuery.ts` pulls `platform`, `tags`, and `propertiesGame.releaseDate` for the standalone game page; the ranking query/mapping just never wires them through.

*Status: Pure plumbing fix, no AI/content work needed. Independent of Finding 1 — can be fixed immediately once scoped.*

---

## Finding 4 — No FAQ or methodology trust signal on ranking pages

Zero matches for "methodology" anywhere in the frontend. The Game page's FAQ (`GameFAQ.tsx`) is fully deterministic — 3 questions generated from existing structured fields (`platforms`, `isCrossPlatform`, `players`), no CMS authoring involved at all. The Ranking page has no equivalent component.

Per `company/persona/persona.md`, visible methodology is the #1 trust signal for "The Targeted Seeker" — the persona that lands cold on a ranking page from Google. Per `keyword-strategy.md`, Tier 3 FAQ content belongs on ranked lists too, not just game pages. Neither currently exists in code for this page type.

*Status: Net-new component, but most of it is reusable from existing structured data — see chat discussion for field-level breakdown.*

---

## Finding 5 — Intro accuracy and templating

The live intro contains a duplicated-word typo ("the best the best") and frames the list around "split-screen gaming... a cherished tradition" — none of the four games in this list (Warframe, Valorant, FragPunk, Counter-Strike 2) support local split-screen. Reads like a reused generic hook, not copy tailored to this list's actual niche, contradicting `write-ranked-list`'s "original copy, no sentences from any source" requirement for the intro specifically (which isn't the duplicated section — the intro is already meant to be unique, it's just low quality here).

*Status: Lowest priority per user — deprioritized to "do last."*

---

## Priority order (per user, 2026-06-25)

1. Schema/query fix (Finding 1) — prerequisite for everything else
2. FAQ + methodology addition to ranking template (Finding 4)
3. Hardcoded tag/year fix (Finding 3)
4. Intro accuracy/typo cleanup (Finding 5) — last

## Open Items

| Item | Status |
|---|---|
| New ACF fields on Ranking's game-entry repeater (`entryGood`, `entryBad`, `entryVerdict`) | **Done.** Added to the existing `selectGames` repeater rows. |
| `RankingBySlugQuery.ts` updated to select the new fields plus `tags`/`platform`/`crossplatform`/`releaseDate` on the nested Game | **Done.** |
| `app/ranking/[slug]/page.tsx` mapping updated: real tags/release date/platform/crossplatform, override fallback to game's own Pros/Cons/Verdict when entry fields are blank, `console.warn` per unbackfilled entry | **Done.** Fallback logic needed a second pass — ACF repeaters always keep one row present even when "empty" (`[{ goodPoint: null }]`), so the initial `.length > 0` check falsely treated blank rows as populated. Fixed by filtering for non-blank trimmed values instead of checking array length. |
| Ranking-level FAQ component (`RankingFAQ.tsx`), placed between At a Glance and Detailed Breakdown | **Done.** 5 questions, all derived from existing data (top game by score, free-to-play tag filter, crossplatform filter, platform union) plus one static, hardcoded methodology paragraph (doubles as the missing trust-signal fix from Finding 4). Split-screen question excluded per decision — no taxonomy field exists to answer it. |
| End-to-end verification with real entry data | **Done.** Valorant's WP test data (`Test Good 1/2`, `Test Bad 1`, `Test Entry Verdict`) renders correctly on the live page; Warframe/FragPunk/Counter-Strike 2 correctly fall back to their own game-page content since their override fields are still blank, pending backfill. |
| Wire real `releaseDate`/`tags`/`platform` into ranking query instead of hardcoded placeholders (Finding 3) | **Done**, as part of the same query/mapping update above. |
| `FAQPage` / structured data for ranking pages — currently zero JSON-LD on this page type | Not started — noticed during this work, flagged but out of scope unless prioritized |
| Intro typo + split-screen framing fix on this specific list (Finding 5) | Deferred — last in priority order, not yet done |
| Backfill of `entryGood`/`entryBad`/`entryVerdict` across existing rankings | Not started — content-ops task, expected to take a few weeks per user |
