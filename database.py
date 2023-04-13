import sqlite3
from sqlite3 import Error


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_file):
    connection = sqlite3.connect(db_file)

    with open('./static/sql/schema.sql') as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()

def insert_db(table_name, date_names ,data_values):
    conn = get_db_connection()
    insert_string = f'INSERT INTO {table_name} ({date_names}) VALUES ({("?,"*len(data_values))[:-1]})'
    print(insert_string)
    conn.execute(insert_string, data_values)
    conn.commit()
    conn.close()