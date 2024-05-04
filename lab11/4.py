import psycopg2
from config import config

def get_users_with_pagination():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        limit_rows = int(input("Введите количество записей для вывода: "))
        offset_rows = int(input("Введите смещение: "))

        cur.callproc('get_users_with_pagination', (limit_rows, offset_rows))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Вызов функции для запроса данных с пагинацией
get_users_with_pagination()
