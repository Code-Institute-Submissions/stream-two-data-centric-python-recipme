#!/usr/bin/env python
import os
import pymysql
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME
# Get the username from the Cloud9 workspace
# (modify this variable if running on another environment)



##http://127.0.0.1:5000/
##print(username)

# Connect to the database

os.environ['DATABASE_HOST'] = REMOTE_HOST
os.environ['DATABASE_USER'] = REMOTE_USER
os.environ['DATABASE_PASSWORD'] = REMOTE_PASSWORD
os.environ['DATABASE_NAME'] = DATABASE_NAME

connection = pymysql.connect(host=os.environ.get('DATABASE_HOST'), 
                        port=3306, user=os.environ.get('DATABASE_USER'),
                        password=os.environ.get('DATABASE_PASSWORD'), 
                        db=os.environ.get('DATABASE_NAME'))

def read_all(table):
    query = []
    if connection.open:  
        try:
            with connection.cursor(pymysql.cursors.DictCursor) as cursor:
                sql = "SELECT * FROM {0};".format(table)
                cursor.execute(sql)
                for results in cursor:
                    query.append(results) 
        except pymysql.err.OperationalError as e:
            print(e)     
        finally:
            connection.close()
    else:
        print("could not carry out query")
    return print(query)



ingredient_query.sql('Ingredient')