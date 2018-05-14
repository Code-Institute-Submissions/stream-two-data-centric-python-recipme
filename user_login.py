import os
import db_create
from db_read import UserVerify, QueryReadRecipes

###################################################################################
##################### LOGIN/SIGNUP FUNCTIONS ######################################
###################################################################################

 ################ CREATE A NEW USER ################################
 
class LogIn():

    def __init__(self, user_values):
        self.user_values = user_values
         
    def create_user(self):
        new_user = db_create.QueryCreateUser(self.user_values)
        new_user.create_user()
        return self.user_values

    ############### SEARCH USER TABLE FOR USER AND RETURN RESULT ######

    def get_existing_user(self):
        print(self.user_values)
        new_verify = UserVerify(self.user_values)
        existing_user = new_verify.query_user()

        return existing_user
        
    ############### IF THE USERNAME DOESN'T EXIST SIGN UP ###########

    def sign_up(self):
        existing_user = LogIn.get_existing_user(self)
        if existing_user == []:
            LogIn.create_user(self)
            return True
        elif existing_user[0]['Username'] == self.user_values['Username']:
            print('Username taken, enter a unique username')
            return False

    ############## IF THE USERNAME AND PASSWORD MATCH LOGIN ###########

    def user_login(self): 
        existing_user = LogIn.get_existing_user(self)
        if existing_user != []:
            if existing_user[0]['Username'] == self.user_values['Username']:
                if existing_user[0]['Password'] == self.user_values['Password']:
                    return True
        else:
            return False
        



