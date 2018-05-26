
describe("Accordian", function() {

    const buttonOne = document.createElement('button');
    const buttonTwo = document.createElement('button');
    const showSection = document.createElement('section');
    const hideSection = document.createElement('section');

    describe("Accordian", function() {
        
        it("should pass element input type is text", function() {
           
            expect(input.getAttribute('type')).toBe('text');
        });

        it("should pass element input id is Ingredient-1", function() {
    
            expect(input.getAttribute('id')).toBe('Ingredient-1');
        });

        it("should pass element input name is Ingredient", function() {
    
            expect(input.getAttribute('name')).toBe('Ingredient');
        });

        it("should pass element input placeholder is Ingredient", function() {
    
            expect(input.getAttribute('placeholder')).toBe('Ingredient');
        });

    });
});