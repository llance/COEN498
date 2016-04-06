import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne
from shelvedApp.dbOperations import find_items

# @csrf_exempt
# def getBooks(request):
#     if request.method == 'GET':
#         myMongoClient = MongoClient()
#         myMongoDb = myMongoClient.myMongoDb
#         cursor = myMongoDb.books.find()

#         json_format_data = {}

#         list_of_dict = []

#         for elem in cursor:
#             list_of_dict.append(elem)

#         for listIndex, dict_in_list in enumerate(list_of_dict):
#             for elem in dict_in_list:
#                 print("elem ", elem, 'val', dict_in_list[elem])
#                 if str(elem).find('_id') > -1: #ignore those while creating json
#                     print('not an elem!')
#                 else:
#                     json_format_data[elem] = dict_in_list[elem]
#         print('json_format_data', json_format_data)
#         json_data = json.dumps(json_format_data)
#         return HttpResponse(json_data, status=200);

def getBooks(request):
    try:
        if request.method == 'GET':
            #current_user = request.user
            data = find_items('type','book',current_user='books')
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)

def getMovies(request):
    try:
        if request.method == 'GET':
            #current_user = request.user
            data = find_items('type','movie',current_user='books')
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)
    
def getMusic(request):
    try:
        if request.method == 'GET':
            #current_user = request.user
            data = find_items('type','music',current_user='books')
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)
    

