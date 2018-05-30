

const mobileNavMenu = new NavDropDown();
const element = new MyRecipmeVariables();
const accordian = new Accordian(); 


accordian.recipemeAccordian(element.outerAccordian, 
                            'show-recipme-accordian-inner', 
                            'accordian-outer--active');

mobileNavMenu.clickBurgerMenu();

