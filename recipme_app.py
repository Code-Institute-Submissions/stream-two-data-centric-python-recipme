import os
import pymysql
import myenviron
import json
import db_create
from db_read import user_verify
from db import db
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
    ############### IF THE USERNAME DOESN'T EXIST SIGN UP ###########
    existing_user = get_existing_user(user_values)
    if existing_user == []:
        create_user(user_values)
        return True
    elif existing_user[0]['Username'] == user_values['Username']:
        print('Username taken, enter a unique username')
        return False
      
def user_login(user_values):
    ############## IF THE USERNAME AND PASSWORD MATCH LOGIN ###########
    existing_user = get_existing_user(user_values)
    if existing_user != []:
        if existing_user[0]['Username'] == user_values['Username']:
            if existing_user[0]['Password'] == user_values['Password']:
                return True
    else:
        return False
        
   

################################# ROUTES ###########################################    

################################# LOGIN ROUTES #####################################

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_values = request.form
        new_user = sign_up(user_values)
        print(user_values)
        if new_user == True:
            return redirect('my_recipme')
        else:
            return redirect('user_taken') 

@app.route('/user_taken', methods=['GET', 'POST'])
def user_taken():    
    return render_template('user_taken.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_values = request.form
        returning_user = user_login(user_values)
        print(user_values)
        if returning_user == True:
            return redirect('my_recipme')
        else:
            return redirect('invalid_login')

@app.route('/invalid_login', methods=['GET', 'POST'])
def invalid_login():
    return render_template('invalid_login.html')
    
@app.route('/my_recipme')
def my_recipme():
    return render_template('my_recipme.html')

###################### NEED TO PASS USERNAME AND ID THROUGH TO REDIRECT TO MY RECIPE ################

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port = os.getenv('PORT'), debug=True)