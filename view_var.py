#import find_recipe
import write_recipe
from find_recipe import Get
from db_update_delete import QueryDeleteRecipe
from db_read import QueryReadRecipes, QueryAllData, TotalCuisinesCourses, QueryRating

############## CLASS TO RETURN VARIABLES FOR VIEW FUNCTIONS, CALLED FROM WITHIN VIEW FUNCTIONS ##################

class ViewVariables():
    
    def __init__(self, username):
        self.username = username
        
#---------------- GET PUBLIC RECIPE CATEGORY GROUPINGS ----------------##

    def public_recipe_groupings(self):
        make_public = 1
        for_user = False
        public = Get().get_cuisine_and_course_count(make_public, for_user)
        return public

    def user_recipe_groupings(self):
        user_id = Get().get_user_id(self.username)['UserId']
        for_user = True
        user = Get().get_cuisine_and_course_count(user_id, for_user)
        return user
        
##---------------- GET CATEGORY GROUPINGS OF COURSE AND CUISINE FOR MY_RECIPME PAGE ---------------- ##

    def groupings(self):
        public = ViewVariables(self.username).public_recipe_groupings()
        user = ViewVariables(self.username).user_recipe_groupings()
        return user, public

##---------------- RETURN ALL RECIPES FOR GIVEN USER, COUNT AND CATEGORIES---------------- ##

    def var_all_myrecipme(self, order_by, direction):
        user_id = Get().get_user_id(self.username)
        result = QueryReadRecipes().query_all_mini_recipes('User.UserId', user_id['UserId'], 
                                                            order_by, direction)       
        recipes = Get().date_time_converter(result)
        count = len(recipes)
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings

##---------------- RETURN ALL RECIPES FOR GIVEN INGREDIENT SEARCH ---------------- ##

    def var_ing_search(self, search_by, search_value, ingredient, order_by, direction):
        recipes = []
        count = 0
        result = QueryReadRecipes().query_search_ingredient(search_by, search_value, 
                                                            ingredient, order_by, direction)
        if result == []:
            count = 0
        else:
            recipes = Get().date_time_converter(result)
            count = len(recipes)
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings

##---------------- RETURN ALL RECIPES FOR CHOSEN CUISINE OR COURSE CATEGORY ----------------#
##------------------------- PUBLIC OR USER SPECIFIC ----------------##

    def var_cat_search(self, table, search_by, search_value, 
                            column, category, order_by, direction):
        query = QueryReadRecipes()
        results = query.query_category_mini_recipes(table, search_by, search_value, 
                                                    column, category, order_by, direction)
        recipes = Get().date_time_converter(results)
        count = len((recipes))
        groupings = ViewVariables(self.username).groupings()
    
        return recipes, count, groupings#, form[column[0]], column[0], 

##---------------- RETURN FULL RECIPE VIEW FOR CHOSEN RECIPE ----------------##

    def var_full_recipe(self, recipe_id):
        username = [{'Username':self.username}]
        result = QueryReadRecipes().query_all_mini_recipes('Recipe.RecipeId', recipe_id, 
                                                            'RecipeTitle', 'asc')
        recipe = Get().date_time_converter(result)
        ingredients = QueryReadRecipes().query_ingredients_for_full_recipe(recipe_id)
        method = QueryReadRecipes().query_method_for_full_recipe(recipe_id)
        user_id = Get().get_user_id(username[0]['Username'])['UserId']
        is_saved = Get().get_is_recipe_saved(user_id, recipe_id)
        ratings = QueryRating(recipe_id).query_rating_and_comments()
        #average = Get().get_average_rating(ratings)

        return username, recipe, ingredients, method, is_saved, ratings#, average

##---------------- RETURN ALL PUBLIC RECIPES ----------------##

    def var_all_public(self, order_by, direction):
        result = QueryReadRecipes().query_all_mini_recipes('MakePublic', 1, 
                                                            order_by, direction)
        recipes = Get().date_time_converter(result)
        count = len(recipes)
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings

##---------------- RETURN ALL SAVED RECIPES FOR GIVEN USER ----------------##

    def var_saved_recipes(self, user_id, order_by, direction):
        result = QueryReadRecipes().query_users_saved_recipes(user_id, 
                                                                order_by, direction)
        recipes = Get().date_time_converter(result)
        count = len(recipes)
        groupings = ViewVariables(self.username).groupings()
        ### INSERT RECIPE AUTHOR INTO RECIPE DICT ##
        for recipe in recipes:
            author = QueryReadRecipes().query_username_or_id('Username', 'UserId', 
                                                                int(recipe['UserId']))
            recipe['Author'] = author[0]['Username']
        return recipes, count, groupings
        
    
################## CLASS HOLDING FUNCTIONS CALLED FROM VIEWS THAT DON'T RETURN VARIABLES ################

class ViewFunc():

##---------------- SAVE OR DELETE RECIPE FROM SAVED RECIPE TABLE ----------------##

    def save_or_unsave_recipe(self, saved, username, recipe_id):
        user_id = Get().get_user_id(username)['UserId']
        if saved == 1:
            write_recipe.Create().write_saved_recipe(user_id, recipe_id)
        elif saved == 0:
            QueryDeleteRecipe(recipe_id, 'SavedRecipes').delete_saved_recipe(user_id)

        return True

##---------------- WRITE RECIPE RATING AND COMMENTS TO RATINGS TABLE ----------------##  

    def rate_recipe(self, form, recipe_id, username):
        rating, comments = form['Rating'], form['Comments']
        user_id = Get().get_user_id(username)['UserId']
        write_recipe.Create().write_rating(rating, comments, recipe_id, user_id)
        
        return True

################## CLASS RETURNING STATS FOR AJAX ################

class Totals():
    
    def get_all_totals(self):
        recipes = Get().get_total_recipes()
        public = Get().get_total_public()
        users = Get().get_total_users()
        cuisines_courses = Get().get_cuisines_courses()
        totals = [recipes[0], public[0], users[0], cuisines_courses]
       
        return totals

    def get_percentage_shared(self, stats):
        total_recipes = int(stats[0]['TotalRecipe'])
        total_shared = int(stats[1]['PublicRecipe'])
        percentage_shared = int((total_shared/total_recipes) * 100)

        return percentage_shared
    

    

    