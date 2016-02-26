jQuery(document).ready(function($) {
    var result;
    var jsonOrProto = true; //true for json, false for proto

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
        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                try {
                    parsedJson = JSON.parse(xmlHttp.responseText);
                }
                catch(err) {
                    document.getElementById("contentHolder").innerHTML = err.message;
                }
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

        if(jsonOrProto == true){
            xmlHttp.open("POST", theUrl, true); // false for synchronous request
            xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            var jsonResponse = {};
            jsonResponse.question = result;
            jsonResponse.answer = AnswerInBool;
            var stringifiedJson = JSON.stringify(jsonResponse);
            xmlHttp.send(stringifiedJson);

        } else{
            var ProtoBuf = dcodeIO.ProtoBuf;
            var ByteBuffer = dcodeIO.ByteBuffer;

            var builder = ProtoBuf.loadProtoFile("../static/QnA.proto");
            //console.log("builder is :  " + builder);
            var MyPkg = builder.build("MyPkg");
            //console.log("MyPkg is :  " + MyPkg);

            var Carrier = MyPkg.Animals.Carrier;

            console.log("Carrier is : " + Carrier);


            console.log("result is : " + String(result.text));
            console.log("id is : " + String(result.id));
            console.log("answerinbool is : " + AnswerInBool);

            var response = new Carrier(question = result.text, id = result.id, answer = String(AnswerInBool));

            console.log('response is : ' , response);
            var buffer = response.encode();

            var xmlHttp = new XMLHttpRequest();

            xmlHttp.open("POST", theUrl, true); // false for synchronous request
            xmlHttp.setRequestHeader("Content-Type", "application/x-google-protobuf;charset=UTF-8");
            console.log("buffer.toArrayBuffer() is : " + buffer.toArrayBuffer())
            xmlHttp.send(buffer.toArrayBuffer());
        }

    }


    $('#yesButton').click(function() {
        if (jsonOrProto == true){
            console.log("using json");
            var url = 'question_answer';
            //console.log("clicked" + testurl);
            httpPost(url, true);
        } else {
            console.log("using protobuf");
            var url = 'q_a_proto';
            httpPost(url, true);
        }

    });

    $('#noButton').click(function() {
        if (jsonOrProto == true){
            var url = 'question_answer';
            console.log("clicked" + url);
            httpPost(url, false);

        } else {
            console.log("using protobuf");
            var url = 'q_a_proto';
            httpPost(url, false);
        }


    });

    $('#guessButton').click(function() {
        var url = 'guess';
        console.log("clicked" + url);
        httpGet(url, "guess");
    });


    $('#nextQuestion').click(function() {
        var url = 'startGame';
        console.log("clicked" + url);
        httpGet(url);
    });

    $('#myonoffswitch').click(function() {
        if (jsonOrProto == true){
            console.log("switching to protobuf");
            jsonOrProto = false;
        } else {
            console.log("switching to json");
            jsonOrProto = true;
        }
    });

});
