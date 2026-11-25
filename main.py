"""One Line, Big Laugh — entry writer (stdlib only).

Writes the chosen one-liner to /output/entry.txt and verifies it
against the competition gate: UTF-8 text, 1-200 characters, not
only whitespace.
"""

import os

# The chosen line (66 characters). See the run log for the candidates
# and why this one won.
LINE = "I asked AI to write my wedding vows and it proposed to my fiancée."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def count_characters(text):
    """Number of characters (code points) in the text."""
    return len(text)


def check_gate(text):
    """Check the competition gate: 1-200 chars, not whitespace-only.

    Returns (ok, reason).
    """
    n = count_characters(text)
    if n < MIN_CHARS or n > MAX_CHARS:
        return False, "length %d outside %d-%d" % (n, MIN_CHARS, MAX_CHARS)
    if not text.strip():
        return False, "only whitespace"
    return True, "ok"


def write_entry(path=OUTPUT_PATH):
    """Write LINE to path, creating the parent directory if needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return path


def verify_read_back(path):
    """Read path back as UTF-8 and compare byte-identically to LINE.

    Returns (identical, text).
    """
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    return text == LINE, text


def main():
    path = write_entry()
    ok, reason = check_gate(LINE)
    identical, read_back = verify_read_back(path)
    print("line: %r" % LINE)
    print("characters: %d" % count_characters(LINE))
    print("gate: %s (%s)" % ("PASS" if ok else "FAIL", reason))
    print("read-back byte-identical: %s" % identical)
    if not ok or not identical:
        raise SystemExit(1)
    print("wrote %s" % path)


if __name__ == "__main__":
    main()
