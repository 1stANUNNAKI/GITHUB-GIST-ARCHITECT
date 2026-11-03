# 🏛️ GITHUB-GIST-ARCHITECT — محول المشاريع الذكي إلى GitHub Gists نظيفة ومفهرسة (النسخة العربية)

<div align="center">

[![Language: English](https://img.shields.io/badge/Language-English_(Primary_README)-2563EB?style=for-the-badge)](./README.md)
[![اللغة: العربية](https://img.shields.io/badge/%D8%A7%D9%84%D9%84%D8%BA%D8%A9-%D8%A7%D9%84%D9%86%D8%B3%D8%AE%D8%A9_%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9_(Secondary)-10B981?style=for-the-badge)](./README_AR.md)

![Security Sanitized](https://img.shields.io/badge/Security-100%25_Token_Sanitized-10B981?style=for-the-badge)
![Gist Catalog](https://img.shields.io/badge/Curated_Gists-10_Modules_%2F_3_Lists-6366F1?style=for-the-badge)
![AI Skill](https://img.shields.io/badge/AI_Skill-project--to--gist--converter-F59E0B?style=for-the-badge)

**المنظومة الهندسية المتكاملة لتحليل المشاريع البرمجية، تطهيرها من التوكنات والرموز الشخصية، وتحويل كل أداة ووظيفة فيها إلى GitHub Gist مستقل بعناوين بحثية قياسية (SEO-Optimized) ومجمّعة في قوائم مهام كبرى (Master Gist Lists).**

[🇬🇧 Primary English Documentation (`README.md`)](./README.md) · [📐 الخطة والمعمارية بالتفصيل](./docs/PLAN_AND_ARCHITECTURE_AR.md) · [📚 الفهرس العام والقوائم الثلاث](./collections/00_MASTER_GIST_CATALOG.md) · [🤖 مهارة الذكاء الاصطناعي (`SKILL.md`)](./skills/project-to-gist-converter/SKILL.md)

</div>

---

## 🌟 1. ماذا يقدم هذا المستودع؟

يجمع هذا المستودع بين **مكتبة Gists قياسية جاهزة** (مستخلصة من أنظمتنا السابقة لأتمتة بروفايل GitHub، البطاقات الحية، طلبات السحب الموثقة بـ GPG عبر GraphQL، وفحص المستودعات المجتمعية) وبين **محرك ومهارة ذكاء اصطناعي (`/gistify`)** لتحويل أي مشروع مستقبلي إلى Gists خالية تماماً من التوكنات والبيانات الحساسة.

### المزايا الرئيسية:
* 🧹 **تطهير أمني آلي صارم (`src/secret_sanitizer.py`):** فحص وحذف أي مفاتيح سرية (`ghp_`, `github_pat_`, `sk-`, `AKIA`) أو عناوين بريد إلكتروني شخصية واستبدالها بعناصر نائبة آمنة (`[YOUR_GITHUB_TOKEN]`) قبل النشر.
* 🔍 **عناوين بحثية ذكية (GitHub Search SEO):** صياغة عنوان كل Gist بكلمات مفتاحية دقيقة ومباشرة بحيث يجده أي مطور يبحث في GitHub فوراً.
* 🗂️ **نظام القوائم المجمعة (Curated Gist Lists / Collections):** تجميع كل مجموعة Gists تشترك في مهمة كبرى داخل قائمة مرجعية موحدة (`collections/`) وفهرس Gist جامع.
* 🤖 **مهارة وأمر ذكاء اصطناعي جاهز (`project-to-gist-converter` & `/gistify`):** إعداد متكامل للوكلاء لتحويل أي مستودع إلى Gists منظمة بأمر واحد.

---

## 🗂️ 2. قوائم الـ Gists الكبرى (The 3 Master Gist Lists)

لتنظيم الـ Gists حسب المهام الكبيرة، تم تقسيم النظام إلى **3 قوائم رئيسية**:

| رقم القائمة | اسم القائمة ومهمتها الكبرى | عدد الـ Gists | رابط القائمة الكاملة |
| :-: | :--- | :-: | :---: |
| **List 01** | **منظومة أتمتة بروفايل GitHub والبطاقات الحية (Profile Telemetry & SVG Suite)** | `4 Gists` | [📂 استعراض القائمة الأولى](./collections/LIST_01_PROFILE_TELEMETRY_AND_SVG.md) |
| **List 02** | **منظومة هندسة طلبات السحب الموثقة والأوسمة (GraphQL GPG PR & Achievements Suite)** | `3 Gists` | [📂 استعراض القائمة الثانية](./collections/LIST_02_PR_AND_ACHIEVEMENTS_ENGINE.md) |
| **List 03** | **منظومة فحص المستودعات المجتمعية والأمان الوقائي (Community Scanner & Security Suite)** | `3 Gists` | [📂 استعراض القائمة الثالثة](./collections/LIST_03_COMMUNITY_SCANNER_AND_SECURITY.md) |

---

## 📋 3. جدول الـ 10 Gists التفصيلية (مع الكود والشرح المستقل)

| # | عنوان الـ Gist البحثي (SEO Title) والوظيفة | ملف الكود النظيف | الشرح المستقل |
| :-: | :--- | :---: | :---: |
| **#01** | **Auto-Update GitHub Profile README Live Contributions & Streak Stats via GraphQL (Python)**<br/>_جلب إجمالي المساهمات الحقيقية عبر جميع السنوات (Lifetime Contributions) والسلسلة اليومية (Current & Longest Streak) عبر GraphQL وتحديث بطاقات البروفايل تلقائياً مع كسر الكاش._ | [`github_profile_live_metrics_sync.py`](./gists/01_profile_live_metrics_sync/github_profile_live_metrics_sync.py) | [`الشرح المفصل`](./gists/01_profile_live_metrics_sync/00_01_profile_live_metrics_sync_GUIDE_AR.md) |
| **#02** | **Generate Custom GitHub Streak & Achievements Trophy SVG Cards Locally (Midnight Galaxy Theme - Python)**<br/>_توليد بطاقات SVG الإحصائية (`streak-stats.svg` و `trophies.svg`) محلياً داخل المستودع بألوان ثيم `Midnight Galaxy` الموحدة دون الاعتماد على خوادم الطرف الثالث البطيئة أو المتوقفة._ | [`github_custom_svg_cards_generator.py`](./gists/02_custom_svg_cards_generator/github_custom_svg_cards_generator.py) | [`الشرح المفصل`](./gists/02_custom_svg_cards_generator/00_02_custom_svg_cards_generator_GUIDE_AR.md) |
| **#03** | **Generate Interactive 3D Spiral Galaxy SVG of GitHub Repositories & Languages (Python)**<br/>_رسم مجرة حلزونية فلكية (`repo-galaxy.svg`) تمثل جميع مستودعات الحساب كنجوم مضيئة مصنفة حسب لغات البرمجة وحجم النجوم._ | [`github_repo_galaxy_svg_visualizer.py`](./gists/03_repo_galaxy_svg_visualizer/github_repo_galaxy_svg_visualizer.py) | [`الشرح المفصل`](./gists/03_repo_galaxy_svg_visualizer/00_03_repo_galaxy_svg_visualizer_GUIDE_AR.md) |
| **#04** | **GitHub Actions Cron Workflow to Auto-Sync Profile README Stats Every 6 Hours (YAML)**<br/>_ملف سير عمل GitHub Actions يعمل تلقائياً كل 6 ساعات لتحديث إحصائيات البروفايل وبطاقات الـ SVG وعمل Commit آلي دون أي تدخل يدوي._ | [`profile-metrics-auto-sync.yml`](./gists/04_github_actions_profile_cron/profile-metrics-auto-sync.yml) | [`الشرح المفصل`](./gists/04_github_actions_profile_cron/00_04_github_actions_profile_cron_GUIDE_AR.md) |
| **#05** | **Create GPG-Verified GitHub Commits & Pull Requests via GraphQL createCommitOnBranch (Python)**<br/>_إنشاء التزامات (Commits) موقعة رقمياً وموثقة بعلامة `Verified` الرسمية من GitHub عبر طفرة GraphQL `createCommitOnBranch` مع دعم المشاركين (`Co-authored-by`) وفتح ودمج طلبات السحب آلياً._ | [`github_graphql_gpg_verified_pr_engine.py`](./gists/05_graphql_gpg_verified_pr_engine/github_graphql_gpg_verified_pr_engine.py) | [`الشرح المفصل`](./gists/05_graphql_gpg_verified_pr_engine/00_05_graphql_gpg_verified_pr_engine_GUIDE_AR.md) |
| **#06** | **Create Answered GitHub Discussions & Mark Accepted Answer via GraphQL API (Python)**<br/>_أتمتة إنشاء النقاشات المعرفية (Q&A Discussions) في مستودعات GitHub وإضافة الرد النموذجي واعتماده كإجابة مقبولة (`markDiscussionCommentAsAnswer`) لتوثيق الحلول الهندسية._ | [`github_graphql_discussion_answer_automator.py`](./gists/06_graphql_discussion_answer_automator/github_graphql_discussion_answer_automator.py) | [`الشرح المفصل`](./gists/06_graphql_discussion_answer_automator/00_06_graphql_discussion_answer_automator_GUIDE_AR.md) |
| **#07** | **Audit GitHub Profile Achievements & Merged PR Signature Status via GraphQL (Python)**<br/>_فحص وتدقيق حالة الأوسمة والشارات على حساب GitHub والتحقق من صحة التوقيع الرقمي (`signature.isValid`) وتذييلات المشاركة (`Co-authored-by`) في طلبات السحب المدمجة._ | [`github_achievements_progress_auditor.py`](./gists/07_github_achievements_progress_auditor/github_achievements_progress_auditor.py) | [`الشرح المفصل`](./gists/07_github_achievements_progress_auditor/00_07_github_achievements_progress_auditor_GUIDE_AR.md) |
| **#08** | **Discover Active Open-Source GitHub Repositories by Star Count & Owner Followers (Python)**<br/>_أداة البحث الذكي عن المستودعات مفتوحة المصدر النشطة ضمن نطاق نجوم محدد (مثلاً 0 إلى 200 نجمة) وفلترة أصحابها حسب عدد المتابعين (مثلاً 50 إلى 500 متابع) لتقديم مساهمات برمجية فعالة._ | [`github_community_repo_discovery_scanner.py`](./gists/08_community_repo_discovery_scanner/github_community_repo_discovery_scanner.py) | [`الشرح المفصل`](./gists/08_community_repo_discovery_scanner/00_08_community_repo_discovery_scanner_GUIDE_AR.md) |
| **#09** | **Sanitize Code Files & Strip API Tokens, PATs, and Personal Emails Before Publishing Gists (Python)**<br/>_الأداة الوقائية لتنظيف وتطهير أي ملف برمجي أو مشروع كامل من التوكنات (`ghp_`, `github_pat_`, `sk-`, `AKIA`) والإيميلات والمعرفات الشخصية قبل نشره كـ Gist عام._ | [`gist_secret_and_token_sanitizer.py`](./gists/09_code_secret_and_token_sanitizer/gist_secret_and_token_sanitizer.py) | [`الشرح المفصل`](./gists/09_code_secret_and_token_sanitizer/00_09_code_secret_and_token_sanitizer_GUIDE_AR.md) |
| **#10** | **Fix GitHub Actions Release Republish Failure with Pre-Flight HTTP 200 Check (Bash / YAML)**<br/>_حل مشكلة توقف خطوط النشر الآلي (CI/CD Release Pipelines) عند إعادة تشغيل Workflow لإصدار منشور مسبقاً، عبر فحص HTTP 200 المسبق وتخطي الرفع المكرر بأمان (Idempotent Release Guard)._ | [`ci_idempotent_publish_guard.sh`](./gists/10_actions_binary_republish_guard/ci_idempotent_publish_guard.sh) | [`الشرح المفصل`](./gists/10_actions_binary_republish_guard/00_10_actions_binary_republish_guard_GUIDE_AR.md) |

---

## 🤖 4. كيف تستخدم مهارة الذكاء الاصطناعي لتحويل أي مشروع إلى Gists؟

### أ. عبر أمر الذكاء الاصطناعي المباشر (`/gistify`)
تم تضمين المهارة في المسارات القياسية:
- [`skills/project-to-gist-converter/SKILL.md`](./skills/project-to-gist-converter/SKILL.md)
- [`.agents/skills/project-to-gist-converter/SKILL.md`](./.agents/skills/project-to-gist-converter/SKILL.md)
- [`.claude/commands/gistify.md`](./.claude/commands/gistify.md)

فقط اطلب من الوكيل:
```text
/gistify ./path/to/any/project
```
أو بالعربية:
```text
استخدم مهارة project-to-gist-converter لتحليل هذا المشروع وتحويله إلى Gists منظمة وخالية من التوكنات.
```

### ب. عبر أداة سطر الأوامر البرمجية (`CLI`)
```bash
python src/project_to_gist_converter.py --source ./path/to/project --output ./dist_gists --strip-user "YOUR_PRIVATE_HANDLE"
```

### ج. نشر جميع الـ Gists دفعة واحدة إلى `gist.github.com`
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\Publish-AllGists.ps1
```
*(يقوم السكربت بالتحقق من صلاحية `gist` وطلب ترقيتها تلقائياً عبر GitHub Device Flow إن لزم، ثم ينشر كافة الـ Gists العشر وينشئ Gist الفهرس الرئيسي الجامع).*
