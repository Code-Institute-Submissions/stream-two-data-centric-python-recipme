import os
import pymysql
import db
import db_read
import user_login
import write_recipe
import find_recipe
import unittest
import datetime


class TestRecipme(unittest.TestCase):
    ########################## READ DB TESTS ################################
    def test_query_user(self):
        user_values = {'Username': 'test', 'Password': 'test'}
        query = db_read.UserVerify(user_values)
        result = query.query_user()

        self.assertEqual(type(result), list)
   

    def test_get_ingredients_for_full_recipe(self):

        recipe_id = 11

        ingredients = find_recipe.Get().get_ingredients_for_full_recipe(recipe_id)

        self.assertEqual(type(ingredients), list)
        self.assertEqual(len(ingredients), 6)

    def test_get_method_for_full_recipe(self):

        recipe_id = 11

        method = find_recipe.Get().get_method_for_full_recipe(recipe_id)

        self.assertEqual(type(method), list)
        self.assertEqual(len(method), 5)
    

    def test_get_recipes_by_ingredient(self):
        user_values = ["Dafydd","Archard","password"]
        search_by = 'Recipe.MakePublic' ## RecipeId, MakePublic, UserId ##
        direction = 'ASC'
        order_by = 'Calories'
        ingredient = 'Eggs'
      
        recipe = find_recipe.Get().get_recipes_by_ingredient(search_by,1, ingredient, order_by, direction)
        result = recipe[0]['RecipeTitle']
        

        self.assertEqual(type(recipe), list)
        self.assertEqual(result, 'Poached Eggs with Asparagus')

    def test_is_recipe_saved(self):
        user_id = 1
        recipe_id = 1111
    
        recipe = find_recipe.Get().get_is_recipe_saved(user_id, recipe_id)

        self.assertEqual(recipe, True)
        

    ############################ LOGIN/SIGNUP TESTS ##################################

    def test_get_existing_user(self):
        user_values = {'Username': 'darchard', 'Password': 'password'}
        user = user_login.LogIn(user_values).get_existing_user()
        username = user[0]['Username']
        password = user[0]['Password']

        self.assertEqual(user_values['Username'], username)
        self.assertEqual(user_values['Password'], password)

    ######### TEST WORKS, COMMENTED OUT TO AVOID DUPLICATION IN TABLE #######
    """
    def test_create_user(self):
        user_values = {
                        'Username': 'jdoe',
                        'First': 'Jane', 
                        'Last':'Doe', 
                        'Password': 'password'
                        }

        write_user = find_recipe_app.create_user(user_values)
        check_user = find_recipe_app.get_existing_user(user_values)
        
        self.assertEqual(user_values['Username'], check_user[0]['Username'])
        self.assertEqual(user_values['First'], check_user[0]['First'])
        self.assertEqual(user_values['Last'], check_user[0]['Last'])
        self.assertEqual(user_values['Password'], check_user[0]['Password'])
    

    def test_sign_up(self):
        existing_user_values = {'Username': 'darchard', 'First':'Dafydd', 'Last':'Archard','Password': 'password'}
        new_user_vales = {'Username': 'newuser', 'First':'newuser', 'Last':'newuser','Password': 'newuser'}

        successful = find_recipe_app.sign_up(existing_user_values)
        unsuccessful = find_recipe_app.sign_up(new_user_vales)

        self.assertEqual(successful, False)
        self.assertEqual(unsuccessful, True)
    """
        

    def test_user_login(self):
        actual_user_values = {'Username': 'darchard', 'Password': 'password'}
        invalid_user_vales = {'Username': 'invalid', 'Password': 'invalid'}

        successful = user_login.LogIn(actual_user_values).user_login()
        unsuccessful = user_login.LogIn(invalid_user_vales).user_login()

        self.assertEqual(successful, True)
        self.assertEqual(unsuccessful, False)

################################### CREATE RECIPE TESTS ##########################################


    def test_get_user_id(self):
        username = 'darchard'

        user_id = find_recipe.Get().get_user_id(username)

        self.assertEqual(type(user_id), dict)
        self.assertEqual(user_id['UserId'], 1)

    def test_merge_recipe_id_into_ingredients(self):
        ingredient_list = [['Chicken Breasts', 'Wraps'], {'UserId': 1}, ['2', '4']]
        recipe_primary_key = 1

        result = write_recipe.Create().merge_recipe_id_into_ingredients(ingredient_list, recipe_primary_key)

        self.assertEqual(result, [['Chicken Breasts', 1, 1, '2'], ['Wraps', 1, 1, '4']])

    def test_merge_recipe_id_into_method(self):
        method_list = [['1', '2'], ['Slice Cheese', 'Pour Wine']]
        recipe_primary_key = 1

        result = write_recipe.Create().merge_recipe_id_into_method(method_list, recipe_primary_key)

        self.assertEqual(result, [['1', 'Slice Cheese', 1], ['2', 'Pour Wine', 1]])

    def test_date_time_converter(self):
        date = [{'Created': datetime.datetime(2018, 5, 7, 13, 26, 5)}]

        result = find_recipe.Get().date_time_converter(date)

        self.assertEqual(result, [{'Created':'13:26:05 on 05.07.2018'}])

    def test_get_all_column_group_for_user(self):
        column = 'CourseName'
        user_id = 11
        table = 'Course'
        for_user = True

        result = find_recipe.Get().get_all_column_group(column, user_id, table, for_user)

        self.assertEqual(result[0]['Total'], 1)
        self.assertEqual(result[0]['CourseName'], 'Breakfast')
   
class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_get_mini_recipes(self):
        
        search_by = 'Recipe.MakePublic'
        direction = 'ASC'
        order_by = 'Calories'
        search_value = 1

        recipes = find_recipe.Get().get_all_mini_recipes(search_by, search_value, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 3)

    @unittest.expectedFailure
    def test_get_category_mini_recipes(self):
        
        search_by = 'User.UserId' ## MakePublic, UserId ##
        direction = 'ASC'
        order_by = 'Calories'
        category = 'Lunch'
        table = 'Course'
        column = 'CourseName'
       
      
        recipe = find_recipe.Get().get_category_mini_recipes(table, search_by, 1, column, 
                                                            category, order_by, direction)
        result = recipe[0]['RecipeTitle']
        

        self.assertEqual(type(recipe), list)
        self.assertEqual(result, 'Chips')