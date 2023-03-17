#!/usr/bin/python3
"""This module contains code for select cities from a database using
a mysql db adapter
"""
import MySQLdb
import sys


if __name__ == "__main__":
    user, password, database = sys.argv[1:]
    connect_options = {
        "user": user,
        "password": password,
        "database": database,
        "host": "localhost",
        "port": 3306
    }

    db = MySQLdb.connect(**connect_options)
    cursor = db.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN \
    states ON cities.state_id=states.id ORDER BY cities.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()
