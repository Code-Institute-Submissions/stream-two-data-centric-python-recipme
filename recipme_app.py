import os
import db_create
import write_recipe
import user_login
import json
from db import Db
from find_recipe import Get
from db_read import UserVerify, QueryReadRecipes
from view_var import ViewVariables, ViewFunc, Totals
from db_update_delete import QueryDeleteRecipe, QueryUpdateRecipe
from flask import Flask, redirect, render_template, request, flash
from flask_paginate import Pagination, get_page_args

app = Flask(__name__)
app.secret_key = 'my_cat_called_sumo'

###################################################################################
################################# ROUTES ###########################################    
###################################################################################

################################# LOGIN ROUTES #####################################

# LANDING PAGE #
@app.route('/', methods=['GET','POST'])
def index():
    stats = Totals().get_all_totals()
    percentage_shared = Totals().get_percentage_shared(stats)
   # print(percentage_shared)
    return render_template('index.html', stats=stats, shared=percentage_shared)

@app.route('/stats', methods = ['GET', 'POST'])
def stats():
    stats = Totals().get_all_totals()
    stats_json = json.dumps(stats)
    #print(stats_json)
    return stats_json
    
# SIGN UP ROUTE #
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        new_user = user_login.LogIn(user_values).sign_up()
        if user_values['Username'] == '':
            flash('Please fill in all the fields.')
            return redirect('/')
        elif  user_values['First'] == '':
            flash('Please fill in all the fields.')
            return redirect('/')
        elif user_values['Last'] == '':
            flash('Please fill in all the fields.')
            return redirect('/')
        else:
            if new_user == True:
                return redirect('my_recipme/%s'% user_values['Username'])
            else:
                flash('Username taken, please choose a unique username.')
                return redirect('/') 

# IF USER ALEADY EXISTS CALL THIS ROUTE #
#@app.route('/user_taken', methods=['GET', 'POST'])
#def user_taken():    
    #eturn render_template('user_taken.html')

# LOGIN ROUTE #
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values= request.form
        returning_user = user_login.LogIn(user_values).user_login()
        if user_values['Username'] == '':
            flash('Please fill in all the fields.')
            return redirect('/')
        elif user_values['Password'] == '':
            flash('Please fill in all the fields.')
            return redirect('/')
        else:
            if returning_user == True:
                return redirect('my_recipme/%s'% user_values['Username'])
            else:
                flash('Check your details and try again.')
                return redirect('/')

# IF LOGIN IS INVALID CALL THIS ROUTE # 
#@app.route('/invalid_login', methods=['GET', 'POST'])
#def invalid_login():
    #return render_template('invalid_login.html')

################ MAIN MY RECIPME ROUTE ##########################       

# USER MY RECIPME MAIN PAGE, POPULATE CUISINES #
@app.route('/my_recipme/<username>')
def my_recipme(username):
    recipe_groups = ViewVariables(username).groupings()
    return render_template('my_recipme.html', search=False, username=username, cuisines=recipe_groups[0][0], 
                            courses=recipe_groups[0][1], public_cuisines=recipe_groups[1][0], 
                            public_courses=recipe_groups[1][1])

################ SEARCH ROUTES #################################
################ USER SPECIFIC ROUTES ##########################


# ALL RECIPES FOR A GIVEN USER #
@app.route('/my_recipme/<username>/my_recipme', methods=['GET', 'POST'])
def all_myrecipme(username):
    if request.method == 'POST':
        order_by, direction = request.form['SortBy'], request.form['Direction']
        username=username   
        return redirect('/my_recipme/all_my_recipme/%s/%s/%s' % (username, order_by, direction)) 

# ALL RECIPES FOR A GIVEN USER PAGINATE #
@app.route('/my_recipme/all_my_recipme/<username>/<order_by>/<direction>')
def all_myrecipme_paginate(username, order_by, direction):
    recipe_info = ViewVariables(username).var_all_myrecipme(order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')

    return render_template('my_recipme.html', search='all', username=username, my_recipme=recipe_info[0],
                            count=recipe_info[1], cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1], 
                            public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                            results=pagination_results, page=page, per_page=per_page, pagination=pagination)
    

