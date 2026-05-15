#!/usr/bin/env python3
"""Validate Markdown files in this repository.

The checks are intentionally dependency-free so they can run locally and in CI
without installing extra tooling.
"""

from __future__ import annotations

import re
import string
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def markdown_files() -> list[Path]:
    return sorted([ROOT / "README.md", *ROOT.glob("docs/*.md")])


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:"))


def strip_code_spans(text: str) -> str:
    return re.sub(r"`([^`]*)`", r"\1", text)


def github_slug(text: str) -> str:
    text = strip_code_spans(text).strip().lower()
    allowed_punctuation = "-_ "
    remove = "".join(ch for ch in string.punctuation if ch not in allowed_punctuation)
    text = text.translate(str.maketrans("", "", remove))
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def anchors_for(path: Path) -> set[str]:
    anchors: set[str] = set()
    counts: dict[str, int] = defaultdict(int)
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue

        base = github_slug(match.group(2))
        index = counts[base]
        counts[base] += 1
        anchors.add(base if index == 0 else f"{base}-{index}")
    return anchors


def iter_links(path: Path) -> list[str]:
    in_fence = False
    links: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        links.extend(match.group(1) for match in MARKDOWN_LINK_RE.finditer(line))
    return links


def validate_file(path: Path, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    lines = path.read_text(encoding="utf-8").splitlines()

    fence_count = sum(1 for line in lines if line.startswith("```"))
    if fence_count % 2:
        errors.append(f"{rel}: odd number of fenced code block markers: {fence_count}")

    visible_lines: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(lines, start=1):
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence:
            visible_lines.append((number, line))

    h1_count = sum(1 for _number, line in visible_lines if line.startswith("# "))
    if h1_count != 1:
        errors.append(f"{rel}: expected exactly one H1 heading, found {h1_count}")

    previous_level = 0
    for number, line in enumerate(lines, start=1):
        if line.rstrip() != line:
            errors.append(f"{rel}:{number}: trailing whitespace")

    for number, line in visible_lines:
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue

        level = len(match.group(1))
        title = match.group(2).strip()
        if not title:
            errors.append(f"{rel}:{number}: empty heading")
        if previous_level and level > previous_level + 1:
            errors.append(f"{rel}:{number}: heading level jumps from H{previous_level} to H{level}")
        previous_level = level


def validate_links(path: Path, errors: list[str]) -> None:
    rel = path.relative_to(ROOT)
    for raw_target in iter_links(path):
        target = raw_target.strip()
        if not target or is_external(target):
            continue

        target_without_query = target.split("?", 1)[0]
        file_part, _, fragment = target_without_query.partition("#")
        linked_file = path.parent / unquote(file_part) if file_part else path
        linked_file = linked_file.resolve()

        try:
            linked_file.relative_to(ROOT)
        except ValueError:
            errors.append(f"{rel}: link leaves repository: {target}")
            continue

        if not linked_file.exists():
            errors.append(f"{rel}: broken local link: {target}")
            continue

        if fragment:
            fragment = unquote(fragment)
            if fragment not in anchors_for(linked_file):
                errors.append(f"{rel}: missing anchor #{fragment} in {linked_file.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    files = markdown_files()

    for path in files:
        validate_file(path, errors)
        validate_links(path, errors)

    if errors:
        print("Markdown validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
