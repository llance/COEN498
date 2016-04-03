__author__ = 'lanceli'

import datetime
import requests
from django.utils import timezone
import os
from amazon.api import AmazonAPI



def getBookByISBN(request):
    timeNowISO8601 = datetime.datetime.now().isoformat()

    os.environ['TZ'] = 'America/Toronto'

    print("timezone is : ", timezone.localtime(timezone.now()))

    print("current date time : ", timeNowISO8601)

    print("formated iso time now",timeNowISO8601[:timeNowISO8601.rfind('.')])

    formatedTimeNow = timeNowISO8601[:timeNowISO8601.rfind('.')] + 'Z'

    httpUrl = "http://webservices.amazon.com/onca/xml?  Service=AWSECommerceService  &Operation=ItemLookup  &ResponseGroup=Large  &SearchIndex=All  &IdType=ISBN  &ItemId=076243631X  &AWSAccessKeyId=[Your_AWSAccessKeyID]  &AssociateTag=[Your_AssociateTag]  &Timestamp=" + formatedTimeNow + " &Signature=[Request_Signature]"

    r = requests.get(httpUrl)
    print("hello foobar", r.text)


#revised method using the simple amazon api
def queryAmazon(upc):
    amazon = AmazonAPI('AKIAIQOSMQ3XYLJ2OWOQ','xBV4OLH9/OorIXGHhUzyeSkPuQGnME/QVQsKQfGS', 'shelvedWebApp')
    product = amazon.lookup(IdType='UPC', ItemId=upc , SearchIndex='All')
    title = product.title #title, include "(format)"
    format = product.binding #explicit format type "blu-ray" or "dvd"
    #all other attributes are variable ; published, label, creators...


    # var today = new Date();
    # var day = today.getDate();
    # var month = today.getMonth()+1;
    # var year = today.getFullYear();
    # var hours = today.getHours() < 10 ? "0"+today.getHours() : today.getHours();
    # var seconds = today.getSeconds() < 10 ? "0"+today.getSeconds() : today.getSeconds();
    # var mins = today.getMinutes() < 10 ? "0"+today.getMinutes() : today.getMinutes();
    # var time = encodeURIComponent(year+"-"+month+"-"+day+"T"+hours+":"+mins+":"+seconds+"Z");
    # var messageToEncrypt ="GET\nwebservices.amazon.com\n\
    #     /onca/xml\nAWSAccessKeyId=ACCESSID&ItemId=0679722769&&SignatureMethod=HmacSHA256&SignatureVersion=2&Operation=ItemLookup&ResponseGroup=ItemAttributes%2COffers%2CImages%2CReviews&Service=AWSECommerceService&Timestamp="+time+"&Version=2013-08-01";
    #
    # var sig = CryptoJS.HmacSHA256(messageToEncrypt, "SECRET KEY");
    #
    # var request = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&AWSAccessKeyId=AccessID&Operation=ItemLookup&ItemId=0976925524&ResponseGroup=SalesRank&Version=2013-08-01&Timestamp="+time+"&Signature="+sig;
    #
    #
    # function GET(url) {
    #     var oFrame = document.getElementById("MyAjaxFrame");
    #     if (!oFrame) {
    #         oFrame = document.createElement("iframe");
    #         oFrame.style.display = "none";
    #         oFrame.id = "MyAjaxFrame";
    #         document.body.appendChild(oFrame);
    #     }
    #     oFrame.src = url;
    # }
    #
    # GET(request);