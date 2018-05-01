import os
import pymysql
import unittest
import service
from myenviron import ROOT_USERNAME, ROOT_PASSWORD, REMOTE_USER, REMOTE_PASSWORD, REMOTE_HOST, DATABASE_NAME

  
#### TO COME FROM FORM ####
user_values = ["Dafydd","Archard","Password"]
###########################

def get_user_id(user_values):
    query = service.query_read_recipes()
    user = query.query_read_user(user_values)
    user_id = [item['UserId'] for item in user]
    #print(user_id)
    return user_id
    
def get_mini_recipe(user_values):
    user_id = get_user_id(user_values)
    query_recipe = service.query_read_recipes()
    recipe = query_recipe.query_mini_recipe_from_user_id(user_id[0])
    print(recipe)
    return recipe

def get_recipe_stats_from_recipe_id(recipe_id):
    query = service.query_read_recipes()
    stats = query.query_read_for_recipe_stats(recipe_id)
    print(stats)
    return stats

##get_user_id(user_values)
get_mini_recipe(user_values)
#get_recipe_stats_from_recipe_id('1')
