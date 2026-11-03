# Pre-Commit Secret Scanner & Token Sanitizer for GitHub Repositories and Gists (Python Zero-Dependency)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_09_pre_commit_secret_sanitizer_GUIDE_AR.md`  
> **Curated Collection:** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **Primary Script:** `github_pre_commit_secret_sanitizer.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Pre-publish security sanitizer that strips API keys, GitHub Personal Access Tokens (`ghp_`, `github_pat_`, `gho_`), OpenAI keys (`sk-`), AWS keys (`AKIA`), Bearer headers, and personal emails from source files before publishing Gists.

## 2. How It Works
1. Scans text/code files against 9 strict regular expression rules for secrets and PII.
2. Replaces sensitive values with standardized placeholders (`[YOUR_GITHUB_TOKEN]`, `[YOUR_GITHUB_USERNAME]`).
3. Verifies zero remaining leaks via `assert_clean_for_gist()`.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
