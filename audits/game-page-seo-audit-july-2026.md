# Game Page — SEO, GEO, Image & Accessibility Audit — July 2026

**Conducted:** 2026-07-07
**Scope:** Game page template — SEO, GEO, image SEO, and accessibility
**Slug audited:** `rainbow-six-mobile` (`http://localhost:3000/game/rainbow-six-mobile/`)
**Cross-referenced:** `eeat-geo-audit-june-2026.md`, external SEO engagement (`audits/seo/`)

---

## Summary

| Pass | Status | Findings |
|---|---|---|
| Pass 1 — Headings & Landmarks | ✅ mostly passing | 1 minor remaining (metric H3 casing — WP content fix) |
| Pass 2 — GEO / Server Content | ✅ fixed 2026-07-08 | Score framing sentence in verdict + sidebar |
| Pass 3 — Structured Data | ⚠️ 1 open | Breadcrumb fixed; test FAQ entry still live in WP |
| Pass 4 — Image SEO | ✅ fixed 2026-07-08 | Alt texts now derive from card title |
| Pass 5 — Meta / Breadcrumbs / Indexability | ⚠️ 1 open | Breadcrumb + `og:locale` fixed; brand suffix in Yoast still open |
| Pass 6 — Accessibility | ✅ fixed 2026-07-08 | MetricDeepDive animation removed entirely |
| Pass 7 — Curl Verified | ✅ pass with notes | 308→200 redirect correct; preload confirmed for hero image |

---

## Gaps Found

### Critical

**Gap 1 — Score not framed as a citable sentence (GEO)**
The score "4.1 out of 5 — Strong" appears in the sidebar but is never expressed as an attributed sentence in the body copy. AI engines extracting this page cannot cite "Metric Gamer scores Rainbow Six Mobile 4.1/5" because that sentence does not exist in the HTML. This was Gap 1 in the June 2026 EEAT audit and remains open.
*Severity: Critical*
*Fix: Add a short framing sentence near the score in `GameSidebar.tsx` — e.g. `Metric Gamer scores {gameTitle} {score}/5 across our player-validated metric breakdown.` — so it always renders in static HTML regardless of rubric match.*
*Status: ✅ Fixed 2026-07-08 — verdict sentence in `GameInfo.tsx` now reads "Metric Gamer scores {gameTitle} {score}/5 —" inline before the editorial quote; `RubricSummary.tsx` verdict phrase also includes the score; sidebar displays `{score}/5` visually.*

---

### High

**Gap 2 — Meta title missing brand suffix**
Live title is "Rainbow Six Mobile Review". The write-game-page spec requires "ends with ` | Metric Gamer`" and the code fallback in `generateMetadata()` includes it — but the Yoast-authored title in WordPress overrides the fallback and omits it. This affects SERP brand recognition and CTR.
*Severity: High*
*Fix: Content/Yoast fix — update the meta title for this game (and audit all others) to end with ` | Metric Gamer`. Not a code change.*
*Status: New*

**Gap 3 — Similar game card images have non-descriptive alt text ("Left" / "Right")**
The two similar game card images render with `alt="Left"` and `alt="Right"`. These are placeholder values from the `ContentCard` component's left/right image slots. Both are indexed by Google and visible to screen readers as meaningless labels.
*Severity: High*
*Fix: `ContentCard` should derive alt text from the game title or card title — e.g. `alt="{game.title} — similar game"` — not a generic directional label. Code fix in `ContentCard.tsx`.*
*Status: ✅ Fixed 2026-07-08 — `GameBlogHeader.tsx` now accepts a `title` prop; both images use `"{title} — featured game"`. `ContentCard.tsx` passes `title={title}` to `GameBlogHeader`.*

**Gap 4 — Test FAQ entry present in live page**
The FAQPage schema and rendered FAQ section include: `"Test Custom FAQ" / "This is the sample answer"`. This is test content published via the WordPress ACF gameFaqs repeater. It appears in both the visible FAQ and the JSON-LD FAQPage schema.
*Severity: High*
*Fix: Content cleanup — remove the test FAQ entry from the Rainbow Six Mobile post in WordPress.*
*Status: New — content issue*

