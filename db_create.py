import os
import pymysql
import myenviron
from db import db

class query_create_user(db):
    
    def __init__(self, user_values):
        self.username = user_values['Username'].lower()
        self.first = user_values['First'].lower()
        self.last = user_values['Last'].lower()
        self.password = user_values['Password']
       

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
        self.recipe_title = recipe['RecipeTitle']
        self.recipe_description = recipe['RecipeDescription']
        self.cooking_time = recipe['CookingTimeMins']
        self.make_public = recipe['MakePublic']
        self.user_id = recipe['UserId']

    def create_recipe(self):
        query = """ INSERT INTO Recipe (`RecipeTitle`, 
                                        `RecipeDescription`, 
                                        `CookingTimeMins`, 
                                        `MakePublic`, 
                                        `UserId`) 
                    VALUES (%s, %s, %s, %s, %s);"""
        values = (self.recipe_title, self.recipe_description,self.cooking_time, self.make_public,self.user_id)
                                                                            
        try:
            with db.connection.cursor() as cursor:
                cursor.execute(query, values);
                db.connection.commit()
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query create recipe completed")

