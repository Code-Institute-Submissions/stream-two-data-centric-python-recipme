import os
import pymysql
import write_recipe
import datetime
from db_read import QueryReadRecipes, QueryRating, QueryAllData, TotalCuisinesCourses

############# CLASSES WITH LOGIC TO RETRIEVE DATA FROM THE DB #################

class Get():
    
    def date_time_converter(self, recipes):
        """ CONVERT DATETIME TO STRING """
        for i in recipes:
            i['Created'] = i['Created'].strftime('%H:%M:%S on %m.%d.%Y')
        return recipes

    def get_user_id(self, username):
        """ GET USER ID FROM USERNAME """
        user = QueryReadRecipes().query_username_or_id('UserId', 'Username', username)
        user_id = user[0]
        return user_id

    def get_method_for_full_recipe(self, recipe_id):
        """ GETS THE METHOD FOR DISPLAY ON THE FULL RECIPE PAGE """
        method = QueryReadRecipes().query_method_for_full_recipe(recipe_id)
       
        return method

    def get_saved_recipes_for_user(self, user_id, order_by, direction):
        """ GET ALL THE SAVED RECIPES FOR A GIVEN USER """
        saved_recipes = QueryReadRecipes().query_users_saved_recipes(user_id, order_by, direction)

        return saved_recipes

    def get_is_recipe_saved(self, user_id, recipe_id):
        """ CHECKS TO SEE IF A RECIPE IS ALREADY SAVED BY USER """
        is_recipe_saved = QueryReadRecipes().query_is_recipe_saved(user_id, recipe_id)
        if is_recipe_saved != []:
            return True
        else:
            return False
        
    def get_all_column_group(self, column, value, table, for_user):
        """ GET GROUP RESULTS FOR SPECIFIC COLUMN, FOR USER OR FOR PUBLIC RECIPES """
        if for_user == True:
            column = QueryReadRecipes().query_count_and_group_column(column, value, table)
        else:
            column = QueryReadRecipes().query_count_and_group_column_public(column, value, table)

        return column

    def get_cuisine_and_course_count(self, value, for_user):
        """ RETURN GROUPED CUISINE AND COURSE RESULTS"""
        cuisines = Get.get_all_column_group(self, 'CuisineName', value, 'Cuisine',for_user)
        courses = Get.get_all_column_group(self, 'CourseName', value, 'Course', for_user)
        
        return cuisines, courses
  
    def get_average_rating(self, all_rating):
        """ GET AVAERAGE RATING FOR SPECIFIC RECIPE """ 
        total = 0
        if all_rating != []:
            for rating in all_rating:
                total = total + rating['Rating']
            average = {'Average': int(total/len(all_rating))}
        else:
            average = {'Average': 0}
    
        return average
      
#------------------ FOR PAGINATION ----------------------------#

    def get_results(self, results, offset=0, per_page=10):
      
        return results[offset: offset + per_page]

#--------------------------------------------------------------#
#------------------ FOR INDEX PAGE DATA DISPLAY ---------------#

    def get_total_recipes(self):
        total_recipes = QueryAllData('Recipe', 'RecipeTitle').get_total()
        
        return total_recipes

    def get_total_public(self):
        total_public = QueryAllData('Recipe', 'RecipeTitle').get_total_public()

        return total_public

    def get_total_users(self):
        total_users = QueryAllData('User', 'Username').get_total()

        return total_users

    def get_cuisines_courses(self):
        cuisines_courses = TotalCuisinesCourses().get_all_cuisines_and_courses()

        return cuisines_courses

