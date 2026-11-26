"""The Funniest Excuse for Skipping a Meeting — make.fun one-line entry.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line is the whole entry: one razor-sharp excuse, under 200 characters,
that the scorer's gate reads from /output/entry.txt.
"""
import os

# The entry line, kept as a named constant so the gate checks below read it.
# 73 characters, one line: the mute button — the most meeting-specific object
# in office life — takes legal action against its own user. Concrete, fresh
# (no wifi, no cat, no dentist), and the turn lands in the last third.
ENTRY_TEXT = "Can't make it — my mute button just filed a restraining order against me."


def check_entry(text):
    """Self-check the line against the scorer's gate before writing."""
    assert text, "entry must not be empty"
    assert "\n" not in text.rstrip("\n"), "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")


def main():
    check_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
