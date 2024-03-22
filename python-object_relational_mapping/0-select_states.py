#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    
    states = cursor.fetchall()
    
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
