import os
import db_create
from db_read import user_verify, query_read_recipes

###################################################################################
############################## CREATE RECIPE FUNCTIONS ############################
###################################################################################

############### CONVERT THE FORM DATA STRINGS TO INTEGERS ###################

def convert_numeric_strings_to_int(recipe):
    for key in recipe:
        is_value_number = recipe[key].isnumeric()
        if is_value_number:
            recipe[key] = int(recipe[key])
    return recipe

#################### GET USERS ID BASED ON USERNAME #######################

def get_user_id(username):
    new_read_query = query_read_recipes()
    user = new_read_query.query_user_id(username)
    user_id = user[0]
    
    return user_id

#################### ADD RECIPE ID TO LIST READY FOR WRITING TO TABLE ############

def merge_recipe_id_into_ingredients(ingredient_list, recipe_primary_key):
    ingredients = [] ## MAKE LIST OF ALL INGREDIENTS INCLUDING RECIPE ID FOR EACH FIELD ##

    for i in range(0, len(ingredient_list[0])):
        ingredients.append(ingredient_list[0][i])
        ingredients.append(ingredient_list[1]['UserId'])
        ingredients.append(recipe_primary_key)
        ingredients.append(ingredient_list[2][i])
     # SPLIT LIST INTO SUBLISTS FOR FIELD ENTRY #
    ingredients_split = [ingredients[i: i+4] for i in range(0, len(ingredients),4)]

    return ingredients_split

def merge_recipe_id_into_method(method_item, recipe_primary_key):
    method = [] ## MAKE LIST OF ALL INGREDIENTS INCLUDING RECIPE ID FOR EACH FIELD ##

    for i in range(0, len(method_item[0])):
        method.append(method_item[0][i])
        method.append(method_item[1][i])
        method.append(recipe_primary_key)
    # SPLIT LIST INTO SUBLISTS FOR FIELD ENTRY #
    method_split = [method[i: i+3] for i in range(0, len(method), 3)]

    return method_split

###################### WRITE DETAILS TO RECIPE TABLE AND STATS TABLES ################

####################### WRITE INGREDIENTS TO INGREDIENTS TABLE ######################
def prep_method_and_ingredients(ingredient_list, method_list, recipe_primary_key):
    prepped_ingredients = merge_recipe_id_into_ingredients(ingredient_list, recipe_primary_key)
    prepped_method = merge_recipe_id_into_method(method_list, recipe_primary_key)
    
    return prepped_ingredients, prepped_method

def write_ingredients_and_method(prepped_ingredients, prepped_method):
    new_ingredient = db_create.query_create_method_items(prepped_ingredients, prepped_method)
    new_ingredient.create_ingredients_and_method()
    
    return True

def write_recipe_and_stats(recipe, user_id):
    new_recipe = db_create.query_create_recipes(recipe, user_id)
    recipe_primary_key = new_recipe.create_recipe()
    new_recipe.create_stats(recipe_primary_key)

    return recipe_primary_key

def write_full_recipe(recipe, user_id, ingredient_list, method_list):
    recipe_primary_key = write_recipe_and_stats(recipe, user_id)
    prep = prep_method_and_ingredients(ingredient_list, method_list,recipe_primary_key)
    write_ingredients_and_method(prep[0], prep[1])

    return True
