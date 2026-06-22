# Metric: Combat Feel
**Genre:** Fighting
**Sub-genre:** Traditional
**Type:** Qualitative (community consensus)
**Direction:** Delight — 5 = every hit lands with weight and intention, inputs feel like extensions of thought, 1 = controls work against you before opponents do

## Why This Matters

Combat feel is the most discussed dimension of fighting games across both research sources and technical game design literature — and it's the hardest to quantify because players often describe it as something they feel rather than something they can name. The r/Fighters research framed it precisely: "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character." That framing is exact — the issue isn't just technical input latency but the perceived connection between intention and outcome.

There are four specific mechanisms that together produce this feeling:

**1. Hit stop (frame freeze):** When an attack lands, the game briefly pauses both characters on impact. This is a deliberate design choice. According to game design analysis of Capcom's own fighting system: "Frame freezing gives a moment for a player to see the attack motion which may be rather quick to see otherwise, and also creates a feeling of resistance caused by the impact." Without it, hits feel like passing through air. Light, medium, and heavy attacks typically produce 8, 12, and 16 frames of hit stop respectively — the difference between a jab and a launcher needs to be felt, not just seen.

**2. Audio design:** Sound design is described as transformative in combat analysis: "Mute the sound while playing some action games and it feels a bit flat. However, turn the volume up and the attack animation may suddenly seem more painful." Tekken's community specifically names hit sparks and sound as what makes it distinctive: "The excessive hit sparks are what makes Tekken hits special. You really know you hit that guy." In fighting games, audio is not atmosphere — it's feedback. A weak-sounding hit undermines the entire exchange.

**3. Enemy reaction:** "For every attack action, there must be a damage or defend reaction. If the player hits an enemy and there is no response then the game will feel less responsive." Hitstun — the period during which the opponent cannot act after being hit — is what makes combo chains physically read as cause and effect rather than coincidence. It's also what gives the neutral game meaning: landing a hit has consequences that unfold visually, not just numerically.

**4. Input responsiveness:** "A delay of even a few frames can disrupt timing, punish windows, and defensive strategies." Motion inputs produce a specific kind of engagement — "every motion performed gives a bit of feedback, a little bit of dopamine" — but only if the input registers cleanly. When it doesn't, it produces the opposite: "making players feel that their decisions have little impact on the outcome of a match."

The combination of all four is what separates a fighting game that feels alive from one that merely functions.

## Sources

- **research.md — Reddit (What makes a good fighting game):** "Control. Or at least the illusion of it. I, the user, must feel that I have proper control of my character", "Freedom of expression and decision-making. Having various options for mechanics like movement and combos is super important", "satisfying gameplay (hard to describe. good animation and audio cues help)", "Inputs shouldn't be hard for the sake of being hard"
- **research.md — Reddit (Brawlhalla):** "movement feels good", "It's arguably one of the fastest fighting games out there"
- **research.md — Google Trends:** brawlhalla combos (36 search interest)
- **Capcom SF seminar (game.capcom.com):** "Frame freezing gives a moment for a player to see the attack motion... and creates a feeling of resistance caused by the impact"; light/medium/heavy hit stop of 8F/12F/16F documented
- **Game Developer: "Improving the Combat Impact of Action Games":** "If the player hits an enemy and there is no response then the game will feel less responsive"; "Mute the sound while playing some action games and it feels flat. Turn the volume up and the animation may suddenly seem more painful"
- **CritPoints — "Stunning Detail":** "Hitfreeze or hitstop... is a short delay at the moment of impact"; "The single biggest thing hitstun does is it allows one character's attacks to interrupt another character's"
- **r/Fighters via NeoGAF:** "Satisfying audiovisual feedback is pretty much a make it or break it feature for fighting games. The excessive hit sparks are what makes Tekken hits special."
- **Reddit/r/Fighters on inputs:** "Every motion performed gives a bit of feedback, a little bit of dopamine"
- **gamedesigning.org:** "A delay of even a few frames can disrupt timing, punish windows, and defensive strategies"

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | Hit stop is tuned so every attack weight class feels physically distinct — a jab and a launcher communicate their difference through the pause and sound before the animation completes. Audio is specific enough that you can identify what landed by ear alone. Enemy reactions to damage are clear and immediate; hitstun is long enough to feel earned. Input responsiveness is clean enough that motion inputs register consistently, and the small dopamine loop of execution pays off. Movement and attacks feel like extensions of thought rather than operations to execute. | You stop thinking about the controls within hours. The game starts talking back to you through feedback instead of numbers. |
| 4 | Strong feedback across most of the attack set with a few weak spots — one attack weight class under-communicates its impact, or certain sound effects don't match the visual weight of the move. Enemy reactions hold up throughout. Inputs are responsive with occasional missed windows under speed. The core feel is reliable. | You'll feel at home quickly. The rare weak spot doesn't undermine the overall experience. |
| 3 | Functional feedback that does its job without distinction. Hit stop exists but doesn't vary meaningfully across attack weights. Audio is present but generic enough that you could swap it for another game's sounds without noticing. Enemy reactions are present without making hits feel consequential. Inputs register reliably without producing the small satisfaction of clean execution. | The controls work. You'll never be stopped by them, but they won't pull you deeper either. |
| 2 | Hit feedback is inconsistent or absent enough that landing a hit feels uncertain — the stop isn't there, the sound doesn't confirm it, or the enemy barely reacts. At least one of the four feedback layers (hit stop, audio, enemy reaction, input responsiveness) is clearly missing or broken. Inputs occasionally fail under normal play speed in ways that feel like the game's failure rather than yours. | You'll find yourself blaming the controls after losses — and sometimes you'll be right. |
| 1 | The controls are the primary obstacle. Input lag, absent hit feedback, enemy reactions that don't register damage, and audio that fails to confirm contact combine to make basic combat feel like guessing. Nothing the game communicates confirms that what you did had the effect you intended. | The game fights back before any opponent does. |
