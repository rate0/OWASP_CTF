# Используйте официальный образ nginx
FROM nginx:latest

# Копируйте ваш HTML-файл в контейнер
COPY index.html /usr/share/nginx/html

# Откройте порт 80
EXPOSE 80

# Запустите nginx
CMD ["nginx", "-g", "daemon off;"]
