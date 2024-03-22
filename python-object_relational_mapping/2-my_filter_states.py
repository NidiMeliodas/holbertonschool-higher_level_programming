#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                   ORDER BY states.id""".format(sys.argv[4],))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
