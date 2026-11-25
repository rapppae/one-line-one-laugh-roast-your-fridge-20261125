"""Entry for make.fun bounty "One Line, One Laugh: Roast Your Fridge".

Entry text (draft v1, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "My fridge has hummed the same tired note since 2019, hoards expired sauces like a dragon, and still can't keep the ice cream frozen. One job, champ."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
