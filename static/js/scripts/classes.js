
// ---------------------------- LOGIN PAGE RELATED JS ------------------------ //
// -------------------------------- VISUALISATION ---------------------------- //


class Charts {

    constructor(recipeData) {

        this.recipeData = recipeData;
    }

    makePieGraph() {

        const ndx = crossfilter(this.recipeData[3]);

        const course_dim = ndx.dimension(dc.pluck('CourseName'));
        const cuisine_dim = ndx.dimension(dc.pluck('CuisineName'));
        const total_course = course_dim.group();
        const total_cuisine = cuisine_dim.group();

        dc.pieChart('#cuisine-chart')
            .height(200)
            .radius(120)
            .transitionDuration(1500)
            .dimension(cuisine_dim)
            .group(total_cuisine);

        dc.pieChart('#course-chart')
            .height(200)
            .radius(120)
            .transitionDuration(1500)
            .dimension(course_dim)
            .group(total_course);
        

        dc.renderAll();
    };
}


//--------------------------- XHR ----------------------------------------//

class AJAXQuery { 

    constructor(url){

        this.url = url;
    }

    getRequest() {

        return new Promise((resolve, reject) => {

            const xhr = new XMLHttpRequest();

            xhr.open("GET", this.url, true)
            xhr.onload = function() {
        
                if (xhr.readyState == 4 && xhr.status == 200) { 
                    const response = xhr.responseText;
                    resolve(response)
                
                } else {
                    const error = xhr.responseText;
                    reject(error)
                }
            };
            
            xhr.send()  
        });
    };

    getRecipesData() {

        // RETRIEVE WORD FROM SERVER AS JSON //
        this.getRequest()
            .then((response) => { 

                const data = JSON.parse(response);
                const recipeData = data;
                const chart = new Charts(recipeData);
                chart.makePieGraph();      
            })
            .catch((error) => {
                console.log(error);
            })

    };

}
    
    //---------------------------------------------------------------------------//
    //---------------------------------------------------------------------------//

    //------------------------ BUTTON AND FORM VARIABLES ----------------------------------//
class LoginVariables {

    constructor() {

        this.signUpButton = document.getElementById('signup-button');
        this.logInButton = document.getElementById('login-button');
        this.signUpForm = document.getElementById('signup');
        this.logInForm = document.getElementById('login');

        // ACCORDIAN VARIABLES FOR JOIN US AND MORE INFO BUTTON //
        this.joinUsButton = document.getElementById('join-us-button');
        this.formsContainer = document.getElementById('forms-container');
        this.stingContainer = document.getElementById('sting');

        this.moreInfoButton = document.getElementById('more-info');
        this.moreInfoContainer = document.getElementById('more-info-container');
        this.scrollToStat = document.getElementById('stat-scroll');
        this.statsContainer = document.getElementById('stats');

        // STICKY HEADER VARIABLES //
        this.header = document.getElementById('header');
        this.unStick = document.getElementById('stats').offsetTop;
    }

    getVariables() {

        return this.signUpButton,this.logInButton,this.signUpForm,
        this.logInForm, this.joinUsButton,  this.formsContainer, this.stingContainer,
        this.moreInfoButton, this.moreInfoContainer, this.scrollToStat, this.statsContainer,
        this.header, this.sticky;
        
    }
}

  

//------------------------ STICKY HEADER -------------------------------//

const stickyHeader = (header, unStick) => {

    if (window.pageYOffset <= unStick){

        header.classList.remove('sticky');

    } else {

        header.classList.add('sticky');
    }
}

// -------------------------- END OF LOGIN PAGE REALATED JS -----------------------//
// ------------------------------------------------------------------------------- //
// -------------------------- MY RECIPME RELATED JS -------------------------------//

class MyRecipmeVariables {
// MY RECIPME RELATED VARIABLES //
    constructor() {

        this.outerAccordian = document.getElementsByClassName('accordian-outer');
        this.allSearchSubmit = document.getElementsByClassName('search-form__submit');
        this.allCategoryButtons = document.getElementsByClassName('search-buttons__button');
        this.ingredientButton = document.getElementById('search-ingredient');
      
    }
   
}

class showHide {
// CLASS TO SHOW/HIDE ELEMENTS BASED ON CLICKED ELEMENT //
    constructor() {

        this.allSearchButtons = document.getElementsByClassName('search-buttons__button');
        this.allSearchForms = document.getElementsByClassName('search-form');
        this.ingredientButton = document.getElementById('search-ingredient');
        this.ingredientForm = document.getElementById('ingredient-form');
    }
// RECIPME SEARCH FORM SHOW/HIDE //
    showHideSearchForms(){
       
        for(let i = 0; i < this.allSearchButtons.length; i++) {
            
            this.allSearchButtons[i].addEventListener('click', () => {
                
                this.ingredientButton.classList.remove('search-buttons__ingredient--hide');
        
                for(let j = 0; j < this.allSearchForms.length; j++) {
                    // IF ALL SEARCH FORMS CONTAIN CLASS OF SEARCH BUTTON ID //
                    if (this.allSearchForms[j].classList.contains(this.allSearchButtons[i].getAttribute('id'))){
                        // REMOVE CLASS TO REVEAL FORM //
                        this.allSearchForms[j].classList.remove('search-form--hide');

                    } else { // CLASS DOESN'T CONTAIN CLASS OF BUTTON ID , ADD CLASS TO HIDE FORM //

                        this.allSearchForms[j].classList.add('search-form--hide');
                    }

                }

            });

        }

    } 

// RECIPME INGREDIENT SEARCH SHOW/HIDE //

