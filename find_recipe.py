import os
import pymysql
import unittest
import db_read
import write_recipe
import datetime
import json
from db_read import query_read_recipes
  
#### TO COME FROM FORM ###
# #
"""
user_values = ["darchard"]
search_by = 'Recipe.MakePublic' ## MakePublic, UserId ##
direction = 'ASC'
order_by = 'Calories'
course = "Lunch"
cuisine = "British"
recipe_id = 1
ingredient = 'Butter'
"""
###########################

########################## DATE TIME CONVERSION ###############################
""""""""""""""""""""""""""""""""""""
"""WRITE A TEST FOR THIS FUNCTION"""
""""""""""""""""""""""""""""""""""""
def date_time_converter(recipes):
   # print(recipes)
    
    
    for i in recipes:
        print(i['Created'])
        i['Created'] = i['Created'].strftime('%H:%M:%S on %m.%d.%Y')
        print(i['Created'])
        
        #recipe['Created'] = recipe['Created'].strftime('%H:%M:%S on %m.%d.%Y')
        #recipe = k.strftime('%H:%M:%S on %m.%d.%Y')
        #print(recipes)
    return recipes
"""
def datetime_converter(my_recipme):
    print('here')
    if isinstance(my_recipme, datetime.datetime):
       
        return my_recipme.strftime('%m/%d/%Y')

def convert_to_json(data):
  
    data_to_json = json.dumps(data, default = datetime_converter)
    return data_to_json
""" 
############################################################################
    
def get_all_mini_recipes(search_by, search_value, order_by, direction):
    """ GET ALL MINI RECIPES THAT ARE DECLARED PUBLIC """ 
    query_recipe = db_read.query_read_recipes()
    recipe = query_recipe.query_all_mini_recipes(search_by, search_value, order_by, direction)
    #print(recipe)
    return recipe


def get_mini_user_recipes(user_values, search_by, order_by, direction):
    """ GET MINI RECIPES FOR DISPLAY ON USERS OWN FEED ONLY """
    user_id = write_recipe.get_user_id(user_values)
    query_recipe = db_read.query_read_recipes()
    recipe = query_recipe.query_all_mini_recipes(search_by, user_id['UserId'], order_by, direction)
    #print(user_id)
    return recipe


def get_ingredients_for_full_recipe(recipe_id):
    """ GETS ALL THE INGREDIENTS FOR DISPLAY ON THE FULL RECIPE PAGE"""
    query_recipe = db_read.query_read_recipes()
    ingredients = query_recipe.query_ingredients_for_full_recipe(recipe_id)
    #print(ingredients)
    return ingredients

def get_method_for_full_recipe(recipe_id):
    """ GETS THE METHOD FOR DISPLAY ON THE FULL RECIPE PAGE """
    query_recipe = db_read.query_read_recipes()
    method = query_recipe.query_method_for_full_recipe(recipe_id)
    #print(method)
    return method

def get_category_mini_recipes(table, search_by, search_value, column, category, order_by, direction):
    """ GETS A FILTERED SET OF RECIPES SET BY CUISINE AND COURSE """
    query_recipe = db_read.query_read_recipes()
    category_recipes = query_recipe.query_category_mini_recipes(table, search_by, search_value, column, category, order_by, direction)
    #print(category_recipes)
    return category_recipes

def get_recipes_by_ingredient(search_by, search_value, ingredient, order_by, direction):
    """ GETS A SET OF RECIPES FILTERED BY AN INGREDIENTS SEARCH """
    query_recipe = db_read.query_read_recipes()
    search_recipe = query_recipe.query_search_ingredient(search_by, search_value, ingredient, order_by, direction)
    #print(search_recipe)
    return search_recipe

def get_saved_recipes_for_user(user_id, order_by, direction):
    """ GET ALL THE SAVED RECIPES FOR A GIVEN USER """
    query_recipe = db_read.query_read_recipes()
    saved_recipes = query_recipe.query_users_saved_recipes(user_id, order_by, direction)
   # print(saved_recipes)
    return saved_recipes

""" WRITE TEST FOR THIS FUNCTION """
def get_all_column_group_for_user(column, user_id, table):
    column_query = query_read_recipes()
    cuisines = column_query.query_count_and_group_column(column, user_id['UserId'], table)
    return cuisines

def get_cuisine_and_course_count(user_id):
    cuisines = get_all_column_group_for_user('CuisineName', user_id, 'Cuisine')
    courses = get_all_column_group_for_user('CourseName', user_id, 'Course')
    return cuisines, courses

"""
def get_all_courses_for_cuisine(user_id, cuisine):
    course_query = query_read_recipes()
    courses = course_query.query_count_and_group_courses(user_id, cuisine)
    return courses
"""


##get_user_id(user_values)
#get_mini_recipe_for_user(user_values)
#get_all_mini_recipes(search_by, recipe_id, order_by, direction)
#get_mini_user_recipes(user_values, search_by, order_by, direction)
#get_method_for_full_recipe(recipe_id)
#get_ingredients_for_full_recipe(recipe_id)
#get_filtered_mini_recipes(search_by, 1, course, cuisine, order_by, direction)
#get_recipes_by_ingredient(search_by,1, ingredient, order_by, direction)
#get_saved_recipes_for_user(11, order_by, direction)
