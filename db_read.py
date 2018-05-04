import os
import pymysql
import myenviron
from db import db

class user_verify(db):
    
    def __init__(self, user_values):
        self.username = user_values['Username'].lower()
        self.password = user_values['Password'].lower()
      
    def query_username_and_password(self):
        """ GET USERNAME AND PASSWORD BASED ON USER INFO """
        try: 
            with db.connection.cursor(pymysql.cursors.DictCursor) as cursor:
                query = """SELECT `Username`, `Password` FROM User
                            WHERE Username = %s;"""
                cursor.execute(query, (self.username))
                from_db = [result for result in cursor]
                return from_db
        except pymysql.err.OperationalError as e:
            print(e)
        finally:
            print("Query Username and Password completed")

    
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
    


