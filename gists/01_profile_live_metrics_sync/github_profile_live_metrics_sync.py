"""
GitHub Profile README Live Stats, Streak & Contribution Counter Auto-Sync.
Queries GitHub REST + GraphQL APIs using only the Python standard library
and updates your Profile README.md with real-time metrics.

Environment Variables Required:
  GITHUB_USERNAME : [YOUR_GITHUB_USERNAME]
  GITHUB_TOKEN    : [YOUR_GITHUB_TOKEN]
"""

import datetime
import json
import os
import re
import time
import urllib.request
from typing import Any, Dict, List, Tuple

USERNAME = os.environ.get("GITHUB_USERNAME", "[YOUR_GITHUB_USERNAME]")
TOKEN = os.environ.get("GITHUB_TOKEN", "[YOUR_GITHUB_TOKEN]")


def github_api(url: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    headers = {
        "User-Agent": "GitHub-Profile-Live-Metrics-Sync/1.0",
        "Accept": "application/vnd.github+json",
    }
    if TOKEN and "[YOUR_" not in TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    data = json.dumps(payload).encode("utf-8") if payload else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_lifetime_contributions(username: str, created_year: int) -> Tuple[int, int, int]:
    """Returns (total_contributions, current_streak, longest_streak) across all years."""
    current_year = datetime.datetime.now(datetime.timezone.utc).year
    total_contribs = 0
    all_days: List[Tuple[str, int]] = []

    for year in range(created_year, current_year + 1):
        start_iso = f"{year}-01-01T00:00:00Z"
        end_iso = f"{year}-12-31T23:59:59Z"
        query = """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            contributionsCollection(from: $from, to: $to) {
              contributionCalendar {
                totalContributions
                weeks {
                  contributionDays {
                    date
                    contributionCount
                  }
                }
              }
            }
          }
        }
        """
        res = github_api(
            "https://api.github.com/graphql",
            {"query": query, "variables": {"login": username, "from": start_iso, "to": end_iso}},
        )
        cal = res["data"]["user"]["contributionsCollection"]["contributionCalendar"]
        total_contribs += int(cal["totalContributions"])
        for week in cal["weeks"]:
            for day in week["contributionDays"]:
                all_days.append((day["date"], int(day["contributionCount"])))

    all_days.sort(key=lambda x: x[0])
    longest, current = 0, 0
    today_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    for date_str, count in all_days:
        if date_str > today_str:
            continue
        if count > 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return total_contribs, current, longest


def main() -> None:
    user_info = github_api(f"https://api.github.com/users/{USERNAME}")
    public_repos = int(user_info.get("public_repos", 0))
    followers = int(user_info.get("followers", 0))
    created_year = int(user_info.get("created_at", "2020-01-01")[:4])

    repos = github_api(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner")
    total_stars = sum(int(r.get("stargazers_count", 0)) for r in repos if isinstance(r, dict))

    total_contribs, current_streak, longest_streak = fetch_lifetime_contributions(USERNAME, created_year)
    print(
        f"Synced {USERNAME}: repos={public_repos}, stars={total_stars}, "
        f"contributions={total_contribs}, streak={current_streak}/{longest_streak}, followers={followers}"
    )

    readme_path = "README.md"
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        cache_bust = str(int(time.time()))
        content = re.sub(r"(\?v=)\d+", rf"\g<1>{cache_bust}", content)
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)


if __name__ == "__main__":
    main()
