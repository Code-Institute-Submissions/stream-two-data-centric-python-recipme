import pymysql
from db import Db
from math import ceil

################### CLASS FOR HOUSING SQL READ QUERY TABLE SELECTIONS #################
    ## USED FOR USER ALL RECIPES SELECTION, INGREDIENT SEARCH AND SAVED RECIPES ##

class QuerySelections():
    
    def __init__(self):
        
        self.select = """ SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, 
                        CookingTimeMins, Created, ImageURL, Price, Servings, CuisineName, 
                        Calories, CourseName, User.Username as Author, Recipe.UserId, MakePublic """
    
    def main_selection(self) :
        main_selection = self.select + """
                                        FROM Recipe 
                                        JOIN User on Recipe.UserId = User.UserId
                                        JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                        JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                        JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                        JOIN Health on Recipe.RecipeId = Health.RecipeId
                                        JOIN Course on Recipe.RecipeId = Course.RecipeId 
                                        """
        return main_selection

    def search_ingredient(self): 
    
        search_ingredient = self.select + """
                                            FROM Ingredient
                                            JOIN User on Ingredient.UserId = User.UserId 
                                            JOIN Recipe on Ingredient.RecipeId = Recipe.RecipeId
                                            JOIN Cost on Ingredient.RecipeId = Cost.RecipeId
                                            JOIN Servings on Ingredient.RecipeId = Servings.RecipeId
                                            JOIN Cuisine on Ingredient.RecipeId = Cuisine.RecipeId
                                            JOIN Health on Ingredient.RecipeId = Health.RecipeId
                                            JOIN Course on Ingredient.RecipeId = Course.RecipeId
                                            """ 
        return search_ingredient


    def saved_recipes(self):
        saved_recipes = """ SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, 
                                CookingTimeMins, Created, ImageURL, Price, Servings, CuisineName, 
                                Calories, CourseName, Recipe.UserId, MakePublic FROM SavedRecipes
                            JOIN User on User.UserId = SavedRecipes.UserId
                            JOIN Recipe on Recipe.RecipeId = SavedRecipes.RecipeId
                            JOIN Cost on Cost.RecipeId = SavedRecipes.RecipeId
                            JOIN Servings on Servings.RecipeId = SavedRecipes.RecipeId
                            JOIN Cuisine on Cuisine.RecipeId = SavedRecipes.RecipeId
                            JOIN Health on Health.RecipeId = SavedRecipes.RecipeId
                            JOIN Course on Course.RecipeId = SavedRecipes.RecipeId
                        """
        return saved_recipes


########################## CLASS FOR COURSE OR CUISINE CATEGORY SEARCH  ################################
                        ## RE-USABLE FUNCTIONS BASED ON CATEGORY SELECTION ##

class QueryCategory(QuerySelections):
    """ QUERIES FOR CUISINE OR COURSE CATEGORY """
    def __init__(self, table, join_table):
        super().__init__()
        self.table = table
        self.join_table = join_table

    def category_selection(self):
        search_category =  self.select + """
                                        FROM %s
                                        JOIN %s on %s.RecipeId = %s.RecipeId
                                        JOIN Recipe on %s.RecipeId = Recipe.RecipeId
                                        JOIN Cost on %s.RecipeId = Cost.RecipeId
                                        JOIN Servings on %s.RecipeId = Servings.RecipeId
                                        JOIN Health on %s.RecipeId = Health.RecipeId
                                        JOIN User on Recipe.UserId = User.UserId 
                                        """ % (self.table, self.join_table, self.table, self.join_table,
                                                self.table, self.table, self.table, self.table)
        return search_category

########################### CLASS TO EXECUTE QUERIES AND CALL SELECTIONS ###############################

