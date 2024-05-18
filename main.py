from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

# Счетчик для подсчета количества обращений к /time endpoint
time_requests_count = 0

# Endpoint для получения текущего времени
@app.route('/time', methods=['GET'])
def get_current_time():
    global time_requests_count

    # Увеличиваем счетчик обращений к /time endpoint
    time_requests_count += 1

    # Отправка запроса к внешнему API для получения текущего времени
    response = requests.get('http://worldtimeapi.org/api/timezone/Europe/Moscow')
    if response.status_code == 200:
        current_time = response.json().get('datetime', 'Нет данных о времени')
    else:
        current_time = f"Ошибка при запросе: {response.status_code}"

    # Возвращаем текущее время
    return jsonify({'current_time': current_time})

# Endpoint для получения статистики обращений к /time endpoint
@app.route('/statistics', methods=['GET'])
def get_time_requests_statistics():
    global time_requests_count

    # Возвращаем количество обращений к /time endpoint
    return jsonify({'time_requests_count': time_requests_count})

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
