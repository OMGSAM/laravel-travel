# Base image PHP avec extensions Laravel
FROM php:8.2-fpm

# Installer dépendances système
RUN apt-get update && apt-get install -y \
    git unzip libzip-dev libonig-dev libxml2-dev curl \
    && docker-php-ext-install pdo pdo_mysql mbstring zip xml bcmath

# Installer Composer
COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

# Copier le projet
WORKDIR /var/www/html
COPY . .

# Installer les dépendances PHP
RUN composer install --no-dev --optimize-autoloader

# Exposer le port
EXPOSE 8000

# Lancer Laravel
CMD php artisan serve --host=0.0.0.0 --port=8000
