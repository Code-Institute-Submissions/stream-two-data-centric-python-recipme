
(()=>{
    
    const mobileNavMenu = new NavDropDown();
    const showSearches = new showHide();
    const element = new MyRecipmeVariables();

// CLICK STYLING //
    const searchButtonClick = new ButtonClick(element.allSearchSubmit, 
                                        'search-buttons__button--clicked');
    const categoryButtonClick = new ButtonClick(element.allCategoryButtons, 
                                                'search-buttons__button--active');
    const resetButtonClick = new ButtonClick(element.searchResetButton, 
                                                    'results__reset--clicked');
    const fullRecipeButtonClick = new ButtonClick(element.fullRecipeButton, 
                                                    'full-recipe-button__button--clicked');
// FUCNTION CALLS //

    mobileNavMenu.clickBurgerMenu();
    showSearches.showHideSearchForms();
    showSearches.showHideIngredientSearch()
    searchButtonClick.multiButtonsClick();
    fullRecipeButtonClick.multiButtonsClick();
    categoryButtonClick.categoryButtonClick();
    categoryButtonClick.ingredientButtonClick(element.ingredientButton);

    if (element.searchResetButton != null) {
        
        resetButtonClick.singleButtonClick();
    }

})();