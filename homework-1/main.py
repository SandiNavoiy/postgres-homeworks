"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

def instantiate_from_csv(file_mame):
    """"""
    with open(os.path.join(file_mame), 'r') as f:
        reader = csv.reader(f)
        next(reader)
        conn = psycopg2.connect(dbname="north", user="postgres", password="1", host="localhost")
        cur = conn.cursor()
        for row in reader:
            cur.execute("INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
                        (row[0], row[1], row[2]))

    conn.commit()
    cur.close()
    conn.close()

instantiate_from_csv("north_data/customers_data.csv")