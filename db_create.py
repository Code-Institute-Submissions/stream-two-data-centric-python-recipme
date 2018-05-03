import os
import pymysql
import unittest
import myenviron
from db_read import db

class query_create_user(db):
    
    def __init__(self, user_values):
        self.username = user_values['Username'].lower()
        self.first = user_values['First'].lower()
        self.last = user_values['Last'].lower()
        self.password = user_values['Password'].lower()
       

    def create_user(self):
        query = """INSERT INTO User (`Username`,`First`,`Last`,`Password` ) VALUES (%s, %s, %s, %s);"""
        try:
            with db.connection.cursor() as cursor:
                cursor.execute(query, (self.username, self.first, self.last, self.password));
                db.connection.commit()
        except pymysql.err.OperationalError as e:
            print(e)
        finally: 
            print('New User Created')

class query_create_recipes(db):

    def __init__(self,recipe):
        self.recipe = recipe

    def create_recipe(self):
        try:
            with db.connection.cursor() as cursor:
                values = [("Daf", 33, "1984-09-14 23:00:00"),
                            ("Jim", 55, "1977-09-14 23:00:00"),
                        ("Jill", 66,"1977-09-14 23:00:00")]
                cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", values);
                connection.commit()
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query create recipe completed")

