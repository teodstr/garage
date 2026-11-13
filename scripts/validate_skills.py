#!/usr/bin/env python3
"""Check that every skill in skills/ follows the garage format.

Checks, for each skills/<folder>/SKILL.md:
- the file starts with a frontmatter block (between two --- lines)
- name: matches the folder, is kebab-case and has at most 64 characters
- description: is present and has at most 1024 characters
- the required sections are present, in order
- the Terminology table has English, Français and Español columns
- the file stays short (at most 250 lines)
- the skill is listed in README.md

Run from the repository root:  python3 scripts/validate_skills.py
Only the Python standard library is needed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"

REQUIRED_SECTIONS = [
    "## When to use",
    "## Inputs",
    "## Method",
    "## Output",
    "## Quality bar",
    "## Terminology",
    "## Sources",
]
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TERMINOLOGY_HEADER = re.compile(r"\|\s*English\s*\|\s*Français\s*\|\s*Español\s*\|")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_LINES = 250


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str]:
    """Return (fields, body). Supports single-line values and folded (>) blocks."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return None, text

    fields: dict[str, str] = {}
    current_key = None
    for line in lines[1:end]:
        if line and not line[0].isspace() and ":" in line:
            key, _, value = line.partition(":")
            key, value = key.strip(), value.strip()
            if value in {">", ">-", "|", "|-"}:
                fields[key] = ""
                current_key = key
            else:
                fields[key] = value.strip("\"'")
                current_key = None
        elif current_key is not None:
            fields[current_key] = f"{fields[current_key]} {line.strip()}".strip()
    return fields, "\n".join(lines[end + 1 :])


def without_code_blocks(markdown: str) -> str:
    """Remove fenced code blocks so headings inside templates are ignored."""
    return re.sub(r"```.*?```", "", markdown, flags=re.DOTALL)


def check_skill(folder: Path, readme_text: str) -> list[str]:
    label = f"skills/{folder.name}"
    skill_file = folder / "SKILL.md"
    if not skill_file.is_file():
        return [f"{label}: SKILL.md is missing"]

    text = skill_file.read_text(encoding="utf-8")
    fields, body = parse_frontmatter(text)
    if fields is None:
        return [f"{label}: SKILL.md must start with a frontmatter block between two --- lines"]

    errors = []
    name = fields.get("name", "")
    description = fields.get("description", "")

    if name != folder.name:
        errors.append(f"{label}: name is '{name}' but must match the folder name '{folder.name}'")
    if not NAME_PATTERN.match(name) or len(name) > MAX_NAME_LENGTH:
        errors.append(f"{label}: name must be kebab-case (like 'porter-five-forces') and at most {MAX_NAME_LENGTH} characters")
    if not description:
        errors.append(f"{label}: description is missing")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(f"{label}: description has {len(description)} characters (maximum {MAX_DESCRIPTION_LENGTH})")

    prose = without_code_blocks(body)
    positions = []
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^{re.escape(section)}\s*$", prose, flags=re.MULTILINE)
        if match is None:
            errors.append(f"{label}: section '{section}' is missing")
        else:
            positions.append(match.start())
    if len(positions) == len(REQUIRED_SECTIONS) and positions != sorted(positions):
        order = ", ".join(section[3:] for section in REQUIRED_SECTIONS)
        errors.append(f"{label}: sections must appear in this order: {order}")

    terminology = prose.split("## Terminology", 1)[-1].split("## Sources", 1)[0]
    if "## Terminology" in prose and not TERMINOLOGY_HEADER.search(terminology):
        errors.append(f"{label}: the Terminology table needs the columns English | Français | Español")

    line_count = len(text.splitlines())
    if line_count > MAX_LINES:
        errors.append(f"{label}: {line_count} lines (maximum {MAX_LINES}); move details to skills/{folder.name}/references/")

    if f"skills/{folder.name}/" not in readme_text:
        errors.append(f"{label}: add this skill to the table in README.md")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("No skills/ folder found. Run this script from the repository.")
        return 1

    readme_text = README.read_text(encoding="utf-8") if README.is_file() else ""
    folders = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    errors = [error for folder in folders for error in check_skill(folder, readme_text)]

    if errors:
        print(f"{len(errors)} problem(s) found:\n")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"All {len(folders)} skills are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
