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
    
    def query_read_user_for_id(self, user_values):
        """ GET USER ID FOR GIVEN USER BASED ON USER DETAILS"""
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


    def query_all_mini_recipe(self, search_by, value):
        """ GET ALL MINI RECIPE VIEW FOR GIVEN USER, UNFILTERED, OR FROM ALL RECIPES DECLARED PUBLIC BY A VALUE OF 1 FOR TRUE """
        
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT RecipeTitle, RecipeDescription, CookingTimeMins, Created, ImageURL, Rating.Rating, 
                                    Rating.Comments, User.Username, Price, Servings, CuisineName, Calories, 
                                    CourseName
                                    FROM Recipe 
                                    JOIN Rating on Recipe.RecipeId = Rating.RatingId
                                    JOIN User on Recipe.UserId = User.UserId
                                    JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                    JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Recipe.RecipeId = Health.RecipeId
                                    JOIN Course on Recipe.RecipeId = Course.RecipeId
                                    WHERE Recipe.%s = %s;""" % (search_by, value)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Completed")

    def query_mini_recipe_sorted(self, search_by, value):
        """ GET ALL MINI RECIPES FILTERED BY CUISINE AND COURSE, SORTED BY EITHER COST,  """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT RecipeTitle, RecipeDescription, CookingTimeMins, Created, ImageURL, Rating.Rating, 
                                    Rating.Comments, User.Username, Price, Servings, CuisineName, Calories, 
                                    CourseName
                                    FROM Recipe 
                                    JOIN Rating on Recipe.RecipeId = Rating.RatingId
                                    JOIN User on Recipe.UserId = User.UserId
                                    JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                    JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Recipe.RecipeId = Health.RecipeId
                                    JOIN Course on Recipe.RecipeId = Course.RecipeId
                                    WHERE Recipe.%s = %s
                                    ORDER BY RecipeTitle asc;""" % (search_by, value)
                                    
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Completed")

    

## NEED TO COMPLETE QUERIES FOR FULL RECIPE VIEW ##