**Gap 5 — Breadcrumb label/URL mismatch**
Both the visible breadcrumb and BreadcrumbList schema show `name: "Games"` pointing to `https://www.metricgamer.com/metrics`. The label "Games" does not match the URL path `/metrics`. This is a semantic inconsistency that Google treats as a quality signal.
*Severity: High*
*Fix: Align the label and URL — either rename the breadcrumb item to "Metrics" to match the URL, or change the URL to `/games/` if that route is intended to be the games hub. Decision needed before implementing.*
*Status: ✅ Fixed 2026-07-08 — label renamed to "Metrics" in `page.tsx` breadcrumbs array. Applies to both visible breadcrumb nav and BreadcrumbList schema (same array feeds both).*

---

### Medium

**Gap 6 — `og:locale` missing**
No `og:locale` meta tag is present in the page HTML. All other OG tags are present. Missing locale can affect how social platforms interpret the content language/region.
*Severity: Medium*
*Fix: Add `og:locale` to `generateMetadata()` in the game page template — value should be `en_US` or `en_GB` depending on the site's target market.*
*Status: New*

**Gap 7 — Meta description lacks CTA and opens with throat-clearing**
Current description: "Welcome to our Rainbow Six Mobile review; a tactical mobile shooter with strategic 5v5 gameplay, operators, and team-based multiplayer."
- Starts with "Welcome to our" — generic opener, not keyword-forward
- No CTA ("Read to find out", "We scored every metric", etc.)
- Semicolon structure is less punchy than a direct tension/question frame
*Severity: Medium*
*Fix: Content/Yoast fix — rewrite per the write-game-page spec: primary keyword in first half, tension or question framing, CTA close. Not a code change.*
*Status: New — content issue*

**Gap 8 — Similar games intro sentence broken by multi-value genre string**
The `SimilarGames` component was updated today (2026-07-07) to inject `genre` into the intro sentence. For Rainbow Six Mobile, the genre value is "FPS, free to play, mobile, multiplayer" — a comma-separated string — which renders as: *"Discover more FPS, free to play, mobile, multiplayer games like Rainbow Six Mobile..."*. This reads as broken copy and could hurt CTR on the section.
*Severity: Medium*
*Fix: In `SimilarGames.tsx`, extract only the first genre segment before the first comma — `genre.split(',')[0].trim()` — so it reads "Discover more FPS games like Rainbow Six Mobile..."*
*Status: ✅ Fixed 2026-07-07 — `genre.split(',')[0].trim()` applied in `SimilarGames.tsx`.*

**Gap 9 — MetricDeepDive score bar has no `prefers-reduced-motion` handling**
`MetricDeepDive.tsx` animates metric score bars with `initial={{ width: 0 }}` + `whileInView`. The bar itself is decorative (scores are visible as numbers), so this is low SEO impact, but the animation forces motion on every user including those with vestibular disorders.
*Severity: Medium (accessibility)*
*Fix: Add `useReducedMotion()` from `framer-motion` and skip the bar animation when it returns `true`.*
*Status: ✅ Fixed 2026-07-08 — animation removed entirely from `MetricDeepDive.tsx`. `"use client"` and `framer-motion` import also removed; bars now render at final width as a static Server Component.*

---

### Low

**Gap 10 — Hero image alt text is the title only**
Hero image has `alt="Rainbow Six Mobile"` — the game title. Functional and not empty, but misses an opportunity to describe the content (e.g. "Rainbow Six Mobile tactical 5v5 mobile shooter").
*Severity: Low*
*Fix: The hero image alt comes from `alt={title}` in `GameHeader.tsx`. A per-game image description field in WordPress would allow richer alt text without hardcoding. Lower priority than Gap 3.*
*Status: New*

**Gap 11 — Metric H3 casing inconsistency**
One metric heading renders as "Rainbow Six Mobile Weapon selection Review" (lowercase "s") vs all others which are Title Case ("Gunplay Review", "Co-op and Multiplayer Review"). This is a data/CMS content issue.
*Severity: Low*
*Fix: Content fix — update the metric label in WordPress for this game to use consistent casing.*
*Status: New — content issue*

---

## Verified Passing

