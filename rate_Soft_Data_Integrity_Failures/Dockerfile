# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем переменную среды для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию контейнера
WORKDIR /app

# Копируем зависимости Python
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения в рабочую директорию
COPY ./app /app

# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]
