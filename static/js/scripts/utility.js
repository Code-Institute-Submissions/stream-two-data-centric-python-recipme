//---------------------------  GENERAL CLASSES/FUNCTIONS  --------------------------------- // 
//------------------------- BUTTIN CLICK CLASS  ---------------------------------//

class ButtonClick {

    constructor(buttons, style) {

        this.buttons = buttons;
        this.style = style;
        
    }

    singleButtonClick() {
      
        this.buttons.addEventListener('mousedown', () => {
    
            this.buttons.classList.add(`${this.style}`);
        });
    
        this.buttons.addEventListener('mouseup', () => {
    
            this.buttons.classList.remove(`${this.style}`);
        });
    }

    multiButtonsClick() {
        
        for(let i=0; i < this.buttons.length; i++) {
            
            this.buttons[i].addEventListener('mousedown', () => {
                
                this.buttons[i].classList.add(`${this.style}`);

            });

            this.buttons[i].addEventListener('mouseup', () => {

                this.buttons[i].classList.remove(`${this.style}`);

            });

        }

    }

    categoryButtonClick() {

        for (let i=0; i < this.buttons.length; i++) {

            this.buttons[i].addEventListener('click', () => {

                for (let j=0; j < this.buttons.length; j++) {

                    this.buttons[j].classList.remove(`${this.style}`);
                    this.buttons[i].classList.add(`${this.style}`);

                }
            });
        }

    }

    ingredientButtonClick(ingredientButton) {

        const selfButtons = this.buttons;
        const selfStyle = this.style;
        
        ingredientButton.addEventListener('click', () => {

            for (let i=0; i < this.buttons.length; i++) {

                this.buttons[i].classList.remove('search-buttons__button--active');

            }
           

        });

    }

}



 //-------------------------- ACCORDIANS ----------------------------------------//

class NavDropDown {
    // CLASS TO TOGGLE SCSS CLASS FOR ANIMATING BURGER MENU //
    constructor() {

        this.burgerMenu = document.getElementById('burger-menu');
        this.navSideBar = document.getElementById('side-bar');

    }

    clickBurgerMenu() {

        this.burgerMenu.addEventListener('click', () => {

            this.burgerMenu.classList.toggle('alter');
            this.navSideBar.classList.toggle('show-side-bar');
        })
    }

    
}

class Accordian {
    // DROP DOWN FORM AND CLOSE ALREADY OPENED FORM //
    accordian(button, show,  showStyle){

        button.addEventListener('click', () => {

            show.classList.toggle(`${showStyle}`);
            
        });
        
    };

    // SIGN UP FORM ACCORDIAN SECTION //
    formSectionAccordian(button, formsContainer, stingContainer) {
        button.addEventListener('click', () => {

            formsContainer.classList.toggle('forms-login-display');
            stingContainer.classList.toggle('sting--style');
        
        });

    }

    // RECIPME MAIN ACCORDIAN //
    recipemeAccordian(element, showStyle, activeStyle) {
            
        for (let i=0; i < element.length; i++) { // LOOP THROUGH ARRAY OF CONTAINERS ASSIGN EACH TO 'i'

            element[i].addEventListener('click', function() { // ADD EVENT LISTENER

            if (this.nextElementSibling.classList.contains(`${showStyle}`)){ 

                this.classList.remove(`${activeStyle}`);
                this.nextElementSibling.classList.remove(`${showStyle}`); // REMOVE STYLE ON BUTTON
                
            } else {

                for (let j=0; j < element.length; j++) { // LOOP THROUGH CONTAINERS AGAIN BUT ASSIGN TO 'j', REMOVE SHOW STYLE ON J

                    if(element[j].nextElementSibling.classList.contains(`${showStyle}`)){

                        element[j].nextElementSibling.classList.remove(`${showStyle}`);
                        element[j].classList.remove(`${activeStyle}`);
                    }
                }

                this.classList.add(`${activeStyle}`);
                this.nextElementSibling.classList.add(`${showStyle}`); // RE-APPLY SHOW STYLE TO CLICKED 'i'
                
            }

            });
        
        }

    }
}