| Item | Confirmed |
|---|---|
| Single `<h1>` with entity name + "review" keyword | ✅ "Rainbow Six Mobile Review" |
| All H2s include entity name | ✅ All 10 sections correctly named |
| FAQ accordion: `<h3>` wraps `<button aria-expanded aria-controls>` | ✅ Confirmed in source and HTML |
| FAQ answers always in DOM (CSS collapse, not JS unmount) | ✅ `grid-rows-[0fr]` pattern — 5 answers present in static HTML |
| `GameHeader` Framer Motion: `initial={false}` | ✅ Not hiding content from bots |
| Hero image `priority` prop | ✅ Confirmed via `<link rel="preload" as="image">` in `<head>` |
| All images use `next/image` (no bare `<img>`) | ✅ 8 images, all `data-nimg` |
| VideoGame + Review + BlogPosting + FAQPage + BreadcrumbList schema | ✅ All 5 types present |
| `reviewRating.bestRating: 5, worstRating: 1` | ✅ Matches /5 scale |
| `author` as Person, `publisher` as Organization — both set | ✅ |
| Canonical URL: absolute, trailing slash | ✅ `https://www.metricgamer.com/game/rainbow-six-mobile/` |
| OG tags: title, description, url, type, image | ✅ All 5 present |
| Twitter card: all 4 tags present | ✅ |
| Visible breadcrumb nav present | ✅ "Home › Metrics › Rainbow Six Mobile" (label updated 2026-07-08) |
| Decorative icons `aria-hidden="true"` in GameSidebar | ✅ All 6 icons |
| FAQ trigger focus-visible ring | ✅ `focus-visible:ring-2 focus-visible:ring-[#F6CA56]` |
| 308 redirect to trailing-slash URL works | ✅ |

---

## Open Items Carried Over from June 2026 EEAT Audit

| Item | Status |
|---|---|
| Score framing paragraph in Overall Score section (Gap 1) | ✅ Fixed 2026-07-08 |
| Table of Contents | ✅ Fixed — `TableOfContents` component live |
| "Who Is This Game For?" block | ✅ Fixed — `WhoIsThisFor` component live |
| /5 score label definition | ✅ Partial — "Strong" label renders via `getScoreLabel()` |
| Methodology page `/how-we-score/` | ⚠️ Not audited — requires separate check against dev to-do |
| VideoGame schema with AggregateRating | ✅ Fixed — `Review` schema with `reviewRating` present |

---

## Deferred to User / Chromatic

- `text-gray-400` contrast ratio on `#160026` background (sidebar "Metric Score" label) — needs browser/AT verification
- OG and Twitter image URLs use EC2 internal IP in local dev — verify production Yoast outputs the correct CDN URL before marking as resolved
- Focus trap behaviour and keyboard navigation in `BuyNowDialog` — known existing gap, needs browser testing

---

## Priority Fix Order

| Priority | Gap | Type | Status |
|---|---|---|---|
| 1 | Gap 8 — Similar games genre string regression | Code fix | ✅ Fixed 2026-07-07 |
| 2 | Gap 1 — Score framing sentence | Code fix | ✅ Fixed 2026-07-08 |
| 3 | Gap 3 — Similar game card alt text | Code fix | ✅ Fixed 2026-07-08 |
| 4 | Gap 5 — Breadcrumb label/URL mismatch | Code fix | ✅ Fixed 2026-07-08 |
| 5 | Gap 9 — MetricDeepDive animation | Code fix | ✅ Fixed 2026-07-08 |
| 6 | Gap 4 — Test FAQ entry in production | Content/WP | ❌ Open — remove in WordPress |
| 7 | Gap 2 — Meta title missing brand suffix | Content/Yoast | ❌ Open — update in Yoast per game |
| 8 | Gap 6 — `og:locale` missing | Code fix | ✅ Fixed 2026-07-08 — `locale: "en_US"` added to `openGraph` in `generateMetadata()` |
| 9 | Gap 7 — Meta description weak | Content/Yoast | ❌ Open — rewrite in Yoast per game |
| 10 | Gap 10 — Hero alt text | Future CMS field | ❌ Open — low priority |
| 11 | Gap 11 — Metric H3 casing | Content/WP | ❌ Open — update metric label in WP |
