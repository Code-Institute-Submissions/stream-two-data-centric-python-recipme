// ----------------- LOGIN PAGE ---------------------------------------------------- //
(() => {

    // ------------ VARIABLES ---------------------------------------- //

    const signUpButton = document.getElementById('signup-button');
    const logInButton = document.getElementById('login-button');
    const signUpForm = document.getElementById('signup');
    const joinUsButton = document.getElementById('join-us-button');
    const moreInfoButton = document.getElementById('more-info');
    const moreInfoContainer = document.getElementById('more-info-container');
    const statsContainer = document.getElementById('stats');
    const header = document.getElementById('header');
    const unStick = document.getElementById('stats').offsetTop;

    // ------------ FUNCTIONS ---------------------------------------- //

    // --------------- XHR ------------------------------------------- //

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

    const getRecipesData = (url) => {

        // RETRIEVE WORD FROM SERVER AS JSON //
        getRequest(url)
            .then((response) => { 

                const data = JSON.parse(response);
                const recipeData = data;
                //const chart = new Charts(recipeData);
                makePieGraph(recipeData);      
            })
            .catch((error) => {
                console.log(error);
            })

    };

    // -------------------- VISUALISATION ----------------------------- //

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

    // ------------------------- ACCORDIANS -----------------------------------//

    const accordian = (button, show,  showStyle) => {

        button.addEventListener('click', () => {

            show.classList.toggle(`${showStyle}`);
            
        });
        
    };

    // ----------------------- STATS SECTION ACCORDIAN WITH SCROLL WINDOW TO -------------- //

    const scrollTo = () => {
            
        window.scroll({
        behavior: 'smooth',
        left: 0,
        top: document.getElementById('stat-scroll').offsetTop
        });
    }

    const statsAccordian = (moreInfoButton, statsContainer, moreInfoContainer) => {

        moreInfoButton.addEventListener('click', () => {
            
            if (statsContainer.classList.contains('stats-show')) {

                statsContainer.classList.remove('stats-show');
                moreInfoContainer.classList.remove('more-info--style');

            } else {
            
                statsContainer.classList.add('stats-show');
                moreInfoContainer.classList.add('more-info--style');
                setTimeout(scrollTo, 1000);
            }
            
        });
    }

    //------------------------ STICKY HEADER FUNCTION -------------------------------//

    const stickyHeader = (header, unStick) => {

        if (window.pageYOffset <= unStick){

            header.classList.remove('sticky');

        } else {

            header.classList.add('sticky');
        }
    }


   
//------------------------------------------------------------------------------------//
//-------------------------- CALL FUNCTIONS ------------------------------------------//

    // CALL XHR //
    getRecipesData('/stats');

    // CALL WINDOW SCROLL //
    window.onscroll = () => {

        stickyHeader(header, unStick);
    
    }

    // CALL ACCORDIANS //
    statsAccordian(moreInfoButton, statsContainer, moreInfoContainer);
    accordian(joinUsButton, signUpForm, 'show-signup-form');

    // CALL CLICK STYLES //
    singleButtonClick(logInButton, 'login__button--click');
    singleButtonClick(signUpButton, 'signup__button--click');

})();