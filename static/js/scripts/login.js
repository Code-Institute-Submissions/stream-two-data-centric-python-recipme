// ----------------- LOGIN PAGE ---------------------------------------------------- //
(() => {

    const element = new LoginVariables();
    const form = new Accordian();
    const stat = new StatAccordian(element.moreInfoButton, element.statsContainer, 
                                    element.moreInfoContainer);
    const loginButtonClick = new ButtonClick(element.logInButton, 'login__button--click');
    const signUpButtonClick = new ButtonClick(element.signUpButton, 'signup__button--click');

//-------------------------- STICKY HEADER --------------------------------------//
    window.onscroll = () => {

    stickyHeader(element.header, element.unStick);
    
    }
//------------------------------------------------------------------------------------//
    // CALL ACCORDIANS //
    form.formSectionAccordian(element.joinUsButton, element.formsContainer, 
                                                    element.stingContainer);
    stat.statsAccordian();
    form.accordian(element.joinUsButton, element.signUpForm, 'show-signup-form');

    // CALL XHR //

    const query = new AJAXQuery('/stats');
    query.getRecipesData();

    // CLICK STYLES //

    loginButtonClick.singleButtonClick();
    signUpButtonClick.singleButtonClick();

})();