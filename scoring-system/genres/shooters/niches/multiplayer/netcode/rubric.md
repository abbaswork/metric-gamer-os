# Metric: Netcode & Server Quality
**Sub-genre:** Shooters — Multiplayer
**Type:** Qualitative (community consensus)
**Direction:** Complaint — 5 = online play reflects skill accurately, 1 = netcode produces outcomes that don't match what happened

## Why This Matters

Netcode in shooters determines whether your actions in a match are what the server records. This matters differently from fighting games — in a shooter, the key issue isn't input latency but hit registration and server tick rate. A shot that lands on your screen needs to register as a hit on the server. At low tick rates or with poor server-side lag compensation, a shot that clearly hit on your client misses on the server, or vice versa. The community phrase for the worst version of this is "getting shot around corners" — dying to damage the server applied after your character had already moved to cover on your screen.

Apex Legends' server tick rate of 20Hz (compared to CS:GO's 128Hz in competitive) is the most cited modern reference for this problem in a large-scale game. Warzone's lag compensation model attracted sustained community criticism for producing situations where players with higher ping appeared to have an advantage because the game's lag compensation gave their actions server-side priority. Valorant's approach — proprietary servers, 128Hz tick rate, client-side prediction with server validation — is the documented positive reference for this generation of competitive shooters.

## Sources

- **r/apexlegends** (training data) — 20Hz tick rate debate is one of the game's most consistent community criticisms; "server tick rate" is a term that became mainstream in the Apex community's vocabulary
- **r/CODWarzone** (training data) — lag compensation advantage for high-ping players is among the most documented technical complaints in Warzone's history; "dying behind cover" is a phrase the community uses routinely
- **r/VALORANT** (training data) — Riot's 128Hz servers and server architecture are consistently cited as the positive standard; the competitive shooting community treats it as the benchmark for what servers should do
- **Battle(non)sense on YouTube** (training data) — detailed tick rate and network testing for major multiplayer shooters is one of the most cited community resources for understanding netcode differences

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | Servers run at a tick rate that makes hit registration consistent. Shot-to-kill timing matches what you see on screen. Lag compensation doesn't create situations where high-ping players have a systematic advantage. Connection quality between players is the limiting factor, not server architecture. | What you do in the game is what the server records. Shots that land, land. Deaths that feel fair, are fair. |
| 4 | Hit registration is reliable in most situations with occasional inconsistency under poor connections. Tick rate is adequate for the game's pace. Lag compensation works in most scenarios with some edge cases. The community recognises server quality as good with specific known issues. | Most matches feel consistent. You'll have the occasional shot that should have connected and didn't, but it won't define how you play. |
| 3 | Hit registration is inconsistent enough to be noticed regularly. Tick rate is lower than competitive standards, which is felt in fast-paced or close-range exchanges. Lag compensation produces occasional situations where outcomes don't match what happened on screen. The community discusses server quality as an ongoing concern. | You'll notice the servers in close situations. Some deaths will feel wrong. You'll play around it — leading shots, avoiding close-range fights — rather than trusting your first instinct. |
| 2 | Hit registration is unreliable enough to affect how you approach the game. Lag compensation creates documented asymmetric situations. Getting shot from cover, or having shots clearly miss register as hits, happens regularly. Server quality is a consistent community complaint that the developer has not resolved. | The netcode is part of the opponent. You're playing against the servers as much as the other team. |
| 1 | Servers are functionally broken for competitive play. Hit registration is random enough that aiming is partially decoupled from killing. Lag compensation gives high-ping players a systematic advantage. The community has documented the server quality as the primary reason the game isn't taken competitively seriously. | The game doesn't work online. What you do and what the server records are two different things. |
