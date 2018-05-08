import os
#import pymysql
import myenviron
import json
import db_create
import collections
from db_read import user_verify, query_read_recipes
from db import db
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

###################################################################################
##################### LOGIN/SIGNUP FUNCTIONS ######################################
###################################################################################

 ################ CREATE A NEW USER ################################

def create_user(user_values):
    new_user = db_create.query_create_user(user_values)
    new_user.create_user()
    return user_values

############### SEARCH USER TABLE FOR USER AND RETURN RESULT ######

def get_existing_user(user_values):
    new_verify = user_verify(user_values)
    existing_user = new_verify.query_user()
    print(existing_user)
    return existing_user

############### IF THE USERNAME DOESN'T EXIST SIGN UP ###########

def sign_up(user_values):
    existing_user = get_existing_user(user_values)
    if existing_user == []:
        create_user(user_values)
        return True
    elif existing_user[0]['Username'] == user_values['Username']:
        print('Username taken, enter a unique username')
        return False

############## IF THE USERNAME AND PASSWORD MATCH LOGIN ###########

def user_login(user_values): 
    existing_user = get_existing_user(user_values)
    if existing_user != []:
        if existing_user[0]['Username'] == user_values['Username']:
            if existing_user[0]['Password'] == user_values['Password']:
                return True
    else:
        return False

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

###################################################################################
################################# ROUTES ###########################################    
###################################################################################

################################# LOGIN ROUTES #####################################

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        username = user_values['Username']
        new_user = sign_up(user_values)
        print(user_values)
        if new_user == True:
            return redirect('my_recipme/%s'% username)
        else:
            return redirect('user_taken') 

@app.route('/user_taken', methods=['GET', 'POST'])
def user_taken():    
    return render_template('user_taken.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values = request.form
        username = user_values['Username']
        returning_user = user_login(user_values)
        if returning_user == True:
            return redirect('my_recipme/%s'% username)
        else:
            return redirect('invalid_login')
    
@app.route('/invalid_login', methods=['GET', 'POST'])
def invalid_login():
    return render_template('invalid_login.html')

################ MAIN MY RECIPME ROUTE ##########################

@app.route('/my_recipme/<username>')
def my_recipme(username):
    return render_template('my_recipme.html', username=username)

@app.route('/my_recipme/<username>/add_recipe')
def add_recipe(username):        
    return render_template('add_recipe.html',username=username)

@app.route('/my_recipeme/<username>/recipe_created', methods=['GET', 'POST'])
def recipe_created(username):
    if request.method == 'POST':
        recipe = request.form
        user_id = get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,request.form.getlist('Quantity') ]
        write_full_recipe(recipe, user_id, ingredient_list, method_list)
    
        return redirect('my_recipme/%s'% username)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)