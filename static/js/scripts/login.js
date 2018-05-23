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
        .height(330)
        .radius(120)
        .transitionDuration(1500)
        .dimension(cuisine_dim)
        .group(total_cuisine);

    dc.barChart('#course-chart')
        .width(600)
        .height(200)
        .margins({top: 10, right: 50, bottom: 30, left: 50})
        .transitionDuration(1500)
        .dimension(course_dim)
        .group(total_course)
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .xAxisLabel('Courses')
        .yAxis().ticks(4);

    dc.renderAll();
};


const getRecipesData = (url) => {

    // RETRIEVE WORD FROM SERVER AS JSON //
    getRequest(url)
        .then((response) => { 

            const data = JSON.parse(response);
            const recipeData = data;
            makePieGraph(recipeData);
            
        })
        .catch((error) => {
            console.log(error);
        })

};

//---------------------- CALL XHR -------------------------------------------//

getRecipesData('/stats');

//---------------------------------------------------------------------------//