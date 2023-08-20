#!/usr/bin/python3
'''
    Takes in an argument and displays all values in the states table
'''

import sys
import MySQLdb


def get_states(username, password, db_name, search_value):
    ''' Access database to get states '''
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=db_name, port=3306)

    cursor = db.cursor()
    bad_query = "SELECT * FROM states WHERE name=('{}')\
                 ORDER BY id ASC".format(search_value)
    cursor.execute(bad_query)
    rows = cursor.fetchall()
    for row in rows:
        if (row[1] == search_value):
            print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    credentials = sys.argv
    username = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    search_value = sys.argv[4]
    get_states(username, passwd, db_name, search_value)
