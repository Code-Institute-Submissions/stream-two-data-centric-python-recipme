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
    })
}

const getRecipesData = (url) => {

    // RETRIEVE WORD FROM SERVER AS JSON //
    getRequest(url)
        .then((response) => {

            const dataRequest = JSON.parse(response);
            console.log(dataRequest);
        })
        .catch((error) => {
            console.log(error);
        })

}

getRecipesData('/stats');

