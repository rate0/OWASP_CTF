FROM php:5.6-apache

# Используем архивные репозитории для Debian Stretch
RUN set -ex; \
    sed -i 's|http://deb.debian.org/debian|http://archive.debian.org/debian|g' /etc/apt/sources.list; \
    sed -i 's|http://security.debian.org/debian-security|http://archive.debian.org/debian-security|g' /etc/apt/sources.list; \
    echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf.d/99no-check-valid-until; \
    sed -i '/stretch-updates/d' /etc/apt/sources.list; \
    apt-get update; \
    apt-get install -y \
        libjpeg-dev \
        libpng-dev \
        vim \
    ; \
    rm -rf /var/lib/apt/lists/*; \
    docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \
    docker-php-ext-install gd mysqli opcache

# Настройки PHP.ini
RUN { \
        echo 'opcache.memory_consumption=128'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=4000'; \
        echo 'opcache.revalidate_freq=2'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN a2enmod rewrite expires

VOLUME /var/www/html

ENV WORDPRESS_VERSION 4.8.2
ENV WORDPRESS_SHA1 a99115b3b6d6d7a1eb6c5617d4e8e704ed50f450

RUN set -ex; \
    curl -o wordpress.tar.gz -fSL "https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \
    echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \
    tar -xzf wordpress.tar.gz -C /usr/src/; \
    rm wordpress.tar.gz

COPY docroot/wp-config.php /usr/src/wordpress/
COPY docroot/akismet /usr/src/wordpress/wp-content/plugins/akismet/
COPY docroot/myplugin.php /usr/src/wordpress/wp-content/plugins/
RUN rm -f /usr/src/wordpress/wp-content/plugins/hello.php

RUN rm -f /usr/src/wordpress/wp-content/plugins/index.php /usr/src/wordpress/wp-content/plugins/akismet/index.php

COPY docroot/upload.html /usr/src/wordpress/wp-content/plugins
COPY docroot/upload.php /usr/src/wordpress/wp-content/plugins

RUN chown -R www-data:www-data /usr/src/wordpress
RUN chown root:root /usr/src/wordpress/wp-content/plugins/*
RUN chmod -R ugo-w /usr/src/wordpress/

RUN mkdir /usr/src/wordpress/uploads
RUN chmod +w /usr/src/wordpress/uploads
RUN chown www-data:www-data /usr/src/wordpress/uploads

COPY docroot/000-default.conf /etc/apache2/sites-available/000-default.conf

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["apache2-foreground"]
