import os
import pymysql
import db_read
import write_recipe
import datetime
from db_read import query_read_recipes

########################## DATE TIME CONVERSION ###############################

class get():
    def date_time_converter(self, recipes):
        """ CONVERT DATETIME TO STRING """
        for i in recipes:
            i['Created'] = i['Created'].strftime('%H:%M:%S on %m.%d.%Y')
        return recipes

    ############################################################################

    def get_user_id(self, username):
        """ GET USER ID FROM USERNAME """
        new_read_query = query_read_recipes()
        user = new_read_query.query_user_id(username)
        user_id = user[0]
        return user_id
        
    def get_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET MINI RECIPES BY RECIPE ID OR PUBLIC """ 
        query_recipe = db_read.query_read_recipes()
        recipe = query_recipe.query_all_mini_recipes(search_by, search_value, order_by, direction)
        #print(recipe)
        return recipe

    def get_mini_user_recipes(self, user_values, search_by, order_by, direction):
        """ GET MINI RECIPES FOR DISPLAY ON USERS OWN FEED ONLY """
        user_id = get.get_user_id(self, user_values)
        query_recipe = db_read.query_read_recipes()
        recipe = query_recipe.query_all_mini_recipes(search_by, user_id['UserId'], order_by, direction)
        #print(user_id)
        return recipe


    def get_ingredients_for_full_recipe(self, recipe_id):
        """ GETS ALL THE INGREDIENTS FOR DISPLAY ON THE FULL RECIPE PAGE"""
        query_recipe = db_read.query_read_recipes()
        ingredients = query_recipe.query_ingredients_for_full_recipe(recipe_id)
        #print(ingredients)
        return ingredients

    def get_method_for_full_recipe(self, recipe_id):
        """ GETS THE METHOD FOR DISPLAY ON THE FULL RECIPE PAGE """
        query_recipe = db_read.query_read_recipes()
        method = query_recipe.query_method_for_full_recipe(recipe_id)
        #print(method)
        return method

    def get_category_mini_recipes(self, table, search_by, search_value, column, category, order_by, direction):
        """ GETS A FILTERED SET OF RECIPES SET BY CUISINE AND COURSE """
        query_recipe = db_read.query_read_recipes()
        category_recipes = query_recipe.query_category_mini_recipes(table, search_by, search_value, column, category, order_by, direction)
        #print(category_recipes)
        return category_recipes

    def get_recipes_by_ingredient(self, search_by, search_value, ingredient, order_by, direction):
        """ GETS A SET OF RECIPES FILTERED BY AN INGREDIENTS SEARCH """
        query_recipe = db_read.query_read_recipes()
        search_recipe = query_recipe.query_search_ingredient(search_by, search_value, ingredient, order_by, direction)
        #print(search_recipe)
        return search_recipe

    def get_saved_recipes_for_user(self, user_id, order_by, direction):
        """ GET ALL THE SAVED RECIPES FOR A GIVEN USER """
        query_recipe = db_read.query_read_recipes()
        saved_recipes = query_recipe.query_users_saved_recipes(user_id, order_by, direction)
    # print(saved_recipes)
        return saved_recipes

    def get_all_column_group_for_user(self, column, user_id, table):
        column_query = query_read_recipes()
        column = column_query.query_count_and_group_column(column, user_id['UserId'], table)
        return column

    def get_cuisine_and_course_count(self, user_id):
        cuisines = get.get_all_column_group_for_user(self, 'CuisineName', user_id, 'Cuisine')
        courses = get.get_all_column_group_for_user(self, 'CourseName', user_id, 'Course')
        return cuisines, courses

    ################################# CLASS VARIABLES FOR EACH VIEW ####################################

