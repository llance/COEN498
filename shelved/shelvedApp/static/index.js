var LoginModalController = {
    tabsElementName: ".logmod__tabs li",
    tabElementName: ".logmod__tab",
    inputElementsName: ".logmod__form .input",
    hidePasswordName: ".hide-password",

    inputElements: null,
    tabsElement: null,
    tabElement: null,
    hidePassword: null,

    activeTab: null,
    tabSelection: 0, // 0 - first, 1 - second

    findElements: function() {
        var base = this;

        base.tabsElement = $(base.tabsElementName);
        base.tabElement = $(base.tabElementName);
        base.inputElements = $(base.inputElementsName);
        base.hidePassword = $(base.hidePasswordName);

        return base;
    },

    setState: function(state) {
        var base = this,
            elem = null;

        if (!state) {
            state = 0;
        }

        if (base.tabsElement) {
            elem = $(base.tabsElement[state]);
            elem.addClass("current");
            $("." + elem.attr("data-tabtar")).addClass("show");
        }

        return base;
    },

    getActiveTab: function() {
        var base = this;

        base.tabsElement.each(function(i, el) {
            if ($(el).hasClass("current")) {
                base.activeTab = $(el);
            }
        });

        return base;
    },

    addClickEvents: function() {
        var base = this;

        base.hidePassword.on("click", function(e) {
            var $this = $(this),
                $pwInput = $this.prev("input");

            if ($pwInput.attr("type") == "password") {
                $pwInput.attr("type", "text");
                $this.text("Hide");
            } else {
                $pwInput.attr("type", "password");
                $this.text("Show");
            }
        });

        base.tabsElement.on("click", function(e) {
            var targetTab = $(this).attr("data-tabtar");

            e.preventDefault();
            base.activeTab.removeClass("current");
            base.activeTab = $(this);
            base.activeTab.addClass("current");

            base.tabElement.each(function(i, el) {
                el = $(el);
                el.removeClass("show");
                if (el.hasClass(targetTab)) {
                    el.addClass("show");
                }
            });
        });

        base.inputElements.find("label").on("click", function(e) {
            var $this = $(this),
                $input = $this.next("input");

            $input.focus();
        });

        return base;
    },

    initialize: function() {
        var base = this;

        base.findElements().setState().getActiveTab().addClickEvents();
    }
};


// function httpGet(theUrl, calledFrom) {
//     var xmlHttp = new XMLHttpRequest();
//     var parsedJson;

//     xmlHttp.onreadystatechange = function() {
//         if (xmlHttp.readyState == 4) {
//             console.log("xmlHttp response text is : " + xmlHttp.response);

//             parsedJson = JSON.parse(xmlHttp.response);

//             if (calledFrom == 'guess') {

//                 console.log("parsedJson.name is : " + parsedJson.name);

//                 for (var key in parsedJson) {
//                     if (parsedJson.hasOwnProperty(key)) {
//                         console.log(key + " -> " + parsedJson[key]);
//                     }
//                 }

//                 document.getElementById("contentHolder").innerHTML = parsedJson.name;

//             } else {
//                 result = parsedJson;
//                 for (var key in parsedJson) {
//                     if (parsedJson.hasOwnProperty(key)) {
//                         console.log(key + " -> " + parsedJson[key]);
//                     }
//                 }
//                 console.log("parsedJson['question'] is : " + parsedJson.text);

//                 document.getElementById("contentHolder").innerHTML = parsedJson.text;
//             }


//         }
//     }
//     xmlHttp.open("GET", theUrl, true); // false for synchronous request
//     xmlHttp.send();
// }

function httpPost(theUrl, jsonToSend) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("POST", theUrl, true); // false for synchronous request

    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4) {
            console.log("xmlHttp response text is : " + xmlHttp.responseText);
        }
    }

    xmlHttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

    var stringifiedJson = JSON.stringify(jsonToSend);
    xmlHttp.send(stringifiedJson);
}

jQuery(document).ready(function($) {
    LoginModalController.initialize();


    $('#regSubmit').click(function() {
        var url = 'register/';

        var registrationEmail = document.getElementById("user-email").value;
        var registrationPW = document.getElementById("user-pw").value;
        console.log("user-email is :", document.getElementById("user-email").value);
        console.log("user-email is :", document.getElementById("user-pw").value);

        var jsonResponse = {};
        jsonResponse.regEmail = registrationEmail;
        jsonResponse.regPW = registrationPW;

        httpPost(url, jsonResponse);

    });

});
