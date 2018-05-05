import os
import pymysql
import myenviron
import json
import db_create
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
def validate_recipe_dict(username,recipe):
    recipe = convert_numeric_strings_to_int(recipe)
    user_id = get_user_id(username)
    recipe = add_user_id_to_recipe_dict(recipe, user_id)
    #print(recipe)
    #print(user_id)
    return recipe

def write_to_recipe_table(recipe):
    new_recipe = db_create.query_create_recipes(recipe)
    new_recipe.create_recipe()
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
        recipe = request.form.to_dict()
        recipe = validate_recipe_dict(username, recipe)
        print(recipe)
       # write_to_recipe_table(recipe)
        
        return redirect('my_recipme/%s'% username)
    
    

###################### NEED TO PASS USERNAME AND ID THROUGH TO REDIRECT TO MY RECIPE ################

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)