# Используйте официальный образ Python как базовый
FROM python:3.9-slim

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app

# Установите необходимые зависимости
RUN pip install --no-cache-dir Flask

# Определите переменную окружения для Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Откройте порт 5000 для доступа к серверу
EXPOSE 1000

# Запустите приложение Flask
CMD ["flask", "run"]
