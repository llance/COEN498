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

    function protobufPost(){
        var ProtoBuf = dcodeIO.ProtoBuf;
        //var protoify = protoify;
        var ByteBuffer = dcodeIO.ByteBuffer;

        var testjson = {                                                     // Object holding each data type
            1: 1,
            0.1: 0.1,
            "John": "John",
            true: true,
            false: false,
            null: null,
            array: [],
            object: {},
            undefined: undefined
        }

        var builder = ProtoBuf.loadProtoFile("../static/json.proto");
            Game = builder.build("Game"),
            Car = Game.Cars.Car;
        var car = new Car("Rusty", new Car.Vendor("Iron Inc.", new Car.Vendor.Address("US")), Car.Speed.SUPERFAST);

        var buffer = car.encode();

        //console.log("builder is : " + builder);
        //var buf = builder.build(testjson);

        // Print some nice debugging information
        console.log(JSON.stringify(testjson));
        console.log("-------------------------------------------------------------------");
        //console.log(ByteBuffer.wrap(buf).toDebug(true));

        //// Decode the Buffer back to JSON
        //var decodedSample = protoify.parse(buf);

        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                result = xmlHttp.responseText;
            }
            document.getElementById("contentHolder").innerHTML = xmlHttp.responseText;
        }
        xmlHttp.open("POST", 'prototest', true); // false for synchronous request
        xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xmlHttp.send(buffer);
    };


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

    $('#protoButton').click(function() {
        var url = 'guess';
        console.log("clicked" + url);
        protobufPost();
    });

    $('#nextQuestion').click(function() {
        var url = 'startGame';
        console.log("clicked" + url);
        httpGet(url);
    });
});
