#!/usr/bin/env python3
"""
Skill: Write Ranked List
Collects list_title, target_query, niche_focus, author, and draft_paths inputs,
then outputs a structured prompt block for Claude.
"""

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


def prompt_draft_paths() -> list:
    print("\nGame Page Draft Paths *")
    print("  Enter the path to each source game page draft, one per line.")
    print("  Press Enter twice when done. Minimum 2 paths required.\n")

    paths = []
    while True:
        raw = input(f"  Draft {len(paths) + 1}: ").strip()
        if not raw:
            if len(paths) >= 2:
                break
            if len(paths) == 0:
                print("  At least 2 draft paths are required.\n")
            else:
                print("  At least one more draft path is required.\n")
        else:
            paths.append(raw)

    return paths


def main():
    print("\n=== Metric Gamer — Write Ranked List ===\n")
    print("This skill produces a complete, publish-ready ranked list page.")
    print("All entries are reworded from source game page drafts and tailored")
    print("to the list's niche to avoid duplicate content.\n")
    print("-" * 50 + "\n")

    list_title = prompt_input(
        label="List Title",
        required=True,
        hint="Full title of the ranking (e.g. Best Free Mobile Football Games 2026)"
    )

    target_query = prompt_input(
        label="Target Search Query",
        required=True,
        hint="The primary search query this list targets (e.g. best free mobile football games 2026)"
    )

    niche_focus = prompt_input(
        label="Niche Focus",
        required=True,
        hint="One sentence on what makes this list specific — platform, price point, sub-genre, or audience\n  (e.g. free-to-play football games on iOS and Android)"
    )

    author = prompt_choice(
        label="Author",
        options=AUTHORS,
        required=True
    )

    draft_paths = prompt_draft_paths()

    cluster_context = prompt_input(
        label="Cluster Context",
        required=False,
        hint="Cannibalisation flags or shared game constraints from the keyword strategy.\n  e.g. 'max 1 game shared with best-arcade-racing-ps5 cluster'\n  Leave blank if not part of a campaign."
    )

    print("\n" + "-" * 50)
    print("SKILL: write-ranked-list")
    print("INPUTS:")
    print(f"  list_title: {list_title}")
    print(f"  target_query: {target_query}")
    print(f"  niche_focus: {niche_focus}")
    print(f"  author: {author}")
    print(f"  draft_paths:")
    for path in draft_paths:
        print(f"    - {path}")
    if cluster_context:
        print(f"  cluster_context: {cluster_context}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
