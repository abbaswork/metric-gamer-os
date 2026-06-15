# Q3 2026 — To-Do
*Early start: June 2026. Tasks ordered by priority within each area.*

---

## Team — Cadence
*Do this in week 1 before anything else. Everything below depends on coordination being live.*

- [ ] Schedule the first weekly team sync and set it as a recurring calendar event
- [ ] Agree on a fixed agenda format for the sync: shipped / blocked / next week — 30 min max
- [ ] Create role checklists: dev publish checklist, content acceptance criteria, SEO keyword sign-off, social participation log
- [ ] Agree on where async written updates get posted (Slack, Notion, etc.) and confirm all roles know to submit before each sync

---

## Development

### Priority 1 — Fix the Foundation
*Nothing new gets published until these are done.*

**Broken links & pagination**
- [ ] Run a site crawl on metricgamer.com using Screaming Frog (free up to 500 URLs) or Ahrefs
- [ ] Export the full list of 404s and broken internal links
- [ ] For each 404, decide: restore the page or set a 301 redirect to the closest live page
- [ ] Fix /game/toukiden-2-review/ — restore or redirect
- [ ] Fix /game/monster-hunter-stories-remaster-review/ — restore or redirect
- [ ] Fix /blog/ — redirect to wherever blog content now lives
- [ ] Fix WordPress pagination so every game page is browsable without the search bar
- [ ] Re-run the crawl and confirm 0 broken links before moving on

**Core Web Vitals**
- [ ] Run PageSpeed Insights on mobile for the homepage and 2 game pages — record the LCP and CLS scores
- [ ] Identify which element is causing the LCP failure (usually the largest above-the-fold image)
- [ ] Compress and convert all page images to WebP format
- [ ] Add width and height attributes to all images to eliminate layout shift
- [ ] Defer or async any render-blocking resources flagged in PageSpeed diagnostics
- [ ] Re-run PageSpeed Insights and confirm LCP under 2.5s and CLS under 0.1 on mobile

**Author attribution**
- [ ] Log into WordPress and check how author assignment works (custom field, native author field, or theme option)
- [ ] Open a broken game page on the live site and use browser dev tools to find which template file is rendering the wrong author
- [ ] Fix the template or field mapping so the correct author shows on the live site
- [ ] Spot-check 5 live game pages to confirm the fix worked
- [ ] Write bio content for each active author: niche, genres covered, experience, social links
- [ ] Build an author profile page template in WordPress
- [ ] Create one author profile page per active author
- [ ] Link the author name on the game page template to their profile page
- [ ] Verify all byline links are working on the live site

**Methodology page**
- [ ] Draft the page content: how the rubric works, how player evidence is sourced (Steam, Reddit, forums), how authors are matched to genres
- [ ] Create a new WordPress page at /how-we-score/
- [ ] Add the link to the site footer
- [ ] Add the link to the game page template
- [ ] Submit the URL to Google Search Console

---

### Priority 2 — Visual & Structural
*Begin once Priority 1 is confirmed done.*

**Rubric score component**
- [ ] Screenshot an existing game page on the live site and list every element currently present
- [ ] Decide on the visual format: score bars or radar chart
- [ ] Identify which WordPress theme file controls the game page layout
- [ ] Write rubric level descriptions for each metric — what does a 1, 2, 3, 4, and 5 look like specifically (not generic)
- [ ] Build the visual score component in the theme
- [ ] Add hover or expand interaction so rubric level descriptions are visible
- [ ] Write the "how we scored this" transparency panel copy template (2–3 sentences, adaptable per game)
- [ ] Add the transparency panel to the game page template
- [ ] Test the template on 3 existing pages across different genres on mobile
- [ ] Retrofit all pages that passed the EEAT audit to the new template

**Static category pages**
- [ ] Confirm the 2 pillar genre verticals with the content team — URL structure must match their decision
- [ ] Design the URL structure (e.g. /racing-games/, /fps-games/)
- [ ] Check if WordPress already has a genre taxonomy or category structure to repurpose
- [ ] Build the category page template in the WordPress theme
- [ ] Create the 2 category pages and populate with relevant published reviews
- [ ] Verify both pages are not blocked in robots.txt
- [ ] Submit both URLs to Google Search Console

**Schema markup**
- [ ] Run all existing game page URLs through Google Rich Results Test — list which pass and which fail
- [ ] Decide on implementation method: Yoast custom schema, RankMath review schema, or manual JSON-LD
- [ ] Write the VideoGame + Review JSON-LD template with all required fields (name, author, datePublished, reviewRating, description, gamePlatform, genre)
- [ ] Implement the schema on all pages currently missing it
- [ ] Test each via Google Rich Results Test and fix any validation errors
- [ ] Add schema verification to the publish checklist

---

## Content

### Priority 1 — Audit & Fix Existing Content
*Complete this before writing anything new.*

