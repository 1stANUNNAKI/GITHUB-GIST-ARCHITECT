# 📄 Gist #07: Automate GitHub Discussions Q&A Creation and Mark Accepted Answers via GraphQL API (Python)

> **القائمة الأم (Collection):** `List 02: GitHub Pull Request & Achievements Automation Suite`  
> **اسم الملف الرئيسي:** `github_discussions_qna_automator.py`  
> **حالة التطهير الأمني:** ✅ خالٍ تماماً من التوكنات والرموز الشخصية (`100% Sanitized`)

---

## 1. 🎯 الوظيفة والهدف (Purpose)
أتمتة بناء قاعدة المعرفة والأسئلة الشائعة (Q&A Discussions) في مستودعات GitHub واعتماد الإجابات الصحيحة عبر GraphQL API (المسار التقني الخاص بوسام Galaxy Brain).

---

## 2. ⚙️ كيف يعمل هذا الكود؟ (How It Works)
1. ينفذ طفرة `createDiscussion` داخل فئة الأسئلة والأجوبة (`Q&A Category ID`).
2. يضيف الرد الهندسي المفصل عبر طفرة `addDiscussionComment`.
3. يعتمد الإجابة رسمياً عبر طفرة `markDiscussionCommentAsAnswer`.

---

## 3. 🚀 طريقة الاستخدام السريع (Quick Start)
1. انسخ ملف `github_discussions_qna_automator.py` أو استنسخ هذا الـ Gist مباشرة:
   ```bash
   git clone https://gist.github.com/[GIST_ID].git
   ```
2. عيّن المتغيرات البيئية الخاصة بك في ملف `.env` محلي (لا تضع التوكن داخل الكود أبداً):
   ```bash
   export GITHUB_USERNAME="[YOUR_GITHUB_USERNAME]"
   export GITHUB_TOKEN="[YOUR_GITHUB_TOKEN]"
   ```
