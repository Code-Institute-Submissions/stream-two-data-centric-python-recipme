
describe("AddElement", function() {
    describe("Create Input Element", function() {
        
        const element = new createElement("Ingredient", 1);
        const input = element.createInput();

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

    describe(" Create StepNumber Input Element ", function() {
        const counter = 1
        const element = new createElement('Step', counter);
        const input = element.createStepNumber();

        it("should pass StepNumber Element Id is s-1", function() {

            expect(input.getAttribute('id')).toBe('s-1');
        });

        it("should pass StepNumber class is step-number", function() {

            expect(input.class).toBe('step-number');
        });

        it("should pass StepNumber Element min is 1", function() {

            expect(input.getAttribute('min')).toBe('1');
        });

        it("should pass StepNumber Element max is 1", function() {

            expect(input.getAttribute('min')).toBe('1');
        });

        it("should pass StepNumber Element name is StepNumber", function() {

            expect(input.getAttribute('name')).toBe('StepNumber');
        });

        it("should pass StepNumber Element value is 1", function() {

            expect(input.value).toBe('1');
        });
        
    });

    describe(" Create Br Element ", function() {
        const counter = 1
        const element = new createElement('Ingredient', counter);
        const input = element.createBr();

        it("should pass Br Element Id is br-Ingredient-1", function() {

            expect(input.getAttribute('id')).toBe('br-Ingredient-1');
        });
        
    });
}); 