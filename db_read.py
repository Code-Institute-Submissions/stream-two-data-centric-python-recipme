import os
import pymysql
import myenviron
from db import db

class user_verify(db):
    
    def __init__(self, user_values):
        self.username = user_values['Username']
        self.password = user_values['Password']
      
    def query_user(self):
        """ GET USER BASED ON USER INFO """
        try: 
            with db() as cursor:
                query = """SELECT `Username`,`First`,`Last`,`Password`, `UserId` FROM User
                            WHERE Username = %s;"""
                cursor.execute(query, (self.username))
                from_db = [result for result in cursor]
                return from_db
        finally:
            print("Query Username and Password completed")

class query():
    
    def __init__(self):
        
        self.select = """ SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, 
                        CookingTimeMins, Created, ImageURL, Price, Servings, CuisineName, 
                        Calories, CourseName, User.Username as Author, Recipe.UserId """
    
    def main_selection(self) :
        main_selection = self.select + """
                                        FROM Recipe 
                                        JOIN User on Recipe.UserId = User.UserId
                                        JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                        JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                        JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                        JOIN Health on Recipe.RecipeId = Health.RecipeId
                                        JOIN Course on Recipe.RecipeId = Course.RecipeId 
                                        """
        return main_selection

    def search_ingredient(self): 
    
        search_ingredient = self.select + """
                                            FROM Ingredient
                                            JOIN User on Ingredient.UserId = User.UserId 
                                            JOIN Recipe on Ingredient.RecipeId = Recipe.RecipeId
                                            JOIN Cost on Ingredient.RecipeId = Cost.RecipeId
                                            JOIN Servings on Ingredient.RecipeId = Servings.RecipeId
                                            JOIN Cuisine on Ingredient.RecipeId = Cuisine.RecipeId
                                            JOIN Health on Ingredient.RecipeId = Health.RecipeId
                                            JOIN Course on Ingredient.RecipeId = Course.RecipeId
                                            """ 
        return search_ingredient


    def saved_recipes(self):
        saved_recipes = self.select + """
                                        FROM SavedRecipes
                                        JOIN User on SavedRecipes.UserId = User.UserId
                                        JOIN Recipe on SavedRecipes.RecipeId = Recipe.RecipeId
                                        JOIN Cost on SavedRecipes.RecipeId = Cost.RecipeId
                                        JOIN Servings on SavedRecipes.RecipeId = Servings.RecipeId
                                        JOIN Cuisine on SavedRecipes.RecipeId = Cuisine.RecipeId
                                        JOIN Health on SavedRecipes.RecipeId = Health.RecipeId
                                        JOIN Course on SavedRecipes.RecipeId = Course.RecipeId
                                        """
        return saved_recipes

class query_category(query):
    
    def __init__(self, table, join_table):
        super().__init__()
        self.table = table
        self.join_table = join_table

    def category_selection(self):
        search_category =  self.select + """
                                        FROM %s
                                        JOIN %s on %s.RecipeId = %s.RecipeId
                                        JOIN Recipe on %s.RecipeId = Recipe.RecipeId
                                        JOIN Cost on %s.RecipeId = Cost.RecipeId
                                        JOIN Servings on %s.RecipeId = Servings.RecipeId
                                        JOIN Health on %s.RecipeId = Health.RecipeId
                                        JOIN User on Recipe.UserId = User.UserId 
                                        """ % (self.table, self.join_table, self.table, self.join_table,
                                                self.table, self.table, self.table, self.table )
        return search_category
    

class query_read_recipes(db):

    def query_user_id(self, username):
        """ QUERY DB USER TABLE FOR USER ID BASED ON USER LOGIN DETAILS"""
        try:
            with db() as cursor:
                get_id_query = f"""SELECT UserId FROM User
                                    WHERE Username = '{username}';""" #% (username)                  
                cursor.execute(get_id_query)
                user_id = [row for row in cursor]
                return(user_id)
        finally:
            print("Query read user completed")

    def query_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET ALL MINI RECIPES ORDERED BY GIVEN USER SELECTION, AND FILTERED BY 
            GIVEN USER SELECTION, PUBLIC AND USER SPECIFIC  """
        try:
            with db() as cursor:
                new_query = query()
                recipes_query = new_query.main_selection() + f""" WHERE {search_by} = {search_value} 
                                                                    ORDER BY {order_by} {direction};""" #% (search_by, search_value, order_by, direction) #SEARCH BY VALUE CAN BE USERID,MAKEPUBLIC, RECIPE ID#                    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get mini recipes completed")


    def query_category_mini_recipes(self, table, search_by, search_value, column, category, order_by, direction):
        """ GET ALL MINI RECIPES FILTERED BY COURSE AND CUISINE, SORTED BY GIVEN USER SELECTION, FOR USER OR PUBLIC FEED """
        join_table = []
        if table == 'Cuisine':
            join_table = 'Course'
        else:
            join_table ='Cuisine'
        try:
            with db() as cursor:
                new_query = query_category(table, join_table)
                recipes_query = new_query.category_selection() + f""" WHERE {search_by} = {search_value} AND {column} = '{category}' 
                                                                        ORDER BY {order_by} {direction};"""                                                                 
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                #print(recipes_query)
                return recipes
        finally:
            print("Query get mini recipes completed")

    def query_search_ingredient(self, search_by, search_value, ingredient, order_by, direction):
        """ GET ALL MINI RECIPES FOR GIVEN INGREDIENT """
        try:
            with db() as cursor:
                new_query = query()
                recipes_query = new_query.search_ingredient() + f""" WHERE {search_by} = {search_value} 
                                                                    AND Ingredient.IngredientName LIKE '{ingredient}'
                                                                    ORDER BY {order_by} {direction};""" #% (search_by, search_value, ingredient, order_by, direction)    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get mini recipes completed")

    def query_ingredients_for_full_recipe(self, recipe_id):
        """ GET INGREDIENTS BASED ON GIVEN RECIPE ID """
        try:
            with db() as cursor:
                recipes_query = f"""SELECT IngredientName, Quantity FROM Ingredient
                                    WHERE Ingredient.RecipeId = {recipe_id};""" #% (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get ingredients completed")

    def query_method_for_full_recipe(self, recipe_id):
        """ GET FULL METHOD BASED ON GIVEN RECIPE ID """
        try:
            with db() as cursor:
                recipes_query = f"""SELECT StepNumber, StepDescription FROM Method
                                    WHERE Method.RecipeId = {recipe_id};""" #% (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get method completed")
    
    def query_users_saved_recipes(self, user_id, order_by, direction):
        """ QUERY USERS SAVED RECIPES BASED ON USER ID """
        try:
            with db() as cursor:
                new_query = query()
                recipes_query = new_query.saved_recipes() + f""" 
                                WHERE SavedRecipes.UserId = {user_id} 
                                ORDER BY {order_by} {direction};""" #% (user_id, order_by, direction)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get method completed")    
    
    def query_count_and_group_column(self, column, user_id, table):
        """ QUERY THE COUNT OF A SPECIFIC COLUMN AND GROUP BY THAT COLUMN """
        """ USE FOR GROUPING CUISINE AND COURSE IN RECIPE SEARCH """
        try:
            with db() as cursor:
                recipes_query = f""" SELECT COUNT({column}) as Total,{column},Recipe.UserId
                                    FROM {table}
                                    JOIN Recipe on {table}.RecipeId = Recipe.RecipeId
                                    WHERE UserId = {user_id} 
                                    GROUP BY {column};""" #% (column, column,table, table, user_id, column)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query count Column based on UserId Completed")
 
