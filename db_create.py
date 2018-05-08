import os
#import pymysql
import myenviron
from db import db

class query_create_user(db):
    
    def __init__(self, user_values):
        self.username = user_values['Username'].lower()
        self.first = user_values['First'].lower()
        self.last = user_values['Last'].lower()
        self.password = user_values['Password']
       

    def create_user(self):
        query = """INSERT INTO User (`Username`,`First`,`Last`,`Password` ) VALUES (%s, %s, %s, %s);"""
        try:
            with db(commit=True) as cursor:
                cursor.execute(query, (self.username, self.first, self.last, self.password))
                #db.connection.commit()
        finally: 
            print('New User Created')

class create_query(db):
    
    recipe_query = """ INSERT INTO Recipe (`RecipeTitle`, 
                                        `RecipeDescription`, 
                                        `CookingTimeMins`, 
                                        `MakePublic`, 
                                        `UserId`) 
                    VALUES (%s, %s, %s, %s, %s); """

    
    cuisine_query = """ INSERT INTO Cuisine (`CuisineName`, `RecipeId`) 
                    VALUES (%s, %s); """

    course_query = """ INSERT INTO Course (`CourseName`, `RecipeId`) 
                    VALUES (%s, %s); """
    
    calories_query = """ INSERT INTO Health (`Calories`, `RecipeId`) 
                    VALUES (%s, %s); """

    cost_query = """ INSERT INTO Cost (`Price`, `RecipeId`) 
                    VALUES (%s, %s); """

    servings_query = """ INSERT INTO Servings (`Servings`, `RecipeId`) 
                    VALUES (%s, %s); """

    ingredients_query = """ INSERT INTO Ingredient (`IngredientName`, `UserId`, `RecipeId`, `Quantity`)
                    VALUES (%s, %s, %s, %s); """
    
    method_query = """ INSERT INTO Method (`StepNumber`, `StepDescription`, `RecipeId`)
                    VALUES (%s, %s, %s); """



class query_create_recipes(db):

    def __init__(self,recipe, user_id):
        self.recipe_title = recipe['RecipeTitle']
        self.recipe_description = recipe['RecipeDescription']
        self.cooking_time = int(recipe['CookingTimeMins'])
        self.make_public = int(recipe['MakePublic'])
        self.user_id = int(user_id['UserId'])
        self.cuisine_name = recipe['CuisineName']
        self.course_name = recipe['CourseName']
        self.calories = int(recipe['Calories'])
        self.cost = int(recipe['Cost'])
        self.servings = int(recipe['Servings'])
        

    def create_recipe(self):
        recipe_values = (self.recipe_title, self.recipe_description,
                                self.cooking_time, self.make_public,self.user_id) 
                                       
        try:
            with db(commit=True) as cursor:
                print(recipe_values)
                cursor.execute(create_query.recipe_query, recipe_values)
                recipe_primary_key = cursor.lastrowid
        finally:
            print("Query create recipe completed")
            return recipe_primary_key
           
    def create_stats(self, recipe_primary_key):
        stat_queries = [[create_query.cuisine_query,(self.cuisine_name, recipe_primary_key)],
                        [create_query.course_query,(self.course_name, recipe_primary_key)],
                        [create_query.calories_query,(self.calories, recipe_primary_key)],
                        [create_query.cost_query,(self.cost, recipe_primary_key)],
                        [create_query.servings_query,(self.servings, recipe_primary_key)]]
        try:
            with db(commit=True) as cursor:
                for stat in stat_queries:
                    cursor.execute(stat[0], stat[1])
                #db().connection.commit()
        finally:
            print("Query create recipe completed")
    

class query_create_method_items(db):
    
    def __init__(self, prepped_ingredients, prepped_method):
        self.ingredients = prepped_ingredients
        self.method = prepped_method
        #self.step_number = prepped_items[1]
        #self.step = prepped_items[2]

    def create_ingredients_and_method(self):
        try:
            with db(commit=True) as cursor:
                cursor.executemany(create_query.ingredients_query, self.ingredients)
                cursor.executemany(create_query.method_query,self.method)
        finally:
            print("Query create recipe completed")
        
