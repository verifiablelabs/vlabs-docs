"""CI gate: docs carry only approved claims and no secret-shaped strings."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECRET = re.compile(r"sk-or-v1-[A-Za-z0-9]|AKIA[0-9A-Z]{16}|xox[baprs]-")
FORBIDDEN = re.compile(
    r"formally verified (system|product|api|code|service)"
    r"|prove[sd]? that the model generalizes"
    r"|eliminates? contamination"
    r"|(build|solve|prove)s? AGI",
    re.IGNORECASE,
)
NEGATION = re.compile(r"do not|never|claims? we do not|not a claim", re.IGNORECASE)


def main() -> int:
    bad: list[str] = []
    for p in sorted(ROOT.rglob("*.md")):
        for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if SECRET.search(line):
                bad.append(f"{p}:{i}: secret-shaped string")
            if FORBIDDEN.search(line) and not NEGATION.search(line):
                bad.append(f"{p}:{i}: forbidden claim: {line.strip()[:80]}")
    for b in bad:
        print("FAIL:", b)
    print("OK: docs clean" if not bad else f"{len(bad)} violation(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
