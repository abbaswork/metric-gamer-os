# Metric: Combat Feedback
**Genre:** Fighting
**Sub-genre:** Party Fighter
**Type:** Qualitative (observable signals)
**Direction:** Delight — 5 = core interactions (punch, grab, throw) all produce clear confirmation signals that make actions feel authored, 1 = core interactions fail to confirm clearly enough for players to tell whether inputs registered

## Why This Matters

Combat feedback in party fighters does not require the frame-perfect hitstop calibration and motion input responsiveness of competitive fighting games. It requires something more specific to the sub-genre: core physical interactions need to be legible. When you grab someone and throw them, the audio, animation, and physics response should confirm the action clearly enough that the moment reads as intentional even when the outcome is chaotic.

Gang Beasts demonstrates this well. The research notes that players actively search for "how to drop kick, punch, throw" — the interactions are learnable and satisfying specifically because they communicate clearly when they work. The searches exist because the payoff of executing them correctly is distinct enough to motivate learning. That distinctness is the observable signal: do the game's core interactions produce a different, recognisable response when they succeed versus when they miss?

The balance specific to this sub-genre is that party fighters deliberately use exaggerated, physics-heavy animation that is not tuned for competitive precision. A character flailing while trying to regain balance is a feature, not a failure — it creates the comedic moments the genre runs on. The physics producing chaotic outcomes from clean inputs is expected. The test is not whether the outcome is predictable, but whether the input that caused it was confirmed. Players need authorship over the chaos, not just a front-row seat to it.

## Sources

- **research.md — Notes:** "specifically for Gang Beasts there is lots of queries asking how to drop kick, punch, throw etc" — physics interactions are actively learned because they feel distinct and satisfying when they work
- **research.md — Reddit (What makes a good fighting game):** "satisfying gameplay (hard to describe. good animation and audio cues help)", "Control. Or at least the illusion of it"
- **Game Developer — "Improving the Combat Impact of Action Games":** Audio confirming impact; opponent reaction making hits feel real

---

## Observable Signals

| Signal | What to check |
|---|---|
| Punch/attack audio | Hit and whiff produce distinct sounds; connecting a punch sounds different from swinging through air |
| Grab confirmation | Successful grab produces a clear audio or visual signal that distinguishes a registered grab from a missed attempt |
| Throw readability | Thrown character follows a physics arc readable in real time; you can follow what happened to them during the throw |
| Input acknowledgment | Inputs register consistently; grabs and attacks register when inputs are performed correctly |

---

## Rubric

| Score | Description | What This Means for You |
|---|---|---|
| 5 | All four signals present. Punch audio clearly distinguishes hit from whiff. Grab confirmation is unambiguous — a registered grab looks and sounds different from a missed attempt. Throw arcs are readable in real time. Inputs register consistently. | You feel like you did that. The chaos feels authored even when the outcome surprises you. |
| 4 | Core signals present with one weak area. Grab confirmation is present but occasionally subtle, or throw arcs are readable in most situations but obscured in the most chaotic moments. Punch audio distinguishes hit from whiff. Inputs are reliable. | The controls feel intentional most of the time. The exceptions are noticeable but rare. |
| 3 | All signals present but weakly. Punch audio distinguishes hit from whiff but the difference is subtle rather than distinct. Grab confirmation is present but easy to miss in a chaotic session. Throw arcs are readable when there are few bodies on screen but get lost in busier situations. Input is reliable. | The controls confirm correctly but without the pop that makes party fighters memorable. The chaos happens to you as much as you cause it. |
| 2 | At least one signal absent or broken. Punch audio does not clearly distinguish hit from whiff, grab registration is inconsistent with the same input sometimes registering and sometimes not, or throw arcs are not readable in real time. Input registration is unreliable. | You cannot reliably tell whether your inputs registered. The chaos stops being funny. |
| 1 | Multiple signals absent or broken. Core interactions — punch, grab, throw — do not produce clear confirmation. Input registration is unreliable. | Nothing feels physical or authored. You are a spectator to your own inputs. |