**EEAT audit**
- [ ] Export a full list of all published game page URLs from WordPress
- [ ] Create an audit spreadsheet: URL | author | publish date | verdict
- [ ] Evaluate each page against 4 criteria: first-person play evidence, specific data cited, author niche relevance clear, unique player insight
- [ ] Mark each page: Pass / Rewrite / Remove
- [ ] Check GSC impressions for flagged pages — prioritise rewrites for pages that already have impressions
- [ ] Set up 301 redirects for all Remove pages to the closest live page or relevant pillar page
- [ ] Rewrite each Rewrite page to EEAT standard
- [ ] For each rewritten page: request re-indexing in Google Search Console via URL Inspection

**Meta titles and descriptions**
- [ ] Add every existing published page to the audit spreadsheet with its current meta title and description
- [ ] Mark each as compliant or not (title under 60 chars + emotive/question format; description under 155 chars + keyword + CTA)
- [ ] For each non-compliant page: research the primary keyword and confirm KD under 20 in Semrush
- [ ] Write a new meta title: emotive or question format, under 60 characters, ends with | Metric Gamer
- [ ] Write a new meta description: keyword included, tension-framed, CTA at the end, under 155 characters
- [ ] Update each page in WordPress via Yoast or RankMath

---

### Priority 2 — Affiliate Setup
*Set up accounts before writing new content — links need to go into reviews from day one.*

- [ ] Apply for the Humble Bundle affiliate program at partners.humblebundle.com
- [ ] Apply for Amazon Associates at affiliate-program.amazon.com
- [ ] Once approved for Humble Bundle: generate a tracking ID and create a test link for one game to confirm it works
- [ ] Once approved for Amazon Associates: generate a tracking ID and create a test link
- [ ] Install ThirstyAffiliates plugin (free) to manage affiliate links centrally
- [ ] Add a Humble Bundle link to every existing published game review
- [ ] Add affiliate link requirement to the publish checklist — no new review goes live without one
- [ ] At the 60-day mark: check Amazon account status and confirm 3 qualifying purchases have been made

---

### Priority 3 — New Content
*Begin only after the audit is complete and the Dev template is live.*

**Genre clusters**
- [ ] Decide and lock the 2 pillar genre verticals in the first team sync — this gates everything below
- [ ] Check scoring-system/metrics/genres/ and complete the rubric for vertical 1 if not done
- [ ] Complete the rubric for vertical 2 if not done
- [ ] Research the pillar page keyword for vertical 1 and confirm KD under 20 in Semrush
- [ ] Research the pillar page keyword for vertical 2 and confirm KD under 20
- [ ] Identify 4 games for supporting reviews in vertical 1
- [ ] Identify 4 games for supporting reviews in vertical 2
- [ ] Write pillar page for vertical 1
- [ ] Write pillar page for vertical 2
- [ ] Write supporting review 1 of 4 for vertical 1
- [ ] Write supporting review 2 of 4 for vertical 1
- [ ] Write supporting review 3 of 4 for vertical 1
- [ ] Write supporting review 4 of 4 for vertical 1
- [ ] Write supporting review 1 of 4 for vertical 2
- [ ] Write supporting review 2 of 4 for vertical 2
- [ ] Write supporting review 3 of 4 for vertical 2
- [ ] Write supporting review 4 of 4 for vertical 2
- [ ] Add internal link to the pillar page in every supporting review
- [ ] Update both pillar pages to link back to all their supporting reviews

**Buyer-intent pieces**
- [ ] Research keyword for the curated list format (e.g. "best [genre] games for [context]") — confirm KD under 20
- [ ] Research keyword for the "worth it" format (e.g. "is [game] worth it in 2026") — confirm KD under 20
- [ ] Research keyword for the comparison format (e.g. "[game A] vs [game B]") — confirm KD under 20
- [ ] Write the curated list piece — include a Humble Bundle link for each game listed
- [ ] Write the "worth it" verdict piece — include a Humble Bundle link
- [ ] Write the comparison piece — include Humble Bundle links for both games
- [ ] Publish all 3 with correct meta title, description, schema, and internal link to the relevant pillar page

---

## SEO

### Priority 1 — Clean the Profile
*Submit disavow in week 1. It takes 60 days to reflect — the clock starts now.*

**Backlink audit and disavow**
- [ ] Log into Moz Link Explorer or Ahrefs and run a full backlink export for metricgamer.com
- [ ] Sort by spam score (Moz) or low DR + irrelevant niche (Ahrefs) and flag every suspicious domain
- [ ] For each flagged domain: open the site and confirm it is spam, a link farm, or unrelated
- [ ] Build the disavow file in Google format (domain:example.com — one domain per line)
- [ ] Upload the disavow file via Google Search Console → Disavow Links
- [ ] Record the exact submission date
- [ ] Set a calendar reminder for 60 days post-submission to re-check spam score in Moz

