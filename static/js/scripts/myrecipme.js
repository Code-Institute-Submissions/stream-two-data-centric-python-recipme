

const mobileNavMenu = new NavDropDown();
const element = new MyRecipmeVariables();
//const accordian = new Accordian(); 


//accordian.recipemeAccordian(element.outerAccordian, 
                           // 'show-recipme-accordian-inner', 
                           // 'accordian-outer--active');

mobileNavMenu.clickBurgerMenu();

const searchAllButton = document.getElementById('search-all');
const showAllSearchForm = document.getElementById('all-recipe');

const searchCategory = (button, showForm, showStyle) => {

    button.addEventListener('click', () => {

        if (showForm.classList.contains(`${showStyle}`)) {
            
            showForm.classList.remove(`${showStyle}`);

        } else {

            showForm.classList.add(`${showStyle}`);

        }

       

    });

}

searchCategory(searchAllButton, showAllSearchForm, 'search-form--hide');

