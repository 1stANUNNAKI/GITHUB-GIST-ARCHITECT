# 📐 الخطة الشاملة والدليل المعماري لتحويل الأنظمة والمشاريع إلى GitHub Gists نظيفة ومنظمة

## 1. 💡 الفلسفة الهندسية: لماذا نحول أنظمتنا إلى Gists؟
عندما نبني مشروعاً كبيراً، غالباً ما تبقى الأدوات الفرعية القوية بداخله مدفونة وسط عشرات الملفات. تحويل كل أداة أو وظيفة مستقلة إلى **GitHub Gist** مستقل يحقق ثلاث فوائد استراتيجية:
1. **سهولة الاكتشاف عبر محرك بحث GitHub (Searchability / SEO):** الباحث في GitHub أو Google يكتب عادةً جملة وظيفية مباشرة (مثل: `GitHub Profile Live Stats Python` أو `Create GPG Verified Commit GraphQL Python`)؛ وجود Gist يحمل هذا العنوان الصريح يجعله يظهر في صدارة النتائج.
2. **إعادة الاستخدام الفوري (Zero-Friction Reuse):** يمكن لأي مطور نسخ ملف واحد أو استنساخ الـ Gist بأمر واحد دون الحاجة لتحميل مشروع ضخم.
3. **بناء السمعة التقنية والنجوم (Stars & Forks & Gist Trophy):** كل Gist عام يستقبل النجوم (Stars) والتفرعات (Forks) والتعليقات بشكل مستقل، ويرفع تصنيف كأس الـ Gists في بطاقة إنجازات الحساب.

---

## 2. 🗂️ كيف نجمع مجموعة Gists في "قائمة" واحدة لكل مهمة كبيرة؟
بما أن منصة `gist.github.com` تعرض الـ Gists بترتيب زمني مسطح افتراضياً، فقد صممنا في هذا النظام **آلية القوائم المجمعة الثلاثية (Triple-Layer Gist Collections)** لتنظيم كل مهمة كبيرة تتكون من عدة Gists:

1. **الطبقة الأولى — Gist الفهرس الرئيسي لكل مهمة (`00_COLLECTION_INDEX.md`):**
   - لكل مهمة كبيرة (مثل: *أتمتة البروفايل* أو *فحص المستودعات*)، ينشئ محركنا Gist خاصاً بصيغة Markdown يعمل كـ **قائمة تشغيل (Playlist / Directory Gist)** يحتوي على جدول بروابط جميع الـ Gists الفرعية التابعة لهذه المهمة مع شرح مختصر لكل منها.
2. **الطبقة الثانية — الـ Gist ثنائي الملفات (Code + Guide Bundle):**
   - كل Gist فرعي يحتوي داخله على ملفين:
     - ملف الشرح العربي والإنجليزي (`00_<name>_GUIDE_AR.md`) في الأعلى لتوضيح الوظيفة وطريقة التشغيل.
     - ملف الكود البرمجي المنقى (`<script_name>.py` أو `.yml`) تحته مباشرة.
3. **الطبقة الثالثة — التثبيت في واجهة البروفايل (Pinned Gists):**
   - يمكنك من إعدادات بروفايلك على GitHub تثبيت (Pin) قوائم الـ Gists الرئيسية لتظهر في الصفحة الأولى لحسابك.

---

## 3. 🛡️ بروتوكول التطهير الأمني الصارم (Zero-Token & Zero-PII Sanitization)
قبل تحويل أي ملف من أي مشروع إلى Gist، يمر الكود إلزامياً عبر محرك `src/secret_sanitizer.py` الذي يقوم بـ:
- مسح واستبدال جميع أنواع مفاتيح GitHub (`ghp_...`, `github_pat_...`, `gho_...`, `ghs_...`) بالعنصر النائب الآمن `[YOUR_GITHUB_TOKEN]`.
- مسح واستبدال مفاتيح OpenAI و AWS و Slack والمفاتيح الخاصة (`PRIVATE KEY`).
- مسح واستبدال عناوين البريد الإلكتروني الشخصية (`@gmail.com`, `@yahoo.com`, إلخ) ومعرفات `users.noreply.github.com` الخاصة بالمستخدمين بـ `[YOUR_EMAIL_ADDRESS]` و `[YOUR_ID]+[YOUR_GITHUB_USERNAME]@users.noreply.github.com`.
- تطبيق بوابة المنع `assert_clean_for_gist()` التي توقف عملية النشر فوراً إذا تبقى أي نمط سري غير معقم.

---

## 4. 🤖 استخدام مهارة وأمر الذكاء الاصطناعي (`/gistify`)
يحتوي هذا المستودع على إعداد كامل لمهارة الذكاء الاصطناعي في:
- `skills/project-to-gist-converter/SKILL.md`
- `.agents/skills/project-to-gist-converter/SKILL.md`
- `.claude/commands/gistify.md`

### كيف تأمر الذكاء الاصطناعي بتحويل أي مشروع جديد إلى Gists؟
يكفي أن تكتب للوكيل:
> **"طبق مهارة `project-to-gist-converter` (أو الأمر `/gistify`) على هذا المشروع وحوله إلى Gists منظمة ونظيفة من التوكنات مع قوائمها وشروحاتها العربية."**

أو تشغيل المحرك برمجياً عبر سطر الأوامر:
```powershell
# فحص وتطهير أي مشروع وتحويله إلى حزم Gists جاهزة
python -m src.project_to_gist_converter --scan-dir "path/to/any/project" --out-dir "dist_gists"

# نشر جميع الـ Gists الـ 10 + قوائمها المجمعة إلى حسابك في gist.github.com
powershell -ExecutionPolicy Bypass -File scripts/Publish-AllGists.ps1
```
