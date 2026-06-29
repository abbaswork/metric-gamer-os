# Metric: Combat Feedback
**Genre:** Fighting
**Sub-genre:** Traditional
**Type:** Qualitative (observable signals)
**Direction:** Delight — 5 = all core feedback signals present and functioning across the full attack set, 1 = one or more core signals absent or broken in ways that make hits feel uncertain

## Why This Matters

Combat feedback is the most discussed dimension of fighting games across both research sources and technical game design literature. The r/Fighters research framed the player-side expectation precisely: "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character." That feeling is produced by four specific, observable mechanisms. When all four are present and calibrated, the game feels alive. When one breaks down, the whole exchange stops being satisfying.

**1. Hitstop:** When an attack lands, the game briefly freezes both characters on impact. According to Capcom's own fighting system documentation, light, medium, and heavy attacks produce 8, 12, and 16 frames of hitstop respectively. The difference between a jab and a launcher needs to be felt through pause duration, not just seen through animation length. Hitstop is observable: you can see whether it is present and whether the duration varies meaningfully by attack class.

**2. Hit audio:** Sound design is documented as transformative: "Mute the sound while playing some action games and it feels flat. Turn the volume up and the animation may suddenly seem more painful." Tekken's community names this directly: "The excessive hit sparks are what makes Tekken hits special. You really know you hit that guy." The test is specific: can you distinguish a hit from a block from a whiff by audio alone, and does each attack weight class sound different on contact?

**3. Opponent reaction (hitstun):** "For every attack action, there must be a damage or defend reaction. If the player hits an enemy and there is no response then the game will feel less responsive." Hitstun is observable: is the opponent visibly locked in a reaction animation following a hit, and does the duration scale with attack weight?

**4. Input acknowledgment:** "A delay of even a few frames can disrupt timing, punish windows, and defensive strategies." The observable signal is whether inputs register consistently under normal play speed — no dropped inputs, no phantom inputs, no moves failing to come out when executed correctly.

A fifth signal applies specifically to traditional fighters: **attack phase readability**. Startup, active, and recovery frames should produce visually distinguishable animation phases for most moves, so that players can learn when to act from observation rather than purely from frame data lookup.

## Sources

- **research.md — Reddit (What makes a good fighting game):** "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character", "satisfying gameplay (hard to describe. good animation and audio cues help)", "Inputs shouldn't be hard for the sake of being hard"
- **Capcom SF seminar (game.capcom.com):** "Frame freezing gives a moment for a player to see the attack motion... and creates a feeling of resistance caused by the impact"; light/medium/heavy hitstop of 8F/12F/16F documented
- **Game Developer: "Improving the Combat Impact of Action Games":** "If the player hits an enemy and there is no response then the game will feel less responsive"; "Mute the sound while playing some action games and it feels flat. Turn the volume up and the animation may suddenly seem more painful"
- **CritPoints — "Stunning Detail":** "Hitstop... is a short delay at the moment of impact"; "The single biggest thing hitstun does is it allows one character's attacks to interrupt another character's"
- **r/Fighters via NeoGAF:** "Satisfying audiovisual feedback is pretty much a make it or break it feature for fighting games. The excessive hit sparks are what makes Tekken hits special."
- **gamedesigning.org:** "A delay of even a few frames can disrupt timing, punish windows, and defensive strategies"

---

## Observable Signals

The five signals scored against in the rubric below:

| Signal | What to check |
|---|---|
| Hitstop | Present on hit; duration varies between light, medium, and heavy attacks |
| Hit audio | Hit, block, and whiff produce distinct sounds; audio varies by attack weight class |
| Visual confirmation | Clear on-contact signal (flash, spark, or particle) on every hit |
| Input acknowledgment | Inputs register consistently; no dropped inputs or phantom inputs under normal play speed |
| Hitbox accuracy | Hitboxes match animations; no phantom hits or moves that miss visually but register |

Traditional-only signal:

| Signal | What to check |
|---|---|
| Attack phase readability | Startup, active, and recovery phases are visually distinguishable for most moves in-match |

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | All five universal signals present and functioning. Hitstop is calibrated so each attack weight class produces a perceptibly different duration. Hit, block, and whiff audio are distinguishable by ear alone, and the audio varies by attack weight. Visual hit confirmation is present on every hit. Inputs register consistently with no dropped inputs or hitbox inaccuracies. Attack phase readability is present for most of the move set. | You stop thinking about the controls within hours. The game communicates what happened through feedback before you have to read numbers. |
| 4 | All signals present with one weak area. One attack weight class under-communicates via hitstop or audio, or hitboxes have rare edge cases that do not affect normal play. Input is reliable. Attack phases are readable for most moves with a few exceptions. | You will feel at home quickly. The single weak spot stands out because the rest is solid. |
| 3 | Signals present but one is poorly calibrated. Most commonly: hitstop is present but uniform across attack weights so jabs and launchers do not feel distinct through pause alone. Or audio is present but not distinct enough between hit and block to be identified by ear. Input is reliable. Hitboxes are broadly accurate. | The controls work. You will never be stopped by the feedback, but it will not pull you deeper either. |
| 2 | At least one signal absent or clearly broken. Either no hitstop, or hit and block audio are indistinct, or input lag affects normal play, or hitbox inaccuracies produce phantom hits in matches. | You will blame the controls after losses. Sometimes you will be right. |
| 1 | Multiple signals absent or broken. Input drops or lag affecting normal play alongside missing or broken hitstop, audio that does not confirm contact, and hitboxes that do not match animations. | The game fights back before any opponent does. |
