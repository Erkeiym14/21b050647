import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres", 
    user = "postgres", 
    password = "2466190"
)

cursor = conn.cursor()
cursor.execute("DELETE from PHONETABLE")

conn.commit()
conn.close()
