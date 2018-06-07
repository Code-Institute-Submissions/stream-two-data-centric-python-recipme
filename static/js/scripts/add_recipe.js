 // -----------------------  DOM VARIABLES -------------------------- //


 const ingredients = document.getElementById("ingredients");
 const addIngredientButton =  document.getElementById("add-ingredient");
 const removeIngredientButton =  document.getElementById("remove-ingredient");
 const method = document.getElementById("method");
 const addStepButton = document.getElementById("add-step");
 const removeStepButton = document.getElementById("remove-step");
 const submitButton = document.getElementById("add-recipe");
 const addButtons = document.getElementsByClassName("full-recipe__add-button");
 const removeButtons = document.getElementsByClassName("full-recipe__remove-button");

 // --------------------- INPUT FIELD COUNTERS --------------------//

 let ingredientCounter = 1;
 let methodCounter = 1;
 // --------------------------------------------------------------//



 // ----------------- INPUT FIELD CHARACTER COUNTERS ----------------//
 
 const characterCounter = (input, counter, count) => {
     document.getElementById(input).onkeyup = function() {

         document.getElementById(counter).innerHTML = "Remaining:"+ (count-this.value.length);
     };
 };
 
 const totalCharacters = (counter, count) => {

     document.getElementById(counter).innerHTML = "Remaining:"+ count;
 };

 // ------------------- CREATE INPUT TEXT FIELD -------------------- //

 class createElement {

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




 // ----------------- ADD INGREDIENT TEXT FIELD ON CLICK ------------- //
 const addAnIngredient = (button, parent) => {

     button.addEventListener("click", (e) => {    

         if (ingredientCounter <= 25) {

             const quantity = new createElement("Quantity", ingredientCounter, "full-recipe__input-ingredient");
             const ingredient = new createElement("Ingredient", ingredientCounter, "full-recipe__input-ingredient");
             //const br = new createElement("Ingredient", ingredientCounter);

             parent.appendChild(quantity.createInput());
             parent.appendChild(ingredient.createInput());
             parent.appendChild(ingredient.createBr());
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

     });
     
 };

 // ----------------- ADD METHOD TEXT FIELD ON CLICK ------------- //
 const addStep = (button, parent) => {

     button.addEventListener("click", (e) => {    

         if (methodCounter <= 25) {
             
             const step = new createElement("Step", methodCounter, "full-recipe__input-step");
             const stepNumber = new createElement("Step", methodCounter, "full-recipe__numeric-input");
             const br = new createElement("Step", methodCounter);

             parent.appendChild(stepNumber.createStepNumber());
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
        
     });

 };

 // FUNCTION CALLS //
const mobileNavMenu = new NavDropDown();
const formSubmit = new ButtonClick(submitButton, "full-recipe__form--clicked");
const inputAddClickStyle = new ButtonClick(addButtons, "full-recipe__add-button--clicked" );
const inputRemoveClickStyle = new ButtonClick(removeButtons, "full-recipe__remove-button--clicked");

formSubmit.singleButtonClick();
mobileNavMenu.clickBurgerMenu();
inputAddClickStyle.multiButtonsClick();
inputRemoveClickStyle.multiButtonsClick();


//totalCharacters("recipe-title-counter",50 );
//totalCharacters("recipe-description-counter",150 );

characterCounter("RecipeTitle","recipe-title-counter",50 );
characterCounter("RecipeDescription","recipe-description-counter", 150);
characterCounter("Cuisine","cuisine-description-counter",50);
characterCounter("Course","course-description-counter", 50);

addAnIngredient(addIngredientButton, ingredients);
removeIngredient(removeIngredientButton, ingredients);
addStep(addStepButton, method);
removeStep(removeStepButton, method);
     
console.log(submitButton);