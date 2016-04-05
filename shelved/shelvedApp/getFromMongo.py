import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne



@csrf_exempt
def getBooks(request):
    if request.method == 'GET':
        myMongoClient = MongoClient()
        myMongoDb = myMongoClient.myMongoDb
        insertedDatas = myMongoDb.books.find()

        for insertedData in insertedDatas:
            print("data from mongo is : " + str(insertedData))
            insertedData


        data = {}
        data['title'] = ''
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=200);

