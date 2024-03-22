#!/usr/bin/python3
"""
 script that lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    database.close()
