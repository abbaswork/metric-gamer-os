#!/usr/bin/env python3
"""
Skill: Generate Metrics & Rubrics
Collects genre and sub-genre inputs, then outputs a structured prompt for Claude.
"""

KNOWN_GENRES = [
    "Racing", "Fighting", "RPG", "Action RPG", "Sports", "Platformer",
    "Shooter", "Strategy", "Puzzle", "Adventure", "Simulation", "Horror",
    "Beat 'em Up", "Stealth", "Rhythm"
]


def prompt_input(label: str, required: bool, hint: str = "") -> str:
    marker = "*" if required else "(optional)"
    display = f"{label} {marker}"
    if hint:
        display += f"\n  {hint}"
    display += "\n> "

    while True:
        value = input(display).strip()
        if value:
            return value
        if not required:
            return ""
        print(f"  {label} is required. Please enter a value.\n")


def main():
    print("\n=== Metric Gamer — Generate Metrics & Rubrics ===\n")
    print("This skill researches and produces a set of player-validated metrics")
    print("with scoring rubrics for a given genre or sub-genre.\n")
    print("Sources used: Reddit, Steam reviews, GameFAQs, YouTube (player-only).\n")
    print("-" * 50 + "\n")

    genre = prompt_input(
        label="Genre",
        required=True,
        hint=f"e.g. {', '.join(KNOWN_GENRES[:5])}, ..."
    )

    sub_genre = prompt_input(
        label="Sub-genre",
        required=False,
        hint="e.g. Split Screen, Kart Racing, Beat 'em Up — leave blank if not applicable"
    )

    print("\n" + "-" * 50)
    print("SKILL: generate-metrics-rubrics")
    print("INPUTS:")
    print(f"  genre: {genre}")
    if sub_genre:
        print(f"  sub_genre: {sub_genre}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
