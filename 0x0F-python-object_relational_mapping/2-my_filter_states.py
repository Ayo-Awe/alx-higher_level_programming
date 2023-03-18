#!/usr/bin/python3
"""MySQLClient task to filter state by search string"""
import MySQLdb
import sys

if __name__ == "__main__":
    # set connection options
    connect_options = {
        "user":  sys.argv[1],
        "password": sys.argv[2],
        "database": sys.argv[3],
        "host": "localhost",
        "port": 3306
    }
    search_name = sys.argv[4]

    conn = MySQLdb.connect(**connect_options)
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(
        search_name)
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
