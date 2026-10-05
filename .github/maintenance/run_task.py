#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
import json

ROOT = Path(__file__).resolve().parents[2]
SCHEDULE_FILE = ROOT / ".github/maintenance/schedule.json"
README_FILE = ROOT / "README.md"
IST = ZoneInfo("Asia/Kolkata")

def add_section(title, text):
    if not README_FILE.exists():
        return False
    current = README_FILE.read_text(encoding="utf-8")
    marker = f"## {title.title()}"
    if marker in current:
        return False
    README_FILE.write_text(current.rstrip() + f"

{marker}

{text}
", encoding="utf-8")
    return True

def main():
    schedule = json.loads(SCHEDULE_FILE.read_text(encoding="utf-8"))
    task = schedule.get(datetime.now(IST).date().isoformat())
    if not task:
        return 0
    sections = {
        "accessibility_notes": ("accessibility notes", "Document the accessibility-focused features already present in the portfolio."),
        "performance_notes": ("performance notes", "Add a concise note about keeping the static portfolio lightweight."),
        "deployment_notes": ("deployment notes", "Document the GitHub Pages deployment path used by the portfolio."),
    }
    title, text = sections[task["task_id"]]
    add_section(title, text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
