
(()=> {
    // ----------------------- DOM VARIABLES -------------------------- //
    const element = new AddRecipeVariables();
    // ------------------ CREATE INPUT ELEMENT CLASS INSTANTIATE --------- //
    const counter = new Counter();
    const input = new InputCreate(counter);
 
    // ----------------------- UI FUNCTION CALLS --------------------- //
    singleButtonClick(element.submitButton, "full-recipe__form--clicked");
    clickBurgerMenu();
    multiButtonsClick(element.addButtons, "full-recipe__add-button--clicked" );
    multiButtonsClick(element.removeButtons, "full-recipe__remove-button--clicked");

    characterCounter("RecipeTitle", "recipe-title-counter", 50 );
    characterCounter("RecipeDescription", "recipe-description-counter", 150);
    characterCounter("Cuisine", "cuisine-description-counter", 50);

    // ---------------------- CALL INPUT FIELD FORM FUNCTIONS ------- //

    input.addAnIngredient(element.addIngredientButton, element.ingredients);
    input.removeIngredient(element.removeIngredientButton, element.ingredients);
    input.addStep(element.addStepButton, element.method);
    input.removeStep(element.removeStepButton, element.method);
     
})();
