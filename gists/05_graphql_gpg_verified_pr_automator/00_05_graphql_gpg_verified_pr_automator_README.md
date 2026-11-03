# Create GPG-Verified Commits & Merge Pull Requests via GitHub GraphQL API (createCommitOnBranch Python)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_05_graphql_gpg_verified_pr_automator_GUIDE_AR.md`  
> **Curated Collection:** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **Primary Script:** `github_graphql_gpg_verified_pr_automator.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Creates server-side GPG-verified commits (`signature.isValid = true`, signed by GitHub's official web-flow key) via the GraphQL `createCommitOnBranch` mutation, supports `Co-authored-by:` trailers, and opens/merges Pull Requests.

## 2. How It Works
1. Resolves the target repository ID and base branch `HEAD` OID via GraphQL.
2. Creates a feature branch and commits base64-encoded file changes via `createCommitOnBranch`.
3. Appends optional `Co-authored-by:` trailers and merges the resulting Pull Request cleanly.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
