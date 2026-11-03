"""
GitHub Open-Source Repository Scanner & Community Contribution Assistant.
Finds repositories matching custom star and owner-follower ranges and audits
their README and GitHub Actions workflows for high-value improvements.

Environment Variables Required:
  GITHUB_TOKEN : [YOUR_GITHUB_TOKEN]
"""

import base64
import json
import os
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Dict, List

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "[YOUR_GITHUB_TOKEN]")

COMMON_DOC_TYPOS: Dict[str, str] = {
    r"\bteh\b": "the",
    r"\benviroment\b": "environment",
    r"\bdependancies\b": "dependencies",
    r"\bconfiguraton\b": "configuration",
    r"\brepostory\b": "repository",
    r"\boccured\b": "occurred",
    r"\bsuccesfully\b": "successfully",
}


@dataclass
class RepoAuditCandidate:
    full_name: str
    owner_login: str
    stars: int
    owner_followers: int
    suggestion_ar: str


def api_get(path: str) -> dict:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "OpenSource-Repo-Scanner/1.0"}
    if GITHUB_TOKEN and "[YOUR_" not in GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(f"https://api.github.com{path}", headers=headers)
    with urllib.request.urlopen(req, timeout=25) as resp:
        return json.loads(resp.read().decode("utf-8"))


def discover_repositories(
    topic_query: str = "language:python",
    min_stars: int = 0,
    max_stars: int = 200,
    min_followers: int = 50,
    max_followers: int = 500,
    limit: int = 10,
) -> List[RepoAuditCandidate]:
    """Finds public repositories filtered by star count and owner follower count."""
    q = urllib.parse.quote(f"{topic_query} stars:{min_stars}..{max_stars} archived:false")
    search_res = api_get(f"/search/repositories?q={q}&sort=updated&order=desc&per_page=30")
    results: List[RepoAuditCandidate] = []

    for item in search_res.get("items", []):
        owner = item["owner"]["login"]
        user_info = api_get(f"/users/{owner}")
        followers = int(user_info.get("followers", 0))
        if not (min_followers <= followers <= max_followers):
            continue

        full_name = item["full_name"]
        suggestion = "تحسين هيكلة ملف التوثيق README.md وإضافة إرشادات المساهمة القياسية."
        try:
            readme = api_get(f"/repos/{full_name}/readme")
            raw_md = base64.b64decode(readme.get("content", "")).decode("utf-8", errors="ignore")
            for pattern, fix in COMMON_DOC_TYPOS.items():
                if re.search(pattern, raw_md, flags=re.IGNORECASE):
                    suggestion = f"إصلاح خطأ إملائي في التوثيق واستبداله بـ '{fix}' مع تحسين تنسيق الأكواد."
                    break
        except Exception:
            pass

        results.append(
            RepoAuditCandidate(
                full_name=full_name,
                owner_login=owner,
                stars=int(item.get("stargazers_count", 0)),
                owner_followers=followers,
                suggestion_ar=suggestion,
            )
        )
        if len(results) >= limit:
            break

    return results
