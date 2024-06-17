# Dockerfile
FROM python:3.9-slim

# Установка зависимостей
RUN pip install flask

# Копируем приложение в контейнер
COPY app.py /app.py
COPY templates /templates
COPY static /static

# Указываем рабочую директорию
WORKDIR /

# Установим переменные окружения
ENV FLAG="IR{c0ngr4tul4ti0ns_y0u_br0ke_1t}"

# Запуск приложения
CMD ["python", "app.py"]