class QueryReadRecipes():

    def query_username_or_id(self, select_column, search_column, value):
        try:
            with Db() as cursor:
                get_id_query = """SELECT %s FROM User
                                    WHERE %s = '%s';""" % (select_column, search_column, value)                  
                cursor.execute(get_id_query)
                username = [row for row in cursor]
                return(username)
        finally:
            print("Query read user completed")

    def query_all_mini_recipes(self, search_by, search_value, order_by, direction):
        """ GET ALL MINI RECIPES ORDERED BY GIVEN USER SELECTION, AND FILTERED BY 
                    GIVEN USER SELECTION, PUBLIC AND USER SPECIFIC  """
        try:
            with Db() as cursor:
                condition = """ WHERE %s = %s 
                                ORDER BY %s %s; """ % (search_by, search_value, 
                                                     order_by, direction) 

                recipes_query = QuerySelections().main_selection() + condition          
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get mini recipes completed")


    def query_category_mini_recipes(self, table, search_by, search_value, 
                                    column, category, order_by, direction):
        """ GET ALL MINI RECIPES FILTERED BY COURSE AND CUISINE, 
            SORTED BY GIVEN USER SELECTION, FOR USER OR PUBLIC FEED """
        print(table )
        join_table = []
        if table == 'Cuisine':
            join_table = 'Course'
        else:
            join_table ='Cuisine'
        try:
            with Db() as cursor:
                condition = """ WHERE %s = %s AND %s = '%s' 
                                ORDER BY %s %s;""" % (search_by, search_value, 
                                                        column, category,
                                                        order_by, direction)                                                           
                new_query = QueryCategory(table, join_table)
                recipes_query = new_query.category_selection() + condition
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get mini recipes completed")

    def query_search_ingredient(self, search_by, search_value, 
                                ingredient, order_by, direction):
        """ GET ALL MINI RECIPES FOR GIVEN INGREDIENT """
        try:
            with Db() as cursor:
                condition = """ WHERE %s = %s 
                                AND MATCH(Ingredient.IngredientName) 
                                AGAINST ('%s' IN NATURAL LANGUAGE MODE)
                                ORDER BY %s %s;""" % (search_by, search_value, 
                                                        ingredient, order_by, direction)
                recipes_query = QuerySelections().search_ingredient() + condition
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get mini recipes completed")

    def query_ingredients_for_full_recipe(self, recipe_id):
        """ GET INGREDIENTS BASED ON GIVEN RECIPE ID """
        try:
            with Db() as cursor:
                recipes_query = """SELECT IngredientName, Quantity, IngredientId FROM Ingredient
                                    WHERE Ingredient.RecipeId = %s;""" % (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get ingredients completed")

    def query_method_for_full_recipe(self, recipe_id):
        """ GET FULL METHOD BASED ON GIVEN RECIPE ID """
        try:
            with Db() as cursor:
                recipes_query = """SELECT StepNumber, StepDescription, MethodId FROM Method
                                    WHERE Method.RecipeId = %s;""" % (recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get method completed")
    
    def query_users_saved_recipes(self, user_id, order_by, direction):
        """ QUERY USERS SAVED RECIPES BASED ON USER ID, GET MINI RECIPES INFO BACK """
        try:
            with Db() as cursor:
                recipes_query = QuerySelections().saved_recipes() + """ 
                                WHERE SavedRecipes.UserId = %s 
                                ORDER BY %s %s;""" % (user_id, order_by, direction)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query get method completed")

    def query_is_recipe_saved(self, user_id, recipe_id):
        """ QUERY IF A USER HAS SAVED A RECIPE """
        try:
            with Db() as cursor:
                recipes_query = """ SELECT * FROM SavedRecipes 
                                    WHERE UserId = %s 
                                    AND RecipeId = %s """ % (user_id, recipe_id)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query is Recipe Saved Complete")
    
    def query_count_and_group_column(self, column, user_id, table):
        """ QUERY THE COUNT OF A SPECIFIC COLUMN FOR A USER, AND GROUP BY THAT COLUMN """
        """ USE FOR GROUPING CUISINE AND COURSE IN RECIPE SEARCH """
        try: 
            with Db() as cursor:
                recipes_query = """ SELECT COUNT(%s) as Total,%s
                                    FROM %s
                                    JOIN Recipe on Recipe.RecipeId = %s.RecipeId
                                    WHERE UserId = %s 
                                    GROUP BY %s;""" % (column, column, table, 
                                                        table, user_id, column)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query count Column based on UserId Completed")
 
    def query_count_and_group_column_public(self, column, value, table):
        """ QUERY THE COUNT OF A SPECIFIC COLUMN FOR A USER, AND GROUP BY THAT COLUMN """
        """ USE FOR GROUPING CUISINE AND COURSE IN RECIPE SEARCH """
        try: 
            with Db() as cursor:
                recipes_query = """ SELECT COUNT(%s) as Total, %s
                                    FROM Recipe
                                    JOIN %s on Recipe.RecipeId = %s.RecipeId
                                    WHERE MakePublic = %s 
                                    GROUP BY %s;""" % (column, column, table, 
                                                        table, value, column)
                cursor.execute(recipes_query)
                recipes = [row for row in cursor]
                return recipes
        finally:
            print("Query count Column based on UserId Completed")


################### CLASS FOR USER DB QUERY  #################

class UserVerify():
    
    def __init__(self, user_values):
        self.username = user_values['Username']
        self.password = user_values['Password']
      
    def query_user(self):
        """ GET USER BASED ON USER INFO """
        try: 
            with Db() as cursor:
                query = """SELECT `Username`,`First`,`Last`,`Password`, `UserId` FROM User
                            WHERE Username = %s;"""
                cursor.execute(query, (self.username))
                from_db = [result for result in cursor]
                return from_db
        finally:
            print('Query User Complete')

######################## CLASS TO QUERY RATINGS TABLE ###################################################

class QueryRating():

    def __init__(self, recipe_id):
        self.recipe_id = recipe_id

    def query_rating_and_comments(self):
        try: 
            with Db() as cursor:
                rating_query = """ SELECT Rating, Comments, Username FROM Rating
                                    JOIN User on Rating.UserId = User.UserId
                                    WHERE Rating.RecipeId = %s; """ 
                cursor.execute(rating_query, self.recipe_id)
                rating = [row for row in cursor]
                return rating
        finally:
            print("Query Ratings based on RecipeId Completed")

######################## CLASSES TO GET STATS ON ALL RECIPES  ###################################################
 
class QueryAllData():
    
    def __init__(self, table, column):
        self.table = table
        self.column = column

    def get_total(self):
        try: 
            with Db() as cursor:
                rating_query = """ SELECT COUNT(%s) as Total%s 
                                    FROM %s; """ % (self.column, 
                                                    self.table, self.table)
                cursor.execute(rating_query)
                rating = [row for row in cursor]
                return rating
        finally:
            print("Query Total table results complete")

    def get_total_public(self):
        try:
            with Db() as cursor:
                query = """SELECT COUNT(%s) as Public%s
                            FROM %s WHERE MakePublic = 1; """ % (self.column, 
                                                                self.table, self.table)
                cursor.execute(query)
                result = [row for row in cursor]
                return result
        finally:
            print("Query get total shared recipes complete")
     

class TotalCuisinesCourses():
    
    def get_all_cuisines_and_courses(self):
        try:
            with Db() as cursor:
                query = """SELECT CuisineName, CourseName 
                            FROM Course
                            JOIN Cuisine on Course.RecipeId = Cuisine.RecipeId;"""
                cursor.execute(query)
                results = [row for row in cursor]
                return results 
        finally:
            print("Query all cuisine and courses complete")  
        