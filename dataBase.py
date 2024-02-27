import psycopg2

    # connect to database
conn = psycopg2.connect(
    database="resoniteUsers",
    host="10.0.0.",
    user="postgres",
    password="",
    port="5432",
    )
    # add row
cur = conn.cursor()