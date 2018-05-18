import os
import pymysql
import db_read
import write_recipe
import datetime
from db_read import QueryReadRecipes

############# CLASSES WITH LOGIC TO RETRIEVE DATA FROM THE DB #################

class Get():
    def date_time_converter(self, recipes):
        """ CONVERT DATETIME TO STRING """
        for i in recipes:
            i['Created'] = i['Created'].strftime('%H:%M:%S on %m.%d.%Y')
        return recipes

    def get_user_id(self, username):
        """ GET USER ID FROM USERNAME """
        user = QueryReadRecipes().query_user_id(username)
        user_id = user[0]
        return user_id
        
    def get_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET MINI RECIPES BY RECIPE ID OR PUBLIC """ 
        recipe = QueryReadRecipes().query_all_mini_recipes(search_by, search_value, order_by, direction)
        #print(recipe)
        return recipe

    def get_mini_user_recipes(self, user_values, search_by, order_by, direction):
        """ GET MINI RECIPES FOR DISPLAY ON USERS OWN FEED ONLY """
        user_id = Get.get_user_id(self, user_values)
        recipe = QueryReadRecipes().query_all_mini_recipes(search_by, user_id['UserId'], order_by, direction)
        #print(user_id)
        return recipe


    def get_ingredients_for_full_recipe(self, recipe_id):
        """ GETS ALL THE INGREDIENTS FOR DISPLAY ON THE FULL RECIPE PAGE"""
        ingredients = QueryReadRecipes().query_ingredients_for_full_recipe(recipe_id)
        #print(ingredients)
        return ingredients

    def get_method_for_full_recipe(self, recipe_id):
        """ GETS THE METHOD FOR DISPLAY ON THE FULL RECIPE PAGE """
        method = QueryReadRecipes().query_method_for_full_recipe(recipe_id)
        #print(method)
        return method

    def get_category_mini_recipes(self, table, search_by, search_value, column, category, order_by, direction):
        """ GETS A FILTERED SET OF RECIPES SET BY CUISINE AND COURSE """
        category_recipes = QueryReadRecipes().query_category_mini_recipes(table, search_by, search_value, column, category, order_by, direction)
        #print(category_recipes)
        return category_recipes

    def get_recipes_by_ingredient(self, search_by, search_value, ingredient, order_by, direction):
        """ GETS A SET OF RECIPES FILTERED BY AN INGREDIENTS SEARCH """
        search_recipe = QueryReadRecipes().query_search_ingredient(search_by, search_value, ingredient, order_by, direction)
        #print(search_recipe)
        return search_recipe

    def get_saved_recipes_for_user(self, user_id, order_by, direction):
        """ GET ALL THE SAVED RECIPES FOR A GIVEN USER """
        saved_recipes = QueryReadRecipes().query_users_saved_recipes(user_id, order_by, direction)
    # print(saved_recipes)
        return saved_recipes

    def get_is_recipe_saved(self, user_id, recipe_id):
        """ CHECKS TO SEE IF A RECIPE IS ALREADY SAVED BY USER """
        is_recipe_saved = QueryReadRecipes().query_is_recipe_saved(user_id, recipe_id)
        print(is_recipe_saved)
        if is_recipe_saved != []:
            return True
        else:
            return False
        
    def get_all_column_group(self, column, value, table, for_user):
        column_query = QueryReadRecipes()
        if for_user == True:
            column = QueryReadRecipes().query_count_and_group_column(column, value, table)
        else:
            column = QueryReadRecipes().query_count_and_group_column_public(column, value, table)
        return column

    def get_cuisine_and_course_count(self, value, for_user):
        cuisines = Get.get_all_column_group(self, 'CuisineName', value, 'Cuisine',for_user)
        courses = Get.get_all_column_group(self, 'CourseName', value, 'Course', for_user)
        return cuisines, courses



