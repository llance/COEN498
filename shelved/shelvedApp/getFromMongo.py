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

        json_format_data = {}

        list_of_dict = []

        for elem in cursor:
            list_of_dict.append(elem)

        for listIndex, dict_in_list in enumerate(list_of_dict):
            for elem in dict_in_list:
                print("elem ", elem, 'val', dict_in_list[elem])
                if str(elem).find('_id') > -1: #ignore those while creating json
                    print('not an elem!')
                else:
                    json_format_data[elem] = dict_in_list[elem]
        print('json_format_data', json_format_data)
        json_data = json.dumps(json_format_data)
        return HttpResponse(json_data, status=200);

