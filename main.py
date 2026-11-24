"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes one out-of-office auto-reply to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). The file is what the judge reads --
printing alone is not enough. Single line, 159 characters or fewer,
no image, no link, no second line.
"""

import os

LINE = "I'm on leave until Monday. My inbox is now answered by a backup model trained on my unread emails \u2014 sorry in advance, it learned from the worst of me."

# The gate requires 1-159 characters, one line, not only whitespace.
# Fail loudly here rather than ship an invalid entry.
assert 1 <= len(LINE) <= 159, f"entry is {len(LINE)} chars, must be 1-159"
assert "\n" not in LINE, "entry must be a single line"
assert LINE.strip(), "entry must not be only whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
