import psycopg2
from config import config

def delete_user_by_name_or_phone(user_name=None, user_phone=None):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('CALL delete_user_by_name_or_phone(%s, %s)', (user_name, user_phone))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    user_name = input("Enter user's name to delete (or leave blank): ")
    user_phone = input("Enter user's phone number to delete (or leave blank): ")
    delete_user_by_name_or_phone(user_name, user_phone)
