import psycopg2

conn = psycopg2.connect( #создает соединение с базой данных 
    host = "localhost", #создает хост 
    database = "postgres", #имя базы данных
    user = "postgres", #имя пользователя и пароль
    password = "2466190")

cursor = conn.cursor() #создает курсор, который используется для выполнения SQL-запросов к базе данных через соединение conn.

cursor.execute("""CREATE TABLE PHONETABLE (NAME TEXT NOT NULL, PHONE CHAR(12));""")  #создает sql запрос создает новую
# таблицу с двумя столбцами phone и name ограниченный 12 символами 

cursor.close() #закрывает курсор после выполнения всех операций 
conn.commit() #фиксирует создание новой таблицы, подверждает все изменения 
conn.close() #закрывает соединение с базой данных 