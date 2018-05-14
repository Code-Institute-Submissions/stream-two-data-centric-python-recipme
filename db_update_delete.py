import pymysql
from db import Db
from db_create import Query

class QueryDeleteRecipe():
    
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        self.query = """ DELETE FROM Recipe 
                            WHERE RecipeId = %s""" % (self.recipe_id)    
    
    def delete(self):
        try:
            with Db(commit=True) as cursor:            
                cursor.execute(self.query)
        finally:
            print("Query Delete Recipe Completed")

class QueryUpdateRecipe():

    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def print_query(self):
        new_query = Query()
        print(new_query.recipe_query)