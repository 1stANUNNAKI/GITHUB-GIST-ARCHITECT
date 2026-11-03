# 📄 Gist #09: Pre-Commit Secret Scanner & Token Sanitizer for GitHub Repositories and Gists (Python Zero-Dependency)

> **القائمة الأم (Collection):** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **اسم الملف الرئيسي:** `github_pre_commit_secret_sanitizer.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
فحص وتطهير الأكواد والملفات قبل رفعها إلى GitHub أو نشرها كـ Gist، واكتشاف أي مفاتيح سرية (`ghp_`, `github_pat_`, `sk-`, `AKIA`) أو إيميلات شخصية واستبدالها تلقائياً بعناصر نائبة آمنة.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يطبق مصفوفة تعبيرات نمطية (Regex) تغطي كافة صيغ رموز GitHub و AWS و OpenAI و Slack والمفاتيح الخاصة (Private Keys).
2. يوفر دالة `sanitize_text()` لاستبدال أي رمز سري فوراً بـ `[YOUR_GITHUB_TOKEN]` أو `[YOUR_EMAIL_ADDRESS]`.
3. يوفر بوابة تحقق صارمة `assert_zero_secrets()` تمنع عملية الرفع إذا تبقى أي تسريب محتمل.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_pre_commit_secret_sanitizer.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
