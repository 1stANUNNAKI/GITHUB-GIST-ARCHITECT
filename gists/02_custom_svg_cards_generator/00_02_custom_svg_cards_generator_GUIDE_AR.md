# 📄 Gist #02: Generate Custom GitHub Streak & Achievements Trophy SVG Cards Locally (Midnight Galaxy Theme - Python)

> **القائمة الأم (Collection):** `List 01: GitHub Profile Live Telemetry & Dynamic SVG Suite`  
> **اسم الملف الرئيسي:** `github_custom_svg_cards_generator.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
توليد بطاقات SVG الإحصائية (`streak-stats.svg` و `trophies.svg`) محلياً داخل المستودع بألوان ثيم `Midnight Galaxy` الموحدة دون الاعتماد على خوادم الطرف الثالث البطيئة أو المتوقفة.

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. يستقبل أرقام الحساب الحية (إجمالي المساهمات، السلسلة الحالية، أطول سلسلة، وتواريخ البدء).
2. يبني شجرة SVG قياسية بخلفية داكنة (`#060B1E`)، حدود بنفسجية فلكية (`#5B5C8A`)، عناوين (`#8087E2`)، وأيقونات ذهبية (`#FACC15`).
3. يحفظ الملف بصيغة `streak-stats.svg` جاهزاً للتضمين الفوري في `README.md`.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_custom_svg_cards_generator.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
