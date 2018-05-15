import find_recipe
import write_recipe

############## CLASS TO RETURN VARIABLES FOR VIEW FUNCTIONS, CALLED FROM WITHIN VIEW FUNCTIONS ##################

class ViewVariables():
    
    def __init__(self, username):
        self.username = username

## GET CATEGORY GROUPINGS OF COURSE AND CUISINE FOR MY_RECIPME PAGE ##
    def var_myrecipme(self):
        user_id = find_recipe.Get().get_user_id(self.username)
        categories = find_recipe.Get().get_cuisine_and_course_count(user_id)
        return categories

## RETURN ALL RECIPES FOR GIVEN USER, COUNT AND CATEGORIES AGAIN ##
    def var_all_myrecipme(self, order_by, direction):
        user_id = find_recipe.Get().get_user_id(self.username)
        result = find_recipe.Get().get_mini_user_recipes(self.username, 'User.UserId', order_by, direction)        
        recipes = find_recipe.Get().date_time_converter(result)
        count = len(recipes)
        categories = find_recipe.Get().get_cuisine_and_course_count(user_id)
        return recipes, count, categories

## RETURN ALL RECIPES FOR GIVEN INGREDIENT SEARCH ##
    def var_ing_search(self, ingredient, order_by, direction):
        recipes = []
        count = 0
        user_id = find_recipe.Get().get_user_id(self.username)
        result = find_recipe.Get().get_recipes_by_ingredient('User.UserId', user_id['UserId'], 
                                                        ingredient, order_by, direction)
        if result == []:
            count = 0
        else:
            recipes = find_recipe.Get().date_time_converter(result)
            count = len(recipes)
        categories = find_recipe.Get().get_cuisine_and_course_count(user_id)
        return recipes, count, categories

## RETURN ALL RECIPES FOR CHOSEN CUISINE OR COURSE CATEGORY ##
    def var_cat_search(self, form):
        order_by, direction = form['SortBy'], form['Direction']
        user_id = find_recipe.Get().get_user_id(self.username)
        column = [key for key in form]
        column_name = column[0] + 'Name'
        results = find_recipe.Get().get_category_mini_recipes(column[0], 'User.UserId', user_id['UserId'], 
                                                        column_name, form[column[0]], 
                                                        order_by, direction)
        recipes = find_recipe.Get().date_time_converter(results)
        count = len((recipes))
        categories = find_recipe.Get().get_cuisine_and_course_count(user_id)
       
        return recipes, count, categories, form[column[0]], column[0]

## RETURN FULL RECIPE VIEW FOR CHOSEN RECIPE ##
    def var_full_recipe(self, recipe_id):
        username = [{'Username':self.username}]
        result = find_recipe.Get().get_all_mini_recipes('Recipe.RecipeId', recipe_id, 
                                                       'RecipeTitle', 'asc')
        recipe = find_recipe.Get().date_time_converter(result)
        ingredients = find_recipe.Get().get_ingredients_for_full_recipe(recipe_id)
        method = find_recipe.Get().get_method_for_full_recipe(recipe_id)
        return username, recipe, ingredients, method

    
        

