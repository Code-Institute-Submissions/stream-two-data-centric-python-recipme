import os
import db_create
import write_recipe
import find_recipe
import user_login
import view_var
from db import db
from db_read import user_verify, query_read_recipes
from db_update_delete import query_delete_recipe
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
        new_user = user_login.login(user_values).sign_up()
        if new_user == True:
            return redirect('my_recipme/%s'% user_values['Username'])
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
        user_values= request.form
        returning_user = user_login.login(user_values).user_login()
        if returning_user == True:
            return redirect('my_recipme/%s'% user_values['Username'])
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
    recipe_info = view_var.view_var(username).var_myrecipme()
    return render_template('my_recipme.html', username=username, cuisines=recipe_info[0], courses=recipe_info[1])

################ SEARCH ROUTES #################################

""" GET ALL RECIPES FOR A GIVEN USER """
@app.route('/my_recipme/<username>/all_myrecipme')
def all_myrecipme(username):
    recipe_info = view_var.view_var(username).var_all_myrecipme()
    return render_template('all_my_recipme.html', username=username, my_recipme=recipe_info[0], 
                                                    cuisines=recipe_info[2][0], courses=recipe_info[2][1], 
                                                    count=recipe_info[1])

@app.route('/my_recipme/<username>/search', methods=['GET','POST'])
def ingredient_search(username):
    if request.method == 'POST':
        ingredient = request.form['Ingredient']
        recipe_info = view_var.view_var(username).var_ing_search(ingredient)
        
    return render_template('ingredient_search.html', username=username, 
                            ingredient=ingredient, my_recipme=recipe_info[0], count=recipe_info[1],
                            cuisines=recipe_info[2][0], courses=recipe_info[2][1])

@app.route('/my_recipme/<username>/category/search', methods=['GET','POST'])
def category_search(username):
    if request.method == 'POST':
        recipe_info = view_var.view_var(username).var_cat_search(request.form)
        return render_template('category_search.html', username=username, my_recipme=recipe_info[0], 
                                                        count=recipe_info[1], cuisines=recipe_info[2][0], 
                                                        courses=recipe_info[2][1], category=recipe_info[3], 
                                                        category_item=recipe_info[4])
                                                        
############### FULL RECIPE VIEW ##############################
@app.route('/my_recipme/<username>/redirect', methods=['GET', 'POST'])
def full_redirect(username):
    if request.method == 'POST':
        recipe_id = request.form['RecipeId']
        full_recipe = view_var.view_var(username).var_full_recipe(recipe_id)
        title = full_recipe[1][0]['RecipeTitle']
        
        return redirect('/my_recipme/%s/%s/%s'% (username, title, recipe_id))

@app.route('/my_recipme/<username>/<title>/<recipe_id>')
def full_recipe(username, title, recipe_id):
    full_recipe = view_var.view_var(username).var_full_recipe(recipe_id)
    print(full_recipe)
    return render_template('full_recipe_partial.html', title=title, username=username, 
                                                        full_recipe=full_recipe, recipe_id=recipe_id)

############### CREATE RECIPE ROUTES #############################

""" ADD RECIPE FOR GIVEN USER"""
@app.route('/my_recipme/<username>/add_recipe')
def add_recipe(username):  
    return render_template('add_recipe.html',username=username)

""" RECIPE FORM SUBMISSION AND REDIRECT TO USER MY RECIPME PAGE """
@app.route('/my_recipme/<username>/create_recipe', methods=['GET', 'POST'])
def creating_recipe(username):
    if request.method == 'POST':
        recipe = request.form
        user_id = find_recipe.get().get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,request.form.getlist('Quantity') ]
        write_recipe.create().write_full_recipe(recipe, user_id, ingredient_list, method_list)
        print(recipe)
        return redirect('my_recipme/%s/%s'% (username, 'create'))

@app.route('/my_recipme/<username>/<action>')
def recipe_action(username, action):
    return render_template('crud_action.html', username=username, action=action)

############## UPDATE RECIPE ROUTE #########################
@app.route('/my_recipme/<username>/update_recipe', methods=['GET', 'POST'])
def update_recipe(username):
    if request.method == 'POST':
        recipe_id = request.form['RecipeId']
        full_recipe = view_var.view_var(username).var_full_recipe(recipe_id)
        title = full_recipe[1][0]['RecipeTitle']
        print(full_recipe)
    return render_template('update_recipe.html', username=username, full_recipe=full_recipe, title=title)

############## DELETE RECIPE ROUTE ##########################

@app.route('/my_recipme/<username>/delete_recipe', methods=['GET', 'POST'])
def delete_recipe(username):
    if request.method == 'POST':
        print(request.form['RecipeId'])
        query_delete_recipe(request.form['RecipeId']).delete()

        return redirect('my_recipme/%s/%s'%(username, 'delete'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)