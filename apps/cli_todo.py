from __future__ import annotations

import sys
from dataclasses import dataclass, asdict
from pathlib import Path

from lib.utils import read_json, write_json

REPO_ROOT = Path(__file__).resolve().parents[1]
DB_PATH = REPO_ROOT / "data" / "todos.json"

@dataclass
class Todo:
    text: str
    done: bool = False

def load() -> list[Todo]:
    raw = read_json(DB_PATH, default=[])
    return [Todo(**item) for item in raw]

def save(todos: list[Todo]) -> None:
    write_json(DB_PATH, [asdict(t) for t in todos])

def _norm_text(s: str) -> str:
    return " ".join(s.strip().lower().split())

def cmd_add(todos: list[Todo], text: str, *, unique: bool = False) -> None:
    if unique:
        needle = _norm_text(text)
        if any(_norm_text(t.text) == needle for t in todos):
            print("Already exists (skipped).")
            return

    todos.append(Todo(text=text))
    save(todos)
    print("Added.")

def cmd_list(todos: list[Todo]) -> None:
    if not todos:
        print("(no todos)")
        return
    for i, t in enumerate(todos, start=1):
        mark = "x" if t.done else " "
        print(f"{i:02d}. [{mark}] {t.text}")

def cmd_done(todos: list[Todo], idx: int) -> None:
    if idx < 1 or idx > len(todos):
        raise SystemExit(f"Invalid index: {idx}")
    todos[idx - 1].done = True
    save(todos)
    print("Marked done.")

def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python apps/cli_todo.py (add|list|done) ...")
        return 2

    todos = load()
    cmd = sys.argv[1]

    if cmd == "add":
        unique = False
        args = sys.argv[2:]

        if args and args[0] == "--unique":
            unique = True
            args = args[1:]

        if not args:
            raise SystemExit("Usage: ... add [--unique] <text>")

        cmd_add(todos, " ".join(args), unique=unique)

    elif cmd == "list":
        cmd_list(todos)
    elif cmd == "done":
        if len(sys.argv) != 3:
            raise SystemExit("Usage: ... done <index>")
        cmd_done(todos, int(sys.argv[2]))
    else:
        raise SystemExit(f"Unknown command: {cmd}")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
