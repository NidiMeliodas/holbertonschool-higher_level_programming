#!/usr/bin/python3
"""
script that lists all states
 with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user_name = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]

    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user_name,
        password=pwd,
        database=db
    )
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
