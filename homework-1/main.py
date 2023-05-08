"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

def instantiate_from_csv(file_mame):
    """"""
    with open(os.path.join(file_mame), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()
        for row in reader:
            cur.execute("INSERT INTO my_table (column1, column2, column3) VALUES (%s, %s, %s)",
                        (row[0], row[1], row[2]))

    conn.commit()
    cur.close()
    conn.close()