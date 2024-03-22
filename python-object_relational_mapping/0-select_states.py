#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
