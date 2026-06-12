# Metric: Netcode Quality
**Sub-genre:** Fighting (Multiplayer / Competitive)
**Type:** Qualitative (community consensus)
**Direction:** Complaint — 5 = online play feels close to offline, 1 = netcode prevents competitive play

## Why This Matters

Rollback netcode became the non-negotiable standard for the fighting game community after a sustained campaign that ran through the early 2020s. The argument is straightforward: delay-based netcode introduces input lag that scales with connection quality, meaning your execution in practice mode doesn't match your execution online. Rollback netcode predicts opponent inputs and corrects when wrong, keeping local input delay constant and low regardless of connection. Games that adopted rollback — Guilty Gear Strive, Street Fighter 6, Tekken 8 — received immediate community praise for their online experience. Games that shipped with delay-based netcode in the same era faced sustained criticism from the FGC regardless of how good the underlying game was.

The community distinction is specific: rollback doesn't guarantee good online play, only that input latency is controlled. A poorly implemented rollback system still causes visual rollbacks during correction, and connection quality still matters. But delay-based netcode is now considered a failure to meet the basic standard the community established.

## Sources

- **Gameshub: "What is Rollback Netcode in fighting games?"** — "for dedicated fighting game fans, rollback netcode is one of the most important modern online multiplayer features a fighting game can have" (live source, confirmed via web search)
- **Rushdown Radio: "Netcode For Dummies"** — explains the mechanical difference between delay-based and rollback; documents delay-based as causing "input lag, freezes, and stutters that make outcomes feel unpredictable" (live source, confirmed via web search)
- **toptier.gg: "Great Fighting Games with Rollback Netcode"** — confirms SF6, GGStrive, Tekken 8, and KOF XV as community-praised rollback implementations (live source, confirmed via web search)
- **GitHub: "Netcode in Fighting Games"** — technical breakdown of how rollback works and why it's preferred by the competitive community (live source, confirmed via web search)
- **r/Fighters and r/Kappa** (training data) — community pressure for rollback adoption is well-documented; games shipping delay-based received immediate backlash regardless of other qualities

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | Rollback netcode with low and consistent input delay. Online play against same-region opponents feels close to offline. Frame-precise execution that works in practice mode works online. | Your online performance reflects your actual skill level. What you practiced is what you get. |
| 4 | Rollback netcode in place with occasional variance on weaker connections. Online play is reliable enough that skill is the limiting factor in most matches. Some visual rollbacks appear under poor connections but input feel is preserved. | You'll notice the connection on bad matchups but it won't stop you playing. Most online sessions feel fair. |
| 3 | Rollback with implementation issues, or delay-based netcode that performs acceptably on good connections. Online play is functional but execution-heavy techniques become less reliable. The gap between offline and online is felt in precision situations. | You'll adjust your gameplan for online play. Some of what you can do offline won't land consistently. |
| 2 | Delay-based netcode or poor rollback that introduces input lag as a constant presence even on good connections. Timing that works offline stops working online. The connection quality affects the match more than player skill in close situations. | Playing online means playing a different, worse version of the game. You'll stop going for your better options. |
| 1 | The netcode prevents competitive play. Matches are characterized by dropped inputs, frame stutters, or rollback visual artifacts severe enough that outcomes feel random regardless of skill level. | Online play isn't worth the time. The lag is the opponent. |