class StatAccordian {

    constructor(moreInfoButton, statsContainer, moreInfoContainer) { 

        this.moreInfoButton = moreInfoButton;
        this.statsContainer = statsContainer;
        this.moreInfoContainer = moreInfoContainer;
    
    }

// STATS SECTION ACCORDIAN WITH SCROLL TO FUNCTIONALITY //
    statsAccordian(){

        this.moreInfoButton.addEventListener('click', () => {
            
            if (this.statsContainer.classList.contains('stats-show')) {

                //scrollTo(this.moreInfoContainer);
                this.statsContainer.classList.remove('stats-show');
                this.moreInfoContainer.classList.remove('more-info--style');

            } else {
            // getRecipesData('/stats');
                this.statsContainer.classList.add('stats-show');
                this.moreInfoContainer.classList.add('more-info--style');
                setTimeout(this.scrollTo, 1000);
            }
            
        });
    }

//------------------------------ AUTO SCROLL -----------------------------//

// SCROLL TO WINDOW ELEMENT FUNCTION // 

    scrollTo() {
        
        console.log('here');
        window.scroll({
        behavior: 'smooth',
        left: 0,
        top: document.getElementById('stat-scroll').offsetTop
        });
    }

}
// ---------------------------- LOGIN PAGE RELATED JS ------------------------ //

//------------------------ BUTTON AND FORM VARIABLES ----------------------------------//
class LoginVariables {

    constructor() {

        this.signUpButton = document.getElementById('signup-button');
        this.logInButton = document.getElementById('login-button');
        this.signUpForm = document.getElementById('signup');
        this.logInForm = document.getElementById('login');

        // ACCORDIAN VARIABLES FOR JOIN US AND MORE INFO BUTTON //
        this.joinUsButton = document.getElementById('join-us-button');
        this.formsContainer = document.getElementById('forms-container');
        this.stingContainer = document.getElementById('sting');

        this.moreInfoButton = document.getElementById('more-info');
        this.moreInfoContainer = document.getElementById('more-info-container');
        this.scrollToStat = document.getElementById('stat-scroll');
        this.statsContainer = document.getElementById('stats');

        // STICKY HEADER VARIABLES //
        this.header = document.getElementById('header');
        this.unStick = document.getElementById('stats').offsetTop;
    }


}
    
// -------------------------------- DATA VISUALISATION ---------------------------- //
class Charts {

    constructor(recipeData) {

        this.recipeData = recipeData;
    }

    makePieGraph() {

        const ndx = crossfilter(this.recipeData[3]);

        const course_dim = ndx.dimension(dc.pluck('CourseName'));
        const cuisine_dim = ndx.dimension(dc.pluck('CuisineName'));
        const total_course = course_dim.group();
        const total_cuisine = cuisine_dim.group();

        dc.pieChart('#cuisine-chart')
            .height(200)
            .radius(120)
            .transitionDuration(1500)
            .dimension(cuisine_dim)
            .group(total_cuisine);

        dc.pieChart('#course-chart')
            .height(200)
            .radius(120)
            .transitionDuration(1500)
            .dimension(course_dim)
            .group(total_course);
        

        dc.renderAll();
    };
}

//--------------------------- XHR ----------------------------------------//

class AJAXQuery { 

    constructor(url){

        this.url = url;
    }

    getRequest() {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();

            xhr.open("GET", this.url, true)
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 
                    const response = xhr.responseText;
                    resolve(response)
                
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send()  
        });
    };

    getRecipesData() {

        // RETRIEVE WORD FROM SERVER AS JSON //
        this.getRequest()
            .then((response) => { 

                const data = JSON.parse(response);
                const recipeData = data;
                const chart = new Charts(recipeData);
                chart.makePieGraph();      
            })
            .catch((error) => {
                console.log(error);
            })

    };

}

//------------------------ STICKY HEADER -------------------------------//

const stickyHeader = (header, unStick) => {

    if (window.pageYOffset <= unStick){

        header.classList.remove('sticky');

    } else {

        header.classList.add('sticky');
    }
}

