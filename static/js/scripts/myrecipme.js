
(()=>{
    // ------------------- VARIABLES ------------------------------// 
    const allSearchSubmit = document.getElementsByClassName('search-form__submit');
    const allCategoryButtons = document.getElementsByClassName('search-buttons__button');
    const ingredientButton = document.getElementById('search-ingredient');
    const searchResetButton = document.getElementById('search-reset-button');
    const fullRecipeButton = document.getElementsByClassName('full-recipe-button__button');

    // INSTANTIATE CLASS TO SHOW AND HIDE SEARCHES //
    const showSearches = new showHide();
   
    // FUNCTION CALLS //
    clickBurgerMenu();
    showSearches.showHideSearchForms();
    showSearches.showHideIngredientSearch()
    multiButtonsClick(allSearchSubmit,'search-buttons__button--clicked' );
    multiButtonsClick(fullRecipeButton,'full-recipe-button__button--clicked');
    categoryButtonClick(allCategoryButtons, 'search-buttons__button--active' );
    ingredientButtonClick(ingredientButton, allCategoryButtons);

    if (searchResetButton != null) {
        
        singleButtonClick(searchResetButton, 'results__reset--clicked');
    }

})();