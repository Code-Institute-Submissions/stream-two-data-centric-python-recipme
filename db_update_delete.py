import pymysql
from db import db

class query_delete_recipe(db):
    
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        self.query = """ DELETE FROM Recipe 
                            WHERE RecipeId = %s""" % (self.recipe_id)    
    
    def delete(self):
        try:
            with db(commit=True) as cursor:            
                cursor.execute(self.query)
        finally:
            print("Query Delete Recipe Completed")
