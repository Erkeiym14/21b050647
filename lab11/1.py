import psycopg2
from config import config

def get_user(pattern):
    """Функция для получения данных о пользователе по заданному шаблону (например, номеру телефона или имени)."""
    conn = None
    try:
        # Читаем конфигурацию базы данных
        params = config()
        # Подключаемся к базе данных PostgreSQL
        conn = psycopg2.connect(**params)
        # Создаем объект курсора для выполнения запросов
        cur = conn.cursor()
        # Вызываем хранимую процедуру в зависимости от шаблона
        if pattern == "phone":
            cur.callproc('phone', "")
        elif pattern == "name":
            cur.callproc("username", "")
        # Обрабатываем результат запроса
        rows = cur.fetchall()
        for row in rows:
            print(row)
        # Закрываем соединение с сервером базы данных PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Получаем шаблон от пользователя
    pattern = input()
    # Вызываем функцию get_user с заданным шаблоном
    get_user(pattern)
