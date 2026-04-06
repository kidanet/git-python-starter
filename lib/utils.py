from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def read_json(path: str | Path, default: Any):
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))

def write_json(path: str | Path, obj: Any) -> None:
    p = Path(path)
    p.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
