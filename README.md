# 🏛️ GITHUB-GIST-ARCHITECT — محول المشاريع الذكي إلى GitHub Gists نظيفة ومفهرسة

<div align="center">

![Security Sanitized](https://img.shields.io/badge/Security-100%25_Token_Sanitized-10B981?style=for-the-badge)
![Gist Catalog](https://img.shields.io/badge/Curated_Gists-10_Modules_%2F_3_Lists-6366F1?style=for-the-badge)
![AI Skill](https://img.shields.io/badge/AI_Skill-project--to--gist--converter-F59E0B?style=for-the-badge)

**المنظومة الهندسية المتكاملة لتحليل المشاريع البرمجية، تطهيرها من التوكنات والرموز الشخصية، وتحويل كل أداة ووظيفة فيها إلى GitHub Gist مستقل بعناوين بحثية قياسية (SEO-Optimized) ومجمّعة في قوائم مهام كبرى (Master Gist Lists).**

[📐 الخطة والمعمارية بالتفصيل](./docs/PLAN_AND_ARCHITECTURE_AR.md) · [📚 الفهرس العام والقوائم الثلاث](./collections/00_MASTER_GIST_CATALOG.md) · [🤖 مهارة الذكاء الاصطناعي (`SKILL.md`)](./skills/project-to-gist-converter/SKILL.md)

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
| **#01** | **GitHub Profile README Live Stats, Streak & Contribution Counter Auto-Sync (Python GraphQL & REST)**<br/>_مزامنة إحصائيات بروفايل GitHub الحية (إجمالي المساهمات الفعلية عبر GraphQL، أطول سلسلة أيام متتالية Streak، النجوم، المستودعات العامة، والمتابعين) وتحديث ملف README.md تلقائياً بدون أي مكتبات خارجية._ | [`github_profile_live_metrics_sync.py`](./gists/01_profile_live_metrics_sync/github_profile_live_metrics_sync.py) | [`الشرح المفصل`](./gists/01_profile_live_metrics_sync/00_01_profile_live_metrics_sync_GUIDE_AR.md) |
| **#02** | **Generate Custom GitHub Streak & Achievements Trophy SVG Cards Locally (Midnight Galaxy Theme - Python)**<br/>_توليد بطاقات SVG الإحصائية (`streak-stats.svg` و `trophies.svg`) محلياً داخل المستودع بألوان ثيم `Midnight Galaxy` الموحدة دون الاعتماد على خوادم الطرف الثالث البطيئة أو المتوقفة._ | [`github_custom_svg_cards_generator.py`](./gists/02_custom_svg_cards_generator/github_custom_svg_cards_generator.py) | [`الشرح المفصل`](./gists/02_custom_svg_cards_generator/00_02_custom_svg_cards_generator_GUIDE_AR.md) |
| **#03** | **GitHub Actions Workflow: Auto-Update Profile README Stats & SVG Cards Every Hour (Cron Schedule)**<br/>_ملف أتمتة GitHub Actions جاهز يعمل تلقائياً على مدار الساعة (`0 * * * *`) لتشغيل سكربت المزامنة وتوليد البطاقات ورفع التحديثات إلى المستودع دون أي تدخل يدوي._ | [`github_profile_hourly_sync_workflow.yml`](./gists/03_profile_hourly_sync_workflow/github_profile_hourly_sync_workflow.yml) | [`الشرح المفصل`](./gists/03_profile_hourly_sync_workflow/00_03_profile_hourly_sync_workflow_GUIDE_AR.md) |
| **#04** | **GitHub Actions Workflow: Generate Dark & Light Contribution Grid Snake Animation SVG (Platane/snk)**<br/>_توليد رسم الثعبان المتحرك على شبكة المساهمات الخضراء (Contribution Grid Snake) للوضعين الليلي والنهاري تلقائياً كل 6 ساعات ونشره في فرع `output`._ | [`github_contribution_snake_grid_workflow.yml`](./gists/04_contribution_snake_grid_workflow/github_contribution_snake_grid_workflow.yml) | [`الشرح المفصل`](./gists/04_contribution_snake_grid_workflow/00_04_contribution_snake_grid_workflow_GUIDE_AR.md) |
| **#05** | **Create GPG-Verified Commits & Merge Pull Requests via GitHub GraphQL API (createCommitOnBranch Python)**<br/>_إنشاء التزامات موقّعة رسمياً بتوقيع GitHub GPG (`Verified` / `signature.isValid = true`) مع دعم تذييل المؤلف المشارك (`Co-authored-by:`) وفتح ودمج طلبات السحب عبر GraphQL API._ | [`github_graphql_gpg_verified_pr_automator.py`](./gists/05_graphql_gpg_verified_pr_automator/github_graphql_gpg_verified_pr_automator.py) | [`الشرح المفصل`](./gists/05_graphql_gpg_verified_pr_automator/00_05_graphql_gpg_verified_pr_automator_GUIDE_AR.md) |
| **#06** | **GitHub REST & GraphQL API Adaptive Rate-Limit Controller with Exponential Backoff (Python)**<br/>_حماية سكربتات الأتمتة من تجاوز حدود طلبات GitHub API (`Primary & Secondary Rate Limits`) عبر قراءة ترويسات الاستجابة وإدارة التوقف الذكي التلقائي._ | [`github_adaptive_api_rate_limiter.py`](./gists/06_adaptive_api_rate_limiter/github_adaptive_api_rate_limiter.py) | [`الشرح المفصل`](./gists/06_adaptive_api_rate_limiter/00_06_adaptive_api_rate_limiter_GUIDE_AR.md) |
| **#07** | **Automate GitHub Discussions Q&A Creation and Mark Accepted Answers via GraphQL API (Python)**<br/>_أتمتة بناء قاعدة المعرفة والأسئلة الشائعة (Q&A Discussions) في مستودعات GitHub واعتماد الإجابات الصحيحة عبر GraphQL API (المسار التقني الخاص بوسام Galaxy Brain)._ | [`github_discussions_qna_automator.py`](./gists/07_discussions_qna_automator/github_discussions_qna_automator.py) | [`الشرح المفصل`](./gists/07_discussions_qna_automator/00_07_discussions_qna_automator_GUIDE_AR.md) |
| **#08** | **GitHub Open-Source Repository Scanner: Find & Fix Typos, Deprecated Actions & Docs via Automated PRs (Python)**<br/>_فحص المستودعات العامة على GitHub حسب نطاق النجوم وعدد متابعي المالك، واكتشاف فرص التحسين الحقيقية (إصلاح الأخطاء الإملائية، ترقية GitHub Actions القديمة، وتحسين تنسيق Markdown) وتوليد تقارير مشاركة مجتمعية بالعربية._ | [`github_open_source_repo_scanner.py`](./gists/08_open_source_repo_scanner/github_open_source_repo_scanner.py) | [`الشرح المفصل`](./gists/08_open_source_repo_scanner/00_08_open_source_repo_scanner_GUIDE_AR.md) |
| **#09** | **Pre-Commit Secret Scanner & Token Sanitizer for GitHub Repositories and Gists (Python Zero-Dependency)**<br/>_فحص وتطهير الأكواد والملفات قبل رفعها إلى GitHub أو نشرها كـ Gist، واكتشاف أي مفاتيح سرية (`ghp_`, `github_pat_`, `sk-`, `AKIA`) أو إيميلات شخصية واستبدالها تلقائياً بعناصر نائبة آمنة._ | [`github_pre_commit_secret_sanitizer.py`](./gists/09_pre_commit_secret_sanitizer/github_pre_commit_secret_sanitizer.py) | [`الشرح المفصل`](./gists/09_pre_commit_secret_sanitizer/00_09_pre_commit_secret_sanitizer_GUIDE_AR.md) |
| **#10** | **Fix GitHub Actions Release & npm/OVSX/VSCode Marketplace Duplicate Version Republish Failures (YAML Pattern)**<br/>_قالب GitHub Actions هندسي جاهز لحل مشكلة فشل عمليات الـ Deploy والـ Release عند إعادة تشغيل المهام (Re-run Failed Jobs) بسبب وجود الإصدار مسبقاً على npm أو VS Code Marketplace أو OpenVSX أو فشل تحميل FFmpeg._ | [`github_actions_binary_republish_guard.yml`](./gists/10_actions_binary_republish_guard/github_actions_binary_republish_guard.yml) | [`الشرح المفصل`](./gists/10_actions_binary_republish_guard/00_10_actions_binary_republish_guard_GUIDE_AR.md) |

---

## 🤖 4. كيف تستخدم مهارة الذكاء الاصطناعي لتحويل أي مشروع إلى Gists؟

### أ. عبر أمر الذكاء الاصطناعي المباشر (`/gistify`)
تم تضمين المهارة في المسارات القياسية:
- [`skills/project-to-gist-converter/SKILL.md`](./skills/project-to-gist-converter/SKILL.md)
- [`.agents/skills/project-to-gist-converter/SKILL.md`](./.agents/skills/project-to-gist-converter/SKILL.md)
- [`.claude/commands/gistify.md`](./.claude/commands/gistify.md)

فقط اطلب من الوكيل:
```text
/gistify حول هذا المشروع إلى Gists منظمة ونظيفة من التوكنات مع قوائمها وشروحاتها العربية
```

### ب. عبر المحرك البرمجي المباشر (`Python CLI`)
```bash
# 1. فحص أي مجلد مشروع وتطهيره وتحويله إلى حزم Gists في مجلد dist_gists
python -m src.project_to_gist_converter --scan-dir "./my-project" --out-dir "./dist_gists"

# 2. فحص ملف معين للتأكد من خلوه التام من التوكنات والأسرار
python src/secret_sanitizer.py ./gists/01_profile_live_metrics_sync/github_profile_live_metrics_sync.py
```

### ج. نشر جميع الـ Gists الـ 10 وقائمتها الرئيسية إلى `gist.github.com`
```powershell
powershell -ExecutionPolicy Bypass -File ./scripts/Publish-AllGists.ps1
```

---

## 📐 5. هيكلة المستودع (Repository Structure)

```text
GITHUB-GIST-ARCHITECT/
├── README.md                                  # الواجهة الرئيسية والفهرس الشامل
├── docs/
│   └── PLAN_AND_ARCHITECTURE_AR.md            # الخطة التفصيلية ودليل تحويل الأنظمة إلى Gists
├── collections/                               # قوائم تجميع الـ Gists حسب كل مهمة كبرى
│   ├── 00_MASTER_GIST_CATALOG.md              # الفهرس العام لجميع القوائم
│   ├── LIST_01_PROFILE_TELEMETRY_AND_SVG.md   # قائمة أتمتة البروفايل والبطاقات
│   ├── LIST_02_PR_AND_ACHIEVEMENTS_ENGINE.md  # قائمة طلبات السحب الموثقة والأوسمة
│   └── LIST_03_COMMUNITY_SCANNER_AND_SECURITY.md # قائمة فحص المجتمع والأمان
├── gists/                                     # حزم الـ 10 Gists المعقمة والجاهزة
│   ├── 01_profile_live_metrics_sync/
│   ├── 02_custom_svg_cards_generator/
│   ├── ...
│   └── 10_actions_binary_republish_guard/
├── src/                                       # المحرك البرمجي للتطهير والتحويل والنشر
│   ├── secret_sanitizer.py
│   └── project_to_gist_converter.py
├── scripts/
│   └── Publish-AllGists.ps1                   # سكربت النشر الآلي إلى gist.github.com
├── skills/
│   └── project-to-gist-converter/SKILL.md     # مهارة الذكاء الاصطناعي القياسية
└── .claude/
    └── commands/gistify.md                    # أمر /gistify السريع
```
