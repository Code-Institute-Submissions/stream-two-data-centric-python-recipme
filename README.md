# Stream Two Data Centric Python Project - Online Cookbook
 
## Create a web application that allows users to store and easily access cooking recipes.
	
	The main aims of the application are: 
		
	1. To allow a user to create an account, be able to store their favourite recipes, and edit or delete them.
	2. To allow a user to search their own recipes based on ingredient, cuisine or course and be able to sort the results 		according to certain criteria.	
	3. To allow users to share their recipe with the wider community, and be able to search other users recipes.
	4. To allow users to comment and rate other users recipes.
	5. To be simple to use and user friendly.

## Demo

A live demo of the site is available [here] (https://stream-two-recipme-cookbook.herokuapp.com/). A github repo of the application is available [here] (https://github.com/darchard1984/stream-two-data-centric-python-recipme).

## Getting Started/Deployment

* If you wish to run this site locally, please clone or download this repo. Navigate to your local directory and then run "my_recipe.py" in your terminal. You will have to set your own environment variables and local server config to do so. You will also need to provision your own MySQL DB and run the MYSQL script to create the necessary schema.
* If you wish to deploy a live version of this site, then you will need to create your own Heroku repo/app (or the same on a similar hosting platform) and re-deploy the repo.


## Built With 

** VSCODE, HTML, CSS, SASS/SCSS, FLEXBOX, JAVASCRIPT, PYTHON3, MYSQL, FLASK, JINJA, PHOTOSHOP, BALSAMIQ.

## UX Design

Details of the UX design and research process is available in the repo "documentation" folder. The documents show how I approached the design of the site using the 5 layers approach. (Strategy, Structure, Scope, Skeleton, Surface). 

## Build Approach

1. I began the build by first designing the MYSQL Schema. Using the 3 phases approach I first worked on a conceptual model, thorugh to a logical model before writing scripts and commands to create a physial MySQL DB. 
2. I built a local MySQL DB first, and using terminal wrote basic CRUD SQL Commands to populate the tables, modify and delete them, making sure the relationshps between each table were correct before moving on. At this point some changes were made to better suit my needs.
3. After this, I concentrated on writing all the necessary Python backend code to carry out CRUD Operations on the tables. At this point I didn't take any UI input from the Front End. I wanted to get all the necessary CRUD functionality written first, hardcoding input to tables at this stage. I wanted to make sure data to and from the DB was behaving as expected. A TDD approach to this phase carried where possible.
4. Once happy with the my backend functionality. I provisioned a remoted DB on Heroku using ClearDB. 
5. I decided to split my CRUD operations into separate modules. 
	- db.py - Class containing the main DB connection which is called on by all CRUD operations. 
	- db_read.py - Classes containing code which carries out read queries on the DB.
	- db_create.py - Classes containing code which carry out create queries on the DB.
	- db.update_delete - Classes containg code which carry out update and delete queries on the db.
6. At this point I began to build the front end functionality. Starting with basic unstyled forms to provide the input for user login, signup, recipe creation, recipe editing or deletion. 
7. I then began connecting the Front End forms with views. 
8. As the development continued I found it necessary to further split my code into modules. 
	- find_recipe.py - Classes containing code that does something with a db_read.py class or function.
	- write_recipe.py - Classes containing code that does something with a db_create.py class or function.
	- view_var.py - Classes that contain code called by views to return variables, or do something that a view needs to do to return data to a 		template or to/from the db.
	- recipme_app.py - View functions.
9. Once happy with the backend, I began applying styles and JS to the front end. 
10. I again found it necessary to split my JS into separate files. 
	- classes.js - contains classes used by multiple templates.
	- each_page.js - each URL has it's own JS file which calls on classes/functions contained in the classes.js script sheet.
11. I again tried to write classes and functions that are able to be utlised more than once.
12. All styles are custom and the grid system is Flexbox.
131. I used http://pleeease.io/play/ to generate vendor prefixes once the building of the application was complete. This allowed me to concentrate on writing clean SCSS until ready for submission/deployment.


## Testing

Automated, manual and technical testing of the site was undertaken and passed. 

1. Python Unit Tests were undertaken as I built the logic of the application. All tests pass.
2. Chrome/Firefox dev tools used throughout to test JS, responsiveness and function.
3. Testing the site across different devices in real world scenarios. Mobiles, Tablets, Laptops, and Desktops.
4. Giving the applcation to third party users to get feedback, and see if they could "break" the application.
5. W3C code validator to pass HTML, CSS and JS. 


## Authors

** Dafydd Archard ** this application was created as part of Code Institute's Web Development Online Full-Stack Course in June 2018.

## Acknowledgments

1. http://pleeease.io/play/
2. w3c Validator service
3. Stack Overflow








