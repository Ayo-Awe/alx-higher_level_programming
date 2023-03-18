#!/usr/bin/python3
"""MySQLClient task to select state"""
import MySQLdb
import sys


def filter_states():
    """This function fetchs a list of
    states starting with the letter 'N'
    """
    try:
        user, pwd, db = sys.argv[1:]
        connect_options = {
            "user":  user,
            "password": pwd,
            "database": db,
            "host": "localhost",
            "port": 3306
        }
        conn = MySQLdb.connect(**connect_options)
        cursor = conn.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        cursor.execute(query)
        results = cursor.fetchall()

        for row in results:
            print(row)

        cursor.close()
        conn.close()
    except Exception as e:
        return e


if __name__ == "__main__":
    filter_states()
