#!/usr/bin/env python3
"""
Skill: Write Checklist
Collects sub_genre, genre, metric, and process preference, then outputs a structured input block for Claude.
"""

PROCESS_OPTIONS = [
    "review",
    "direct"
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
    print("\n=== Metric Gamer — Write Checklist ===\n")
    print("Produces a 5-band metric score checklist from an existing rubric.")
    print("No web research required — the checklist is derived from the rubric alone.\n")
    print("-" * 50 + "\n")

    sub_genre = prompt_input(
        label="Sub-genre",
        required=False,
        hint="e.g. fps, cozy, party, platform-fighter. Leave blank if the metric sits at genre level."
    )

    genre = prompt_input(
        label="Genre",
        required=True,
        hint="e.g. fighting, shooters, rpg — the parent genre folder name"
    )

    metric = prompt_input(
        label="Metric",
        required=True,
        hint="e.g. gunplay, campaign-structure, character-development — the metric folder name"
    )

    process = prompt_choice(
        label="Process — show draft for approval before writing, or write directly to file?",
        options=PROCESS_OPTIONS,
        required=True
    )

    print("\n" + "-" * 50)
    print("SKILL: write-checklist")
    print("INPUTS:")
    if sub_genre:
        print(f"  sub_genre: {sub_genre}")
    print(f"  genre: {genre}")
    print(f"  metric: {metric}")
    print(f"  process: {process}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
