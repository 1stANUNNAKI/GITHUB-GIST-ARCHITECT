---
name: project-to-gist-converter
description: Analyzes any software project or codebase, sanitizes all tokens/secrets/personal identifiers, decomposes modules into standalone SEO-optimized GitHub Gists with bilingual Arabic/English guides, and groups them into Master Gist Lists (Collections).
---

# 🧩 مهارة تحويل المشاريع إلى Gists نظيفة ومنظمة (`project-to-gist-converter`)

## 🎯 الهدف والوظيفة
تُمكّن هذه المهارة وكيل الذكاء الاصطناعي من تحليل أي مشروع برمجي وتفكيكه إلى **مقتطفات وأدوات مستقلة (Atomic GitHub Gists)** مع:
1. **تطهير أمني صارم 100% (Zero-Secret & Zero-PII Sanitization):** إزالة كافة التوكنات (`ghp_`, `github_pat_`, `sk-`, `AKIA`) والإيميلات الشخصية وأسماء المستخدمين الخاصة، واستبدالها بعناصر نائبة قياسية (`[YOUR_GITHUB_TOKEN]`, `[YOUR_GITHUB_USERNAME]`, `[YOUR_EMAIL_ADDRESS]`).
2. **عنونة بحثية ذكية (GitHub Search SEO Optimization):** صياغة عنوان (Gist Description) واضح وبسيط وغني بالكلمات المفتاحية التقنية لكل Gist بحيث يظهر فوراً لأي مطور يبحث داخل GitHub عن كود يؤدي تلك الوظيفة.
3. **توثيق مستقل لكل Gist:** إرفاق ملف شرح مفصل (`GUIDE_AR.md`) مع كل ملف كود داخل الـ Gist يشرح الوظيفة، المتطلبات، وطريقة التشغيل.
4. **تجميع الـ Gists في قوائم مهام كبرى (Master Gist Lists / Collections):** إنشاء فهرس Gist رئيسي لكل مهمة كبيرة يربط مجموعة الـ Gists الفرعية في جدول منظم واحد.

---

## ⚙️ خطوات التنفيذ الإلزامية للوكيل (Execution Workflow)

### الخطوة 1: الفحص والتحليل المعماري (`Analyze & Decompose`)
- افحص شجرة ملفات المشروع المستهدف وحدد الوحدات البرمجية القابلة لإعادة الاستخدام (السكربتات، أدوات الـ API، ملفات GitHub Actions، أدوات الأمان).
- صنّف الوحدات المترابطة ضمن **قوائم مهام كبرى (Task Collections / Lists)**.

### الخطوة 2: التطهير الأمني الصارم (`Sanitize & Verify`)
- مرّر كل ملف عبر `src/secret_sanitizer.py` (`sanitize_content` ثم `assert_clean_for_gist`).
- يُمنع منعاً باتاً بقاء أي توكن حقيقي أو بريد إلكتروني شخصي أو معرف حساب خاص داخل الكود أو الشرح.

### الخطوة 3: صياغة العنوان البحثي والملف الإرشادي (`SEO Title & Guide`)
- اكتب لكل Gist عنواناً بصيغة:
  `<الفعل والوظيفة المباشرة> (<التقنية/اللغة وأهم ميزة>)`
  *مثال:* `GitHub Profile README Live Stats, Streak & Contribution Counter Auto-Sync (Python GraphQL & REST)`
- أنشئ ملف `GUIDE_AR.md` يشرح:
  1. وظيفة الكود والهدف منه.
  2. آلية العمل خطوة بخطوة.
  3. طريقة التشغيل والمتغيرات البيئية المطلوبة.

### الخطوة 4: التجميع والنشر (`Bundle & Publish`)
- احفظ كل Gist في مجلد `gists/<id>_<slug>/`، وحدّث قوائم المهام في `collections/`.
- عند توفر `GITHUB_TOKEN` بصلاحية `gist`، شغّل `python -m src.project_to_gist_converter --publish-catalog` أو `scripts/Publish-AllGists.ps1` لنشر الـ Gists وإنشاء قوائم الفهرس المجمعة على `gist.github.com`.
