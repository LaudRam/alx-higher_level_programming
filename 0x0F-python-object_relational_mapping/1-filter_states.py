#!/usr/bin/python3
''' Lists all states with a name starting with N from the database '''

import sys
import MySQLdb


def get_states(username, password, db_name):
    ''' Access database to get states '''
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`\
                   WHERE `name` REGEXP '^N' ORDER BY `id` ASC")
    rows = cursor.fetchall()
    for row in rows:
        if ("N" in row[1]):
            print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    credentials = sys.argv
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    get_states(username, passwd, db_name)
