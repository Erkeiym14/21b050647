import psycopg2
from config import config

def insert_game_state(game_state):
    """ вставить состояние игры в таблицу users """
    sql = """INSERT INTO users(game_pause, game_end, game_win, level) VALUES(%s, %s, %s, %s) RETURNING user_id"""
    conn = None
    user_id = None
    try:
        # читаем конфигурацию базы данных
        params = config()
        # подключаемся к базе данных PostgreSQL
        conn = psycopg2.connect(**params)
        # создаем новый курсор
        cur = conn.cursor()
        # выполняем запрос INSERT
        cur.execute(sql, game_state)
        # получаем сгенерированный идентификатор обратно
        user_id = cur.fetchone()[0]
        # фиксируем изменения в базе данных
        conn.commit()
        # закрываем соединение с базой данных
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return user_id
