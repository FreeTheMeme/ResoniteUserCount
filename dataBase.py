import psycopg2
import passwords

users_count = 0

def addrow(uesrs):
    conn = psycopg2.connect(database="resoniteUserCount",
                        host="10.0.0.104",
                        user="postgres",
                        password=passwords.DBpassword,
                        port="5432")

    cur = conn.cursor()

    insert_script = 'INSERT INTO resoniteUserCount_data (users, time) VALUES (%s, %s)'
    insert_value = (uesrs, "now")
    cur.execute(insert_script, insert_value)
    conn.commit()

    cur.close()
    conn.close()
    print("added row ",uesrs," here")
