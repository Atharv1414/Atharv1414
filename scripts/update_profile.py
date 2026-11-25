"""Refresh the "Latest projects" part of the profile README from the daily-projects table.

Only the text between the two markers is replaced. Nothing is written if a link does not work, if
the table cannot be read, or if nothing has changed.
"""

from __future__ import annotations

import re
import sys
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

OWNER = "Atharv1414"
SOURCE = f"https://raw.githubusercontent.com/{OWNER}/daily-projects/main/README.md"
TREE = f"https://github.com/{OWNER}/daily-projects/tree/main/"
START, END = "<!-- latest:start -->", "<!-- latest:end -->"
SHOW = 6

ROW = re.compile(
    r"^\|\s*(\d{3})\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|"
    r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*$", re.M)


def parse(markdown: str) -> list[dict]:
    rows = [
        {"n": int(n), "date": date.fromisoformat(d), "title": re.sub(r"^\W+", "", title).strip(),
         "folder": folder.strip("./"), "role": role, "stack": stack}
        for n, d, title, folder, role, stack in ROW.findall(markdown)
    ]
    numbers = [r["n"] for r in rows]
    if not rows or len(set(numbers)) != len(numbers):
        raise ValueError("the projects table is missing or has repeated numbers")
    return sorted(rows, key=lambda r: r["n"])


def short_stack(stack: str, limit: int = 64, items: int = 3) -> str:
    """The first few tools, without bracketed detail, never cut inside a word."""
    plain = re.sub(r"\s*\([^()]*\)", "", stack)
    parts = [p.strip() for p in re.split(r"[,;:]", plain) if p.strip()]
    out = parts[0]
    for p in parts[1:items]:
        if len(out) + len(p) + 2 > limit:
            break
        out += f", {p}"
    return out


def render(rows: list[dict]) -> str:
    latest = list(reversed(rows))[:SHOW]
    roles = Counter(r["role"] for r in rows)
    lines = ["| Added | Project | Role | Built with |", "|---|---|---|---|"]
    lines += [
        f"| {r['date'].day} {r['date']:%b %Y} | [{r['title']}]({TREE}{r['folder']}) "
        f"| {r['role']} | {short_stack(r['stack'])} |" for r in latest]
    count = f"{len(rows)} project{'s' if len(rows) != 1 else ''}"
    areas = f"{len(roles)} role{'s' if len(roles) != 1 else ''}"
    lines += ["", f"{count} so far, covering {areas}."]
    return "\n".join(lines)


def replace(readme: str, body: str) -> str:
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(START) > readme.index(END):
        raise ValueError("the README must contain the two markers once each, in order")
    head, rest = readme.split(START)
    return f"{head}{START}\n{body}\n{END}{rest.split(END)[1]}"


def fetch(url: str) -> str:
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode()


def works(url: str) -> bool:
    try:
        request = urllib.request.Request(url, method="HEAD")
        return urllib.request.urlopen(request, timeout=30).status == 200
    except OSError:
        return False


def main(path: Path = Path("README.md")) -> int:
    rows = parse(fetch(SOURCE))
    broken = [r["folder"] for r in rows[-SHOW:] if not works(TREE + r["folder"])]
    if broken:
        print(f"these links do not work, so nothing was changed: {', '.join(broken)}")
        return 1
    old = path.read_text()
    new = replace(old, render(rows))
    if new == old:
        print("already up to date")
    else:
        path.write_text(new)
        print("updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
