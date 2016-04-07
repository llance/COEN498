import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne
from shelvedApp.dbOperations import find_items
from shelvedApp.views import getUserIdFromToken

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
            jwt_token = request.META['HTTP_AUTHORIZATION']

            print('jwt_token', jwt_token)
            jwt_token_no_bearer = jwt_token[7:]
            print('jwt_token_no_bearer', jwt_token_no_bearer)
            userid_from_payload = getUserIdFromToken(jwt_token_no_bearer)

            data = find_items('type','book', userid_from_payload)
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)

def getMovies(request):
    try:
        if request.method == 'GET':

            jwt_token = request.META['HTTP_AUTHORIZATION']

            print('jwt_token', jwt_token)
            jwt_token_no_bearer = jwt_token[7:]
            print('jwt_token_no_bearer', jwt_token_no_bearer)
            userid_from_payload = getUserIdFromToken(jwt_token_no_bearer)

            data = find_items('type','movie', userid_from_payload)
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)
    
def getMusic(request):
    try:
        if request.method == 'GET':

            jwt_token = request.META['HTTP_AUTHORIZATION']

            print('jwt_token', jwt_token)
            jwt_token_no_bearer = jwt_token[7:]
            print('jwt_token_no_bearer', jwt_token_no_bearer)
            userid_from_payload = getUserIdFromToken(jwt_token_no_bearer)

            data = find_items('type','music', userid_from_payload)
            json_data = json.dumps(data)
            return HttpResponse(json_data, status=200)
    except:
        return HttpResponse(status=400)
    

