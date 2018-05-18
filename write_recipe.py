import os
import db_create
import find_recipe
from db_read import UserVerify, QueryReadRecipes
from db_update_delete import QueryDeleteRecipe, QueryUpdateRecipe

################# CLASSES WITH LOGIC FOR PREPPING OR WRITING DATA TO DB ####################

class Create():

    def convert_numeric_strings_to_int(self, recipe):
        """CONVERT THE FORM DATA STRINGS TO INTEGERS """
        for key in recipe:
            is_value_number = recipe[key].isnumeric()
            if is_value_number:
                recipe[key] = int(recipe[key])
        return recipe

    def merge_recipe_id_into_ingredients(self,ingredient_list, recipe_primary_key):
        """ ADD RECIPE ID TO LIST READY FOR WRITING TO TABLE """
        ingredients = [] 
    
        for i in range(0, len(ingredient_list[0])):
            ingredients.append(ingredient_list[0][i])
            ingredients.append(ingredient_list[1]['UserId'])
            ingredients.append(recipe_primary_key)
            ingredients.append(ingredient_list[2][i])
        # SPLIT LIST INTO SUBLISTS FOR FIELD ENTRY #
        ingredients_split = [ingredients[i: i+4] for i in range(0, len(ingredients),4)]

        return ingredients_split

    def merge_recipe_id_into_method(self,method_item, recipe_primary_key):
        """ ADD RECIPE ID TO LIST READY FOR WRITING TO TABLE """
        method = [] 

        for i in range(0, len(method_item[0])):
            method.append(method_item[0][i])
            method.append(method_item[1][i])
            method.append(recipe_primary_key)
        # SPLIT LIST INTO SUBLISTS FOR FIELD ENTRY #
        method_split = [method[i: i+3] for i in range(0, len(method), 3)]
       
        return method_split

    def prep_method_and_ingredients(self,ingredient_list, method_list, recipe_primary_key):
        """PREP METHOD AND INGREDIENTS BY MERGING RECIPE ID INTO LIST """
        prepped_ingredients = Create.merge_recipe_id_into_ingredients(self, ingredient_list, recipe_primary_key)
        prepped_method = Create.merge_recipe_id_into_method(self, method_list, recipe_primary_key)
        
        return prepped_ingredients, prepped_method

    def write_ingredients_and_method(self,prepped_ingredients, prepped_method):
        new_ingredient = db_create.QueryCreateMethodItems(prepped_ingredients, prepped_method)
        new_ingredient.create_ingredients_and_method()
        
        return True

    def write_recipe_and_stats(self,recipe, user_id):
        new_recipe = db_create.QueryCreateRecipe(recipe, user_id)
        recipe_primary_key = new_recipe.create_recipe()
        new_recipe.create_stats(recipe_primary_key)

        return recipe_primary_key

    def write_full_recipe(self,recipe, user_id, ingredient_list, method_list):
        user_id = user_id
        recipe_primary_key = Create.write_recipe_and_stats(self, recipe, user_id)
        prep = Create.prep_method_and_ingredients(self, ingredient_list, method_list,recipe_primary_key)
        Create.write_ingredients_and_method(self, prep[0], prep[1])

        return True

    def write_saved_recipe(self, user_id, recipe_id):
         db_create.QuerySaveRecipe(user_id, recipe_id).save_recipe()

         return True

###################### CLASS FOR UPDATING FIELDS #############################

class Update():
    
    def update_recipe_and_stats(self, recipe, user_id, recipe_id):
        QueryUpdateRecipe(recipe, user_id, recipe_id).update_recipe()
        QueryUpdateRecipe(recipe, user_id, recipe_id).update_stats()

        return True

    def update_ingredients_and_method(self, recipe_id, ingredient_list, method_list):
        QueryDeleteRecipe(recipe_id,'Ingredient').delete()
        QueryDeleteRecipe(recipe_id,'Method').delete()
        prepped_ing = Create().merge_recipe_id_into_ingredients(ingredient_list, 
                                                                int(recipe_id))
        prepped_method = Create().merge_recipe_id_into_method(method_list, 
                                                            int(recipe_id))
        Create().write_ingredients_and_method(prepped_ing, prepped_method)

        return True