import psycopg2
from config import config

def insert_multiple_users(user_data_list):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for user_data in user_data_list:
            cur.execute('CALL insert_user(%s, %s, %s)', user_data)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    num_users = int(input("Enter the number of users to add: "))
    user_data_list = []
    for _ in range(num_users):
        user_first_name = input("Enter user's first name: ")
        user_last_name = input("Enter user's last name: ")
        user_phone = input("Enter user's phone number: ")
        user_data_list.append([user_first_name, user_last_name, user_phone])

    insert_multiple_users(user_data_list)
