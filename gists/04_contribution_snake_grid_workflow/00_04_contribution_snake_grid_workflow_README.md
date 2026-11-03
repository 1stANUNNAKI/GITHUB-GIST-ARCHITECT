# GitHub Actions Workflow: Generate Dark & Light Contribution Grid Snake Animation SVG (Platane/snk)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_04_contribution_snake_grid_workflow_GUIDE_AR.md`  
> **Curated Collection:** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **Primary Script:** `github_contribution_snake_grid_workflow.yml`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Production-ready GitHub Actions workflow (`profile-metrics-auto-sync.yml`) that runs every 6 hours (`0 */6 * * *`) to synchronize profile metrics, regenerate SVG cards, and commit changes with `[skip ci]` loop protection.

## 2. How It Works
1. Triggers automatically every 6 hours via `schedule` or manually via `workflow_dispatch`.
2. Runs the Python telemetry and SVG generation scripts using `GITHUB_TOKEN`.
3. Commits and pushes updated SVG/README files only when actual changes are detected.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
