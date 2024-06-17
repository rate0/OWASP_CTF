# Базовый образ Python 3.8 slim
FROM python:3.8-slim

# Установка рабочей директории в /app
WORKDIR /app

# Копирование зависимостей и исходного кода приложения
COPY ./app /app/app
COPY ./static /app/static
COPY ./uploads /app/uploads

# Установка Flask
RUN pip install flask

# Команда для запуска приложения
CMD ["python", "/app/app/app.py"]
