# Используем официальный образ PHP с Apache
FROM php:7.4-apache

# Копируем исходный код в контейнер
COPY . /var/www/html/

# Копируем файл флага в корень файловой системы контейнера
COPY flag /flag

# Включаем поддержку .htaccess и переписываем модуль
RUN a2enmod rewrite

# Копируем файл конфигурации для Apache
COPY apache-config.conf /etc/apache2/sites-available/000-default.conf

# Изменяем права доступа к файлу с флагом
RUN chmod 644 /flag

# Указываем Apache запускать фронт контейнера на порту 4000
EXPOSE 4000
