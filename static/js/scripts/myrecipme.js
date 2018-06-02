

const mobileNavMenu = new NavDropDown();
const showSearches = new showHide();
const element = new MyRecipmeVariables();
const searchButtonClick = new ButtonClick(element.allSearchSubmit, 
                                    'search-buttons__button--clicked');
const categoryButtonClick = new ButtonClick(element.allCategoryButtons, 
                                            'search-buttons__button--active');



mobileNavMenu.clickBurgerMenu();
showSearches.showHideSearchForms();
showSearches.showHideIngredientSearch()
searchButtonClick.formButtonsClick();
categoryButtonClick.categoryButtonClick();
categoryButtonClick.ingredientButtonClick(element.ingredientButton);
