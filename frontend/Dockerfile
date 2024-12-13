# Используем официальный образ nginx
FROM nginx:alpine

# Устанавливаем рабочую директорию в контейнере
WORKDIR /usr/share/nginx/html

# Копируем файлы frontend в контейнер
COPY . .

# Nginx по умолчанию использует порт 80
EXPOSE 80