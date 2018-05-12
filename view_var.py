import find_recipe
import write_recipe


class view_var():
    
    def __init__(self, username):
        self.username = username

    def var_myrecipme(self):
        user_id = find_recipe.get_user_id(self.username)
        categories = find_recipe.get_cuisine_and_course_count(user_id)
        return categories

    def var_all_myrecipme(self):
        user_id = find_recipe.get_user_id(self.username)
        result = find_recipe.get_mini_user_recipes(self.username, 'User.UserId', 'RecipeTitle', 'asc' )        
        recipes = find_recipe.date_time_converter(result)
        count = len(recipes)
        categories = find_recipe.get_cuisine_and_course_count(user_id)
        return recipes, count, categories

    def var_ing_search(self, ingredient):
        recipes = []
        count = 0
        user_id = find_recipe.get_user_id(self.username)
        result = find_recipe.get_recipes_by_ingredient('User.UserId', user_id['UserId'], 
                                                        ingredient, 'RecipeTitle', 'asc')
        if result == []:
            count = 0
        else:
            recipes = find_recipe.date_time_converter(result)
            count = len(recipes)
        categories = find_recipe.get_cuisine_and_course_count(user_id)
        return recipes, count, categories

    def var_cat_search(self, form):
        user_id = find_recipe.get_user_id(self.username)
        column = [key for key in form]
        column_name = column[0] + 'Name'
        results = find_recipe.get_category_mini_recipes(column[0], 'User.UserId', user_id['UserId'], 
                                                        column_name, form[column[0]], 
                                                        'RecipeTitle', 'asc')
        recipes = find_recipe.date_time_converter(results)
        count = len((recipes))
        categories = find_recipe.get_cuisine_and_course_count(user_id)
        return recipes, count, categories, form[column[0]], column[0]
        

