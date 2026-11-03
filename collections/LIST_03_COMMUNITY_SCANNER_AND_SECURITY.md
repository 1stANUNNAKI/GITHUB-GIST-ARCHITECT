# 📚 القائمة الكبرى الثالثة: منظومة فحص المستودعات المجتمعية والأمان الوقائي (Community Scanner & Security Suite)

> تجمع هذه القائمة أداة فحص المستودعات المفتوحة المصدر واقتراح التحسينات، وأداة تطهير الأسرار والتوكنات قبل النشر، وقالب إصلاح مشاكل الـ Deploy والـ Release في GitHub Actions.

## 🗂️ قائمة الـ Gists المندرجة تحت هذه المهمة الكبرى

| # | عنوان الـ Gist (SEO Title) والوظيفة | ملف الكود المنقى | دليل الاستخدام المستقل |
| :-: | :--- | :---: | :---: |
| **#08** | **GitHub Open-Source Repository Scanner: Find & Fix Typos, Deprecated Actions & Docs via Automated PRs (Python)**<br/>_فحص المستودعات العامة على GitHub حسب نطاق النجوم وعدد متابعي المالك، واكتشاف فرص التحسين الحقيقية (إصلاح الأخطاء الإملائية، ترقية GitHub Actions القديمة، وتحسين تنسيق Markdown) وتوليد تقارير مشاركة مجتمعية بالعربية._ | [`github_open_source_repo_scanner.py`](../gists/08_open_source_repo_scanner/github_open_source_repo_scanner.py) | [`الشرح بالعربية`](../gists/08_open_source_repo_scanner/00_08_open_source_repo_scanner_GUIDE_AR.md) |
| **#09** | **Pre-Commit Secret Scanner & Token Sanitizer for GitHub Repositories and Gists (Python Zero-Dependency)**<br/>_فحص وتطهير الأكواد والملفات قبل رفعها إلى GitHub أو نشرها كـ Gist، واكتشاف أي مفاتيح سرية (`ghp_`, `github_pat_`, `sk-`, `AKIA`) أو إيميلات شخصية واستبدالها تلقائياً بعناصر نائبة آمنة._ | [`github_pre_commit_secret_sanitizer.py`](../gists/09_pre_commit_secret_sanitizer/github_pre_commit_secret_sanitizer.py) | [`الشرح بالعربية`](../gists/09_pre_commit_secret_sanitizer/00_09_pre_commit_secret_sanitizer_GUIDE_AR.md) |
| **#10** | **Fix GitHub Actions Release & npm/OVSX/VSCode Marketplace Duplicate Version Republish Failures (YAML Pattern)**<br/>_قالب GitHub Actions هندسي جاهز لحل مشكلة فشل عمليات الـ Deploy والـ Release عند إعادة تشغيل المهام (Re-run Failed Jobs) بسبب وجود الإصدار مسبقاً على npm أو VS Code Marketplace أو OpenVSX أو فشل تحميل FFmpeg._ | [`github_actions_binary_republish_guard.yml`](../gists/10_actions_binary_republish_guard/github_actions_binary_republish_guard.yml) | [`الشرح بالعربية`](../gists/10_actions_binary_republish_guard/00_10_actions_binary_republish_guard_GUIDE_AR.md) |
