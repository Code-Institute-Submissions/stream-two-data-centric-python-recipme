// ----------------- LOGIN PAGE ---------------------------------------------------- //

const element = new LoginVariables();
const form = new FormAccordian();
const stat = new StatAccordian(element.moreInfoButton, element.statsContainer, 
                                element.moreInfoContainer);

//-------------------------- STICKY HEADER --------------------------------------//
window.onscroll = () => {

   stickyHeader(element.header, element.unStick);
}

// CALL ACCORDIANS //

form.formSectionAccordian(element.joinUsButton, element.formsContainer, 
                                                element.stingContainer);
stat.statsAccordian();
form.formAccordian(element.joinUsButton, element.signUpForm, 'show-signup-form');

// CALL XHR //

const query = new AJAXQuery('/stats');
query.getRecipesData();

// CLICK STYLES //

formButtonClick(element.logInButton, 'login__button--click');
formButtonClick(element.signUpButton, 'signup__button--click');

//------------------------------------------------------------------------------------//