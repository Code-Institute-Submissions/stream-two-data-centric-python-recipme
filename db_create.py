import os
import pymysql
#import myenviron
from db import Db, WriteErrorToLog, log_file
from datetime import datetime

def capitalize_words(string):
    words = string.split()
    return ' '.join([word.capitalize() for word in words])

######################## CLASS FOR SQL QUERY FOR USER CREATION #########################
 
class QueryCreateUser():
    
    def __init__(self, user_values):
        self.username = user_values['Username'].lower()
        self.first = user_values['First'].lower()
        self.last = user_values['Last'].lower()
        self.password = user_values['Password']
       

    def create_user(self):
        query = """INSERT INTO User (`Username`,`First`,`Last`,`Password` ) VALUES (%s, %s, %s, %s);"""
        try:
            with Db(commit=True) as cursor:
                cursor.execute(query, (self.username, self.first, self.last, self.password))
                #Db.connection.commit()
        except pymysql.err.OperationalError as e:
            message = " FAILED: create_user method in db_create.QueryCreateUser."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("create_user completed")

######################## CLASS FOR SQL QUERY SELECTIONS FOR RECIPE TABLE CREATION, #######################
###############################      INGREDIENTS, METHOD AND STATS            #########################

class CreateQuery():
    
    recipe_query = """ INSERT INTO Recipe (`RecipeTitle`, 
                                        `RecipeDescription`, 
                                        `CookingTimeMins`, 
                                        `MakePublic`, 
                                        `UserId`) 
                    VALUES (%s, %s, %s, %s, %s); """

    ingredients_query = """ INSERT INTO Ingredient (`IngredientName`, `UserId`, `RecipeId`, `Quantity`)
                    VALUES (%s, %s, %s, %s); """
    
    method_query = """ INSERT INTO Method (`StepNumber`, `StepDescription`, `RecipeId`)
                    VALUES (%s, %s, %s); """

    rate_query = """ INSERT INTO Rating (`Rating`, `Comments`, `RecipeId`, `UserId`)
                    VALUES (%s, %s, %s, %s); """

    def two_column_query(self, table, column, column_value, recipe_id):
        query = """ INSERT INTO %s (`%s`, `RecipeId`)
                    VALUES ('%s', %s); """ % (table, column, column_value, recipe_id)
        return query

###################### CLASS TO EXECUTE THE SQL QUERY FOR RECIPE TABLE, AND STATS #########################

class QueryCreateRecipe():

    def __init__(self,recipe, user_id):
        self.recipe_title = recipe['RecipeTitle']
        self.recipe_description = recipe['RecipeDescription']
        self.cooking_time = int(recipe['CookingTimeMins'])
        self.make_public = int(recipe['MakePublic'])
        self.user_id = int(user_id['UserId'])
        self.cuisine_name = capitalize_words(recipe['CuisineName'])
        self.course_name = capitalize_words(recipe['CourseName'])
        self.calories = int(recipe['Calories'])
        self.cost = int(recipe['Cost'])
        self.servings = int(recipe['Servings'])
        
 
    def create_recipe(self):
        recipe_values = (self.recipe_title, self.recipe_description,
                                self.cooking_time, self.make_public,self.user_id) 
                                       
        try:
            with Db(commit=True) as cursor:
                cursor.execute(CreateQuery.recipe_query, recipe_values)
                recipe_primary_key = cursor.lastrowid
        except pymysql.err.OperationalError as e:
            message = " FAILED: create_recipe method in db_create.QueryCreateRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("create_recipe completed")
           
    def create_stats(self, recipe_primary_key):
        stat_queries = [[CreateQuery.two_column_query(self,'Cuisine','CuisineName', 
                                                        self.cuisine_name, recipe_primary_key)],
                        [CreateQuery.two_column_query(self,'Course','CourseName', 
                                                        self.course_name, recipe_primary_key)],
                        [CreateQuery.two_column_query(self,'Health','Calories', 
                                                        self.calories, recipe_primary_key)],
                        [CreateQuery.two_column_query(self,'Cost','Price', 
                                                        self.cost, recipe_primary_key)],
                        [CreateQuery.two_column_query(self,'Servings','Servings', 
                                                        self.servings, recipe_primary_key)]]
        try:
            with Db(commit=True) as cursor:
                for stat in stat_queries:
                    cursor.execute(stat[0])
        except pymysql.err.OperationalError as e:
            message = " FAILED: create_stats method in db_create.QueryCreateRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("create_stats completed")

###################### CLASS TO EXECUTE THE SQL QUERY FOR METHOD, #########################
###########################       AND INGREDIENTS          ################################

class QueryCreateMethodItems():
    
    def __init__(self, prepped_ingredients, prepped_method):
        self.ingredients = prepped_ingredients
        self.method = prepped_method

    def create_ingredients_and_method(self):
        try:
            with Db(commit=True) as cursor:
                cursor.executemany(CreateQuery.ingredients_query, self.ingredients)
                cursor.executemany(CreateQuery.method_query,self.method)
        except pymysql.err.OperationalError as e:
            message = """ FAILED: create_ingredients_and_method 
                                method in db_create.QueryCreateMethodItems."""
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("create_ingredients_and_method completed")
class QuerySaveRecipe():
    
    def __init__(self, user_id, recipe_id):
        self.user_id = user_id
        self.recipe_id = recipe_id

    def save_recipe(self):
        save_recipe = CreateQuery.two_column_query(self,'SavedRecipes','UserId', 
                                                        self.user_id, self.recipe_id)
        try:
            with Db(commit=True) as cursor:
                cursor.execute(save_recipe)
                print(save_recipe)
        except pymysql.err.OperationalError as e:
            message = """ FAILED: save_recipe 
                                method in db_create.QuerySaveRecipe."""
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("save_recipe completed")

class QueryRateRecipe(QuerySaveRecipe):
    
    def __init__(self,rating, comments, recipe_id, user_id):
        super().__init__(user_id, recipe_id)
        self.rating = rating
        self.comments = comments
        

    def rate_recipe(self):
        rating = (self.rating, self.comments, self.recipe_id, self.user_id)
        
        try:
            with Db(commit=True) as cursor:
                cursor.execute(CreateQuery.rate_query, rating)
                print(rating)
        except pymysql.err.OperationalError as e:
            message = """ FAILED: rate_recipe 
                                method in db_create.QuerySaveRecipe."""
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("rate_recipe completed")

        
        
        
