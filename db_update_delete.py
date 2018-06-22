import pymysql
from datetime import datetime
from db import Db, WriteErrorToLog, log_file
from db_create import QueryCreateRecipe, QueryCreateMethodItems

####################### CLASS FOR SQL QUERY TO DELETE RECIPE BASED ON RECIPE ID #########################

class QueryDeleteRecipe():
    
    def __init__(self, recipe_id, table):
        self.recipe_id = recipe_id
        self.table = table
         
    def delete(self):
        try:
            with Db(commit=True) as cursor:            
                cursor.execute(""" DELETE FROM %s 
                                    WHERE RecipeId = %s; 
                                """ % (self.table, self.recipe_id))
        except pymysql.err.OperationalError as e:
            message = " FAILED: delete method in db_read.QueryDeleteRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("delete completed")
    
    def delete_saved_recipe(self, user_id):
        try:
            with Db(commit=True) as cursor:
                cursor.execute(""" DELETE FROM %s
                                    WHERE UserId = %s
                                    AND RecipeId = %s;""" % (self.table, user_id, self.recipe_id))
        except pymysql.err.OperationalError as e:
            message = " FAILED: delete_saved_recipe in db_read.QueryDeleteRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("delete_saved_recipe completed")

############################### CLASS FOR SQL UPDATE QUERIES ############################################
#########################################################################################################

class UpdateQuery():
    
    recipe_query = """ UPDATE Recipe SET 
                        RecipeTitle = %s,
                        RecipeDescription = %s,
                        CookingTimeMins = %s,
                        MakePublic = %s
                        WHERE RecipeId = %s;
                    """

    def single_column_query(self, table, column, column_value, recipe_id):
        query = """ UPDATE %s SET
                    %s = '%s'
                    WHERE RecipeId = %s;
                """ % (table, column, column_value, recipe_id)
        return query

###################### CLASS FOR EXECUTING UPDATE QUERIES TO RECIPE TABLE AND STATS TABLES ###############

class QueryUpdateRecipe(QueryCreateRecipe):

    def __init__(self, recipe, user_id, recipe_id):
        super().__init__(recipe, user_id)
        self.recipe_id = recipe_id

    def update_recipe(self):
        recipe_values = (self.recipe_title, self.recipe_description,
                            self.cooking_time, self.make_public, self.recipe_id)
        try:
            with Db(commit=True) as cursor:
                cursor.execute(UpdateQuery.recipe_query, recipe_values)
        except pymysql.err.OperationalError as e:
            message = " FAILED: update_recipe in db_read.QueryUpdateRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("update_recipe completed")

    def update_stats(self):
        stat_queries = [[UpdateQuery.single_column_query(self,'Cuisine','CuisineName', 
                                                        self.cuisine_name, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Course','CourseName', 
                                                        self.course_name, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Health','Calories', 
                                                        self.calories, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Cost','Price',
                                                         self.cost, self.recipe_id)],
                    [UpdateQuery.single_column_query(self,'Servings','Servings', 
                                                        self.servings, self.recipe_id)]]
        try:
            with Db(commit=True) as cursor:
                for stat in stat_queries:
                    cursor.execute(stat[0])
        except pymysql.err.OperationalError as e:
            message = " FAILED: update_recipe in db_read.QueryUpdateRecipes."
            log = WriteErrorToLog(str(e), message, log_file, str(datetime.now()))
            log.write_to_doc()
        else:
            print("update_recipe completed")

     

 