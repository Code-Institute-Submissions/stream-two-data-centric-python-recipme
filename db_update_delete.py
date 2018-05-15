import pymysql
from db import Db
from db_create import QueryCreateRecipe, QueryCreateMethodItems

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

class UpdateQuery():
    
    recipe_query = """ UPDATE Recipe SET 
                        RecipeTitle = %s,
                        RecipeDescription = %s,
                        CookingTimeMins = %s,
                        MakePublic = %s
                        WHERE RecipeId = %s;
                    """
    ingredients_query = """ UPDATE Ingredient SET
                            IngredientName = %s,
                            Quantity = %s
                            WHERE RecipeId = %s;
                        """

    method_query = """ UPDATE Method SET
                        StepNumber = %s, 
                        StepDescription = %s
                        WHERE RecipeId = %s;
                    """
    def single_column_query(self, table, column, column_value, recipe_id):
        query = """ UPDATE %s SET
                    %s = '%s'
                    WHERE RecipeId = %s;
                """ % (table, column, column_value, recipe_id)
        return query

class QueryUpdateRecipe(QueryCreateRecipe):

    def __init__(self, recipe, user_id, recipe_id):
        super().__init__(recipe, user_id)
        self.recipe_id = recipe_id

    def update_recipe(self):
        recipe_values = (self.recipe_title, self.recipe_description,
                            self.cooking_time, self.make_public, self.recipe_id)
        try:
            with Db(commit=True) as cursor:
                #print(recipe_values)
                cursor.execute(UpdateQuery.recipe_query, recipe_values)
        finally:
            print("Query Update Recipe completed")

    def update_stats(self):
        stat_queries = [[UpdateQuery.single_column_query(self,'Cuisine','CuisineName', 
                                                        self.cuisine_name, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Course','CourseName', 
                                                        self.course_name, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Health','Calories', 
                                                        self.calories, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Cost','Price',
                                                         self.cost, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Servings','Servings', 
                                                        self.servings, self.recipe_id)]]
        try:
            with Db(commit=True) as cursor:
                for stat in stat_queries:
                    cursor.execute(stat[0])
        finally:
            print("Query Update stats completed")
     
class QueryUpdateMethodItems(QueryCreateMethodItems):

    def __init__(self, prepped_ingredients, prepped_method):
        super().__init__(prepped_ingredients, prepped_method)
       
    def update_ingredients_and_method(self):
        try:
            with Db(commit=True) as cursor:
                cursor.executemany(UpdateQuery.ingredients_query, self.ingredients)
                cursor.executemany(UpdateQuery.method_query, self.method)
        finally:
            print("Query Update Recipe completed")
