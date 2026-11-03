# Fix GitHub Actions Release & npm/OVSX/VSCode Marketplace Duplicate Version Republish Failures (YAML Pattern)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_10_actions_binary_republish_guard_GUIDE_AR.md`  
> **Curated Collection:** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **Primary Script:** `github_actions_binary_republish_guard.yml`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Prevents CI/CD release and binary upload pipelines from failing when re-running on an already-published version by performing a pre-flight HTTP `200 OK` check (`curl`) and skipping duplicate uploads gracefully.

## 2. How It Works
1. Sends a `HEAD`/`GET` request with `curl` to check whether the target version artifact already exists (`HTTP 200`).
2. Skips the upload step with exit code `0` if already published, or proceeds with the upload if `HTTP 404`.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
