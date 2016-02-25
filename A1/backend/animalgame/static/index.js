jQuery(document).ready(function($) {
    var result;

    function httpGet(theUrl, calledFrom) {
        var xmlHttp = new XMLHttpRequest();
        var parsedJson;

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.response);

                parsedJson = JSON.parse(xmlHttp.response);

                if (calledFrom == 'guess'){

                    console.log("parsedJson.name is : " + parsedJson.name);

                    for (var key in parsedJson) {
                        if (parsedJson.hasOwnProperty(key)) {
                            console.log(key + " -> " + parsedJson[key]);
                        }
                    }

                    document.getElementById("contentHolder").innerHTML = parsedJson.name;

                } else {
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
                parsedJson = JSON.parse(xmlHttp.responseText);

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
        xmlHttp.open("POST", theUrl, true); // false for synchronous request
        xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        var jsonResponse = {};
        jsonResponse.question = result;
        jsonResponse.answer = AnswerInBool;
        var stringifiedJson = JSON.stringify(jsonResponse);

        xmlHttp.send(stringifiedJson);
    }



    function protobufPost(){
        var ProtoBuf = dcodeIO.ProtoBuf;
        var ByteBuffer = dcodeIO.ByteBuffer;

        var builder = ProtoBuf.loadProtoFile("../static/QnA.proto");
        console.log("builder is :  " + builder);
        var MyPkg = builder.build("MyPkg");
        console.log("MyPkg is :  " + MyPkg);

        var Carrier = MyPkg.Animals.Carrier;

        var response = new Carrier(question = "is this real life?", answer = "not sure");

        var buffer = response.encode();

        console.log("buffer is : " + buffer);

        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                console.log("xmlHttp response is : " + xmlHttp.response);
                result = xmlHttp.response;
                console.log("result is : " + typeof result);
                var rspPkg = builder.build("MyPkg");
                var rspCarrier = rspPkg.Animals.Carrier;
                var myMessage = rspCarrier.decode64(result);

                console.log("myMessage is : " + myMessage);
            }
            document.getElementById("contentHolder").innerHTML = xmlHttp.responseText;
        }
        xmlHttp.open("POST", 'prototest', true); // false for synchronous request
        xmlHttp.setRequestHeader("Content-Type", "application/x-google-protobuf;charset=UTF-8");
        console.log("buffer.toArrayBuffer() is : " + buffer.toArrayBuffer())
        xmlHttp.send(buffer.toArrayBuffer());
//
    };


    $('#yesButton').click(function() {
        var url = 'question_answer';
        //console.log("clicked" + testurl);
        httpPost(url, true);
    });

    $('#noButton').click(function() {
        var url = 'question_answer';
        console.log("clicked" + url);
        response = httpPost(url, false);

        parsedJson = JSON.parse(response);

        result = parsedJson;
        for (var key in parsedJson) {
            if (parsedJson.hasOwnProperty(key)) {
                console.log(key + " -> " + parsedJson[key]);
            }
        }
        console.log("parsedJson['question'] is : " + parsedJson.text);
        document.getElementById("contentHolder").innerHTML = response;

    });

    $('#guessButton').click(function() {
        var url = 'guess';
        console.log("clicked" + url);
        httpGet(url, "guess");
    });

    $('#protoButton').click(function() {
        var url = 'prototest';
        console.log("clicked" + url);
        protobufPost();
    });

    $('#nextQuestion').click(function() {
        var url = 'startGame';
        console.log("clicked" + url);
        httpGet(url);
    });
});
