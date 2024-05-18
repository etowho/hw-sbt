import requests
import time

def log_statistics():
    try:
        # Отправка GET запроса к /statistics
        response = requests.get('http://web-service/statistics')
        
        if response.status_code == 200:
            # Извлечение количества обращений к /time
            stats_count = response.json().get('time_requests_count', 0)
            
            # Запись статистики в файл
            with open('statistics.txt', 'a') as file:
                file.write(f'{stats_count}\n')
        else:
            print(f'Ошибка: статус код {response.status_code}')
    except Exception as e:
        print(f'Ошибка: {e}')

# Основной цикл с интервалом в 5 секунд
def main():
    while True:
        log_statistics()
        time.sleep(5)

if __name__ == '__main__':
    main()
