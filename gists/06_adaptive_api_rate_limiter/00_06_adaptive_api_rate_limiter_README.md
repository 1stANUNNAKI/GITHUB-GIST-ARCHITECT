# GitHub REST & GraphQL API Adaptive Rate-Limit Controller with Exponential Backoff (Python)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_06_adaptive_api_rate_limiter_GUIDE_AR.md`  
> **Curated Collection:** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **Primary Script:** `github_adaptive_api_rate_limiter.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Automates Q&A knowledge sharing on GitHub Discussions by finding a `Q&A` category, opening a technical discussion, posting a detailed solution comment, and marking it as the accepted answer via `markDiscussionCommentAsAnswer`.

## 2. How It Works
1. Queries `discussionCategories` to find an answerable (`isAnswerable = true`) Q&A category.
2. Calls `createDiscussion` and `addDiscussionComment` via GraphQL.
3. Calls `markDiscussionCommentAsAnswer` to mark the solution as accepted.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
