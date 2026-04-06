from __future__ import annotations

import sys
from pathlib import Path

def wordcount(text: str) -> dict[str, int]:
    words = [w.strip(".,!?;:\"'()[]{}").lower() for w in text.split()]
    counts: dict[str, int] = {}
    for w in words:
        if not w:
            continue
        counts[w] = counts.get(w, 0) + 1
    return counts

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python apps/wordcount.py <file>")
        return 2

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    counts = wordcount(text)

    top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    for word, n in top:
        print(f"{word}\t{n}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