# ALL RECIPES FOR A GIVEN CATEGORY #
@app.route('/my_recipme/<username>/category/search', methods=['GET','POST'])
def category_search(username):
    if request.method == 'POST':
        order_by, direction = request.form['SortBy'], request.form['Direction']
        keys = [key for key in request.form]
        table, column = keys[2], keys[2] + 'Name'
        category = request.form[table]
        print(keys)
        return redirect ('/my_recipme/%s/category/search/%s/%s/%s/%s/%s' % (username, table, column, category,
                                                                              order_by, direction))
# ALL RECIPES FOR A GIVEN CATEGORY PAGINATE #
@app.route('/my_recipme/<username>/category/search/<table>/<column>/<category>/<order_by>/<direction>')
def category_paginate(username, table, column, category, order_by, direction):
    user_id = Get().get_user_id(username)['UserId']
    recipe_info = ViewVariables(username).var_cat_search(table, 'User.UserId', user_id, column, 
                                                            category, order_by, direction)

   # print(recipe_info)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')
                                                            
    return render_template('my_recipme.html', search='category', username=username, my_recipme=recipe_info[0], count=recipe_info[1], 
                                                    cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1], 
                                                    public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                                                    category=category, category_item=table, results=pagination_results, 
                                                    page=page, per_page=per_page, pagination=pagination)
    
# ALL RECIPES FOR A GIVEN INGREDIENT #
@app.route('/my_recipme/<username>/search', methods=['GET','POST'])
def ingredient_search(username):
    if request.method == 'POST':
        ingredient = request.form['Ingredient']
        order_by, direction = request.form['SortBy'], request.form['Direction']

        return redirect('/my_recipme/%s/search/%s/%s/%s'% (username, ingredient, order_by, direction))
  
# ALL RECIPES FOR A GIVEN INGREDIENT PAGINATE #
@app.route('/my_recipme/<username>/search/<ingredient>/<order_by>/<direction>')
def ingredient_paginate(username, ingredient, order_by, direction):
    user_id = Get().get_user_id(username)['UserId']
    recipe_info = ViewVariables(username).var_ing_search('User.UserId', user_id, ingredient, order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')
    #print(pagination_results)

    return render_template('my_recipme.html', search='ingredient', username=username, 
                            ingredient=ingredient, my_recipme=recipe_info[0], count=recipe_info[1],
                            cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1],
                            public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                            results=pagination_results, page=page, per_page=per_page, pagination=pagination)

# ALL RECIPES SAVED BY USER #                            
@app.route('/my_recipme/<username>/saved_recipe', methods=['GET', 'POST'])
def saved_search(username):
    if request.method =='POST':
        order_by, direction = request.form['SortBy'], request.form['Direction']

        return redirect('/my_recipme/%s/saved_recipe/%s/%s' % (username, order_by, direction))                     

# ALL RECIPES SAVED BY USER PAGINATE #
@app.route('/my_recipme/<username>/saved_recipe/<order_by>/<direction>')
def saved_paginate(username, order_by, direction):
    user_id = Get().get_user_id(username)['UserId']
    recipe_info = ViewVariables(username).var_saved_recipes(user_id, order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')

    return render_template('my_recipme.html', search='saved', username=username,
                            my_recipme=recipe_info[0], count=recipe_info[1],
                            cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1],
                            public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                            results=pagination_results, page=page, per_page=per_page, pagination=pagination)

############### PUBLIC SEARCH ROUTES ##########################

# ALL PUBLIC RECIPES #  

@app.route('/my_recipme/<username>/public')
def public(username):
    recipe_groups = ViewVariables(username).groupings()
    return render_template('public_recipes.html', search=False, username=username, cuisines=recipe_groups[0][0], 
                            courses=recipe_groups[0][1], public_cuisines=recipe_groups[1][0], 
                            public_courses=recipe_groups[1][1])
                                    
