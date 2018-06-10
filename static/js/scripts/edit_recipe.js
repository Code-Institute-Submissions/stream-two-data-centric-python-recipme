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

    // CHARACTER COUNTER CLASS INSTANTIATION //

    const inputCount = new CharacterCount();

    // FUNCTIONS TO SET COUNTER TO NUMBER OF INSTANCES OF AN INGREDIENT OR METHOD //

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
    inputCount.characterCounter("RecipeTitle","recipe-title-counter",50 );
    inputCount.characterCounter("RecipeDescription","recipe-description-counter", 150);
    inputCount.characterCounter("Cuisine","cuisine-description-counter",50);
    inputCount.characterCounter("Course","course-description-counter", 50);

    // --------------------------- BUTTON CLICK FUNCTION CALLS --------------------- //
    formSubmit.singleButtonClick();
    mobileNavMenu.clickBurgerMenu();
    inputAddClickStyle.multiButtonsClick();
    inputRemoveClickStyle.multiButtonsClick();

    // ------------------------- CALL INPUT FIELD FORM FUNCTIONS ------- //
    input.addAnIngredient(element.addIngredientButton, element.ingredients);
    input.removeIngredient(element.removeIngredientButton, element.ingredients);
    input.addStep(element.addStepButton, element.method);
    input.removeStep(element.removeStepButton, element.method);

})();