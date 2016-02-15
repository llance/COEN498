jQuery(document).ready(function($) {
    var result;

    function httpGet(theUrl) {
        var xmlHttp = new XMLHttpRequest();
        var parsedJson;

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.response);

                parsedJson = JSON.parse(xmlHttp.response);

                result = parsedJson;
                for (var key in parsedJson) {
                  if (parsedJson.hasOwnProperty(key)) {
                    console.log(key + " -> " + parsedJson[key]);
                  }
                }
                console.log("parsedJson['question'] is : " + parsedJson.text);

                document.getElementById("contentHolder").innerHTML = parsedJson.text;
            }
        }
        xmlHttp.open("GET", theUrl, true); // false for synchronous request
        xmlHttp.send();

    }

    function httpPost(theUrl, AnswerInBool) {
        console.log("result is : " + result);
        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                result = xmlHttp.responseText;
            }
            document.getElementById("contentHolder").innerHTML = xmlHttp.responseText;
        }
        xmlHttp.open("POST", theUrl, true); // false for synchronous request
        xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        var jsonResponse = {};
        jsonResponse.question = result;
        jsonResponse.answer = AnswerInBool;
        var stringifiedJson = JSON.stringify(jsonResponse);

        xmlHttp.send(stringifiedJson);
    }


    $('#yesButton').click(function() {
        var url = 'question_answer';
        //console.log("clicked" + testurl);
        httpPost(url, true);
    });

    $('#noButton').click(function() {
        var url = 'question_answer';
        console.log("clicked" + url);
        httpPost(url, false);
    });

    $('#guessButton').click(function() {
        var url = 'guess';
        console.log("clicked" + url);
        httpGet(url, false);
    });

    $('#nextQuestion').click(function() {
        var url = 'startGame';
        console.log("clicked" + url);
        httpGet(url);
    });
});
