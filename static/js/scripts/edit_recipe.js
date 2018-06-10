(()=>{
    // ----------------------- GET DOM VARIABLES -------------------------- //
    const element = new AddRecipeVariables();
    // --------------------------------------------------------------------- //
    // ------------------------- FORM INPUT CREATE ------------------------ //
    const counter = new CounterAPI();
    const input = new InputCreate(counter);
    //---------------------------- UI INTERACTION ------------------------- //
    const mobileNavMenu = new NavDropDown();
    const formSubmit = new ButtonClick(element.submitButton, "full-recipe__form--clicked");
    const inputAddClickStyle = new ButtonClick(element.addButtons, "full-recipe__add-button--clicked" );
    const inputRemoveClickStyle = new ButtonClick(element.removeButtons, "full-recipe__remove-button--clicked");

    // FUNCTIONS TO SET COUNTER TO NUMBER OF INSTANCES OF AN INGREDIENT OR METHOD //

    const setIngredientCounter = () => {

        numberOfIngredients = document.getElementsByClassName('edit-ingredient');
        counter.ingredientCounter = numberOfIngredients.length + 1;
        
    };

    const setMethodCounter = () => {

        numberOfMethods = document.getElementsByClassName('edit-method');
        counter.methodCounter = numberOfMethods.length + 1;

    };

    // SET COUNTER TO NUMBER OF INSTANCES OF AN INGREDIENT OR METHOD //

    setIngredientCounter();
    setMethodCounter();

     // --------------------------- UI FUNCTION CALLS --------------------- //
    formSubmit.singleButtonClick();
    mobileNavMenu.clickBurgerMenu();
    inputAddClickStyle.multiButtonsClick();
    inputRemoveClickStyle.multiButtonsClick();

    characterCounter("RecipeTitle","recipe-title-counter",50 );
    characterCounter("RecipeDescription","recipe-description-counter", 150);
    characterCounter("Cuisine","cuisine-description-counter",50);
    characterCounter("Course","course-description-counter", 50);

    // ------------------------- CALL INPUT FIELD FORM FUNCTIONS ------- //
    input.addAnIngredient(element.addIngredientButton, element.ingredients);
    input.removeIngredient(element.removeIngredientButton, element.ingredients);
    input.addStep(element.addStepButton, element.method);
    input.removeStep(element.removeStepButton, element.method);
      
    console.log(counter.methodCounter);
    console.log(counter.ingredientCounter);

})();

