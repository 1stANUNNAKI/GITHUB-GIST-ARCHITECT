# 📄 Gist #03: GitHub Actions Workflow: Auto-Update Profile README Stats & SVG Cards Every Hour (Cron Schedule)

> **القائمة الأم (Collection):** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **اسم الملف الرئيسي:** `github_profile_hourly_sync_workflow.yml`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
ملف أتمتة GitHub Actions جاهز يعمل تلقائياً على مدار الساعة (`0 * * * *`) لتشغيل سكربت المزامنة وتوليد البطاقات ورفع التحديثات إلى المستودع دون أي تدخل يدوي.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يعمل وفق جدول زمني كل ساعة (`cron: '0 * * * *'`) أو يدوياً عبر `workflow_dispatch`.
2. يسحب أحدث نسخة من المستودع ويشغّل سكربت التحديث.
3. يفحص وجود تغييرات في `README.md` أو ملفات `.svg` ويرفعها تلقائياً بالتزام نظيف.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_profile_hourly_sync_workflow.yml` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
