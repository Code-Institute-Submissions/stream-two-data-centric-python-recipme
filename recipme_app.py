import os
import db_create
import write_recipe
import find_recipe
import user_login
import view_var
from db import Db
from db_read import UserVerify, QueryReadRecipes
from db_update_delete import QueryDeleteRecipe, QueryUpdateRecipe
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


###################################################################################
################################# ROUTES ###########################################    
###################################################################################

################################# LOGIN ROUTES #####################################

# LANDING PAGE #
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

# SIGN UP ROUTE #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        new_user = user_login.LogIn(user_values).sign_up()
        if new_user == True:
            return redirect('my_recipme/%s'% user_values['Username'])
        else:
            return redirect('user_taken') 

# IF USER ALEADY EXISTS CALL THIS ROUTE #
@app.route('/user_taken', methods=['GET', 'POST'])
def user_taken():    
    return render_template('user_taken.html')

# LOGIN ROUTE #
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values= request.form
        returning_user = user_login.LogIn(user_values).user_login()
        if returning_user == True:
            return redirect('my_recipme/%s'% user_values['Username'])
        else:
            return redirect('invalid_login')

# IF LOGIN IS INVALID CALL THIS ROUTE # 
@app.route('/invalid_login', methods=['GET', 'POST'])
def invalid_login():
    return render_template('invalid_login.html')

################ MAIN MY RECIPME ROUTE ##########################

# USER MY RECIPME MAIN PAGE, POPULATE CUISINES #
@app.route('/my_recipme/<username>')
def my_recipme(username):
    recipe_info = view_var.ViewVariables(username).var_myrecipme()
    return render_template('my_recipme.html', username=username, cuisines=recipe_info[0], courses=recipe_info[1])

################ SEARCH ROUTES #################################

# GET ALL RECIPES FOR A GIVEN USER #
@app.route('/my_recipme/<username>/all_myrecipme')
def all_myrecipme(username):
    recipe_info = view_var.ViewVariables(username).var_all_myrecipme()
    return render_template('all_my_recipme.html', username=username, my_recipme=recipe_info[0], 
                                                    cuisines=recipe_info[2][0], courses=recipe_info[2][1], 
                                                    count=recipe_info[1])
# GET ALL RECIPES FOR A GIVEN INGREDIENT #
@app.route('/my_recipme/<username>/search', methods=['GET','POST'])
def ingredient_search(username):
    if request.method == 'POST':
        ingredient = request.form['Ingredient']
        recipe_info = view_var.ViewVariables(username).var_ing_search(ingredient)
        
    return render_template('ingredient_search.html', username=username, 
                            ingredient=ingredient, my_recipme=recipe_info[0], count=recipe_info[1],
                            cuisines=recipe_info[2][0], courses=recipe_info[2][1])

# GET ALL RECIPES FOR A GIVEN CATEGORY #
@app.route('/my_recipme/<username>/category/search', methods=['GET','POST'])
def category_search(username):
    if request.method == 'POST':
        recipe_info = view_var.ViewVariables(username).var_cat_search(request.form)
        return render_template('category_search.html', username=username, my_recipme=recipe_info[0], 
                                                        count=recipe_info[1], cuisines=recipe_info[2][0], 
                                                        courses=recipe_info[2][1], category=recipe_info[3], 
                                                        category_item=recipe_info[4])
                                                        
############### FULL RECIPE VIEW ##############################
@app.route('/my_recipme/<username>/redirect', methods=['GET', 'POST'])
def full_redirect(username):
    if request.method == 'POST':
        recipe_id = request.form['RecipeId']
        full_recipe = view_var.ViewVariables(username).var_full_recipe(recipe_id)
        title = full_recipe[1][0]['RecipeTitle']
        
        return redirect('/my_recipme/%s/%s/%s'% (username, title, recipe_id))

@app.route('/my_recipme/<username>/<title>/<recipe_id>')
def full_recipe(username, title, recipe_id):
    full_recipe = view_var.ViewVariables(username).var_full_recipe(recipe_id)
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
        user_id = find_recipe.Get().get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,
                            request.form.getlist('Quantity')]
        write_recipe.Create().write_full_recipe(recipe, user_id, ingredient_list, method_list)
        return redirect('my_recipme/%s/%s'% (username, 'create'))

@app.route('/my_recipme/<username>/<action>')
def recipe_action(username, action):
    return render_template('crud_action.html', username=username, action=action)

############## UPDATE RECIPE ROUTES #########################
    
@app.route('/my_recipme/<username>/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(username, recipe_id):
    full_recipe = view_var.ViewVariables(username).var_full_recipe(recipe_id)
    title = full_recipe[1][0]['RecipeTitle']
    return render_template('edit_recipe.html', username=username, 
                            full_recipe=full_recipe, title=title, recipe_id=recipe_id)

@app.route('/my_recipme/<username>/updating_recipe/<recipe_id>', methods=['GET', 'POST'])
def updating_recipe(username, recipe_id):
    if request.method == 'POST':
        recipe = request.form
        user_id = find_recipe.Get().get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),
                        request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,
                            request.form.getlist('Quantity')]
        write_recipe.Update().update_recipe_and_stats(recipe, user_id, recipe_id)
        write_recipe.Update().update_ingredients_and_method(recipe_id, ingredient_list, 
                                                            method_list)

        return redirect('my_recipme/%s/%s'% (username, 'update'))
        
############## DELETE RECIPE ROUTE ##########################

@app.route('/my_recipme/<username>/delete_recipe', methods=['GET', 'POST'])
def delete_recipe(username):
    if request.method == 'POST':
        table = 'Recipe'
        QueryDeleteRecipe(request.form['RecipeId'],table).delete()

        return redirect('my_recipme/%s/%s'%(username, 'delete'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)