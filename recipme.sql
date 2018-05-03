/***************** CREATE DATA-BASE *********************/
/*DROP DATABASE IF EXISTS `heroku_4d0654e61ed0a78`;

CREATE DATABASE `heroku_4d0654e61ed0a78`;*/
/*
USE `heroku_8956bc974ce0fed`;

DROP TABLE `Cuisine`;
DROP TABLE `Course`;
DROP TABLE `Rating`;
DROP TABLE `Health`;
DROP TABLE `Ingredient`;
DROP TABLE `Cost`;
DROP TABLE `Method`;
DROP TABLE `Servings`;
DROP TABLE `Recipe`;
DROP TABLE `User`;
DROP TABLE `SavedRecipes`;

SHOW TABLES;


/******************* CREATE TABLES ******************************/
/*
CREATE TABLE `User`
(
    `UserId` INT NOT NULL AUTO_INCREMENT,
    `Username` NVARCHAR(160) NOT NULL,
    `First` NVARCHAR(30) NOT NULL,
    `Last` NVARCHAR(30) NOT NULL,
    `Password` NVARCHAR(30) NOT NULL,
    CONSTRAINT `PK_User` PRIMARY KEY (`UserId`)
);

CREATE TABLE `Recipe`
(
    `RecipeId` INT NOT NULL AUTO_INCREMENT,
    `RecipeTitle` NVARCHAR(160) NOT NULL,
    `Created` DATETIME NOT NULL,
    `ImageURL` NVARCHAR(500) DEFAULT 'NONE',
    `RecipeDescription` NVARCHAR (500) NOT NULL,
    `CookingTimeMins` INT NOT NULL,
    `MakePublic` BOOLEAN NOT NULL,
    `UserId` INT NOT NULL,
    CONSTRAINT `PK_Recipe` PRIMARY KEY (`RecipeId`)
);

CREATE TABLE `Cuisine`
(
    `CuisineId` INT NOT NULL AUTO_INCREMENT,
    `CuisineName` NVARCHAR(160) NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Cuisine` PRIMARY KEY (`CuisineId`)
);

CREATE TABLE `Course`
(
    `CourseId` INT NOT NULL AUTO_INCREMENT,
    `CourseName` NVARCHAR(160) NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Course` PRIMARY KEY (`CourseId`)
);

CREATE TABLE `Rating`
(
    `RatingId` INT NOT NULL AUTO_INCREMENT,
    `Rating` INT NOT NULL,
    `Comments` NVARCHAR(2000),
    `RecipeId` INT NOT NULL,
    `UserId` INT NOT NULL,
    CONSTRAINT `PK_Rating` PRIMARY KEY (`RatingId`)
);

CREATE TABLE `Health`
(
    `HealthId` INT NOT NULL AUTO_INCREMENT,
    `Calories` INT NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Health` PRIMARY KEY (`HealthId`)
);

CREATE TABLE `Ingredient`
(
    `IngredientId` INT NOT NULL AUTO_INCREMENT,
    `UserId` INT NOT NULL,
    `RecipeId` INT NOT NULL,
    `IngredientName` NVARCHAR(200) NOT NULL,
    `Quantity` NVARCHAR(200) NOT NULL,
    CONSTRAINT `PK_Ingredient` PRIMARY KEY (`IngredientId`)
);

CREATE TABLE `Cost`
(
    `CostId` INT NOT NULL AUTO_INCREMENT,
    `Price` INT NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Cost` PRIMARY KEY (`CostId`)
);

CREATE TABLE `Method`
(
    `MethodId` INT NOT NULL AUTO_INCREMENT,
    `StepNumber` INT NOT NULL,
    `StepDescription` TEXT NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Method` PRIMARY KEY (`MethodId`)
);

CREATE TABLE `Servings`
(
    `ServingsId` INT NOT NULL AUTO_INCREMENT,
    `Servings` INT NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_Servings` PRIMARY KEY (`ServingsId`)
);

CREATE TABLE `SavedRecipes`
(   
    `SavedRecipesId` INT NOT NULL AUTO_INCREMENT,
    `UserId` INT NOT NULL,
    `RecipeId` INT NOT NULL,
    CONSTRAINT `PK_SavedRecipes` PRIMARY KEY (`SavedRecipesId`)
);
*/
/******************* CREATE FOREIGN KEYS ******************************/
/*
ALTER TABLE `Recipe` ADD CONSTRAINT `FK_RecipeUserId`
    FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX `IFK_RecipeUserId` ON `Recipe` (`UserId`);


ALTER TABLE `Cuisine` ADD CONSTRAINT `FK_CuisineRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_CuisineRecipeId` ON `Cuisine` (`RecipeId`);


ALTER TABLE `Course` ADD CONSTRAINT `FK_CourseRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_CourseRecipeId` ON `Course` (`RecipeId`);


ALTER TABLE `Rating` ADD CONSTRAINT `FK_RatingRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_RatingRecipeId` ON `Rating` (`RecipeId`);

ALTER TABLE `Rating` ADD CONSTRAINT `FK_RatingUserId`
    FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX `IFK_RatingUserId` ON `Rating` (`UserId`);


ALTER TABLE `Health` ADD CONSTRAINT `FK_HealthRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_HealthRecipeId` ON `Health` (`RecipeId`);


ALTER TABLE `Ingredient` ADD CONSTRAINT `FK_IngredientRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe`(`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_IngredientRecipeId` ON `Ingredient`(`RecipeId`);


ALTER TABLE `Ingredient` ADD CONSTRAINT `FK_IngredientUserId`
    FOREIGN KEY (`UserId`) REFERENCES `User`(`UserId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_IngredientUserId` ON `Ingredient`(`UserId`);


ALTER TABLE `Cost` ADD CONSTRAINT `FK_CostRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_CostRecipeId` ON `Cost` (`RecipeId`);


ALTER TABLE `Method` ADD CONSTRAINT `FK_MethodRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_MethodRecipeId` ON `Method` (`RecipeId`);

ALTER TABLE `Servings` ADD CONSTRAINT `FK_ServingsRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_ServingsRecipeId` ON `Servings` (`RecipeId`);


ALTER TABLE `SavedRecipes` ADD CONSTRAINT `FK_SavedRecipesRecipeId`
    FOREIGN KEY (`RecipeId`) REFERENCES `Recipe` (`RecipeId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_SavedRecipesRecipesId` ON `SavedRecipes` (`RecipeId`);


ALTER TABLE `SavedRecipes` ADD CONSTRAINT `FK_SavedRecipesUserId`
    FOREIGN KEY (`UserId`) REFERENCES `User` (`UserId`) ON DELETE CASCADE ON UPDATE NO ACTION;

CREATE INDEX `IFK_SavedRecipesUserId` ON `SavedRecipes` (`UserId`);





/************************ TEST INSERT DATA ************************************/
/*

INSERT INTO `User` (`Username`,`First`,`Last`,`Password` ) VALUES ('darchard', 'Dafydd','Archard','password');

INSERT INTO `Recipe` (`RecipeTitle`,`Created`,`RecipeDescription`, `CookingTimeMins` ,`UserId`, `MakePublic`) VALUES ('BEANS ON TOAST',NOW(),'Beans on Toast with brown sauce',10,1,1);

INSERT INTO `Cuisine` (`CuisineName`,`RecipeId` ) VALUES ('British', 1);

INSERT INTO `Course` (`CourseName`,`RecipeId`) VALUES ('Lunch', 1);

INSERT INTO `Rating` (`Rating`,`Comments`,`RecipeId`,`UserId`) VALUES (5,'Loveley stuff',1,1);

INSERT INTO `Health` (`Calories`,`RecipeId`) VALUES (500,1);

INSERT INTO `Cost` (`Price`, `RecipeId`) VALUES (10,1);

INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Baked Beans',1,1,'One tin');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Sliced Bread',1,1,'2 Slices');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Butter',1,1,'To taste');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Brown Sauce',1,1,'To taste');

INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (1, 'Slice Bread', 1);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (2, 'Toast Bread', 1);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (3, 'Heat Beans', 1);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (4, 'Butter Bread', 1);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (5, 'Pour Beans and add sauce to taste', 1);

INSERT INTO `Servings`(`Servings`,`RecipeId`) VALUES (4, 1);


INSERT INTO `User` (`Username`,`First`,`Last`,`Password` ) VALUES ('fulph', 'Frances','Ulph','password');

INSERT INTO `Recipe` (`RecipeTitle`,`Created`,`RecipeDescription`,`CookingTimeMins`,`UserId`, `MakePublic`) VALUES ('Poached Eggs with Asparagus',NOW(),'Poached Eggs with Asparagus',15, 11,1);

INSERT INTO `Cuisine` (`CuisineName`,`RecipeId` ) VALUES ('British', 11);

INSERT INTO `Course` (`CourseName`,`RecipeId`) VALUES ('Breakfast', 11);

INSERT INTO `Rating` (`Rating`,`Comments`,`RecipeId`,`UserId`) VALUES (4,'Nice and Light',11,11);

INSERT INTO `Health` (`Calories`,`RecipeId`) VALUES (250,11);

INSERT INTO `Cost` (`Price`,`RecipeId`) VALUES (10,11);

INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Eggs',11,11,'Two Medium');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Muffins',11,11,'One halved');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Butter',11,11,'To taste');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Asparagus',11,11,'To taste');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('Salt and Pepper',11,11,'To taste');
INSERT INTO `Ingredient` (`IngredientName`,`UserId`,`RecipeId`,`Quantity`) VALUES ('White Wine Vinegar',11,11,'To taste');

INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (1, 'Boil Water, add splash of vinegar and add salt to taste', 11);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (2, 'Crack eggs into cup, slowly introduce to water, boil for 3-5 mins', 11);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (3, 'Add Aparagus to grill pan with salt and pepper, knob of butter and fry for 5 min', 11);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (4, 'Toast Muffins', 11);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (5, 'Butter Muffins, lay Asparagus on top of the muffins with eggs on top and serve.', 11);

INSERT INTO `Servings`(`Servings`,`RecipeId`) VALUES (2, 11);

INSERT INTO `Recipe` (`RecipeTitle`,`Created`,`RecipeDescription`,`CookingTimeMins`,`UserId`, `MakePublic`) VALUES ('Bacon Sandwich',NOW(),'Bacon Sandwich with Ketchup',15, 11,1);

INSERT INTO `Cuisine` (`CuisineName`,`RecipeId` ) VALUES ('British', 21);

INSERT INTO `Course` (`CourseName`,`RecipeId`) VALUES ('lUNCH', 21);

INSERT INTO `Rating` (`Rating`,`Comments`,`RecipeId`,`UserId`) VALUES (4,'Yummm!',21,11);

INSERT INTO `Health` (`Calories`,`RecipeId`) VALUES (550,21);

INSERT INTO `Cost` (`Price`,`RecipeId`) VALUES (5,21);

INSERT INTO `Ingredient` (`IngredientName`,`RecipeId`,`Quantity`) VALUES ('Bacon',21,'Four Rashers');
INSERT INTO `Ingredient` (`IngredientName`,`RecipeId`,`Quantity`) VALUES ('White Rolls',21,'One');
INSERT INTO `Ingredient` (`IngredientName`,`RecipeId`,`Quantity`) VALUES ('Butter',21,'To taste');
INSERT INTO `Ingredient` (`IngredientName`,`RecipeId`,`Quantity`) VALUES ('Ketchup',21,'To taste');

INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (1, 'Place bacon under the grill and cook until crispy', 21);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (2, 'Slice Bread and butter', 21);
INSERT INTO `Method` (`StepNumber`,`StepDescription`,`RecipeId`) VALUES (3, 'Add sauce to taste', 21);

INSERT INTO `Servings`(`Servings`,`RecipeId`) VALUES (1, 21);
*/
/*###############################################################*/

INSERT INTO `SavedRecipes` (`RecipeId`, `UserId`) VALUES (1,11);

SHOW TABLES;
