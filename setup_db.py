#!/usr/bin/env python
import os
import pymysql
from myenviron import ROOT_PASSWORD
# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)
username = 'root'
##http://127.0.0.1:5000/
print(username)
##DATABASE_URL="mysql://b9f818ea5afaf2:928b0214@eu-cdbr-west-02.cleardb.net/heroku_8fae79bf14c2152?reconnect=true"
# Connect to the database
connection = pymysql.connect(host='localhost', port=3306, user=username,password=ROOT_PASSWORD, db='')

try:
    with connection.cursor() as cursor:
        print("connected")
        """
        list_of_names = ['Jim', 'Jill']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s'] * len(list_of_names))
        cursor.execute(
            "DELETE FROM Friends WHERE name in ({});".format(format_strings),
            list_of_names)

        connection.commit()
        """
finally:
    connection.close()