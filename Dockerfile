# المرحلة الأولى: بناء وتثبيت الحزم
FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .
# تثبيت الحزم بشكل عام (System-wide) في بيئة البناء لتجنب مشاكل الصلاحيات لاحقاً
RUN pip install --no-cache-dir -r requirements.txt

# المرحلة الثانية: التشغيل النهائية (Multi-stage)
FROM python:3.12-slim-bookworm

WORKDIR /app

# نسخ الحزم المثبتة من مرحلة البناء
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY . .

# إنشاء مستخدم غير رصين (Non-root user) وتشغيل التطبيق بصلاحياته
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# فحص الصحة (Healthcheck)
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

EXPOSE 8000

# أمر تشغيل السيرفر مباشرة
CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
