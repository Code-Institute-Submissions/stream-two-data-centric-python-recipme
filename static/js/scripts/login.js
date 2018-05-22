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

    const getRecipesData = () => 

        // RETRIEVE WORD FROM SERVER AS JSON //
        getRequest(`/${username}/word`)
            .then((response) => {

                let dataRequest = JSON.parse(response);
                wordArray = dataRquest.guessWord;
                createDashes(wordArray);
                clearWinLoseMessage();
                clearImage();
                //console.log(wordArray);

            })
            .catch((error) => {

                console.log(error);
            })

    }
