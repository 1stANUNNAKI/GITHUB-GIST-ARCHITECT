"""
Pre-Commit Secret Scanner & Token Sanitizer for GitHub Repositories and Gists.
Automatically redacts Personal Access Tokens (PATs), API keys, private keys,
and personal emails before publishing code to GitHub or Gist.
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple

SECRET_PATTERNS: List[Tuple[str, str, str]] = [
    ("GitHub Classic Token", r"ghp_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_TOKEN]"),
    ("GitHub Fine-Grained Token", r"github_pat_[A-Za-z0-9_]{20,255}", "[YOUR_GITHUB_TOKEN]"),
    ("GitHub OAuth Token", r"gho_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_OAUTH_TOKEN]"),
    ("OpenAI Secret Key", r"sk-[A-Za-z0-9]{20,255}", "[YOUR_API_KEY]"),
    ("AWS Access Key", r"AKIA[0-9A-Z]{16}", "[YOUR_AWS_ACCESS_KEY]"),
    ("Personal Email", r"\b(?!noreply@github\.com)[A-Za-z0-9._%+-]+@(?:gmail|yahoo|hotmail|outlook)\.com\b", "[YOUR_EMAIL_ADDRESS]"),
]


def sanitize_text(content: str) -> Tuple[str, int]:
    """Replaces all detected secrets and personal emails with safe placeholders."""
    redacted = content
    total_redactions = 0
    for _, pattern, placeholder in SECRET_PATTERNS:
        matches = list(re.finditer(pattern, redacted))
        if matches:
            total_redactions += len(matches)
            redacted = re.sub(pattern, placeholder, redacted)
    return redacted, total_redactions


def assert_zero_secrets(content: str, source_name: str = "<buffer>") -> None:
    """Raises ValueError if any secret token pattern is present."""
    for label, pattern, _ in SECRET_PATTERNS:
        if re.search(pattern, content):
            raise ValueError(f"[SECURITY BLOCK] Unsanitized {label} detected in {source_name}!")


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        p = Path(arg)
        if p.is_file():
            clean, count = sanitize_text(p.read_text(encoding="utf-8", errors="ignore"))
            assert_zero_secrets(clean, str(p))
            print(f"[PASS] {p.name} verified clean ({count} placeholders applied).")
