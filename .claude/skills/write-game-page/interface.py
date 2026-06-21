#!/usr/bin/env python3
"""
Skill: Write Game Page
Collects game_name, genre, sub_genre, and author inputs, then outputs a structured prompt for Claude.
"""

KNOWN_GENRES = [
    "Racing", "Fighting", "RPG", "Action RPG", "Sports", "Platformer",
    "Shooter", "Strategy", "Puzzle", "Adventure", "Simulation", "Horror",
    "Beat 'em Up", "Stealth", "Rhythm", "Cozy", "Board Game", "Mobile"
]

AUTHORS = [
    "ABossProductions",
    "Metric Gamer",
    "Lobotomy_gaming",
    "8-Bit Bandit"
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


def prompt_choice(label: str, options: list, required: bool = True) -> str:
    print(f"\n{label} {'*' if required else '(optional)'}")
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")

    while True:
        raw = input("> ").strip()

        if not raw and not required:
            return ""

        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(options):
                return options[idx]

        match = next((o for o in options if o.lower() == raw.lower()), None)
        if match:
            return match

        print(f"  Please enter a number (1–{len(options)}) or type the option exactly.\n")


def main():
    print("\n=== Metric Gamer — Write Game Page ===\n")
    print("This skill produces a complete, publish-ready game page following")
    print("the EEAT lifecycle and Metric Gamer Writing Style Guide.\n")
    print("Fact-checking via live web research runs before any copy is written.\n")
    print("-" * 50 + "\n")

    game_name = prompt_input(
        label="Game Name",
        required=True,
        hint="Full title exactly as it appears on the platform storefront (e.g. Gran Turismo 7)"
    )

    genre = prompt_input(
        label="Genre",
        required=True,
        hint=f"e.g. {', '.join(KNOWN_GENRES[:6])}, ..."
    )

    sub_genre = prompt_input(
        label="Sub-genre",
        required=False,
        hint="e.g. Shooter — Multiplayer, Racing — Split Screen. Leave blank if not applicable."
    )

    author = prompt_choice(
        label="Author",
        options=AUTHORS,
        required=True
    )

    keyword_assignment = prompt_input(
        label="Keyword Assignment",
        required=False,
        hint="From the keyword strategy output. Format: Tier 2: [keyword] | Tier 3: [q1], [q2], [q3]\n  Leave blank if this page is not part of a campaign."
    )

    print("\n" + "-" * 50)
    print("SKILL: write-game-page")
    print("INPUTS:")
    print(f"  game_name: {game_name}")
    print(f"  genre: {genre}")
    if sub_genre:
        print(f"  sub_genre: {sub_genre}")
    print(f"  author: {author}")
    if keyword_assignment:
        print(f"  keyword_assignment: {keyword_assignment}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
