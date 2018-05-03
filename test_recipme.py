import os
import pymysql
import recipme
import db_read
import unittest
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

class TestRecipme(unittest.TestCase):
    def test_read_all_from_one_table(self):
        table = "recipe"
        query = db_read.read_one_table(table)
        result = query.read_all_from_one_table()

        self.assertEqual(type(result), list)

    def test_get_user_id(self):
        user_values = ["Dafydd","Archard","password"]

        user_id = recipme.get_user_id(user_values)

        self.assertEqual(type(user_id), list)
        self.assertEqual(user_id[0], 1)

    def test_get_mini_recipes(self):
        
        search_by = 'Recipe.MakePublic'
        direction = 'ASC'
        order_by = 'Calories'
        search_value = 1

        recipes = recipme.get_all_mini_recipes(search_by, search_value, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 3)
    
    def test_get_mini_user_recipes(self):
        
        user_values = ["Dafydd","Archard","password"]
        search_by = 'User.UserId'
        direction = 'ASC'
        order_by = 'Calories'

        recipes = recipme.get_mini_user_recipes(user_values, search_by, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 1)
    
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
        