/*

// -----------------------  DOM VARIABLES -------------------------- //
const ingredients = document.getElementById("ingredients");
const addIngredientButton =  document.getElementById("add-ingredient");
const removeIngredientButton =  document.getElementById("remove-ingredient");
const method = document.getElementById("method");
const addStepButton = document.getElementById("add-step");
const removeStepButton = document.getElementById("remove-step");

// --------------------- INPUT FIELD COUNTERS --------------------//

let ingredientCounter = 1;
let methodCounter = 1;

// --------------------------------------------------------------//
// --------------- ONLY APPLICABLE TO EDIT RECIPES -------------- //

const setIngredientCounter = () => {

    numberOfIngredients = document.getElementsByClassName('ingredient');
    ingredientCounter = numberOfIngredients.length + 1;
    
};

const setMethodCounter = () => {

    numberOfMethods = document.getElementsByClassName('method');
    methodCounter = numberOfMethods.length + 1;

};

setIngredientCounter();
setMethodCounter();

//------------------------------------------------------------------//
// ----------------- INPUT FIELD CHARACTER COUNTERS ----------------//

const characterCounter = (input, counter, count) => {
    document.getElementById(input).onkeyup = function() {

        document.getElementById(counter).innerHTML = "Characters remaining:"+ (count-this.value.length);
    };
};

// ------------------- CREATE INPUT TEXT FIELD -------------------- //

class createElement {

    constructor(field, counter) {

        this.field = field;
        this.counter = counter;
    }

    createInput() {

        const input = document.createElement("input");
        input.id = `${this.field}-${this.counter}`;
        input.type = "text";
        input.name = `${this.field}`;
        input.placeholder = `${this.field}`;
        input.required = true;

        return input;
    }

    createStepNumber(counter) {

        const input = document.createElement("input");
        input.id = `s-${counter}`;
        input.class = "step-number";
        input.type = "number";
        input.min = `${counter}`;
        input.max = `${counter}`;
        input.name = `StepNumber`;
        input.value = `${counter}`;
        input.required = true;

        return input;
    }

    // ------------------ CREATE BR -------------------------------- //
    createBr() {

        const br = document.createElement("br");
        br.id = `br-${this.field}-${this.counter}`;
        return br;
    }

}

// ----------------- ADD INGREDIENT TEXT FIELD ON CLICK ------------- //
const addAnIngredient = (button, parent) => {

    button.addEventListener("click", (e) => {    

        if (ingredientCounter <= 25) {

            const quantity = new createElement("Quantity", ingredientCounter);
            const ingredient = new createElement("Ingredient", ingredientCounter);
            const br = new createElement("Ingredient", ingredientCounter);

            parent.appendChild(quantity.createInput());
            parent.appendChild(ingredient.createInput());
            parent.appendChild(br.createBr());
        }
        
        console.log(ingredientCounter);
        ingredientCounter += 1;
            
    });

};

// ----------------- REMOVE INGREDIENT TEXT FIELD ON CLICK ------------- //

const removeIngredient = (button, parent) => {

    button.addEventListener("click", (e) => {
        
        const removeInput = document.getElementById(`Ingredient-${ingredientCounter -1}`);
        const removeBr = document.getElementById(`br-Ingredient-${ingredientCounter -1}`);
        const removeQuantity = document.getElementById(`Quantity-${ingredientCounter - 1}`);

        if (ingredientCounter > 0) {
            parent.removeChild(removeQuantity);
            parent.removeChild(removeInput);
            parent.removeChild(removeBr);

        }
        
        ingredientCounter -=1;
        //console.log(`ingredient-${ingredientCounter-1}`)
    });
    
};

// ----------------- ADD METHOD TEXT FIELD ON CLICK ------------- //
const addStep = (button, parent) => {

    button.addEventListener("click", (e) => {    

        if (methodCounter <= 25) {

            const stepNumber = new createElement();
            const step = new createElement("Step", methodCounter);
            const br = new createElement("Step", methodCounter);

            parent.appendChild(stepNumber.createStepNumber(methodCounter));
            parent.appendChild(step.createInput());
            parent.appendChild(br.createBr());
        }
        
        console.log(methodCounter);
        methodCounter += 1;
        
    });

};

// ----------------- REMOVE METHOD TEXT FIELD ON CLICK ------------- //
const removeStep = (button, parent) => {

    button.addEventListener("click", (e) => {
        
        const removeInput = document.getElementById(`Step-${methodCounter -1}`);
        const removeBr = document.getElementById(`br-Step-${methodCounter -1}`);
        const removeStepNumber = document.getElementById(`s-${methodCounter - 1}`);
        
        if (methodCounter > 0) {

            parent.removeChild(removeStepNumber);
            parent.removeChild(removeInput);
            parent.removeChild(removeBr);

        }
        
        methodCounter -=1;
        //console.log(`ingredient-${ingredientCounter-1}`)
    });

};


characterCounter("RecipeTitle","recipe-title-counter",150 );
characterCounter("RecipeDescription","recipe-description-counter", 250);
characterCounter("Cuisine","cuisine-description-counter",160);
characterCounter("Course","course-description-counter", 160);

addAnIngredient(addIngredientButton, ingredients);
removeIngredient(removeIngredientButton, ingredients);
addStep(addStepButton, method);
removeStep(removeStepButton, method);
        */