@app.route('/my_recipme/<username>/all_public', methods=['GET', 'POST'])
def all_public(username):
    if request.method == 'POST':
        order_by, direction = request.form['SortBy'], request.form['Direction']

        return redirect ('/my_recipme/%s/all_public/%s/%s' % (username, order_by, direction))

# ALL PUBLIC RECIPES PAGINATE # 
@app.route('/my_recipme/<username>/all_public/<order_by>/<direction>')
def public_paginate(username, order_by, direction):
    recipe_info = ViewVariables(username).var_all_public(order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')

    return render_template('public_recipes.html', search='all_public', username=username, my_recipme=recipe_info[0], 
                                count=recipe_info[1], cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1], 
                                public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                                results=pagination_results, page=page, per_page=per_page, pagination=pagination)
    

# ALL PUBLIC RECIPES FOR GIVEN CATEGORY #
@app.route('/my_recipme/<username>/category_public', methods=['GET', 'POST'])
def category_public(username):
    if request.method == 'POST':
        order_by, direction = request.form['SortBy'], request.form['Direction']
        keys = [key for key in request.form]
        table, column = keys[2], keys[2] + 'Name'
        category = request.form[table]
       
        return redirect ('/my_recipme/%s/category_public/search/%s/%s/%s/%s/%s' % (username, table, column, category,
                                                                            order_by, direction))

# ALL PUBLIC RECIPES FOR GIVEN CATEGORY PAGINATE #
@app.route('/my_recipme/<username>/category_public/search/<table>/<column>/<category>/<order_by>/<direction>')
def category_public_paginate(username, table, column, category, order_by, direction):
    recipe_info = ViewVariables(username).var_cat_search(table, 'MakePublic', 1, column, category, order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')
                                                            
    return render_template('public_recipes.html', username=username, search='category_public', my_recipme=recipe_info[0], count=recipe_info[1], 
                                                    cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1], 
                                                    public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                                                    category=category, category_item=table, results=pagination_results, 
                                                    page=page, per_page=per_page, pagination=pagination)

# ALL PUBLIC RECIPES FOR A GIVEN INGREDIENT #
@app.route('/my_recipme/<username>/search_public', methods=['GET','POST'])
def ingredient_search_public(username):
    if request.method == 'POST':
        ingredient = request.form['Ingredient']
        order_by, direction = request.form['SortBy'], request.form['Direction']

        return redirect('/my_recipme/%s/search/public/%s/%s/%s'% (username, ingredient, order_by, direction))

# ALL PUBLIC RECIPES FOR A GIVEN INGREDIENT PAGINATE #
@app.route('/my_recipme/<username>/search/public/<ingredient>/<order_by>/<direction>')
def public_ingredient_paginate(username, ingredient, order_by, direction):
    # VALUE OF 1 IN SEARCH FUNCTION REPRESENTS MAKE PUBLIC VALUE OF 'YES' #
    recipe_info = ViewVariables(username).var_ing_search('MakePublic', 1, ingredient, order_by, direction)
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    pagination_results = Get().get_results(recipe_info[0], offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=recipe_info[1], css_framework='bootstrap4')

    return render_template('public_recipes.html', search='ingredient_public', username=username, 
                            ingredient=ingredient, my_recipme=recipe_info[0], count=recipe_info[1],
                            cuisines=recipe_info[2][0][0], courses=recipe_info[2][0][1],
                            public_cuisines=recipe_info[2][1][0], public_courses=recipe_info[2][1][1],
                            results=pagination_results, page=page, per_page=per_page, pagination=pagination)
 
############### FULL RECIPE VIEW ##############################

@app.route('/my_recipme/<username>/redirect', methods=['GET', 'POST'])
def full_redirect(username):
    if request.method == 'POST':
        recipe_id = request.form['RecipeId']

        return redirect('/my_recipme/%s/%s'% (username, recipe_id))

