# 📄 Gist #05: Create GPG-Verified Commits & Merge Pull Requests via GitHub GraphQL API (createCommitOnBranch Python)

> **القائمة الأم (Collection):** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **اسم الملف الرئيسي:** `github_graphql_gpg_verified_pr_automator.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
إنشاء التزامات موقّعة رسمياً بتوقيع GitHub GPG (`Verified` / `signature.isValid = true`) مع دعم تذييل المؤلف المشارك (`Co-authored-by:`) وفتح ودمج طلبات السحب عبر GraphQL API.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. على عكس نقاط النهاية التقليدية في REST API التي تنتج التزامات غير موقّعة (`isValid = false`)، تستخدم هذه الأداة طفرة GraphQL `createCommitOnBranch`.
2. يقوم GitHub تلقائياً بتوقيع الالتزام بمفتاح GPG الرسمي الخاص بـ `noreply@github.com` ليظهر بشارة **Verified** الخضراء.
3. يدعم إضافة سطر `Co-authored-by:` في جسم الالتزام ثم يفتح ويدمج طلب السحب عبر `createPullRequest` و `mergePullRequest`.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_graphql_gpg_verified_pr_automator.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
