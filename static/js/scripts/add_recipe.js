(()=> {
    // ----------------------- GET DOM VARIABLES -------------------------- //
    const element = new AddRecipeVariables();

    // --------------------- INPUT FIELD COUNTERS --------------------//

    let ingredientCounter = 1;
    let methodCounter = 1;

    // --------------------------------------------------------------//
    // ----------------- ADD INGREDIENT TEXT FIELD ON CLICK ------------- //

    const addAnIngredient = (button, parent) => {

        button.addEventListener("click", (e) => {    

            if (ingredientCounter <= 50) {

                const quantity = new CreateElement("Quantity", ingredientCounter, "full-recipe__input-ingredient");
                const ingredient = new CreateElement("Ingredient", ingredientCounter, "full-recipe__input-ingredient");
                //const br = new createElement("Ingredient", ingredientCounter);

                parent.appendChild(quantity.createInput());
                parent.appendChild(ingredient.createInput());
                parent.appendChild(ingredient.createBr());

                ingredientCounter += 1;
            }
        
        });

    };

    // ----------------- REMOVE INGREDIENT TEXT FIELD ON CLICK ------------- //

    const removeIngredient = (button, parent) => {

        button.addEventListener("click", (e) => {
            
            const removeInput = document.getElementById(`Ingredient-${ingredientCounter -1}`);
            const removeBr = document.getElementById(`br-Ingredient-${ingredientCounter -1}`);
            const removeQuantity = document.getElementById(`Quantity-${ingredientCounter - 1}`);

            if (ingredientCounter > 1) {

                parent.removeChild(removeQuantity);
                parent.removeChild(removeInput);
                parent.removeChild(removeBr);

                ingredientCounter -=1;

            }
            
        });
        
    };

    // ----------------- ADD METHOD TEXT FIELD ON CLICK ------------- //
    const addStep = (button, parent) => {

        button.addEventListener("click", (e) => {    

            if (methodCounter <= 50) {
                
                const step = new CreateElement("Step", methodCounter, "full-recipe__input-step");
                const stepNumber = new CreateElement("Step", methodCounter, "full-recipe__numeric-input");
                const br = new CreateElement("Step", methodCounter);

                parent.appendChild(stepNumber.createStepNumber());
                parent.appendChild(step.createInput());
                parent.appendChild(br.createBr());

                methodCounter += 1;
            }
        
        });

    };

    // ----------------- REMOVE METHOD TEXT FIELD ON CLICK ------------- //
    const removeStep = (button, parent) => {

        button.addEventListener("click", (e) => {
            
            const removeInput = document.getElementById(`Step-${methodCounter -1}`);
            const removeBr = document.getElementById(`br-Step-${methodCounter -1}`);
            const removeStepNumber = document.getElementById(`s-${methodCounter - 1}`);
            
            if (methodCounter > 1) {

                parent.removeChild(removeStepNumber);
                parent.removeChild(removeInput);
                parent.removeChild(removeBr);

                methodCounter -=1;
                
            }
        
        });

    };

    // ------------------------- FUNCTION CALLS --------------------------- //

    const mobileNavMenu = new NavDropDown();
    const formSubmit = new ButtonClick(element.submitButton, "full-recipe__form--clicked");
    const inputAddClickStyle = new ButtonClick(element.addButtons, "full-recipe__add-button--clicked" );
    const inputRemoveClickStyle = new ButtonClick(element.removeButtons, "full-recipe__remove-button--clicked");

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

    addAnIngredient(element.addIngredientButton, element.ingredients);
    removeIngredient(element.removeIngredientButton, element.ingredients);
    addStep(element.addStepButton, element.method);
    removeStep(element.removeStepButton, element.method);
     
})();
