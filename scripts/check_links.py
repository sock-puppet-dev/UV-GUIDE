#!/usr/bin/env python3
"""Check Markdown links.

By default, this checks only local links. Pass --external to also check HTTP(S)
links. External checks are best suited for CI because they need network access.
"""

from __future__ import annotations

import argparse
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
USER_AGENT = "uv-guide-link-checker/1.0"


def markdown_files() -> list[Path]:
    return sorted([ROOT / "README.md", *ROOT.glob("docs/*.md")])


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


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://"))


def check_local_link(path: Path, target: str) -> str | None:
    target_without_query = target.split("?", 1)[0]
    file_part, _, _fragment = target_without_query.partition("#")
    if not file_part:
        return None

    linked_file = (path.parent / unquote(file_part)).resolve()
    try:
        linked_file.relative_to(ROOT)
    except ValueError:
        return f"{path.relative_to(ROOT)}: link leaves repository: {target}"

    if not linked_file.exists():
        return f"{path.relative_to(ROOT)}: broken local link: {target}"

    return None


def request_url(url: str, method: str) -> int:
    request = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
    context = ssl.create_default_context()
    with urllib.request.urlopen(request, timeout=20, context=context) as response:
        return response.status


def check_external_link(path: Path, target: str) -> str | None:
    try:
        status = request_url(target, "HEAD")
    except urllib.error.HTTPError as exc:
        if exc.code in {403, 405, 429}:
            try:
                status = request_url(target, "GET")
            except Exception as get_exc:  # noqa: BLE001 - report any URL failure.
                return f"{path.relative_to(ROOT)}: {target} failed GET fallback: {get_exc}"
        else:
            return f"{path.relative_to(ROOT)}: {target} returned HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report any URL failure.
        return f"{path.relative_to(ROOT)}: {target} failed: {exc}"

    if status >= 400:
        return f"{path.relative_to(ROOT)}: {target} returned HTTP {status}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="also check HTTP(S) links")
    args = parser.parse_args()

    errors: list[str] = []
    checked_external: set[str] = set()

    for path in markdown_files():
        for raw_target in iter_links(path):
            target = raw_target.strip()
            if not target or target.startswith("mailto:"):
                continue

            if is_external(target):
                if args.external and target not in checked_external:
                    checked_external.add(target)
                    error = check_external_link(path, target)
                    if error:
                        errors.append(error)
                continue

            error = check_local_link(path, target)
            if error:
                errors.append(error)

    if errors:
        print("Link check failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    mode = "local and external" if args.external else "local"
    print(f"Checked {mode} links in {len(markdown_files())} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
