from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Главная страница
@app.route('/')
def index():
    ##return app.send_static_file('index.html')
    return "Backend для сохранения данных и чтения из файла"

# Маршрут для приёма данных с фронтенда
@app.route('/submit', methods=['POST'])
def submit_data():
    # Получаем данные из запроса
    data = request.form.get('data')

    # Сохраняем данные в файл
    with open('data.txt', 'a') as f:
        f.write(f'{data}\n')

    return 'Данные успешно сохранены!', 200

# Маршрут для получения данных из файла
@app.route('/fetch', methods=['GET'])
def fetch_data():
    try:
        # Читаем данные из файла data.txt
        with open('data.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return "Файл не найден", 404

    # Возвращаем содержимое файла
    return content.replace('\n', '<br>'), 200

if __name__ == '__main__':
    # Запуск сервера
    app.run(host='127.0.0.1', port=5000, debug=True)
