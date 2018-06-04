const formButtons = document.getElementsByClassName('form-submit');

const mobileNavMenu = new NavDropDown();
const formButtonClick = new ButtonClick(formButtons,'feedback-form-buttons--clicked');


mobileNavMenu.clickBurgerMenu();
formButtonClick.multiButtonsClick();

console.log(formButtons);