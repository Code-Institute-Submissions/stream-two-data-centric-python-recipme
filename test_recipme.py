import os
import pymysql
import recipme
import service
import unittest
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

class TestRecipme(unittest.TestCase):
    def test_read_all_from_one_table(self):
        table = "recipe"
        query = service.read_one_table(table)
        result = query.read_all_from_one_table()

        self.assertEqual(type(result), list)

    def test_get_user_id(self):
        user_values = ["Dafydd","Archard","password"]

        user_id = recipme.get_user_id(user_values)

        self.assertEqual(type(user_id), list)
        self.assertEqual(user_id[0], 1)

    def test_get_mini_recipes(self):
        
        search_by = 'MakePublic'
        direction = 'ASC'
        order_by = 'Calories'
        search_value = 1

        recipes = recipme.get_mini_recipes(search_by, search_value, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 3)
    
    def test_get_mini_user_recipes(self):
        
        user_values = ["Dafydd","Archard","password"]
        search_by = 'UserId'
        direction = 'ASC'
        order_by = 'Calories'

        recipes = recipme.get_all_mini_user_recipes(user_values, search_by, order_by, direction)

        self.assertEqual(type(recipes), list)
        self.assertEqual(len(recipes), 1)
    
    def test_get_ingredients_for_full_recipe(self):

        recipe_id = 11

        ingredients = recipme.get_ingredients_for_full_recipe(recipe_id)

        self.assertEqual(type(ingredients), list)
        self.assertEqual(len(ingredients), 6)

    def test_get_ingredients_for_full_recipe(self):

        recipe_id = 11

        method = recipme.get_method_for_full_recipe(recipe_id)

        self.assertEqual(type(method), list)
        self.assertEqual(len(method), 5)