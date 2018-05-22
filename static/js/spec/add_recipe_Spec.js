
describe("AddRecipe", function() {
    describe("Create Element", function() {
        
        const element = new createElement('Ingredient', 1);
        const input = element.createInput();

        it("should pass element input type is text", function() {
           
            expect(input.getAttribute('type')).toBe('text');
        });

        it("should pass element input type is text", function() {
    
            expect(input.getAttribute('type')).not.toBe(null);
        });
    });
});