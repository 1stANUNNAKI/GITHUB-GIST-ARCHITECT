# 📄 Gist #04: GitHub Actions Workflow: Generate Dark & Light Contribution Grid Snake Animation SVG (Platane/snk)

> **القائمة الأم (Collection):** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **اسم الملف الرئيسي:** `github_contribution_snake_grid_workflow.yml`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
توليد رسم الثعبان المتحرك على شبكة المساهمات الخضراء (Contribution Grid Snake) للوضعين الليلي والنهاري تلقائياً كل 6 ساعات ونشره في فرع `output`.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يستخدم الإجراء القياسي `Platane/snk/svg-only@v3` لقراءة شبكة مساهمات المالك (`github.repository_owner`).
2. يولّد ملفي `github-contribution-grid-snake.svg` و `github-contribution-grid-snake-dark.svg`.
3. ينشرهما على فرع `output` لعرضهما عبر وسم `<picture>` المتجاوب مع ثيم المتصفح.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_contribution_snake_grid_workflow.yml` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
