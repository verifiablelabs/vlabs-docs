"""CI gate: docs carry only approved claims and no secret-shaped strings."""
from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SECRET = re.compile(
    r"sk-or-v1-[A-Za-z0-9_-]{16,}"
    r"|sk-(?:proj-)?[A-Za-z0-9_-]{20,}"
    r"|(?:AKIA|ASIA)[0-9A-Z]{16}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}"
    r"|gh[pousr]_[A-Za-z0-9]{36,}"
    r"|AIza[0-9A-Za-z_-]{35}"
    r"|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"
)
FORBIDDEN = re.compile(
    r"formally verified (system|product|api|code|service)"
    r"|prove[sd]? that the model generalizes"
    r"|eliminates? contamination"
    r"|(build|solve|prove)s? AGI",
    re.IGNORECASE,
)
NEGATION = re.compile(r"do not|never|claims? we do not|not a claim", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")


def validate_docs(root: Path = ROOT) -> list[str]:
    """Return claim, secret, and broken-local-link errors under ``root``."""
    bad: list[str] = []
    root = root.resolve()
    for p in sorted(root.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if SECRET.search(line):
                bad.append(f"{p}:{i}: secret-shaped string")
            if FORBIDDEN.search(line) and not NEGATION.search(line):
                bad.append(f"{p}:{i}: forbidden claim: {line.strip()[:80]}")
            for match in MARKDOWN_LINK.finditer(line):
                target = match.group(1).strip("<>")
                if (
                    not target
                    or target.startswith(("#", "/"))
                    or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE)
                ):
                    continue
                relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if relative and not (p.parent / relative).resolve().exists():
                    bad.append(f"{p}:{i}: broken local link: {target}")
    return bad


def main() -> int:
    bad = validate_docs()
    for b in bad:
        print("FAIL:", b)
    print("OK: docs clean" if not bad else f"{len(bad)} violation(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
