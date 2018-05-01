import os
import pymysql
import unittest
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

os.environ['DATABASE_HOST'] = REMOTE_HOST
os.environ['DATABASE_USER'] = REMOTE_USER
os.environ['DATABASE_PASSWORD'] = REMOTE_PASSWORD
os.environ['DATABASE_NAME'] = DATABASE_NAME

class db_connection():
    
    connection = pymysql.connect(host=os.environ.get('DATABASE_HOST'), 
                port=3306, user=os.environ.get('DATABASE_USER'),
                password=os.environ.get('DATABASE_PASSWORD'), 
                db=os.environ.get('DATABASE_NAME'))

    main_selection = """SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, CookingTimeMins, Created, ImageURL, Rating.Rating, 
                                    Rating.Comments, User.Username, Price, Servings, CuisineName, Calories, 
                                    CourseName
                                    FROM Recipe 
                                    JOIN Rating on Recipe.RecipeId = Rating.RatingId
                                    JOIN User on Recipe.UserId = User.UserId
                                    JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                    JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Recipe.RecipeId = Health.RecipeId
                                    JOIN Course on Recipe.RecipeId = Course.RecipeId"""

class read_one_table(db_connection):
    
    def __init__(self, table):
        self.table = table
      
    def read_all_from_one_table(self):
        """ GET WHOLE TABLE BASED ON TABLE NAME """
        try: 
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                all_fields = "SELECT * FROM {0};".format(self.table)
                cursor.execute(all_fields)
                from_db = [result for result in cursor]
                return from_db
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query read one table completed")
    
class query_read_recipes(db_connection):
    
    def query_user_id(self, user_values):
        """ QUERY DB USER TABLE FOR USER ID BASED ON USER LOGIN DETAILS"""
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
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

##### THIS WILL GET ALL UNFILTERED MINI VIEW RECIPES FOR USER, PUBLIC, RECIPE ID, SORTED BY CALORIES ETC... #####
    def query_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET ALL MINI RECIPES ORDERED BY GIVEN USER SELECTION, AND FILTERED BY GIVEN USER SELECTION  """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db_connection.main_selection + """ 
                                WHERE %s = %s ORDER BY %s %s;""" % (search_by, search_value, order_by, direction) #SEARCH BY VALUE CAN BE USERID,MAKEPUBLIC, RECIPE ID#                    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")

## USE THIS QUERY WHEN UDER SELECTS GIVEN CUISINE, AND COURSE TO CHOOSE FROM ##
    def query_filter_mini_recipes(self, search_by, search_value, course, cuisine, order_by, direction):
        """ GET ALL MINI RECIPES FILTERED BY COURSE AND CUISINE, SORTED BY GIVEN USER SELECTION, FOR USER OR PUBLIC FEED """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = db_connection.main_selection + """
                                    WHERE %s = %s AND CourseName LIKE '%s' AND CuisineName LIKE '%s'
                                    ORDER BY %s %s;""" % (search_by, search_value, course, cuisine, order_by, direction)                   
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")

    def query_search_ingredient(self, search_by, search_value, course, cuisine, order_by, direction):
        """ GET ALL MINI RECIPES FILTERED BY COURSE AND CUISINE, SORTED BY GIVEN USER SELECTION, FOR USER OR PUBLIC FEED """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, CookingTimeMins, Created, ImageURL, Rating.Rating, 
                                    Rating.Comments, User.Username, Price, Servings, CuisineName, Calories, 
                                    CourseName
                                    FROM Recipe 
                                    JOIN Rating on Recipe.RecipeId = Rating.RatingId
                                    JOIN User on Recipe.UserId = User.UserId
                                    JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                    JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Recipe.RecipeId = Health.RecipeId
                                    JOIN Course on Recipe.RecipeId = Course.RecipeId"""              
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get mini recipes completed")

    def query_ingredients_for_full_recipe(self, recipe_id):
        """ GET FULL RECIPE BASED ON GIVEN RECIPE ID """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
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
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT StepNumber, StepDescription FROM Method
                                    WHERE Method.RecipeId = %s;""" % (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query get method completed")
        
        

## NEED TO COMPLETE QUERIES FOR FULL RECIPE VIEW ##

