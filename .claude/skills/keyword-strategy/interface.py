#!/usr/bin/env python3
"""
Skill: Keyword Strategy
Collects campaign brief, CSV paths, and tool access, then outputs
a structured prompt block for Claude to begin keyword analysis.
"""


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


def prompt_boolean(label: str, hint: str = "") -> bool:
    display = f"{label} * (y/n)"
    if hint:
        display += f"\n  {hint}"
    display += "\n> "

    while True:
        raw = input(display).strip().lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  Please enter y or n.\n")


def prompt_existing_content() -> list:
    print("\nExisting MG Content in This Space *")
    print("  Enter every live MG URL related to this campaign topic.")
    print("  One URL per line. Press Enter twice when done.\n")

    urls = []
    while True:
        raw = input(f"  URL {len(urls) + 1}: ").strip()
        if not raw:
            if len(urls) == 0:
                print("  At least one URL is required (enter 'none' if no existing content).\n")
            else:
                break
        else:
            urls.append(raw)

    return urls


def main():
    print("\n=== Metric Gamer — Keyword Strategy ===\n")
    print("This skill produces a validated keyword map for a campaign:")
    print("campaign anchor, cluster map, game page keyword assignments, and gap list.")
    print("No campaign structure is proposed until keyword data is fully validated")
    print("and SERP check results are returned.\n")
    print("-" * 50 + "\n")

    campaign_topic = prompt_input(
        label="Campaign Topic",
        required=True,
        hint="One sentence — the niche with modifiers, not a genre.\n  e.g. 'Free arcade racing games on PS4 and PS5' not 'racing games'"
    )

    existing_content = prompt_existing_content()

    keyword_csv_path = prompt_input(
        label="Keyword Planner CSV Path",
        required=True,
        hint="Path to the keyword planner CSV seeded with the campaign topic.\n  Full export, unfiltered. e.g. C:\\Users\\name\\Downloads\\keywords.csv"
    )

    gsc_csv_path = prompt_input(
        label="GSC Export CSV Path",
        required=True,
        hint="Path to Google Search Console export — last 12 months,\n  all queries, clicks, impressions, position."
    )

    semrush_available = prompt_boolean(
        label="Semrush Access Available This Session",
        hint="If yes, organic KD scores will be requested for shortlisted keywords."
    )

    content_constraints = prompt_input(
        label="Content Constraints",
        required=False,
        hint="Games MG cannot review, platform coverage gaps, timeline constraints.\n  Leave blank if none."
    )

    print("\n" + "-" * 50)
    print("SKILL: keyword-strategy")
    print("INPUTS:")
    print(f"  campaign_topic: {campaign_topic}")
    print(f"  existing_content:")
    for url in existing_content:
        print(f"    - {url}")
    print(f"  keyword_csv_path: {keyword_csv_path}")
    print(f"  gsc_csv_path: {gsc_csv_path}")
    print(f"  semrush_available: {semrush_available}")
    if content_constraints:
        print(f"  content_constraints: {content_constraints}")
    print("-" * 50 + "\n")


if __name__ == "__main__":
    main()
