
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

   //-------------------------- ACCORDIANS ----------------------------------------//

class FormAccordian {
    // DROP DOWN FORM AND CLOSE ALREADY OPENED FORM //
    formAccordian(button, show,  showStyle){

        button.addEventListener('click', () => {

            show.classList.toggle(`${showStyle}`);
            
        });
        
    };

    // SIGN UP FORM ACCORDDIAN SECTION //
    formSectionAccordian(button, formsContainer, stingContainer) {
        button.addEventListener('click', () => {

            formsContainer.classList.toggle('forms-login-display');
            stingContainer.classList.toggle('sting--style');
        
        });

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


//------------------------ STICKY HEADER -------------------------------//

const stickyHeader = (header, unStick) => {

    if (window.pageYOffset <= unStick){

        header.classList.remove('sticky');

    } else {

        header.classList.add('sticky');
    }
}

//-------------------------------------------------------------------------//

//------------------------- CLICK STYLES ---------------------------------//

const formButtonClick = (button, styles) => {

    button.addEventListener('mousedown', () => {

        button.classList.add(`${styles}`);
    });

    button.addEventListener('mouseup', () => {

        button.classList.remove(`${styles}`);
    });
}
    
// -------------------------- END OF LOGIN PAGE REALATED JS -----------------------//


class MyRecipmeVariables {

    constructor () {

        this.burgerMenu = document.getElementById('burger-menu');

    }
}

const clickBurgerMenu = (icon) => {

    icon.addEventListener('click', () => {

        icon.classList.toggle('alter');
    })
}