import os
import pymysql
import db
import db_read
import db_create
import user_login
import write_recipe
import find_recipe
import unittest
import datetime
import tempfile


class TestRecipme(unittest.TestCase):
    ########################## READ DB TESTS ################################
    def test_query_user(self):
        user_values = {'Username': 'test', 'Password': 'test'}
        query = db_read.UserVerify(user_values)
        result = query.query_user()

        self.assertEqual(type(result), list)
   
    def test_get_method_for_full_recipe(self):

        recipe_id = 11

        method = find_recipe.Get().get_method_for_full_recipe(recipe_id)

        self.assertEqual(type(method), list)
        self.assertEqual(len(method), 5)

    def test_is_recipe_saved(self):
        user_id = 1
        recipe_id = 11
    
        recipe = find_recipe.Get().get_is_recipe_saved(user_id, recipe_id)

        self.assertEqual(recipe, False)
        

    ############################ LOGIN/SIGNUP TESTS ##################################

    def test_get_existing_user(self):
        user_values = {'Username': 'darchard', 'Password': 'password'}
        user = user_login.LogIn(user_values).get_existing_user()
        username = user[0]['Username']
        password = user[0]['Password']

        self.assertEqual(user_values['Username'], username)
        self.assertEqual(user_values['Password'], password)

    ######### TEST WORKS, COMMENTED OUT TO AVOID DUPLICATION IN TABLE #######
    
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
        total = result[0]['Total']
        course_name = result[0]['CourseName']
    
        self.assertEqual(total, 1)
        self.assertEqual(course_name, 'Breakfast')
        

    def test_character_capitalize(self):

        word = 'not capital'

        result = db_create.capitalize_words(word)

        self.assertEqual(type(result), str)
        self.assertEqual(result, 'Not Capital')

    def test_write_to_doc(self):
        error = "error"
        message = "message"
        time_stamp = str(datetime.datetime.now())
        log_elements = (error, message, time_stamp, "\n")
        log = " ".join(log_elements)
        file = tempfile.mkstemp()[1]

        try:
            new_log = db.WriteErrorToLog(error, message, file, time_stamp)
            new_log.write_to_doc()
            content = open(file).read()
        finally:
            os.remove(file)

        self.assertEqual(log, content)