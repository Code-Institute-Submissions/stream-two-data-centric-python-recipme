//------------------------- FUNCTION DECLARATIONS ------------------------//

//--------------------------- XHR EXPRESSIONS ----------------------------------------//

const returnData = (data) => {

    return data;
};

const getRequest = (url) => {

    return new Promise((resolve, reject) => {

        const xhr = new XMLHttpRequest();

        xhr.open("GET", url, true)
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


// -------------------------------- VISUALISATION ---------------------------- //

const makePieGraph = (recipeData) => {

    const ndx = crossfilter(recipeData[3]);

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


const getRecipesData = (url) => {

    // RETRIEVE WORD FROM SERVER AS JSON //
    getRequest(url)
        .then((response) => { 

            const data = JSON.parse(response);
            const recipeData = data;
            makePieGraph(recipeData);
            //console.log(recipeData);
            
        })
        .catch((error) => {
            console.log(error);
        })

};

//---------------------------------------------------------------------------//
//---------------------------------------------------------------------------//

//------------------------ BUTTON AND FORM VARIABLES ----------------------------------//

const signUpButton = document.getElementById('signup-button');
const logInButton = document.getElementById('login-button');
const signUpForm = document.getElementById('signup');
const logInForm = document.getElementById('login');

// ACCORDIAN VARIABLES FOR JOIN US AND MORE INFO BUTTON //
const joinUsButton = document.getElementById('join-us-button');
const formsContainer = document.getElementById('forms-container');
const stingContainer = document.getElementById('sting');

const moreInfoButton = document.getElementById('more-info');
const moreInfoContainer = document.getElementById('more-info-container');
const scrollToStat = document.getElementById('stat-scroll');
const statsContainer = document.getElementById('stats');

//-------------------------- ACCORDIAN FUNCTIONS ----------------------------------------//

// DROP DOWN FORM AND CLOSE ALREADY OPENED FORM //
const formAccordian = (button, show,  showStyle) => {

    button.addEventListener('click', () => {

        show.classList.toggle(`${showStyle}`);
        
    });
    
};

// SIGN UP FORM ACCORDDIAN SECTION //
const formSectionAccordian = () => {

    joinUsButton.addEventListener('click', () => {

        formsContainer.classList.toggle('forms-login-display');
        stingContainer.classList.toggle('sting--style');
    
    });

}

// SCROLL TO WINDOW ELEMENT FUNCTION // 

const scrollTo = (element) => {
    window.scroll({
      behavior: 'smooth',
      left: 0,
      top: element.offsetTop
    });
  }

// STATS SECTION ACCORDIAN WITH SCROLL TO FUNCTIONALITY //

const statsAccordian = () => {

    moreInfoButton.addEventListener('click', () => {
        
        if (statsContainer.classList.contains('stats-show')) {

            scrollTo(moreInfoContainer);
            statsContainer.classList.remove('stats-show');
            moreInfoContainer.classList.remove('more-info--style');

        } else {
           // getRecipesData('/stats');
            statsContainer.classList.add('stats-show');
            moreInfoContainer.classList.add('more-info--style');
            setTimeout(scrollToStatElement, 500);
        }
        
    });
}

//------------------------------ AUTO SCROLL -----------------------------//

// CALL SCROLL TO FUNCTION FOR ELEMENT //
const scrollToStatElement = () => {

    if (statsContainer.classList.contains('stats-show')) {

        scrollTo(scrollToStat);
    }

}

//------------------------ STICKY HEADER -------------------------------//

const header = document.getElementById('header');
const sticky = statsContainer.offsetTop;

const stickyHeader = () => {

    if (window.pageYOffset <= sticky){

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

// ----------------------- FUNCTION CALLS ------------------------------- //

window.onscroll = () => {

    stickyHeader();
}

// ACCORDIANS //

formSectionAccordian();
statsAccordian();
formAccordian(joinUsButton, signUpForm, 'show-signup-form');

//CALL XHR //

getRecipesData('/stats');

// CLICK STYLES //

formButtonClick(logInButton, 'login__button--click');
formButtonClick(signUpButton, 'signup__button--click');