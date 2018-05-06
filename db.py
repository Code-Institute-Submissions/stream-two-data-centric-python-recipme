import os
import pymysql
import myenviron
######## TO GO BACK REMOVE THE CONNECTION FROM A SELF INITIALISING class and into s basic class #######
class db():
    def __init__(self, *args, commit=False):
        self.connection = pymysql.connect(host=os.environ.get('DATABASE_HOST'), 
                                            port=3306, user=os.environ.get('DATABASE_USER'),
                                            password=os.environ.get('DATABASE_PASSWORD'), 
                                            db=os.environ.get('DATABASE_NAME'))
        self.commit = commit
        self.cursor = self.connection.cursor(*args)
    def __enter__(self):
        
        return self.cursor
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

class query():
    
    select = """SELECT RecipeTitle, Recipe.RecipeId as RecipeId, RecipeDescription, 
                        CookingTimeMins, Created, ImageURL, 
                        Price, Servings, CuisineName, Calories, 
                        CourseName, User.Username as Author"""

    main_selection = select + """
                                FROM Recipe 
                                JOIN User on Recipe.UserId = User.UserId
                                JOIN Cost on Recipe.RecipeId = Cost.RecipeId
                                JOIN Servings on Recipe.RecipeId = Servings.RecipeId
                                JOIN Cuisine on Recipe.RecipeId = Cuisine.RecipeId
                                JOIN Health on Recipe.RecipeId = Health.RecipeId
                                JOIN Course on Recipe.RecipeId = Course.RecipeId 
                                """

    search_ingredient =  select + """
                                    FROM Ingredient
                                    JOIN Recipe on Ingredient.RecipeId = Recipe.RecipeId
                                    JOIN Cost on Ingredient.RecipeId = Cost.RecipeId
                                    JOIN Servings on Ingredient.RecipeId = Servings.RecipeId
                                    JOIN Cuisine on Ingredient.RecipeId = Cuisine.RecipeId
                                    JOIN Health on Ingredient.RecipeId = Health.RecipeId
                                    JOIN Course on Ingredient.RecipeId = Course.RecipeId
                                    JOIN User on Ingredient.UserId = User.UserId 
                                    """


    saved_recipes = select + """
                                FROM SavedRecipes
                                JOIN Recipe on SavedRecipes.RecipeId = Recipe.RecipeId
                                JOIN Cost on SavedRecipes.RecipeId = Cost.RecipeId
                                JOIN Servings on SavedRecipes.RecipeId = Servings.RecipeId
                                JOIN Cuisine on SavedRecipes.RecipeId = Cuisine.RecipeId
                                JOIN Health on SavedRecipes.RecipeId = Health.RecipeId
                                JOIN Course on SavedRecipes.RecipeId = Course.RecipeId
                                JOIN User on Recipe.UserId = User.UserId
                                """

    
