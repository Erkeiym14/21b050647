import psycopg2

conn = psycopg2.connect(
    host = "localhost", 
    database = "postgres", 
    user = "postgres",
    password = "2466190"
)

cursor = conn.cursor()

x = input()
y = input()

cursor.execute(f"INSERT INTO PHONETABLE (NAME,PHONE) VALUES ('{x}', '{y}')")

conn.commit()
conn.close()