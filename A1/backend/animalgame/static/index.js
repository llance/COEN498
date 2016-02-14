jQuery(document).ready(function($) {
    function httpGet(theUrl) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                console.log("xmlHttp response text is : " + xmlHttp.responseText);
            }
            document.getElementById("contentHolder").innerHTML = xmlHttp.responseText;
        }
        xmlHttp.open("GET", theUrl, true); // false for synchronous request
        xmlHttp.send();
    }

    function httpg(theUrl) {
        var xmlHttp = new XMLHttpRequest();

        xmlHttp.onreadystatechange = function() {
            if (xmlHttp.readyState == 4) {
                //console.log("xmlHttp response text is : " + xmlHttp.responseText);

                document.write(xmlHttp.response);

            }
        }
        xmlHttp.open("GET", theUrl, true); // false for synchronous request
        xmlHttp.send();
    }

    $('#yesButton').click(function() {
        var url = 'play';
        //console.log("clicked" + testurl);
        httpGet(url);
    });

    $('#noButton').click(function() {
        var testurl = 'test3';

        console.log("foo : " + $('#contentHolder').data("my_data"));
        console.log("clicked" + testurl);
        httpGet(testurl);
    });

    $('#playNow').click(function() {
            httpg('startGame');

        }

    );
});
