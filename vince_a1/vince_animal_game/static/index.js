jQuery(document).ready(function($) {
    var result;

    //Initial question get
    function httpGet(url, question) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", url, true); // false for synchronous request
        xmlHttp.send();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                try {
                    parsedJson = JSON.parse(xmlHttp.responseText);
                }
                catch (err) {
                    document.getElementById("questionField").innerHTML = err.message;
                }
                result = parsedJson;
                for (var key in parsedJson) {
                    if (parsedJson.hasOwnProperty(key)) {
                        console.log(key + " -> " + parsedJson[key]);
                    }
                }
                console.log("parsedJson['question'] is : " + parsedJson['question']);
                document.getElementById("questionField").innerHTML = parsedJson['question'];
            }
        }
    }

    function httpPost(url, answer) {
        //Send JSON to backend
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("POST", url, true);
        xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        var jsonPayload = {};
        jsonPayload.question = $('.editText').text();
        console.log("question is : " + jsonPayload.question);
        jsonPayload.answer = answer;
        var serializedJSON = JSON.stringify(jsonPayload);
        xmlHttp.send(serializedJSON);

        //Wait for reply from backend
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                try {
                    parsedJson = JSON.parse(xmlHttp.responseText);
                }
                catch(err) {
                    document.getElementById("questionField").innerHTML = err.message;
                }
                result = parsedJson;
                for (var key in parsedJson) {
                    if (parsedJson.hasOwnProperty(key)) {
                        console.log(key + " -> " + parsedJson[key]);
                    }
                }
                console.log("parsedJson['question'] is : " + parsedJson['question']);
                document.getElementById("questionField").innerHTML = parsedJson['question'];
            }
        }
    }

    function protobufPost(url, answer){
        var ProtoBuf = dcodeIO.ProtoBuf;
        var ByteBuffer = dcodeIO.ByteBuffer;

        var builder = ProtoBuf.loadProtoFile("../static/protoSerializer.proto");
            protoData = builder.build("protoData");
            queryAnswer = protoData.animals.query;

        var response = new queryAnswer(question = $('.editText').text(), answer);

        var buffer = response.encode();

        console.log("buffer is : " + buffer);

        //Send protoBuf to backend
            var xmlHttp = new XMLHttpRequest();
            xmlHttp.open("POST", url , true); // false for synchronous request
            xmlHttp.setRequestHeader("Content-Type", "application/x-google-protobuf;charset=UTF-8");
            console.log("buffer.toArrayBuffer() is : " + buffer.toArrayBuffer())
            xmlHttp.send(buffer.toArrayBuffer());

        //Wait for reply from backend
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                try {
                    parsedJson = JSON.parse(xmlHttp.responseText);
                }
                catch(err) {
                    document.getElementById("questionField").innerHTML = err.message;
                }
                result = parsedJson;
                for (var key in parsedJson) {
                    if (parsedJson.hasOwnProperty(key)) {
                        console.log(key + " -> " + parsedJson[key]);
                    }
                }
                console.log("parsedJson['question'] is : " + parsedJson['question']);
                document.getElementById("questionField").innerHTML = parsedJson['question'];
            }
        }

    };

    $('#start').click(function() {
        console.log("clicked start button");
        $('#jsonButtons').toggle();
        $('#startButton').hide();
        $('#toggleButton').toggle();
        var url = 'get_question';
        console.log("clicked" + url);
        httpGet(url);
    });

    $('#toggleButton').click(function() {
        $(this).text(function(i,text){
            return text === "Use Protocol Buffers" ? "Use JSON" : "Use Protocol Buffers";
        })
        $('#jsonButtons').toggle();
        $('#protobufButtons').toggle();
    });

    $('#yesButton').click(function() {
        var url = 'json';
        console.log("clicked" + url);
        httpPost(url, true);
    });

    $('#yesproto').click(function() {
        var url = 'proto';
        console.log("clicked : " + url);
        protobufPost(url, true);
    });

    $('#noButton').click(function() {
        var url = 'json';
        console.log("clicked" + url);
        httpPost(url, false);
    });

    $('#noproto').click(function() {
        var url = 'proto';
        console.log("clicked : " + url);
        protobufPost(url, false);
    });

});
