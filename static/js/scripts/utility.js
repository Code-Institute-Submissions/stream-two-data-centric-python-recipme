// ---------------------------  GENERAL CLASSES/FUNCTIONS CALLED ON BY  --------------------------------- // 
// ------------------------------------------------------------------------------------------------------ //

const singleButtonClick = (button, style) => {
    
    button.addEventListener('mousedown', () => {

        button.classList.add(`${style}`);
    });

    button.addEventListener('mouseup', () => {

        button.classList.remove(`${style}`);
    });
}

const multiButtonsClick = (buttons, style) => {
    
    for(let i=0; i < buttons.length; i++) {
        
        buttons[i].addEventListener('mousedown', () => {
            
            buttons[i].classList.add(`${style}`);

        });

        buttons[i].addEventListener('mouseup', () => {

            buttons[i].classList.remove(`${style}`);

        });

    }

}

const categoryButtonClick = (buttons, style) => {

    for (let i=0; i < buttons.length; i++) {

        buttons[i].addEventListener('click', () => {

            for (let j=0; j < buttons.length; j++) {

                buttons[j].classList.remove(`${style}`);
                buttons[i].classList.add(`${style}`);

            }
        });
    }

}

const ingredientButtonClick = (ingredientButton, categoryButtons) => {
    
    ingredientButton.addEventListener('click', () => {

        for (let i=0; i < categoryButtons.length; i++) {

            categoryButtons[i].classList.remove('search-buttons__button--active');

        }
        

    });

};

// ------------------------ CLICK BURGER MENU -------------------- //

const clickBurgerMenu = () => {

    const burgerMenu = document.getElementById('burger-menu');
    const navSideBar = document.getElementById('side-bar');

    burgerMenu.addEventListener('click', () => {

        burgerMenu.classList.toggle('alter');
        navSideBar.classList.toggle('show-side-bar');
    })
}

// --- CLASS TO SHOW/HIDE SEARCH FORM ELEMENTS BASED ON CLICKED ELEMENT ---- //
// -------- USE FOR MY RECIPE PAGE PLUS SHARED RECIPE SEARCH PAGE ---------- //

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

// RECIPME INGREDIENT SEARCH FORM SHOW/HIDE //
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


//------------------ ADD RECIPE PAGE FUNCTIONS/CLASSES ----------------------//

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

// ------------------- CREATE INPUT TEXT FIELD -------------------- //

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


const characterCounter = (inputId, counter, count) => {

    document.getElementById(inputId).onkeyup = function() {

        document.getElementById(counter).innerHTML = "Remaining:"+ (count-this.value.length);
    };
};


// ---------------- ADD/REMOVE INPUT FIELDS FOR RECIPE CREATE FORM -------------- //


function Counter() {

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





