# المحاسب الشامل (Universal Accountant)

- Django 5 + DRF + JWT
- PostgreSQL + Docker Compose
- Bootstrap 5 + Chart.js
- Celery + Redis (تنبيهات انخفاض المخزون)
- تقارير (قابل للتوسعة PDF/Excel)

## التشغيل السريع (محلي)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r src/requirements.txt
python src/manage.py migrate
python src/manage.py createsuperuser
python src/manage.py runserver 0.0.0.0:8000
```

## التشغيل عبر Docker
```bash
cd compose && docker compose up --build
```

## الدخول
- المصادقة عبر JWT: `POST /api/auth/login/` (username/password) → ترجع access/refresh.
- استخدم التوكن في `Authorization: Bearer <token>` لاستدعاء بقية الـ APIs.


## ميزات إضافية (إبهار)
- **FIFO COGS**: استهلاك طبقات التكلفة تلقائيًا عند البيع وتسجيل COGS على كل بند.
- **طباعة PDF** لفاتورة المبيعات: `/sales/invoices/<id>/print/`.
- **واجهات عربية بسيطة**: `/ui/products/` و`/ui/customers/` (قابلة للتوسعة).
- **Celery Beat**: خدمة مجدولة للتنبيهات.

> ملاحظة: بعد إضافة حقول/جداول جديدة (CostLayer, cogs) تأكد من تشغيل الهجرات:
```bash
python src/manage.py makemigrations
python src/manage.py migrate
```
# Universal-Accountant
