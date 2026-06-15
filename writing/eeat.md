# Metric Gamer — E-E-A-T Publishing Framework

A 31-step publishing lifecycle covering every stage from keyword discovery to long-term authority growth. Follow each phase in order for new content. Use the post-publish phases for ongoing optimisation.

---

## Phase 1: Discovery and Planning

### Keyword Discovery
- Prioritise low-to-medium difficulty gaming keywords first
- Focus on search intent, not just search volume
- Target long-tail phrases
- Use Reddit, Quora, and YouTube autocomplete for research
- Prioritise informational and transactional hybrid intent
- Build topical clusters
- Identify competitor weak spots

### SERP Research
- Analyse the top 5 ranking pages
- Identify search intent type
- Study competitor structure
- Identify information competitors are missing
- Analyse featured snippets
- Check schema usage
- Identify UX improvements
- Capture the People Also Ask box questions that appear for the primary keyword — these are high-priority FAQ seeds that Google already knows users are asking; targeting them directly improves FAQ section quality and PAA box placement potential

### Topic Qualification
- Publish within gaming topical authority
- Group articles into game clusters
- Strengthen semantic relevance
- Avoid unrelated topics
- Prioritise evergreen searches
- Maintain category consistency
- Focus on scalable topic ecosystems

---

## Phase 2: Content Planning

### Content Angle Planning
- Create unique positioning
- Include firsthand gameplay insights
- Focus on usefulness over fluff
- Add tactical recommendations
- Include comparisons and stats
- Improve depth beyond competitors
- Make content actionable

### Content Brief Creation
- Define primary keyword
- Define secondary keywords
- Define search intent
- Include required headings
- Include internal linking targets
- Add FAQ opportunities
- Predefine schema type

---

## Phase 3: Writing

### Title Optimisation
- Place primary keyword near the beginning
- Use emotional modifiers strategically
- Maintain title clarity
- Avoid clickbait mismatch
- Optimise for CTR
- Match search intent
- Keep titles concise

### URL Structure
- Keep URLs short
- Include primary keyword once
- Avoid unnecessary dates
- Maintain consistent hierarchy
- Use semantic URL structures
- Avoid parameter-heavy URLs
- Keep URLs readable

### Introduction Writing
- Answer the search query immediately
- Establish credibility early
- Mention gameplay experience
- Avoid generic intros
- Add a concise article summary
- Optimise for snippet extraction
- Maintain reader engagement

### Main Content Development
- Use experience-driven writing
- Add step-by-step clarity
- Break content into sections
- Use comparison tables
- Use bullet formatting
- Prioritise readability
- Add original insights
- Try to include keywords naturally every 150 words

### E-E-A-T Optimisation
- Include author names
- Add author bios
- Display expertise clearly
- Add last updated dates
- Cite official sources
- Use firsthand recommendations
- Avoid factual uncertainty

### Semantic SEO Optimisation
- Mention game entities naturally
- Use semantic keywords
- Include character references
- Mention mechanics naturally
- Include maps, classes, and bosses where relevant
- Strengthen contextual relevance
- Improve topical authority

### Header Structure
- Use one H1 only
- Structure H2s around intent
- Use H3s for subsections
- Add keyword variations naturally
- Improve scannability
- Optimise headers for snippets
- Maintain logical hierarchy

### Featured Snippet Optimisation
- Use concise answer blocks
- Use numbered lists where appropriate
- Use comparison tables
- Answer questions directly
- Add FAQ sections
- Optimise for People Also Ask boxes
- Maintain scannable formatting

---

## Phase 4: Technical

### Image Optimisation
- Compress images
- Use descriptive filenames
- Add optimised alt text
- Use WebP format
- Avoid oversized assets
- Optimise lazy loading
- Maintain image relevance

### Internal Linking
- Add 5–15 relevant internal links
- Use descriptive anchor text
- Link related guides
- Strengthen topical clusters
- Link pillar pages
- Maintain logical hierarchy
- Update old content with new links

### External Linking
- Link to official sources
- Use authoritative references
- Avoid excessive outbound links
- Maintain contextual relevance
- Open external links appropriately
- Avoid spammy sources
- Support trust signals

### FAQ Section
- Add FAQ sections strategically
- Use real user questions
- Keep answers concise
- Optimise for FAQ schema
- Use conversational phrasing
- Target People Also Ask opportunities
- Update FAQs regularly

