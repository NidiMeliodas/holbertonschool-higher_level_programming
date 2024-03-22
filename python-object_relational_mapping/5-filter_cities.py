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
    cursor.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id""", (sys.argv[4],))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    cursor.close()
    database.close()
