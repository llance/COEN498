jQuery(document).ready(function($) {

    function httpGet(theUrl) {
        var xmlHttp = new XMLHttpRequest();
        xmlHttp.open("GET", theUrl, false); // false for synchronous request
        xmlHttp.send(null);
        return xmlHttp.responseText;
    }


    $('#sendHttp').click(function() {
        console.log("clicked" + testurl);

        var testurl = 'test';
        httpGet();
    });

});
