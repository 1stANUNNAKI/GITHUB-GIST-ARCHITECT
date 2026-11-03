# Automate GitHub Discussions Q&A Creation and Mark Accepted Answers via GraphQL API (Python)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_07_discussions_qna_automator_GUIDE_AR.md`  
> **Curated Collection:** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **Primary Script:** `github_discussions_qna_automator.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Audits a developer's GitHub Profile achievement badges and inspects merged Pull Requests via GraphQL to verify GPG signature validity (`signature.isValid`), committer identity, and `Co-authored-by:` trailers.

## 2. How It Works
1. Queries the most recent merged Pull Requests authored by the target user.
2. Inspects each commit's `signature.isValid`, `signature.signer`, and commit message body.
3. Prints a structured diagnostic report of GPG-verified and co-authored Pull Requests.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
