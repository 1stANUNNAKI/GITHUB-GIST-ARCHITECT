"""
Automated Project-to-Gist Converter & Master Collection Publisher.
Scans a software project directory, extracts modular scripts/workflows,
sanitizes all tokens and personal identifiers, generates SEO-friendly titles
and Markdown documentation, and publishes individual Gists + a Master Index Gist.
"""

import argparse
import json
import os
import urllib.request
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Optional

from .secret_sanitizer import sanitize_content, assert_clean_for_gist


@dataclass
class GistSpec:
    slug: str
    seo_description: str
    category_list: str
    primary_filename: str
    code_content: str
    guide_filename: str
    guide_markdown: str
    public: bool = True


class GistArchitectPublisher:
    """Publishes sanitized Gists and groups them into a Master Index Gist on GitHub."""

    def __init__(self, github_token: str) -> None:
        if "[YOUR_" in github_token or not github_token.strip():
            raise ValueError(
                "Please set a valid GITHUB_TOKEN with 'gist' scope in your local .env environment."
            )
        self.token = github_token

    def _api(self, method: str, path: str, payload: Optional[dict] = None) -> dict:
        url = f"https://api.github.com{path}"
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(
            url,
            data=data,
            method=method,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "Content-Type": "application/json",
                "User-Agent": "GitHubGistArchitect/1.0",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}

    def publish_gist(self, spec: GistSpec) -> dict:
        """Verifies sanitization and publishes a multi-file Gist (Code + Guide)."""
        assert_clean_for_gist(spec.code_content, spec.primary_filename)
        assert_clean_for_gist(spec.guide_markdown, spec.guide_filename)

        payload = {
            "description": spec.seo_description,
            "public": spec.public,
            "files": {
                spec.guide_filename: {"content": spec.guide_markdown},
                spec.primary_filename: {"content": spec.code_content},
            },
        }
        return self._api("POST", "/gists", payload)

    def publish_collection_index(self, title: str, items: List[Dict[str, str]], public: bool = True) -> dict:
        """Creates a Master Index Gist grouping related Gists into a single searchable list."""
        lines = [
            f"# 📚 {title}",
            "",
            "| # | Gist Title & Function | Direct Gist Link | Primary File |",
            "| :-: | :--- | :---: | :--- |",
        ]
        for idx, item in enumerate(items, start=1):
            lines.append(
                f"| {idx:02d} | **{item['description']}** | [Open Gist]({item['html_url']}) | `{item['filename']}` |"
            )
        content = "\n".join(lines) + "\n"
        assert_clean_for_gist(content, "00_COLLECTION_INDEX.md")

        return self._api(
            "POST",
            "/gists",
            {
                "description": f"[Master Gist List] {title}",
                "public": public,
                "files": {"00_COLLECTION_INDEX.md": {"content": content}},
            },
        )


def scan_and_prepare_directory(source_dir: Path, output_dir: Path) -> List[Path]:
    """Scans a project folder, sanitizes eligible source files, and outputs Gist bundles."""
    eligible_exts = {".py", ".ps1", ".sh", ".js", ".ts", ".yml", ".yaml"}
    created_bundles: List[Path] = []

    for file_path in sorted(source_dir.rglob("*")):
        if not file_path.is_file() or file_path.suffix.lower() not in eligible_exts:
            continue
        if ".git" in file_path.parts or "__pycache__" in file_path.parts:
            continue

        raw_text = file_path.read_text(encoding="utf-8", errors="ignore")
        sanitized = sanitize_content(raw_text).sanitized_text
        assert_clean_for_gist(sanitized, file_path.name)

        bundle_folder = output_dir / file_path.stem
        bundle_folder.mkdir(parents=True, exist_ok=True)
        out_code = bundle_folder / file_path.name
        out_code.write_text(sanitized, encoding="utf-8")
        created_bundles.append(out_code)

    return created_bundles


def main() -> None:
    parser = argparse.ArgumentParser(description="GitHub Gist Architect CLI")
    parser.add_argument("--scan-dir", type=str, help="Project directory to sanitize into Gist bundles")
    parser.add_argument("--out-dir", type=str, default="dist_gists", help="Output folder for sanitized Gists")
    parser.add_argument("--publish-catalog", action="store_true", help="Publish all catalog Gists to GitHub")
    args = parser.parse_args()

    if args.scan_dir:
        bundles = scan_and_prepare_directory(Path(args.scan_dir), Path(args.out_dir))
        print(f"[GIST-ARCHITECT] Prepared {len(bundles)} sanitized Gist bundles in '{args.out_dir}'.")


if __name__ == "__main__":
    main()
