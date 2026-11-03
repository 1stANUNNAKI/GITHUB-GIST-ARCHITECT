# Generate Custom GitHub Streak & Achievements Trophy SVG Cards Locally (Midnight Galaxy Theme - Python)

> **Language:** 🇬🇧 English (Primary) | 🇸🇦 Arabic Guide included below in `00_02_custom_svg_cards_generator_GUIDE_AR.md`  
> **Curated Collection:** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **Primary Script:** `github_custom_svg_cards_generator.py`  
> **Security Status:** `100% Sanitized (Zero Tokens / Zero Personal Identifiers)`

---

## 1. Purpose & Use Case
Generates custom, high-contrast GitHub Streak and Trophy SVG cards (`streak-stats.svg`) locally in a unified Midnight Galaxy theme (`#060B1E`, `#5B5C8A`, `#FACC15`) without relying on slow or rate-limited third-party servers.

## 2. How It Works
1. Receives live contribution metrics (Total Contributions, Current Streak, Longest Streak).
2. Constructs a crisp vector SVG tree styled with the Midnight Galaxy color palette.
3. Saves `streak-stats.svg` directly inside your repository for instant embedding in `README.md`.

## 3. Quick Start & Configuration
Replace any placeholder environment variables before running:

```bash
export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
```