### Schema Selection
- Use Article schema by default
- Add FAQ schema where applicable
- Use Review schema for reviews
- Use Breadcrumb schema
- Validate schema before publishing
- Avoid schema spam
- Maintain structured data consistency

### VideoGame Schema (game pages only)
- Use `VideoGame` schema type — not generic `Article` — on every game review page
- Nest a `Review` object inside `VideoGame` with `reviewRating > ratingValue` set to the Metric Gamer overall score
- Set `bestRating: 5` and `worstRating: 1` on the rating object so Google can interpret the scale
- Include `ratingCount` — even if it is 1 (the reviewer)
- Set `gamePlatform` to the verified platform list from the Game Details Card
- Set `genre` to the primary genre used in the scoring rubric
- Include `author` pointing to the reviewer name and URL if the author has a public profile
- `AggregateRating` generates star ratings in Google SERPs — this is the highest-impact schema addition for game review pages

---

## Phase 5: On-Page SEO

### Meta Title Optimisation
- Keep under 60 characters
- Include primary keyword
- Optimise for CTR
- Avoid keyword stuffing
- Maintain readability
- Match search intent
- Create curiosity naturally

### Meta Description Optimisation
- Keep under 155 characters
- Summarise the article benefit
- Include primary keyword naturally
- Encourage clicks
- Avoid misleading claims
- Maintain readability
- Match search intent

### Category and Tag Selection
- Use intentional categories
- Avoid excessive tags
- Maintain taxonomy cleanliness
- Organise by game or topic
- Prevent duplicate categorisation
- Keep architecture scalable
- Improve crawl structure

---

## Phase 6: Publishing

### WordPress Publishing Settings
- Verify canonical URLs
- Set featured image
- Check index/follow settings
- Verify breadcrumbs
- Ensure mobile responsiveness
- Check permalink structure
- Confirm sitemap inclusion

### Pre-Publish QA
- Spellcheck content
- Verify factual accuracy
- Test all internal links
- Validate schema (use Google Rich Results Test for VideoGame schema)
- Review formatting consistency
- Check mobile UX
- Core Web Vitals targets: LCP under 2.5s, INP under 200ms, CLS under 0.1 — test via PageSpeed Insights before publishing
- Compress and lazy-load all images; use WebP format to keep LCP low

### Publishing Timing
- Publish consistently
- Prioritise freshness for trending games
- Update evergreen content regularly
- Align with gaming trends
- Maintain content cadence
- Monitor seasonal spikes
- Plan around game launches

### Indexing Process
- Submit URLs to Search Console
- Request indexing for priority pages
- Verify sitemap inclusion
- Ensure crawlability
- Check robots.txt rules
- Monitor index status
- Resolve crawl issues quickly

---

## Phase 7: Post-Publish and Growth

### Post-Publish Optimisation
- Monitor rankings
- Improve low CTR titles
- Expand thin sections
- Add new internal links
- Refresh outdated sections
- Improve engagement metrics
- Optimise based on Search Console data

### Content Updating
- Refresh outdated gaming data
- Update patch and meta changes
- Maintain freshness signals
- Add new FAQs
- Improve weak sections
- Update screenshots if needed
- Expand based on ranking data

### Topical Authority Scaling
- Build pillar-cluster systems
- Cover all major search intents
- Expand game ecosystems
- Strengthen semantic relationships
- Publish supporting guides
- Maintain interlinking
- Dominate niche subtopics

### Performance Tracking
- Track rankings weekly
- Monitor indexed pages
- Analyse impressions
- Review CTR performance
- Monitor bounce rate
- Identify near-page-1 opportunities
- Measure topical growth

### Long-Term E-E-A-T Growth
- Build author authority
- Maintain editorial consistency
- Publish trustworthy content
- Develop a recognisable voice
- Strengthen brand reputation
- Maintain quality standards
- Build audience trust

### Brand Entity Monitoring
- Track where Metric Gamer is mentioned across external sources (Reddit, Discord, gaming forums, other sites) — these mentions are signals AI engines use when deciding which sources to cite
- Monitor whether the scoring methodology or individual scores are referenced by other writers or communities; treat this as a signal that the brand is becoming a citable source in the niche
- When a mention is found, note the platform and context — over time this shows which content types and platforms generate the most external reference
- Do not pursue manufactured mentions; this step is monitoring-only — organic mentions from quality content and community presence are the target
