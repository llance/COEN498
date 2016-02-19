jQuery(document).ready(function($) {
    var result;

    function httpGet(theUrl, calledFrom) {
        var xmlHttp = new XMLHttpRequest();
        var parsedJson;

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.response);

                //parsedJson = JSON.parse(xmlHttp.response);

                //if (calledFrom == 'guess'){
                //
                //    console.log("parsedJson.name is : " + parsedJson.name);
                //
                //    for (var key in parsedJson) {
                //        if (parsedJson.hasOwnProperty(key)) {
                //            console.log(key + " -> " + parsedJson[key]);
                //        }
                //    }
                //
                //    document.getElementById("contentHolder").innerHTML = parsedJson.name;

                //} else {
                //    result = parsedJson;
                //    for (var key in parsedJson) {
                //        if (parsedJson.hasOwnProperty(key)) {
                //            console.log(key + " -> " + parsedJson[key]);
                //        }
                //    }
                    //console.log("parsedJson['question'] is : " + parsedJson.text);

                    document.getElementById("contentHolder").innerHTML = xmlHttp.response;
                //}


            }
        }
        xmlHttp.open("GET", theUrl, true); // false for synchronous request
        xmlHttp.send();
    }

    $('#startButton').click(function() {
        var url = 'startGame';
        console.log("clicked" + url);
        httpGet(url);
    });
});
