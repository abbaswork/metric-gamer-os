import sys


def collect_inputs():
    print("=== Skill: fact-check-rubrics ===")
    print("Audits all rubrics in a sub-genre for unsupported inferences.\n")

    genre = input("Genre (e.g. fighting, racing, moba): ").strip().lower()
    if not genre:
        print("Error: genre is required.")
        sys.exit(1)

    sub_genre = input("Sub-genre (e.g. platform-fighter, party, traditional): ").strip().lower()
    if not sub_genre:
        print("Error: sub-genre is required.")
        sys.exit(1)

    print(f"\nSKILL: fact-check-rubrics")
    print(f"INPUTS:")
    print(f"  genre: {genre}")
    print(f"  sub_genre: {sub_genre}")


if __name__ == "__main__":
    collect_inputs()
