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

#################### INSERT USER ID INTO RECIPE DICT #####################
def add_user_id_to_recipe_dict(recipe, user_id):
    recipe['UserId'] = user_id['UserId']
    #print(recipe)
    return recipe  

################### CALL ABOVE THREE FUNCTIONS TO VALIDATE DICT ##########
#def validate_recipe_dict(username,recipe):
   #recipe = convert_numeric_strings_to_int(recipe)
    #user_id = get_user_id(username)
    #recipe = add_user_id_to_recipe_dict(recipe, user_id)
    #print(recipe)
    #print(user_id)
    #return recipe    

def merge_recipe_id_into_ingredient_item(ingredient_item, recipe_primary_key):
    merged = []
    merged_split= []

    for i in range(0, len(ingredient_item[0])):
        merged.append(ingredient_item[0][i])
        merged.append(ingredient_item[1]['UserId'])
        merged.append(recipe_primary_key)
        merged.append(ingredient_item[2][i])

    for item in range(0, len(merged), 4):
        merged_split.append(merged[item: item+4])

    
    return merged_split

#def prep_ingredient_items(recipe_primary_key, ingredient_item):
    #ingredient = merge_recipe_id_into_ingredient_item(ingredient_item, recipe_primary_key)
    #step_number = merge_recipe_id_into_method_item(recipe_primary_key, method_item[1])
    #step = merge_recipe_id_into_method_item(recipe_primary_key, method_item[2])

    #method_items_to_write = [ingredient, step_number, step]
    #return ingredient

def write_recipe(recipe, user_id):
    new_recipe = db_create.query_create_recipes(recipe, user_id)
    recipe_primary_key = new_recipe.create_recipe()
    new_recipe.create_stats(recipe_primary_key)

    return recipe_primary_key

def write_ingredients(prepped_items):
    new_ingredient = db_create.query_create_method_items(prepped_items)
    new_ingredient.create_ingredients()
    #print(prepped_items)
    return  True

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
        ingredients = request.form.getlist('Ingredient')
        step_number = request.form.getlist('StepNumber')
        method = request.form.getlist('Step')
        quantity = request.form.getlist('Quantity')
        user_id = get_user_id(username)
        ingredient_item = [ingredients, user_id, quantity]
        #recipe = validate_recipe_dict(username, recipe)
        
        recipe_primary_key = write_recipe(recipe, user_id)
        prepped_items = merge_recipe_id_into_ingredient_item(ingredient_item, recipe_primary_key)
        write_ingredients(prepped_items)
        #print(type(recipe_primary_key))
        

        return redirect('my_recipme/%s'% username)
    
    
###################### NEED TO INSERT USER ID INTO INGREDIENTS #######################  


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)