(()=>{
    // ----------------------- GET DOM VARIABLES -------------------------- //
    const element = new AddRecipeVariables();
    // --------------------------------------------------------------------- //
    // ------------------------- FORM INPUT CREATE ------------------------ //
    const counter = new Counter();
    const input = new InputCreate(counter);
    //---------------------------- UI INTERACTION ------------------------- //
    const setIngredientCounter = () => {

        numberOfIngredients = document.getElementsByClassName('edit-ingredient');
        counter.ingredientCounter = numberOfIngredients.length + 1;
        
    };

    const setMethodCounter = () => {

        numberOfMethods = document.getElementsByClassName('edit-method');
        counter.methodCounter = numberOfMethods.length + 1;

    };
 // -------------------------------------------------------------------------------- //
    //--- SET COUNTER TO NUMBER OF INSTANCES OF AN INGREDIENT OR METHOD ---//
    setIngredientCounter();
    setMethodCounter();

    //-------------------------------------------------------------------- //
    characterCounter("RecipeTitle","recipe-title-counter",50 );
    characterCounter("RecipeDescription","recipe-description-counter", 150);
    characterCounter("Cuisine","cuisine-description-counter",50);

    clickBurgerMenu();

    // --------------------------- BUTTON CLICK FUNCTION CALLS --------------------- //
    singleButtonClick(element.submitButton, "full-recipe__form--clicked");
    multiButtonsClick(element.addButtons, "full-recipe__add-button--clicked");
    multiButtonsClick(element.removeButtons, "full-recipe__remove-button--clicked");

    // ------------------------- CALL INPUT FIELD FORM FUNCTIONS ------- //
    input.addAnIngredient(element.addIngredientButton, element.ingredients);
    input.removeIngredient(element.removeIngredientButton, element.ingredients);
    input.addStep(element.addStepButton, element.method);
    input.removeStep(element.removeStepButton, element.method);

})();