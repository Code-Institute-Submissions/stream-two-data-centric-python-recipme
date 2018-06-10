(()=>{
    
    const myRecipeButton = document.getElementById('my-recipe-button');
    const myRecipeButtonClick = new ButtonClick(myRecipeButton,'crud-message__button--clicked');
    const mobileNavMenu = new NavDropDown();
    
    mobileNavMenu.clickBurgerMenu();
    myRecipeButtonClick.singleButtonClick();
    
})();