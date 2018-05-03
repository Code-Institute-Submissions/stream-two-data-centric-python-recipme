import os
import pymysql
import unittest
import myenviron
from db_read import db

recipe = [{

    'RecipeTitle': ,
    'RecipeDescription': ,
    'CookingTimeMins': ,
    'UserId': ,
    'MakePublic': ,
    'RecipeId': ,
    'CuisineName': ,
    'CourseName': ,
    'Calories': ,
    'Price': ,
    'IngredientName': []

}]

class 

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