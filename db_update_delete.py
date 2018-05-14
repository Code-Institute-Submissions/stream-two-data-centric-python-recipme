import pymysql
from db import Db
from db_create import Query, QueryCreateRecipe

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

class QueryUpdateRecipe(QueryCreateRecipe):

    def __init__(self, recipe, user_id):
        super().__init__()
    
        

    #def print_query(self):
        