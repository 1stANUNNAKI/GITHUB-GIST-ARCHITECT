"""
GitHub Gist & Repository Secret Sanitizer Engine.
Scans source code and documentation for personal tokens, API keys, credentials,
emails, and account-specific identifiers, replacing them with safe placeholders.
"""

import re
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class SanitizationResult:
    sanitized_text: str
    replacements_made: int
    detected_Categories: List[str]


SANITIZATION_RULES: List[Tuple[str, str, str]] = [
    ("GitHub Classic PAT", r"ghp_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_TOKEN]"),
    ("GitHub Fine-Grained PAT", r"github_pat_[A-Za-z0-9_]{20,255}", "[YOUR_GITHUB_TOKEN]"),
    ("GitHub OAuth Token", r"gho_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_OAUTH_TOKEN]"),
    ("GitHub User-to-Server Token", r"ghu_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_USER_TOKEN]"),
    ("GitHub Server-to-Server Token", r"ghs_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_SERVER_TOKEN]"),
    ("GitHub Refresh Token", r"ghr_[A-Za-z0-9]{20,255}", "[YOUR_GITHUB_REFRESH_TOKEN]"),
    ("OpenAI / API Secret Key", r"sk-[A-Za-z0-9]{20,255}", "[YOUR_API_SECRET_KEY]"),
    ("AWS Access Key ID", r"AKIA[0-9A-Z]{16}", "[YOUR_AWS_ACCESS_KEY_ID]"),
    ("Slack Token", r"xox[baprs]-[A-Za-z0-9-]{10,255}", "[YOUR_SLACK_TOKEN]"),
    ("Private Key Block", r"-----BEGIN [A-Z ]*PRIVATE KEY-----[\s\S]*?-----END [A-Z ]*PRIVATE KEY-----", "[REDACTED_PRIVATE_KEY]"),
    ("GitHub Noreply Email", r"\b\d+\+[A-Za-z0-9-]+@users\.noreply\.github\.com\b", "[YOUR_ID]+[YOUR_GITHUB_USERNAME]@users.noreply.github.com"),
    ("Generic Personal Email", r"\b(?!noreply@github\.com)[A-Za-z0-9._%+-]+@(?:gmail|yahoo|hotmail|outlook|icloud)\.com\b", "[YOUR_EMAIL_ADDRESS]"),
]


def sanitize_content(text: str, custom_identifiers: Dict[str, str] | None = None) -> SanitizationResult:
    """Sanitizes sensitive tokens, emails, and custom user identifiers from text."""
    result = text
    total_replacements = 0
    categories: List[str] = []

    for label, pattern, replacement in SANITIZATION_RULES:
        matches = list(re.finditer(pattern, result))
        if matches:
            total_replacements += len(matches)
            categories.append(label)
            result = re.sub(pattern, replacement, result)

    if custom_identifiers:
        for raw_val, placeholder in custom_identifiers.items():
            if raw_val and raw_val in result:
                count = result.count(raw_val)
                total_replacements += count
                categories.append(f"Custom Identifier ({placeholder})")
                result = result.replace(raw_val, placeholder)

    return SanitizationResult(
        sanitized_text=result,
        replacements_made=total_replacements,
        detected_Categories=categories,
    )


def assert_clean_for_gist(text: str, filename: str = "<memory>") -> None:
    """Raises ValueError if any raw credential pattern remains in the text."""
    for label, pattern, _ in SANITIZATION_RULES[:10]:
        if re.search(pattern, text):
            raise ValueError(f"Security Gate Blocked '{filename}': detected unsanitized {label}!")
