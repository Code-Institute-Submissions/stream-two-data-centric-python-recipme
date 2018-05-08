import os
import json
import db_create
from db_read import user_verify, query_read_recipes
from db import db
import write_recipe
import login_func
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


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
        new_user = login_func.sign_up(user_values)
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
        returning_user = login_func.user_login(user_values)
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
        user_id = write_recipe.get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,request.form.getlist('Quantity') ]
        print(method_list)
        write_recipe.write_full_recipe(recipe, user_id, ingredient_list, method_list)
    
        return redirect('my_recipme/%s'% username)
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)