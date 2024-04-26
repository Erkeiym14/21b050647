import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres", 
    user = "postgres", 
    password = "2466190"
)

cursor = conn.cursor()

cursor.execute("SELECT NAME, PHONE from PHONETABLE")

all_rows = cursor.fetchall()
for row in all_rows:
    print("NAME =", row[0])
    print("PHONE =", row[1])
  
cursor.close()
conn.close()
