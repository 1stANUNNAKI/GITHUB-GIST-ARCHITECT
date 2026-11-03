# 📄 Gist #08: GitHub Open-Source Repository Scanner: Find & Fix Typos, Deprecated Actions & Docs via Automated PRs (Python)

> **القائمة الأم (Collection):** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **اسم الملف الرئيسي:** `github_open_source_repo_scanner.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
فحص المستودعات العامة على GitHub حسب نطاق النجوم وعدد متابعي المالك، واكتشاف فرص التحسين الحقيقية (إصلاح الأخطاء الإملائية، ترقية GitHub Actions القديمة، وتحسين تنسيق Markdown) وتوليد تقارير مشاركة مجتمعية بالعربية.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يبحث عبر `/search/repositories` عن المشاريع المطابقة لمعايير النجوم (مثلاً `0..200` نجمة).
2. يتحقق من عدد متابعي صاحب المستودع عبر `/users/{owner}`.
3. يفحص ملف `README.md` وملفات `.github/workflows/*.yml` لاكتشاف الأخطاء الشائعة أو الإجراءات المتقادمة.
4. ينشئ تقريراً مفصلاً باللغة العربية حول كل مستودع والاقتراح المقدم له.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_open_source_repo_scanner.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
