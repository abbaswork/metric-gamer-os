# Metric: Combat Feedback
**Genre:** Fighting
**Sub-genre:** Platform Fighter
**Type:** Qualitative (observable signals)
**Direction:** Delight — 5 = all core feedback signals present and functioning across aerial combat and kill confirmation, 1 = one or more signals absent or broken in ways that make hits or aerial movement feel uncertain

## Why This Matters

Platform fighters are primarily aerial games — most combat happens off the ground, and the movement system is the game. The same four feedback mechanisms that apply to traditional fighters apply here, but their expressions change when most of combat is happening mid-air and victory comes from launching opponents off stage rather than depleting a health bar.

The universal signals carry through: hitstop still produces the physical moment of impact; audio still distinguishes hit from whiff; visual confirmation still tells you the attack registered; input acknowledgment still depends on whether inputs are being dropped. But the platform-specific context adds signals that do not exist in traditional fighters at all.

**Kill confirmation:** In a stock-based game, the moment a kill move connects near the blast zone is the highest-stakes feedback moment in any match. It needs to be distinct and unambiguous. The observable test is specific: does the kill move produce a visually and audibly different response from a strong non-kill hit? Is there a clear moment before the opponent crosses the blast zone that communicates the stock is gone?

**Aerial physics consistency:** Jump arcs should be consistent across all jump counts for a given character. Aerial drift should behave predictably at the same drift input. These are observable: jump arcs either behave consistently across all jump counts or they do not, and aerial drift either responds predictably to the same input or it does not.

**Knockback direction readability:** At the moment a hit connects, the launch direction should be readable from the attack animation and the relative position of the characters. The test is whether a player can predict roughly where the opponent will be sent before the launch animation completes. Consistent failure here produces unexpected survivals at high percentages and kill moves that feel random rather than earned.

**Dodge timing perceptibility:** A dodge that feels crisp and punishable rewards reading. The observable signal is whether the invincibility window has a visual or audio cue that makes the start and end of the window perceptible. The failure signal is a dodge system where neither the user nor their opponent can develop a reliable read on when the invincibility window starts and ends.

## Sources

- **research.md — Reddit (Brawlhalla):** "movement feels good", "It's arguably one of the fastest fighting games out there"
- **research.md — Reddit (What makes a good fighting game):** "Freedom of expression and decision-making. Having various options for mechanics like movement and combos is super important", "Control. Or at least the illusion of it"
- **playbrawlhalla.com / defy.club:** "three jumps and nearly unlimited wall scaling make for fresh strategies and the buff in mobility means a lot of the high-adrenaline action happens off-stage"
- **Game Developer — "Improving the Combat Impact of Action Games":** Hitstop creating "a feeling of resistance caused by the impact"; audio as a multiplier on visual feedback
- **Capcom SF seminar (game.capcom.com):** Hitstop calibration principles — duration communicating attack weight

---

## Observable Signals

The five universal signals:

| Signal | What to check |
|---|---|
| Hitstop | Present on aerial hits; duration varies between move weights; kill moves produce a perceptibly longer or distinct pause |
| Hit audio | Hit and whiff produce distinct sounds; kill move audio is distinguishable from strong non-kill hit audio |
| Visual confirmation | Clear on-contact signal (flash, spark, or particle) on every aerial hit |
| Input acknowledgment | Inputs register consistently in aerial sequences; no dropped inputs or phantom inputs |
| Hitbox accuracy | Hitboxes match animations; no phantom hits or moves that visually miss but register |

Platform fighter-specific signals:

| Signal | What to check |
|---|---|
| Kill confirmation distinctness | Kill move produces a visually and audibly different response from a strong non-kill hit |
| Aerial physics consistency | Jump arcs consistent across all jump counts; aerial drift predictable at same input |
| Knockback direction readability | Launch direction readable from the hit animation before the opponent crosses the blast zone |
| Dodge timing perceptibility | Dodge invincibility window has a perceptible visual or audio cue; dodges are readable and punishable with the right read |

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | All five universal signals present and functioning. Hitstop is calibrated across move weights including a distinct kill move pause. Hit and whiff audio are distinguishable. Visual confirmation is present on every hit. Inputs register consistently with no drops or hitbox inaccuracies. All four platform-specific signals are present: kill confirmation is distinct, aerial physics are consistent, knockback direction is readable at contact, and dodge timing is perceptible. | You stop thinking about the physics within hours. The game's aerial system becomes a language you learn to read. |
| 4 | All universal signals present with one weak area. Kill confirmation feedback is present but not as distinct as it could be, or one character's aerial physics are inconsistent with the rest of the cast. Knockback direction is readable in most situations with a few exceptions. Dodge timing is generally perceptible. Input is reliable. | You will feel in control quickly. The exceptions stand out because the baseline is solid. |
| 3 | Universal signals mostly present but one platform-specific signal is weak or absent. Kill confirmation is not clearly distinct from a strong non-kill hit. Or knockback direction is not reliably readable at the moment of contact. Aerial physics functional but characters are not distinctly weighted. | The physics work. You will not be stopped by them, but you will not always trust them either. |
| 2 | At least one universal signal absent or broken alongside a platform-specific failure. Kill confirmation absent or delayed so stock losses are only confirmed by the respawn animation. Knockback direction unreliable. Or input lag affecting aerial inputs. | Off-stage deaths start feeling like the game's fault more than your own. |
| 1 | Multiple signals absent or broken. Input drops or lag in aerial sequences. Aerial physics produce unpredictable outcomes. Kill confirmation absent. Hit and whiff audio indistinct. | The game fights back before any opponent does. |
