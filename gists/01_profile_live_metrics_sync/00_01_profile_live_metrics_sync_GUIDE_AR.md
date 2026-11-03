# 📄 Gist #01: GitHub Profile README Live Stats, Streak & Contribution Counter Auto-Sync (Python GraphQL & REST)

> **القائمة الأم (Collection):** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **اسم الملف الرئيسي:** `github_profile_live_metrics_sync.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
مزامنة إحصائيات بروفايل GitHub الحية (إجمالي المساهمات الفعلية عبر GraphQL، أطول سلسلة أيام متتالية Streak، النجوم، المستودعات العامة، والمتابعين) وتحديث ملف README.md تلقائياً بدون أي مكتبات خارجية.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يستعلم السكربت عن نقطة نهاية REST API (`/users/[YOUR_GITHUB_USERNAME]`) لجلب عدد المستودعات العامة والمتابعين.
2. يفحص جميع المستودعات العامة لحساب مجموع النجوم (Stars) الفعلي.
3. ينفذ استعلام GraphQL (`contributionsCollection`) عبر جميع سنوات عمر الحساب لجمع إجمالي المساهمات الحقيقي وحساب السلسلة اليومية الحالية وأطول سلسلة (Current & Longest Streak).
4. يحدّث الأرقام ومعلمات كسر التخزين المؤقت (`?v=timestamp`) داخل `README.md` تلقائياً.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_profile_live_metrics_sync.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
