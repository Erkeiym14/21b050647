import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres", 
    password = "2466190"
)

cursor = conn.cursor()

ex = input()
ex2 = input()

cursor.execute("UPDATE PHONETABLE set PHONE = 87009969920 where NAME = 'Mukha'")

conn.commit()
conn.close()
