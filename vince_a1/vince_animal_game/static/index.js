jQuery(document).ready(function($) {
    var result;

    function httpGet(theUrl, calledFrom) {
        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.response);

                    document.getElementById("contentHolder").innerHTML =xmlHttp.response;
                }
            }

        xmlHttp.open("GET", theUrl, true); // false for synchronous request
        xmlHttp.send();
    }

    function protobufPost(url){
        var ProtoBuf = dcodeIO.ProtoBuf;
        var ByteBuffer = dcodeIO.ByteBuffer;

        var builder = ProtoBuf.loadProtoFile("../static/protoSerializer.proto");

        var byteProto = builder.build("protoData");

        var payloadMessage = byteProto.test.protoMessage;

        var response = new payloadMessage(question = "foo", answer = "bar");

        var buffer = response.encode();

        console.log("buffer is : " + buffer);

        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
                result = xmlHttp.responseText;
                console.log("result is : " + typeof result);
                protoData = builder.build("protoData");
                payloadMessage = protoData.test.protoMessage;
                var myMessage = payloadMessage.decode64(result);

                console.log("myMessage is : " + myMessage);
            }
            document.getElementById("contentHolder").innerHTML = xmlHttp.responseText;
        }
        xmlHttp.open("POST", url , true); // false for synchronous request
        xmlHttp.setRequestHeader("Content-Type", "application/x-google-protobuf;charset=UTF-8");
        console.log("buffer.toArrayBuffer() is : " + buffer.toArrayBuffer())
        xmlHttp.send(buffer.toArrayBuffer());
    };




    $('#yesButton').click(function() {
        var url = 'get_question';
        console.log("clicked" + url);
        httpGet(url);
    });

    $('#protobuf').click(function() {
        var url = 'protoBuf';
        console.log("clicked" + url);
        protobufPost(url);
    });

});
