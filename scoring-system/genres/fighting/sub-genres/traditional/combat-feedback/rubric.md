# Metric: Combat Feedback
**Genre:** Fighting
**Sub-genre:** Traditional
**Type:** Qualitative (community consensus)
**Direction:** Delight — 5 = every hit communicates weight and outcome through feedback the player reads instinctively, 1 = one or more core signals absent or broken in ways that make hits feel uncertain

## Why This Matters

Combat feedback is the most discussed dimension of fighting games across both research sources and technical game design literature. The player-side expectation is precise: "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character." That feeling is produced by specific, calibrated mechanisms working together.

Hitstop is the most technical of these: when an attack lands, the game briefly freezes both characters on impact. Capcom's fighting system documentation specifies light, medium, and heavy attacks producing 8, 12, and 16 frames of hitstop respectively. The difference between a jab and a launcher needs to be felt through pause duration, not just seen through animation length.

Sound design is documented as transformative: "Mute the sound while playing some action games and it feels flat. Turn the volume up and the animation may suddenly seem more painful." Tekken's community names this directly — "the excessive hit sparks are what makes Tekken hits special. You really know you hit that guy." Opponent reaction closes the loop: "for every attack action, there must be a damage or defend reaction. If the player hits an enemy and there is no response then the game will feel less responsive."

Input acknowledgment is the foundation everything else rests on: "a delay of even a few frames can disrupt timing, punish windows, and defensive strategies." Attack phase readability — whether startup, active, and recovery frames produce visually distinguishable animation phases — is the mechanism by which players learn when to act from observation rather than frame data lookup.

## Sources

- **research.md — Reddit (What makes a good fighting game):** "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character", "satisfying gameplay (hard to describe. good animation and audio cues help)"
- **Capcom SF seminar (game.capcom.com):** "Frame freezing gives a moment for a player to see the attack motion... and creates a feeling of resistance caused by the impact"; light/medium/heavy hitstop of 8F/12F/16F documented
- **Game Developer — "Improving the Combat Impact of Action Games":** "If the player hits an enemy and there is no response then the game will feel less responsive"; "Mute the sound while playing some action games and it feels flat. Turn the volume up and the animation may suddenly seem more painful"
- **CritPoints — "Stunning Detail":** "Hitstop... is a short delay at the moment of impact"; "The single biggest thing hitstun does is it allows one character's attacks to interrupt another character's"
- **r/Fighters via NeoGAF:** "The excessive hit sparks are what makes Tekken hits special. You really know you hit that guy."
- **gamedesigning.org:** "A delay of even a few frames can disrupt timing, punish windows, and defensive strategies"

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | Hitstop varies perceptibly between attack classes — jabs, mediums, and heavies each produce a distinct pause duration. Hit, block, and whiff audio are distinguishable by ear alone and vary by attack weight. Opponents react visibly to contact with hitstun that scales with attack weight. Inputs register consistently with no drops or phantom inputs. Attack startup and recovery phases are readable from animation for most moves. | You stop thinking about the controls within hours. The game tells you what happened before you have to look it up. |
| 4 | Hits feel physically distinct and the game communicates what happened, though one attack weight class doesn't produce a clearly different pause on contact than the others, or audio distinguishes hit from block in most but not all situations. Inputs register reliably. Hitboxes are accurate. | You'll feel at home quickly. The single weak spot stands out because the rest is solid. |
| 3 | Hitstop is uniform across attack weights — jabs and launchers don't feel distinct through pause alone. Audio doesn't clearly distinguish between hit, block, and whiff. Inputs register reliably and hitboxes are broadly accurate. | The controls work. You'll never be stopped by the feedback, but it won't pull you deeper either. |
| 2 | At least one thing is absent or clearly broken — no hitstop, hit and block audio that are indistinguishable, input lag affecting normal play, or hitboxes producing phantom hits in matches. | You'll blame the controls after losses. Sometimes you'll be right. |
| 1 | Multiple things absent or broken. Input drops in normal play, missing or inconsistent hitstop, audio that doesn't confirm contact, hitboxes that don't match animations. | The game fights back before any opponent does. |
