//------------------------- FUNCTION DECLARATIONS ------------------------//

    //--------------------------- XHR EXPRESSIONS ----------------------------------------//

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

    const getRecipesData = () => {

        // RETRIEVE WORD FROM SERVER AS JSON //
        getRequest(`/`)
            .then((response) => {

                let dataRequest = JSON.parse(response);
                data = dataRequest;
            
            })
            .catch((error) => {
                console.log(error);
            })

    }
