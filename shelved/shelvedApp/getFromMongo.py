import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne



@csrf_exempt
def getBooks(request):
    if request.method == 'GET':
        myMongoClient = MongoClient()
        myMongoDb = myMongoClient.myMongoDb
        cursor = myMongoDb.books.find()

        list_of_dict = []

        for elem in cursor:
            list_of_dict.append(elem)

        for listIndex, dict_in_list in enumerate(list_of_dict):
            for elem in dict_in_list:
                print ("elem ",elem, 'val', dict_in_list[elem])
                createJson(dict_in_list[elem])
                # if str(elem).contains("u'_id'"):
                #     print('contain')

        data = {}
        data['title'] = ''
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=200);

def createJson(data_in_dict):
    data = {}

    for key in data_in_dict:
        print('key', key, 'val', data_in_dict[key])