@app.route('/my_recipme/<username>/<recipe_id>')
def full_recipe(username, recipe_id):
    full_recipe = ViewVariables(username).var_full_recipe(recipe_id)
    
    return render_template('full_recipe_partial.html', username=username, 
                                                        full_recipe=full_recipe, recipe_id=recipe_id)

############### CREATE RECIPE ROUTES #############################

## ADD RECIPE FOR GIVEN USER##
@app.route('/my_recipme/<username>/add_recipe')
def add_recipe(username):  
    return render_template('add_recipe.html',username=username)

## RECIPE FORM SUBMISSION AND REDIRECT TO USER MY RECIPME PAGE ##
@app.route('/my_recipme/<username>/create_recipe', methods=['GET', 'POST'])
def creating_recipe(username):
    if request.method == 'POST':
        recipe = request.form
        user_id = Get().get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,
                            request.form.getlist('Quantity')]
        write_recipe.Create().write_full_recipe(recipe, user_id, ingredient_list, method_list)
        return redirect('my_recipme/edit/%s/%s'% (username, 'create'))

## ROUTE TO SHOW SUCESSFUL UPLOAD/EDIT OF RECIPE ##
@app.route('/my_recipme/edit/<username>/<action>')
def recipe_action(username, action):
    return render_template('crud_action.html', username=username, action=action)

############## UPDATE RECIPE ROUTES #########################

# EDIT RECIPE VIEW #
@app.route('/my_recipme/<username>/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(username, recipe_id):
    full_recipe = ViewVariables(username).var_full_recipe(recipe_id)
    title = full_recipe[1][0]['RecipeTitle']
    return render_template('edit_recipe.html', username=username, 
                            full_recipe=full_recipe, title=title, recipe_id=recipe_id)

# UPDATING RECIPE, REDIRECT TO RECIPE CRUD ACTION VIEW #
@app.route('/my_recipme/<username>/updating_recipe/<recipe_id>', methods=['GET', 'POST'])
def updating_recipe(username, recipe_id):
    if request.method == 'POST':
        recipe = request.form
        user_id = Get().get_user_id(username)
        method_list = [request.form.getlist('StepNumber'),
                        request.form.getlist('Step')]
        ingredient_list = [request.form.getlist('Ingredient'),user_id,
                            request.form.getlist('Quantity')]
        write_recipe.Update().update_recipe_and_stats(recipe, user_id, recipe_id)
        write_recipe.Update().update_ingredients_and_method(recipe_id, ingredient_list, 
                                                            method_list)

    return redirect('/my_recipme/edit/%s/%s'% (username, 'update'))
        
############## DELETE RECIPE ROUTE ##########################

@app.route('/my_recipme/<username>/delete_recipe', methods=['GET', 'POST'])
def delete_recipe(username):
    if request.method == 'POST':
        table = 'Recipe'
        QueryDeleteRecipe(request.form['RecipeId'], table).delete()
        

        return redirect('my_recipme/edit/%s/%s'%(username, 'delete'))

############# SAVED RECIPE ROUTE ############################

@app.route('/my_recipme/<username>/save_recipe/<recipe_id>', methods=['GET','POST'])
def save_recipe(username, recipe_id):
    if request.method == 'POST':
        saved = int(request.form['Saved'])
        ViewFunc().save_or_unsave_recipe(saved, username, recipe_id)
        return redirect('/my_recipme/%s/%s' % (username, recipe_id))


########### RATE RECIPE ROUTE ##############################

@app.route('/my_recipme/<username>/rate/<recipe_id>', methods=['GET', 'POST'])
def rate_recipe(username, recipe_id):
    if request.method == 'POST':
        rating = request.form
        ViewFunc().rate_recipe(rating, recipe_id, username)
        return redirect('/my_recipme/%s/%s' % (username, recipe_id)) 



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
"""

port = int(os.environ.get("PORT",5000))
##host = int(os.environ.get("IP",0.0.0.0))

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port = port)

"""