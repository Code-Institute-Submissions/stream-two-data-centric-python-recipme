import find_recipe
import write_recipe
from db_update_delete import QueryDeleteRecipe

############## CLASS TO RETURN VARIABLES FOR VIEW FUNCTIONS, CALLED FROM WITHIN VIEW FUNCTIONS ##################

class ViewVariables():
    
    def __init__(self, username):
        self.username = username
        
## GET PUBLIC RECIPE CATEGORY GROUPINGS s##
    def public_recipe_groupings(self):
        make_public = 1
        for_user = False
        public = find_recipe.Get().get_cuisine_and_course_count(make_public, for_user)
        return public

    def user_recipe_groupings(self):
        user_id = find_recipe.Get().get_user_id(self.username)['UserId']
        for_user = True
        user = find_recipe.Get().get_cuisine_and_course_count(user_id, for_user)
        return user
        
## GET CATEGORY GROUPINGS OF COURSE AND CUISINE FOR MY_RECIPME PAGE ##
    def groupings(self):
        public = ViewVariables(self.username).public_recipe_groupings()
        user = ViewVariables(self.username).user_recipe_groupings()
        return user, public

## RETURN ALL RECIPES FOR GIVEN USER, COUNT AND CATEGORIES AGAIN ##
    def var_all_myrecipme(self, order_by, direction):
        result = find_recipe.Get().get_mini_user_recipes(self.username, 'User.UserId', order_by, direction)        
        recipes = find_recipe.Get().date_time_converter(result)
        count = len(recipes)
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings

## RETURN ALL RECIPES FOR GIVEN INGREDIENT SEARCH ##
    def var_ing_search(self, form, search_by, search_value, ingredient):
        recipes = []
        count = 0
        order_by, direction = form['SortBy'], form['Direction']
        result = find_recipe.Get().get_recipes_by_ingredient(search_by, search_value, 
                                                        ingredient, order_by, direction)
        if result == []:
            count = 0
        else:
            recipes = find_recipe.Get().date_time_converter(result)
            count = len(recipes)
        groupings = ViewVariables(self.username).groupings()
        print(search_by)
        return recipes, count, groupings

## RETURN ALL RECIPES FOR CHOSEN CUISINE OR COURSE CATEGORY, PUBLIC OR USER SPECIFIC ##
    def var_cat_search(self, form, search_by, search_value):
        order_by, direction = form['SortBy'], form['Direction']
        #user_id = find_recipe.Get().get_user_id(self.username)['UserId']
        column = [key for key in form]
        column_name = column[0] + 'Name'
        results = find_recipe.Get().get_category_mini_recipes(column[0], search_by, search_value, 
                                                        column_name, form[column[0]], 
                                                        order_by, direction)
        recipes = find_recipe.Get().date_time_converter(results)
        count = len((recipes))
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings, form[column[0]], column[0]

## RETURN FULL RECIPE VIEW FOR CHOSEN RECIPE ##
    def var_full_recipe(self, recipe_id):
        username = [{'Username':self.username}]
        result = find_recipe.Get().get_all_mini_recipes('Recipe.RecipeId', recipe_id, 
                                                       'RecipeTitle', 'asc')
        recipe = find_recipe.Get().date_time_converter(result)
        ingredients = find_recipe.Get().get_ingredients_for_full_recipe(recipe_id)
        method = find_recipe.Get().get_method_for_full_recipe(recipe_id)
        user_id = find_recipe.Get().get_user_id(username[0]['Username'])['UserId']
        print(username[0]['Username'])
        is_saved = find_recipe.Get().get_is_recipe_saved(user_id, recipe_id)

        return username, recipe, ingredients, method, is_saved


## RETURN ALL PUBLIC RECIPES ##

    def var_all_public(self, order_by, direction):
        result = find_recipe.Get().get_all_mini_recipes('MakePublic', 1, order_by, direction)
        recipes = find_recipe.Get().date_time_converter(result)
        count = len(recipes)
        groupings = ViewVariables(self.username).groupings()

        return recipes, count, groupings
    
class ViewFunc():

    def save_or_unsave_recipe(self, saved, username, recipe_id):
        user_id = find_recipe.Get().get_user_id(username)['UserId']
        if saved == 1:
            write_recipe.Create().write_saved_recipe(user_id, recipe_id)
        elif saved == 0:
            QueryDeleteRecipe(recipe_id, 'SavedRecipes').delete_saved_recipe(user_id)

        return True