// -------------------------- END OF LOGIN PAGE REALATED JS -----------------------//
// ------------------------------------------------------------------------------- //

// -------------------------- MY RECIPME PAGE RELATED JS -------------------------------//

// MY RECIPME DOM VARIABLES //
class MyRecipmeVariables {

    constructor() {

        this.outerAccordian = document.getElementsByClassName('accordian-outer');
        this.allSearchSubmit = document.getElementsByClassName('search-form__submit');
        this.allCategoryButtons = document.getElementsByClassName('search-buttons__button');
        this.ingredientButton = document.getElementById('search-ingredient');
        this.searchResetButton = document.getElementById('search-reset-button');
        this.fullRecipeButton = document.getElementsByClassName('full-recipe-button__button');
      
    }
   
}

// CLASS TO SHOW/HIDE ELEMENTS BASED ON CLICKED ELEMENT //
class showHide {

    constructor() {

        this.allSearchButtons = document.getElementsByClassName('search-buttons__button');
        this.allSearchForms = document.getElementsByClassName('search-form');
        this.categoryContainer = document.getElementById('search-forms');
        this.ingredientButton = document.getElementById('search-ingredient');
        this.ingredientForm = document.getElementById('ingredient-form');
    }
// RECIPME SEARCH FORM SHOW/HIDE //
    showHideSearchForms(){
       
        for(let i = 0; i < this.allSearchButtons.length; i++) {
            
            this.allSearchButtons[i].addEventListener('click', () => {
                
                this.ingredientButton.classList.remove('search-buttons__ingredient--hide');
                this.categoryContainer.classList.add('search-buttons-container--show');

                for(let j = 0; j < this.allSearchForms.length; j++) {
                    // IF ALL SEARCH FORMS CONTAIN CLASS OF SEARCH BUTTON ID //
                    if (!this.allSearchForms[j].classList.contains(this.allSearchButtons[i].getAttribute('id'))){
                        // REMOVE CLASS TO REVEAL FORM // 
                        this.allSearchForms[j].classList.add('search-form--hide');
    
                    } else { // CLASS DOESN'T CONTAIN CLASS OF BUTTON ID , ADD CLASS TO HIDE FORM //

                        this.allSearchForms[j].classList.remove('search-form--hide');

                    }

                }

            });

        }

    } 

// RECIPME INGREDIENT SEARCH SHOW/HIDE //
    showHideIngredientSearch() {

        this.ingredientButton.addEventListener('click', () => {

            this.ingredientForm.classList.remove('search-form--hide');
            this.ingredientButton.classList.add('search-buttons__ingredient--hide');
            this.categoryContainer.classList.remove('search-buttons-container--show');

            for (let i = 0; i < this.allSearchForms.length; i++){

                this.allSearchForms[i].classList.add('search-form--hide');
                this.ingredientForm.classList.remove('search-form--hide');
            }

        });
    }
}


//------------------------------ ADD RECIPE PAGE FUNCTIONS/CLASSES ----------------------//

// ------------------- CREATE INPUT TEXT FIELD -------------------- //

class AddRecipeVariables {

    constructor() {

        this.ingredients = document.getElementById("ingredients");
        this.addIngredientButton =  document.getElementById("add-ingredient");
        this.removeIngredientButton =  document.getElementById("remove-ingredient");
        this.method = document.getElementById("method");
        this.addStepButton = document.getElementById("add-step");
        this.removeStepButton = document.getElementById("remove-step");
        this.submitButton = document.getElementById("add-recipe");
        this.addButtons = document.getElementsByClassName("full-recipe__add-button");
        this.removeButtons = document.getElementsByClassName("full-recipe__remove-button");

    }
 
}

class CreateElement {

    constructor(field, counter, _class) {

        this.field = field;
        this.counter = counter;
        this._class = _class;
    }

    createInput() {

        const input = document.createElement("input");
        input.id = `${this.field}-${this.counter}`;
        input.classList.add(`${this._class}`);
        input.type = "text";
        input.name = `${this.field}`;   
        input.placeholder = `${this.field}`;

        return input;
    }