    showHideIngredientSearch() {

        this.ingredientButton.addEventListener('click', () => {

            this.ingredientForm.classList.remove('search-form--hide');
            this.ingredientButton.classList.add('search-buttons__ingredient--hide');

            for (let i = 0; i < this.allSearchForms.length; i++){

                this.allSearchForms[i].classList.add('search-form--hide');
                this.ingredientForm.classList.remove('search-form--hide');
            }

        });
    }
}

//---------------------------  GENERAL CLASSES --------------------------------- // 

//------------------------- CLICK FUNCTION  ---------------------------------//

class ButtonClick {

    constructor(buttons, style) {

        this.buttons = buttons;
        this.style = style;
        
    }

    formButtonClick() {
      
        this.buttons.addEventListener('mousedown', () => {
    
            this.buttons.classList.add(`${this.style}`);
        });
    
        this.buttons.addEventListener('mouseup', () => {
    
            this.buttons.classList.remove(`${this.style}`);
        });
    }

    formButtonsClick() {
        
        for(let i=0; i < this.buttons.length; i++) {
            
            this.buttons[i].addEventListener('mousedown', () => {
                
                this.buttons[i].classList.add(`${this.style}`);

            });

            this.buttons[i].addEventListener('mouseup', () => {

                this.buttons[i].classList.remove(`${this.style}`);

            });

           

        }

    }

    categoryButtonClick() {

        for (let i=0; i < this.buttons.length; i++) {

            this.buttons[i].addEventListener('click', () => {

                if (this.buttons[i].classList.contains(`${this.style}`)){

                    this.buttons[i].classList.remove(`${this.style}`);
                    
                } else {

                    for (let j=0; j < this.buttons.length; j++) {

                        this.buttons[j].classList.remove(`${this.style}`);
                    }
                    
                    this.buttons[i].classList.add(`${this.style}`);

                }
            });
        }

    }

    ingredientButtonClick(ingredientButton) {

        const selfButtons = this.buttons;
        const selfStyle = this.style;
        
        ingredientButton.addEventListener('click', () => {

            for (let i=0; i < this.buttons.length; i++) {

                this.buttons[i].classList.remove('search-buttons__button--active');

            }
           

        });

    }

}



 //-------------------------- ACCORDIANS ----------------------------------------//

 class NavDropDown {
    // CLASS TO TOGGLE SCSS CLASS FOR ANIMATING BURGER MENU //
    constructor() {

        this.burgerMenu = document.getElementById('burger-menu');
        this.navSideBar = document.getElementById('side-bar');

    }

    clickBurgerMenu() {

        this.burgerMenu.addEventListener('click', () => {

            this.burgerMenu.classList.toggle('alter');
            this.navSideBar.classList.toggle('show-side-bar');
        })
    }

    
}

 class Accordian {
    // DROP DOWN FORM AND CLOSE ALREADY OPENED FORM //
    accordian(button, show,  showStyle){

        button.addEventListener('click', () => {

            show.classList.toggle(`${showStyle}`);
            
        });
        
    };

    // SIGN UP FORM ACCORDIAN SECTION //
    formSectionAccordian(button, formsContainer, stingContainer) {
        button.addEventListener('click', () => {

            formsContainer.classList.toggle('forms-login-display');
            stingContainer.classList.toggle('sting--style');
        
        });

    }

    // RECIPME MAIN ACCORDIAN //
    recipemeAccordian(element, showStyle, activeStyle) {
            
        for (let i=0; i < element.length; i++) { // LOOP THROUGH ARRAY OF CONTAINERS ASSIGN EACH TO 'i'

            element[i].addEventListener('click', function() { // ADD EVENT LISTENER

            if (this.nextElementSibling.classList.contains(`${showStyle}`)){ 

                this.classList.remove(`${activeStyle}`);
                this.nextElementSibling.classList.remove(`${showStyle}`); // REMOVE STYLE ON BUTTON
                
            } else {

                for (let j=0; j < element.length; j++) { // LOOP THROUGH CONTAINERS AGAIN BUT ASSIGN TO 'j', REMOVE SHOW STYLE ON J

                    if(element[j].nextElementSibling.classList.contains(`${showStyle}`)){

                        element[j].nextElementSibling.classList.remove(`${showStyle}`);
                        element[j].classList.remove(`${activeStyle}`);
                    }
                }

                this.classList.add(`${activeStyle}`);
                this.nextElementSibling.classList.add(`${showStyle}`); // RE-APPLY SHOW STYLE TO CLICKED 'i'
                
            }

            });
        
        }

    }
}

class StatAccordian {

    constructor(moreInfoButton, statsContainer, moreInfoContainer) { 

        this.moreInfoButton = moreInfoButton;
        this.statsContainer = statsContainer;
        this.moreInfoContainer = moreInfoContainer;
    
    }

// STATS SECTION ACCORDIAN WITH SCROLL TO FUNCTIONALITY //
    statsAccordian(){

        this.moreInfoButton.addEventListener('click', () => {
            
            if (this.statsContainer.classList.contains('stats-show')) {

                //scrollTo(this.moreInfoContainer);
                this.statsContainer.classList.remove('stats-show');
                this.moreInfoContainer.classList.remove('more-info--style');

            } else {
            // getRecipesData('/stats');
                this.statsContainer.classList.add('stats-show');
                this.moreInfoContainer.classList.add('more-info--style');
                setTimeout(this.scrollTo, 1000);
            }
            
        });
    }

//------------------------------ AUTO SCROLL -----------------------------//

// SCROLL TO WINDOW ELEMENT FUNCTION // 

    scrollTo() {
        
        console.log('here');
        window.scroll({
        behavior: 'smooth',
        left: 0,
        top: document.getElementById('stat-scroll').offsetTop
        });
    }

}
