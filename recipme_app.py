import os
import pymysql
import myenviron
import json
import db_create
from db_read import db, user_verify
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

##################### LOGIN/SIGNUP FUNCTIONS ##########################

def create_user(user_values):
    ################ CREATE A NEW USER ################################
    new_user = db_create.query_create_user(user_values)
    new_user.create_user()
    return user_values

def get_existing_user(user_values):
    ############### SEARCH USER TABLE FOR USER AND RETURN RESULT ######
    new_verify = user_verify(user_values)
    existing_user = new_verify.query_username_and_password()
    return existing_user

def sign_up(user_values):
    ############### IF THE USERNAME DOESN'T EXIST 
    existing_user = get_existing_user(user_values)
    print(existing_user)
    if existing_user == []:
        create_user(user_values)
        print('user created')
        return True
    else:
        print('Username taken, enter a unique username')
        return False
      
def user_login(user_values):
    existing_user = get_existing_user(user_values)
    print(existing_user)
    if existing_user[0]['Username'] == user_values['Username']:
        if existing_user[0]['Password'] == user_values['Password']:
            return True
    else:
        return False    

################################# ROUTES ###########################################    


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        print(user_values)
        new_user = sign_up(user_values)
        print(new_user)
        if new_user == True:
            return redirect('my_recipme')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values = request.form
        returning_user = user_login(user_values)
        print(user_values)
        if returning_user == True:
            return redirect('my_recipme')
        else:
            return False ##### NEED TO RETURN A REDIRECT FOR INCORRECT LOGIN ######
    #return render_template('my_recipme.html')

@app.route('/my_recipme')
def my_recipme():
    return render_template('my_recipme.html')

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)