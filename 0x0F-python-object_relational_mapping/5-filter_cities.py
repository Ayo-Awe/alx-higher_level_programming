#!/usr/bin/python3
"""This module contains code to fetch all the cities in a given
state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user, pwd, db, state = sys.argv[1:]
    connect_options = {
        "user": user,
        "password": pwd,
        "database": db,
        "host": "localhost",
        "port": 3306
    }

    conn = MySQLdb.connect(**connect_options)
    cursor = conn.cursor()

    query = """SELECT cities.name FROM cities JOIN states ON
    states.id=cities.state_id WHERE states.name LIKE %s ORDER
    BY cities.id ASC """
    cursor.execute(query, (state,))
    results = cursor.fetchall()

    # Turn results to a list of strings and print the list
    list_results = list(map(lambda x: x[0], list(results)))
    print(", ".join(list_results))