**De-indexed pages**
- [ ] Open Google Search Console → Pages / Coverage report
- [ ] Export all excluded or not-indexed URLs — note the reason Google gives for each
- [ ] Categorise each: Rewrite and restore / 301 redirect / Leave excluded
- [ ] Coordinate with Content on any restore pages that need rewriting
- [ ] Set up 301 redirects for all redirect pages in WordPress
- [ ] For each restored page: go to GSC → URL Inspection → Request Indexing
- [ ] Set a 2-week calendar reminder to check indexing status for each submitted URL

---

### Priority 2 — Build Authority

**Internal linking**
- [ ] Create a spreadsheet mapping every published game page URL to its genre and pillar cluster
- [ ] For each existing page in a cluster: add a contextual link to the pillar page in the body of the review
- [ ] For each pillar page: add links to all its supporting reviews
- [ ] Identify orphan pages (no internal links pointing to them) and connect them to a cluster or 301 redirect
- [ ] Add internal linking to the publish checklist: every new review links to its pillar before publishing; pillar updated within 48 hours of new review going live

**10 referring domains — outreach**
- [ ] Create a tracking spreadsheet: source type | target URL | status | date acquired
- [ ] Reddit: identify specific existing threads in the 3 target subreddits where an MG review directly answers the question — hold to share after the Social 30-day participation period
- [ ] Medium: identify which MG articles will be syndicated — confirm canonical URL will be set to metricgamer.com on each
- [ ] List every indie game MG has reviewed — find each developer's contact email or social DM
- [ ] Draft a personalised outreach email (3–4 sentences: introduce MG, link to their game's review, ask if they'd like to share it)
- [ ] Send outreach to at least 5 developers
- [ ] Update the tracker each time a referring domain is confirmed live

---

## Social

### Priority 1 — Start Immediately
*Reddit is time-gated. The 30-day participation window must start now or link sharing is pushed back.*

**Reddit — 30-day participation clock**
- [ ] Log into the MG Reddit account and check its age and current karma score
- [ ] If under 30 days old or under 100 karma: start by commenting on general gaming discussions — nothing MG-related
- [ ] Subscribe to r/patientgamers, r/ShouldIBuyThisGame, and the genre sub for the first pillar vertical
- [ ] Set a weekly target: 3 substantive comments per subreddit (9 total per week — answers, opinions, no link posts)
- [ ] Keep a participation log: date | subreddit | comment topic | upvotes
- [ ] After 30 days: review comment history and karma before sharing any MG content
- [ ] When sharing after 30 days: only in direct response to a relevant question, never as a standalone post

**Medium**
- [ ] Log into the MG Medium account and confirm access (bio complete, link to metricgamer.com, profile image set)
- [ ] Find the canonical URL field in Medium: each story → Settings → Advanced Settings → Canonical URL
- [ ] Search for active gaming publications with 1,000+ followers — identify 3 target publications and read their submission guidelines
- [ ] Plan 4+ article topics for Q3 (opinion or explainer only, not game reviews)
- [ ] Write article 1 (minimum 1,200 words), set canonical URL to the relevant metricgamer.com page, submit to the target publication
- [ ] Repeat weekly: write → set canonical tag → submit to publication
- [ ] Check referral traffic from Medium monthly in GA4 under Traffic Sources

---

### Priority 2 — Ongoing

**Steam Curator**
- [ ] Log into the MG Steam Curator account and confirm credentials are working
- [ ] Review the curator profile — update bio, banner, and description if out of date
- [ ] List all existing MG game pages and identify which games are missing from the Steam Curator feed
- [ ] Write Steam Curator recommendations for all unrepresented MG pages (short, in Steam tone, not copy-pasted from the review)
- [ ] Add to the publish checklist: update Steam Curator within 7 days of every new game page going live

**External byline**
- [ ] Research 3–5 platforms that accept gaming contributor submissions — note whether bio links or in-body links are permitted
- [ ] Shortlist 2 platforms that fit MG's voice
- [ ] Write a pitch email for each (3–4 sentences: who you are, what MG covers, specific article idea)
- [ ] Send pitches to both platforms
- [ ] Once accepted: write a piece specifically for that platform with a contextual backlink to a relevant MG page in the body or author bio
- [ ] Confirm the published piece includes the backlink and record the live URL in the referring domain tracker

**GitHub README**
- [ ] Read the current README.MD in metric-gamer-os
- [ ] Write a new README: what MG is, how the rubric works, what a 1–5 score means, which rubric sets exist, how player evidence is sourced, how authors are matched
- [ ] Add a directory map so someone outside the project can navigate the repo without guidance
- [ ] Have someone outside the project read the draft and confirm they understand the methodology without any explanation
- [ ] Revise based on their feedback, commit and push to the GitHub repo
