#! /usr/local/bin/python
#
# source: https://www.blog.pythonlibrary.org/2021/09/30/sqlite/

import sqlite3

def get_cursor():
    conn = sqlite3.connect("db/macs.sqlite")
    return conn.cursor()

def select_all_records_by_device(cursor, device):
    sql = "SELECT * FROM macs WHERE device=?"
    cursor.execute(sql, [device])
    print(cursor.fetchall())  # or use fetchone()
    print("\nHere is a listing of the rows in the table\n")
    for row in cursor.execute("SELECT rowid, * FROM macs ORDER BY device"):
        print(row)

def select_using_like(cursor, text):
    print("\nLIKE query results:\n")
    sql = f"""
    SELECT * FROM macs
    WHERE device LIKE '{text}%'"""
    cursor.execute(sql)
    print(cursor.fetchall())

if __name__ == '__main__':
    cursor = get_cursor()
    select_all_records_by_device(cursor,
                                 device='laptop1')
    select_using_like(cursor, text='vrsn')