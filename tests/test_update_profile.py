import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_profile as u  # noqa: E402

TABLE = """
| # | Date | Project | Role focus | Stack |
|---|---|---|---|---|
| 001 | 2026-11-20 | [💸 Expense Tracker](expense-tracker-cli/) | Software Engineer | Python, SQLite (migrations, window functions), pytest |
| 002 | 2026-11-21 | [🏨 Hotel Agent](hotel-agent/) | AI Engineer | Python, Claude tool use (Anthropic SDK), evals |

| Project | Role focus | Stack |
|---|---|---|
| [Other](other/) | Software Engineer | Flask |
"""


def test_reads_only_the_numbered_table():
    rows = u.parse(TABLE)
    assert [(r["n"], r["title"], r["folder"]) for r in rows] == [
        (1, "Expense Tracker", "expense-tracker-cli"), (2, "Hotel Agent", "hotel-agent")]


def test_newest_first_with_counts():
    out = u.render(u.parse(TABLE)).splitlines()
    assert out[2].startswith("| 21 Nov 2026 | [Hotel Agent](https://github.com/")
    assert out[-1] == "2 projects in the series so far: AI Engineer 1 · Software Engineer 1."


def test_stack_is_cut_cleanly():
    assert u.short_stack("Python, SQLite (migrations, window functions), pytest") == "Python, SQLite, pytest"
    long = u.short_stack("C# / .NET 10, " + ", ".join(["Something"] * 20))
    assert len(long) <= 64 and not long.endswith(",")


def test_only_the_marked_part_changes():
    before = f"intro\n{u.START}\nold\n{u.END}\noutro\n"
    after = u.replace(before, "new")
    assert after == f"intro\n{u.START}\nnew\n{u.END}\noutro\n"
    assert u.replace(after, "new") == after


@pytest.mark.parametrize("bad", ["none", u.START, u.END + u.START, u.START * 2 + u.END])
def test_missing_or_wrong_markers_are_refused(bad):
    with pytest.raises(ValueError):
        u.replace(bad, "x")


@pytest.mark.parametrize("bad", ["", "| 001 | soon | [x](y) | r | s |", TABLE.replace("002", "001")])
def test_an_unreadable_table_is_refused(bad):
    with pytest.raises(ValueError):
        u.parse(bad)


def test_a_broken_link_changes_nothing(tmp_path, monkeypatch):
    readme = tmp_path / "README.md"
    readme.write_text(f"{u.START}\nold\n{u.END}\n")
    monkeypatch.setattr(u, "fetch", lambda _: TABLE)
    monkeypatch.setattr(u, "works", lambda url: "hotel" not in url)
    assert u.main(readme) == 1 and "old" in readme.read_text()
    monkeypatch.setattr(u, "works", lambda url: True)
    assert u.main(readme) == 0 and "Hotel Agent" in readme.read_text()


def test_the_real_readme_has_the_markers():
    u.replace((ROOT / "README.md").read_text(), "x")
