import os
import pymysql
import recipme
import recipme_app
import db
import db_read
import unittest
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

class TestRecipme(unittest.TestCase):
    ########################## READ DB TESTS ################################
    def test_query_user(self):
        user_values = {'Username': 'test', 'Password': 'test'}
        query = db_read.user_verify(user_values)
        result = query.query_user()

        self.assertEqual(type(result), list)
   
    def test_get_mini_recipes(self):
        
        search_by = 'Recipe.MakePublic'
        direction = 'ASC'
        order_by = 'Calories'
        search_value = 1

        recipes = recipme.get_all_mini_recipes(search_by, search_value, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 3)
    """
    def test_get_mini_user_recipes(self):
        
        user_values = ["darchard"]
        search_by = 'User.UserId'
        direction = 'ASC'
        order_by = 'Calories'

        recipes = recipme.get_mini_user_recipes(user_values, search_by, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 1)
    """
    def test_get_ingredients_for_full_recipe(self):

        recipe_id = 11

        ingredients = recipme.get_ingredients_for_full_recipe(recipe_id)

        self.assertEqual(type(ingredients), list)
        self.assertEqual(len(ingredients), 6)

    def test_get_method_for_full_recipe(self):

        recipe_id = 11

        method = recipme.get_method_for_full_recipe(recipe_id)

        self.assertEqual(type(method), list)
        self.assertEqual(len(method), 5)

    def test_get_filtered_mini_recipes(self):
        user_values = ["Dafydd","Archard","password"]
        search_by = 'Recipe.MakePublic' ## MakePublic, UserId ##
        direction = 'ASC'
        order_by = 'Calories'
        course = "Lunch"
        cuisine = "British"
      
        recipe = recipme.get_filtered_mini_recipes(search_by, 1, course, cuisine, order_by, direction)
        result = recipe[0]['RecipeTitle']
        

        self.assertEqual(type(recipe), list)
        self.assertEqual(result, 'BEANS ON TOAST')

    def test_get_recipes_by_ingredient(self):
        user_values = ["Dafydd","Archard","password"]
        search_by = 'Recipe.MakePublic' ## RecipeId, MakePublic, UserId ##
        direction = 'ASC'
        order_by = 'Calories'
        ingredient = 'Eggs'
      
        recipe = recipme.get_recipes_by_ingredient(search_by,1, ingredient, order_by, direction)
        result = recipe[0]['RecipeTitle']
        

        self.assertEqual(type(recipe), list)
        self.assertEqual(result, 'Poached Eggs with Asparagus')

    def test_get_saved_recipes_for_user(self):
        user_id = 11
        direction = 'ASC'
        order_by = 'Calories'

        recipe = recipme.get_saved_recipes_for_user(user_id, order_by, direction)
        author = recipe[0]['Author']

        # TESTS TO SEE THAT RETURNED USERNAME IS THE ORIGINAL AUTHOR, NOT THE
        # USERNAME FROM GIVEN ID

        self.assertEqual(type(recipe), list)
        self.assertEqual(author, 'darchard')

    ############################ LOGIN/SIGNUP TESTS ##################################

    def test_get_existing_user(self):
        user_values = {'Username': 'darchard', 'Password': 'password'}
        user = recipme_app.get_existing_user(user_values)
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

        write_user = recipme_app.create_user(user_values)
        check_user = recipme_app.get_existing_user(user_values)
        
        self.assertEqual(user_values['Username'], check_user[0]['Username'])
        self.assertEqual(user_values['First'], check_user[0]['First'])
        self.assertEqual(user_values['Last'], check_user[0]['Last'])
        self.assertEqual(user_values['Password'], check_user[0]['Password'])
    

    def test_sign_up(self):
        existing_user_values = {'Username': 'darchard', 'First':'Dafydd', 'Last':'Archard','Password': 'password'}
        new_user_vales = {'Username': 'newuser', 'First':'newuser', 'Last':'newuser','Password': 'newuser'}

        successful = recipme_app.sign_up(existing_user_values)
        unsuccessful = recipme_app.sign_up(new_user_vales)

        self.assertEqual(successful, False)
        self.assertEqual(unsuccessful, True)
    """
        

    def test_user_login(self):
        actual_user_values = {'Username': 'darchard', 'Password': 'password'}
        invalid_user_vales = {'Username': 'invalid', 'Password': 'invalid'}

        successful = recipme_app.user_login(actual_user_values)
        unsuccessful = recipme_app.user_login(invalid_user_vales)

        self.assertEqual(successful, True)
        self.assertEqual(unsuccessful, False)

################################### CREATE RECIPE TESTS ##########################################
        
    def test_convert_numeric_strings_to_int(self):
        recipe = {
                'RecipeTitle': 'Sausage and Mash', 
                'RecipeDescription': "Lot's of it.", 
                'CookingTimeMins': '30', 
                'MakePublic': '1', 
                }

        converted_recipe = recipme_app.convert_numeric_strings_to_int(recipe)
        
        self.assertEqual(type(converted_recipe['CookingTimeMins']), int)
        self.assertEqual(type(converted_recipe['MakePublic']), int)

    def test_get_user_id(self):
        username = 'darchard'

        user_id = recipme_app.get_user_id(username)

        self.assertEqual(type(user_id), dict)
        self.assertEqual(user_id['UserId'], 1)

    def test_add_user_id_to_recipe_dict(self):
        recipe = {
                'RecipeTitle': 'Sausage and Mash', 
                'RecipeDescription': "Lot's of it.", 
                'CookingTimeMins': 30, 
                'MakePublic': 1, 
                }
        user_id = {'UserId': 1}
        new_recipe = recipme_app.add_user_id_to_recipe_dict(recipe, user_id)

        self.assertEqual(new_recipe['UserId'], user_id['UserId'] )
    
        
    def test_validate_recipe_dict(self):
        username = 'darchard'
        recipe = {
                'RecipeTitle': 'Sausage and Mash', 
                'RecipeDescription': "Lot's of it.", 
                'CookingTimeMins': '30', 
                'MakePublic': '1', 
                }

        validate = recipme_app.validate_recipe_dict(username, recipe)

        self.assertEqual(type(validate['CookingTimeMins']), int)
        self.assertEqual(type(validate['MakePublic']), int)
        self.assertEqual(type(validate['UserId']), int)
        self.assertEqual(validate['UserId'], 1)
    """
    NEED TO WRITE ADDITIONAL READ TABLE CLASS
    
    def test_write_to_recipe_table(self):
        recipe = {
                'RecipeTitle': 'Sausage and Mash', 
                'RecipeDescription': "Lot's of it.", 
                'CookingTimeMins': 30, 
                'MakePublic': 1,
                'UserId': 1
                }

        write_recipe = recipme_app.write_to_recipe_table(recipe)
        read_recipe = read_db
    """