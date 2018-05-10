import os
import db_create
from db_read import user_verify, query_read_recipes
from db import db
import write_recipe
import login_func
import find_recipe
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


###################################################################################
################################# ROUTES ###########################################    
###################################################################################

################################# LOGIN ROUTES #####################################

""" LANDING PAGE """
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

""" SIGN UP ROUTE """
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        username = user_values['Username']
        new_user = login_func.sign_up(user_values)
        #print(user_values)
        if new_user == True:
            return redirect('my_recipme/%s'% username)
        else:
            return redirect('user_taken') 

""" IF USER ALEADY EXISTS CALL THIS ROUTE """
@app.route('/user_taken', methods=['GET', 'POST'])
def user_taken():    
    return render_template('user_taken.html')

""" LOGIN ROUTE """
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values = request.form
        username = user_values['Username']
        returning_user = login_func.user_login(user_values)
        if returning_user == True:
            return redirect('my_recipme/%s'% username)
        else:
            return redirect('invalid_login')

""" IF LOGIN IS INVALID CALL THIS ROUTE """ 
@app.route('/invalid_login', methods=['GET', 'POST'])
def invalid_login():
    return render_template('invalid_login.html')

################ MAIN MY RECIPME ROUTE ##########################

""" USER MY RECIPME MAIN PAGE, POPULATE CUISINES """
@app.route('/my_recipme/<username>')
def my_recipme(username):
    user_id = write_recipe.get_user_id(username)
    cuisines = find_recipe.get_all_column_group_for_user('CuisineName', user_id, 'Cuisine')
    return render_template('my_recipme.html', username=username, cuisines=cuisines)

@app.route('/my_recipme/<username>/courses', methods=['GET','POST'])
def get_courses(username):
    if request.method == 'POST':
        cuisine = request.form['Cuisine']
        user_id = write_recipe.get_user_id(username)
        courses = find_recipe.get_all_courses_for_cuisine(user_id['UserId'], cuisine)
        print(courses)
        return redirect('my_recipme/%s'% username)
    

################ SEARCH ROUTES #################################

""" GET ALL RECIPES FOR A GIVEN USER """
@app.route('/my_recipme/<username>/all_myrecipme')
def all_myrecipme(username):
    result = find_recipe.get_mini_user_recipes(username, 'User.UserId', 'RecipeTitle', 'asc' )        
    recipes = find_recipe.date_time_converter(result)
    count = len(recipes)
    return render_template('all_my_recipme.html', username=username, my_recipme=recipes, count=count)

@app.route('/my_recipme/<username>/search', methods=['GET','POST'])
def ingredient_search(username):
    if request.method == 'POST':
        ingredient = request.form['Ingredient']
        user_id = write_recipe.get_user_id(username)
        result = find_recipe.get_recipes_by_ingredient('User.UserId', user_id['UserId'], ingredient, 'RecipeTitle', 'asc')
        recipes = find_recipe.date_time_converter(result)
        count = len(recipes)
        print(result)
    return render_template('ingredient_search.html', username=username, ingredient=ingredient, my_recipme=recipes, count=count)

############### ADD RECIPE ROUTES #############################

""" ADD RECIPE FOR GIVEN USER"""
@app.route('/my_recipme/<username>/add_recipe')
def add_recipe(username):  
    return render_template('add_recipe.html',username=username)

""" RECIPE FORM SUBMISSION AND REDIRECT TO USER MY RECIPME PAGE """
@app.route('/my_recipeme/<username>/recipe_created', methods=['GET', 'POST'])
def recipe_created(username):
    if request.method == 'POST':
        recipe = request.form
        user_id = write_recipe.get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,request.form.getlist('Quantity') ]
        write_recipe.write_full_recipe(recipe, user_id, ingredient_list, method_list)
    
        return redirect('my_recipme/%s'% username)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)