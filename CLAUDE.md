# Metric Gamer OS — Downstream Relationship

This repo is the authoritative source for strategy/content data consumed by the sibling `metric-gamer-headless-app` repo (a Next.js app). See `../metric-gamer-headless-app/docs/guidelines/content-source-map.md` for the full map of which file here backs which feature there.

## Known Gap: Rubric Sync Is Manual
`scoring-system/genres/{genre}/sub-genres/{sub-genre}/{metric}/rubric.md` and the `niches/` equivalents are hand-copied once into `metric-gamer-headless-app/src/data/rubrics/*.ts`, with no build step or codegen keeping them in sync. This is a known, accepted gap for now — not something to fix unprompted.

- [ ] When a `rubric.md` (or a peer-review pass that changes one — e.g. merging/rewording score bands) is edited here, flag that the corresponding `src/data/rubrics/*.ts` in `metric-gamer-headless-app` is now stale and needs a matching manual update — don't assume someone will remember on their own.

## Skills and Slash Commands

All skills live in `.claude/skills/{skill-name}/`. All slash commands live in `.claude/commands/{command-name}.md`. The command file is the authoritative execution spec.

If a slash command fails to invoke (e.g. "Unknown skill" error), **read `.claude/commands/{command-name}.md` before executing anything manually.** Never improvise from memory or prior session context — executing without reading the spec risks wrong output format or skipped required phases.
