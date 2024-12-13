# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы backend в контейнер
COPY . /app

# Устанавливаем зависимости
RUN pip install --no-cache-dir flask flask-cors

# Указываем порт, который будет открыт в контейнере
EXPOSE 5000

# Запускаем Flask-приложение
CMD ["python", "app.py"]
