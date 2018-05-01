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
            print("Query Completed")
    
class query_read_recipes(db_connection):
    
    def query_read_user(self, user_values):
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
            print("Query Completed")

## UPDATE THIS QUERY SO THAT IT JOINS ALL THE INFO NEEDED FOR THE MINI RECIPE DISPLAY, ##
## NOT JUST FULL RECIPE TABLE VIEW, USE FOR PUBLIC FEED, SEARCH FEED AND MY RECIPES VIEW ##
    def query_mini_recipe_from_user_id(self, user_id):
        """ GET ALL MINI RECIPE VIEW FOR GIVEN USER, UNFILTERED, USE FOR ME PAGE OF MINI RECIPES """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = """SELECT RecipeTitle, RecipeDescription, CookingTimeMins, Rating.Rating, 
                                    Rating.Comments, User.Username, Cost.Cheap, Cost.Moderate, Cost.Pricey,
                                    One, TwotoFour, FourtoEight, EightandOver, CuisineName, Healthy, 
                                    Health.Moderate as Medium,Unhealthy, CourseName
                                    FROM Recipe 
                                    JOIN Rating on Recipe.RecipeId = Rating.RatingId
                                    JOIN User on Recipe.UserId = User.UserId
                                    JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                    JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Recipe.RecipeId = Health.RecipeId
                                    JOIN Course on Recipe.RecipeId = Course.RecipeId
                                    WHERE Recipe.UserId = %s;"""
                cursor.execute(recipes_query, user_id)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Completed")

    """
    def query_read_recipe_table_from_user_id(self, user_id):
        GET MINI RECIPE VIEW FOR GIVEN USER 
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                recipes_query = ""SELECT * FROM Recipe WHERE UserId = %s;""
                cursor.execute(recipes_query, user_id)
                recipes = [row for row in cursor]
                return recipes
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Completed")        

    """
  ## START OF PARTIAL QUERIES FOR FULL RECIPE VIEW ##
    def query_read_for_recipe_stats(self, recipe_id):
        """ GET STATS FOR GIVEN RECIPE BASED ON RECIPE ID """
        try:
            with db_connection.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                stats_query = """SELECT Rating.Rating, Comments, Cheap , Cost.Moderate, Pricey, 
                                        Healthy, Health.Moderate, Unhealthy, One, TwotoFour, FourtoEight, EightandOver
                                        FROM Rating 
                                        INNER JOIN Cost on Rating.RecipeId = Cost.RecipeId 
                                        INNER JOIN Health on Rating.RatingId = Health.RecipeId 
                                        INNER JOIN Servings on Rating.RatingId = Servings.RecipeId
                                        WHERE Rating.RecipeId = %s;"""
                                    
                cursor.execute(stats_query, recipe_id)
                stats = [row for row in cursor]
                return(stats)
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Completed")

## NEED TO COMPLETE QUERIES FOR FULL RECIPE VIEW ##

