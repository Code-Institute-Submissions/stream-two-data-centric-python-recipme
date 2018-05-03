import os
import pymysql
import unittest
import myenviron

class db():
    
    connection = pymysql.connect(host=os.environ.get('DATABASE_HOST'), 
                port=3306, user=os.environ.get('DATABASE_USER'),
                password=os.environ.get('DATABASE_PASSWORD'), 
                db=os.environ.get('DATABASE_NAME'))

    select = """SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, CookingTimeMins, Created, ImageURL, Rating.Rating, 
                        Rating.Comments,Price, Servings, CuisineName, Calories, 
                        CourseName, User.Username as Author"""

    main_selection = select + """
                                FROM Recipe 
                                JOIN Rating on Recipe.RecipeId = Rating.RecipeId
                                JOIN User on Recipe.UserId = User.UserId
                                JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                JOIN Health on Recipe.RecipeId = Health.RecipeId
                                JOIN Course on Recipe.RecipeId = Course.RecipeId 
                                """

    search_ingredient =  select + """
                                    FROM Ingredient
                                    JOIN Recipe on Ingredient.RecipeId = Recipe.RecipeId
                                    JOIN Rating on Ingredient.RecipeId = Rating.RecipeId
                                    JOIN Cost on Ingredient.RecipeId = Cost.RecipeId
                                    JOIN Servings on Ingredient.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Ingredient.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Ingredient.RecipeId = Health.RecipeId
                                    JOIN Course on Ingredient.RecipeId = Course.RecipeId
                                    JOIN User on Ingredient.UserId = User.UserId 
                                    """


    saved_recipes = select + """
                                FROM SavedRecipes
                                JOIN Recipe on SavedRecipes.RecipeId = Recipe.RecipeId
                                JOIN Rating on SavedRecipes.RecipeId = Rating.RecipeId
                                JOIN Cost on SavedRecipes.RecipeId = Cost.RecipeId
                                JOIN Servings on SavedRecipes.RecipeId = Servings.RecipeId
                                JOIN Cuisine on SavedRecipes.RecipeId = Cuisine.RecipeId
                                JOIN Health on SavedRecipes.RecipeId = Health.RecipeId
                                JOIN Course on SavedRecipes.RecipeId = Course.RecipeId
                                JOIN User on Recipe.UserId = User.UserId
                                """


class read_one_table(db):
    
    def __init__(self, table):
        self.table = table
      
    def read_all_from_one_table(self):
        """ GET WHOLE TABLE BASED ON TABLE NAME """
        try: 
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                all_fields = "SELECT * FROM {0};".format(self.table)
                cursor.execute(all_fields)
                from_db = [result for result in cursor]
                return from_db
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query read one table completed")
    
class query_read_recipes(db):
    
    def query_user_id(self, user_values):
        """ QUERY DB USER TABLE FOR USER ID BASED ON USER LOGIN DETAILS"""
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                get_id_query = """SELECT UserId FROM User 
                            WHERE First = %s 
                            AND Last = %s 
                            AND Password = %s;"""
                cursor.execute(get_id_query, user_values)
                user_id = [row for row in cursor]
                return(user_id)
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query read user completed")


    def query_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET ALL MINI RECIPES ORDERED BY GIVEN USER SELECTION, AND FILTERED BY 
            GIVEN USER SELECTION, PUBLIC AND USER SPECIFIC  """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db.main_selection + """ 
                                WHERE %s = %s ORDER BY %s %s;""" % (search_by, search_value, order_by, direction) #SEARCH BY VALUE CAN BE USERID,MAKEPUBLIC, RECIPE ID#                    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")


    def query_filter_mini_recipes(self, search_by, search_value, course, cuisine, order_by, direction):
        """ GET ALL MINI RECIPES FILTERED BY COURSE AND CUISINE, SORTED BY GIVEN USER SELECTION, FOR USER OR PUBLIC FEED """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db.main_selection + """
                                WHERE %s = %s AND CourseName LIKE '%s' AND CuisineName LIKE '%s'
                                ORDER BY %s %s;""" % (search_by, search_value, course, cuisine, order_by, direction)                   
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")

    def query_search_ingredient(self, search_by, search_value, ingredient, order_by, direction):
        """ GET ALL MINI RECIPES FOR GIVEN INGREDIENT """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db.search_ingredient + """ 
                                WHERE %s = %s AND Ingredient.IngredientName LIKE '%s'
                                ORDER BY %s %s;""" % (search_by, search_value, ingredient, order_by, direction)    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")

    def query_ingredients_for_full_recipe(self, recipe_id):
        """ GET INGREDIENTS BASED ON GIVEN RECIPE ID """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT IngredientName, Quantity FROM Ingredient
                                    WHERE Ingredient.RecipeId = %s;""" % (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get ingredients completed")

    def query_method_for_full_recipe(self, recipe_id):
        """ GET FULL METHOD BASED ON GIVEN RECIPE ID """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT StepNumber, StepDescription FROM Method
                                    WHERE Method.RecipeId = %s;""" % (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get method completed")
    
    def query_users_saved_recipes(self, user_id, order_by, direction):
        """ QUERY USERS SAVED RECIPES BASED ON USER ID """
        try:
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db.saved_recipes + """ 
                                WHERE SavedRecipes.UserId = %s 
                                ORDER BY %s %s;""" % (user_id, order_by, direction)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get method completed")    
    


