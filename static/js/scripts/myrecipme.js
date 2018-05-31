

const mobileNavMenu = new NavDropDown();
const element = new MyRecipmeVariables();
//const accordian = new Accordian(); 


//accordian.recipemeAccordian(element.outerAccordian, 
                           // 'show-recipme-accordian-inner', 
                           // 'accordian-outer--active');

mobileNavMenu.clickBurgerMenu();

const searchAllButton = document.getElementById('search-all');
const showAllSearchForm = document.getElementById('all-recipe');

const allSearchButtons = document.getElementsByClassName('search-buttons__button');
const allSearchForms = document.getElementsByClassName('search-form');

const searchCategory = (button, showForm, showStyle) => {

    button.addEventListener('click', () => {

        if (showForm.classList.contains(`${showStyle}`)) {
            
            showForm.classList.remove(`${showStyle}`);

        } else {

            showForm.classList.add(`${showStyle}`);

        }   

    });

}

const showSearchForms = () => {

    for(let i = 0; i < allSearchButtons.length; i++) {

        allSearchButtons[i].addEventListener('click', function(event) {

            for(let j = 0; j < allSearchForms.length; j++) {

                if (allSearchForms[j].classList.contains(allSearchButtons[i].getAttribute('id'))){

                    allSearchForms[j].classList.remove('search-form--hide');
                    console.log(allSearchButtons[i]);
                    console.log(allSearchForms[j]);
                } else {

                    allSearchForms[j].classList.add('search-form--hide');
                }

            }

        });

    }

}
//searchCategory(searchAllButton, showAllSearchForm, 'search-form--hide');
showSearchForms();
