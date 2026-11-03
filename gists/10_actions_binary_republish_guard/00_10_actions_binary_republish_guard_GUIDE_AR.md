# 📄 Gist #10: Fix GitHub Actions Release & npm/OVSX/VSCode Marketplace Duplicate Version Republish Failures (YAML Pattern)

> **القائمة الأم (Collection):** `List 03: Open-Source Community Repo Scanner & Secret Guard Suite`  
> **اسم الملف الرئيسي:** `github_actions_binary_republish_guard.yml`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
قالب GitHub Actions هندسي جاهز لحل مشكلة فشل عمليات الـ Deploy والـ Release عند إعادة تشغيل المهام (Re-run Failed Jobs) بسبب وجود الإصدار مسبقاً على npm أو VS Code Marketplace أو OpenVSX أو فشل تحميل FFmpeg.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يتحقق قبل النشر على `npm` عبر `npm view <pkg>@<version>` ويتخطى النشر بأمان إذا كان الإصدار منشوراً بالفعل.
2. يتحقق من `vsce show` قبل النشر على سوق إضافات VS Code ويتفادى خطأ `already exists` في `ovsx publish`.
3. يتحقق من وجود وسم الإصدار (`gh release view`) قبل استدعاء `gh release create` لمنع توقف خط أنابيب الإطلاق.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_actions_binary_republish_guard.yml` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
