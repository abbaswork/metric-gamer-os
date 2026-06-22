# Metric: Netcode & Server Quality
**Genre:** Fighting — Multiplayer Niche
**Type:** Qualitative (community consensus)
**Direction:** Complaint — 5 = online play is indistinguishable from local, 1 = online makes the game unplayable

## Why This Matters

Netcode was named explicitly in Reddit's "what makes a good fighting game" discussions as a top-tier factor. In fighting games specifically, the online experience isn't one of many modes — for most players, it IS how the game is played. Frame-perfect inputs mean that even small amounts of input delay or packet loss destroy the gameplay in ways that don't affect other genres.

The mechanism is specific: delay-based netcode adds 3–4 frames of input lag to both players — about 50–67ms at 60fps. At fighting game pace, this is the difference between landing a punish and missing it. The experience: "The delay feels like your character is underwater." Rollback netcode eliminates that: "Your own inputs are never delayed. Zero frames of added input lag" — the system predicts the opponent's input and corrects when wrong, resulting in occasional visual artifacts but never the systemic lag that defines delay-based play.

The practical benchmark: "A game with rollback at 150ms ping feels better than a game with delay at 50ms ping." Under 80ms, rollback corrections are nearly invisible. At 200ms+, they become disruptive. Delay-based has no equivalent threshold — degradation is linear and permanent. As superjumpmagazine.com frames it: "Perception is reality, and so where traditional approaches had each player second-guessing their own gaming reality, rollback tries to sync player experiences as closely as possible."

## Sources

- **research.md — Reddit (What makes a good fighting game):** "netcode" named directly as a key quality factor
- **research.md — Google Trends:** brawlhalla crossplay (27 search interest, +30%), brawlhalla online (43, +90%), brawlhalla ranked (44, -2)
- **iflpvp.com — Rollback vs Delay Netcode Explained:** "Your own inputs are never delayed. Zero frames of added input lag"; "The delay feels like your character is underwater"; "A game with rollback at 150ms ping feels better than a game with delay at 50ms ping"; ping thresholds (under 80ms = nearly invisible, 200ms+ = disruptive)
- **superjumpmagazine.com — The Importance of Rollback Netcode:** "it would have been the same timing for both of us as if we were playing in the same room"; "Perception is reality, and so where traditional approaches had each player second-guessing their own gaming reality, rollback tries to sync player experiences as closely as possible"

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | Rollback netcode or equivalent that produces near-local play quality at normal connection levels. Matches are stable across regions. Crossplay functions without degrading the experience. Servers are consistently available. | You stop noticing you're playing online. The connection quality removes itself from the conversation. |
| 4 | Reliable online with minor issues at poor connections. Matches are mostly stable. Input lag is present but consistent enough to adjust to. Crossplay works where available. | Online is a solid experience. You'll occasionally notice the connection but it doesn't define the session. |
| 3 | Functional online that works under good conditions but degrades noticeably at average connection quality. Delay-based netcode produces a perceivable lag floor. Matchmaking is slow or limited in region options. | Online works for players with strong connections. Others will hit the wall quickly. |
| 2 | Unreliable online with frequent disconnects, visible input lag under normal connections, or desync issues. Rollback is absent and delay-based performance is poor. Crossplay causes additional instability. | Online feels like a gamble. You get a good match occasionally but can't count on it. |
| 1 | Online is effectively unplayable. Constant disconnects, severe input delay, or server instability make matches incompletable. The online mode undermines the entire competitive experience. | The online mode is a liability. Playing locally is the only reliable option. |
