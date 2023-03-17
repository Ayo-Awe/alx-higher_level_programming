#!/usr/bin/python3
"""MySQLClient task to select state"""
import MySQLdb
import sys

if __name__ == "__main__":
    connect_options = {
        "user":  sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
        "host": "localhost",
        "port": 3306
    }
    conn = MySQLdb.connect(**connect_options)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
