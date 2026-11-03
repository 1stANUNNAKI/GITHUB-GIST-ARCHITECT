# 📄 Gist #06: GitHub REST & GraphQL API Adaptive Rate-Limit Controller with Exponential Backoff (Python)

> **القائمة الأم (Collection):** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **اسم الملف الرئيسي:** `github_adaptive_api_rate_limiter.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
حماية سكربتات الأتمتة من تجاوز حدود طلبات GitHub API (`Primary & Secondary Rate Limits`) عبر قراءة ترويسات الاستجابة وإدارة التوقف الذكي التلقائي.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يقرأ ترويسة `X-RateLimit-Remaining` و `X-RateLimit-Reset` بعد كل طلب HTTP.
2. إذا انخفض الرصيد المتبقي عن الحد الآمن (`min_remaining = 50`)، يحسب الثواني المتبقية حتى إعادة ضبط النافذة الزمنية وينتظر تلقائياً.
3. يطبق خوارزمية التأخير الأسي (`Exponential Backoff`) عند مصادفة `HTTP 403` أو `HTTP 429`.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_adaptive_api_rate_limiter.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