    createStepNumber() {

        const input = document.createElement("input");
        input.id = `s-${this.counter}`;
        input.classList.add(`${this._class}`);
        input.type = "number";
        input.min = `${this.counter}`;
        input.max = `${this.counter}`;
        input.name = `StepNumber`;
        input.value = `${this.counter}`;
        
        return input;
    }

    // ------------------ CREATE BR -------------------------------- //
    createBr() {

        const br = document.createElement("br");
        br.id = `br-${this.field}-${this.counter}`;
        
        return br;
    }

}

 // ----------------- INPUT FIELD CHARACTER COUNTERS ----------------//

class CharacterCount {

    characterCounter(inputId, counter, count){

        document.getElementById(inputId).onkeyup = function() {

            document.getElementById(counter).innerHTML = "Remaining:"+ (count-this.value.length);
        };
    };

    totalCharacters(counter, count){

        document.getElementById(counter).innerHTML = "Remaining:"+ count;
    };
}
// ---------------- ADD/REMOVE INPUT FIELDS FOR RECIPE CREATE FORM -------------- //


function CounterAPI() {

    this.ingredientCounter = 1;
    this.methodCounter = 1;

}

function InputCreate(counter) {

    //this.counter = new CounterAPI;

    this.addAnIngredient = (button, parent) => {

        button.addEventListener("click", (e) => {    
    
            if (counter.ingredientCounter <= 50) {
    
                const quantity = new CreateElement("Quantity", counter.ingredientCounter, "full-recipe__input-ingredient");
                const ingredient = new CreateElement("Ingredient", counter.ingredientCounter, "full-recipe__input-ingredient");
                //const br = new createElement("Ingredient", ingredientCounter);
    
                parent.appendChild(quantity.createInput());
                parent.appendChild(ingredient.createInput());
                parent.appendChild(ingredient.createBr());
    
                counter.ingredientCounter += 1;
            }
        
        });
    
    };
    
    // ----------------- REMOVE INGREDIENT TEXT FIELD ON CLICK ------------- //
    
    this.removeIngredient = (button, parent) => {
    
        button.addEventListener("click", (e) => {
            
            const removeInput = document.getElementById(`Ingredient-${counter.ingredientCounter -1}`);
            const removeBr = document.getElementById(`br-Ingredient-${counter.ingredientCounter -1}`);
            const removeQuantity = document.getElementById(`Quantity-${counter.ingredientCounter - 1}`);
    
            if (counter.ingredientCounter > 1) {
    
                parent.removeChild(removeQuantity);
                parent.removeChild(removeInput);
                parent.removeChild(removeBr);
                
                counter.ingredientCounter -=1;
    
            }
            
        });
        
    };
    
    // ----------------- ADD METHOD TEXT FIELD ON CLICK ------------- //
    this.addStep = (button, parent) => {
    
        button.addEventListener("click", (e) => {    
    
            if (counter.methodCounter <= 50) {
                
                const step = new CreateElement("Step", counter.methodCounter, "full-recipe__input-step");
                const stepNumber = new CreateElement("Step", counter.methodCounter, "full-recipe__numeric-input");
                const br = new CreateElement("Step", counter.methodCounter);
    
                parent.appendChild(stepNumber.createStepNumber());
                parent.appendChild(step.createInput());
                parent.appendChild(br.createBr());
    
                counter.methodCounter += 1;

            }
        
        });
    
    };
    
    // ----------------- REMOVE METHOD TEXT FIELD ON CLICK ------------- //
    this.removeStep = (button, parent) => {
    
        button.addEventListener("click", (e) => {
            
            const removeInput = document.getElementById(`Step-${counter.methodCounter -1}`);
            const removeBr = document.getElementById(`br-Step-${counter.methodCounter -1}`);
            const removeStepNumber = document.getElementById(`s-${counter.methodCounter - 1}`);
            
            if (counter.methodCounter > 1) {
    
                parent.removeChild(removeStepNumber);
                parent.removeChild(removeInput);
                parent.removeChild(removeBr);

                counter.methodCounter -=1;

                
            }
        
        });
    
    };

}





