# GitHub Open-Source Repository Scanner: Find & Fix Typos, Deprecated Actions & Docs via Automated PRs (Python)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_08_open_source_repo_scanner_GUIDE_AR.md`  
> **Curated Collection:** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **Primary Script:** `github_open_source_repo_scanner.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Discovers active open-source GitHub repositories within a specific star range (e.g., `0..200` stars) and filters repository owners by follower count (e.g., `50..500` followers) to identify high-impact community collaboration targets.

## 2. How It Works
1. Searches GitHub repositories by language and star range (`stars:0..200 archived:false`).
2. Queries each repository owner's profile to check their `followers` count.
3. Exports matching repositories to a clean JSON report.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
