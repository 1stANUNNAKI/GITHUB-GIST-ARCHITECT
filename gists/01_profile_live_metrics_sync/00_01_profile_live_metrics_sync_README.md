# GitHub Profile README Live Stats, Streak & Contribution Counter Auto-Sync (Python GraphQL & REST)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_01_profile_live_metrics_sync_GUIDE_AR.md`  
> **Curated Collection:** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **Primary Script:** `github_profile_live_metrics_sync.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Fetches your lifetime GitHub contributions across all years since account creation plus current and longest daily streaks via the GitHub GraphQL API, and updates your Profile README.md with cache-busting timestamps.

## 2. How It Works
1. Queries `user(login)` to detect the exact account creation year.
2. Iterates year-by-year over `contributionsCollection.contributionCalendar` via GraphQL.
3. Computes total lifetime contributions, current streak, and longest streak.
4. Updates `README.md` badge/SVG URLs with `?v=<timestamp>` to bypass GitHub Camo CDN caching.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
