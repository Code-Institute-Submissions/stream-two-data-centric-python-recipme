import os
import db_create
from db_read import user_verify, query_read_recipes


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




