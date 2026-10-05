# 1. Базовий образ з Python
FROM python:3.12-slim

# 2. Python не пише .pyc файли і одразу виводить логи
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Робоча папка всередині контейнера
WORKDIR /app

# 4. Спочатку тільки залежності (так Docker кешує цей шар)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Потім увесь код застосунку
COPY . .

# 6. Запуск не від root - безпечніше
RUN useradd --create-home appuser
USER appuser

# 7. Порт і команда запуску (gunicorn - продакшн-сервер для Django)
EXPOSE 8000
CMD ["gunicorn", "mysite.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]