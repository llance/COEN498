import json

from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings

from shelvedApp.dbOperations import find_items


def getUserIdFromToken(jwt_token_no_bearer):
    get_pay_load_from_token = api_settings.JWT_DECODE_HANDLER

    get_user_name_hander = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

    get_user_id_hander = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER

    payload_from_token = get_pay_load_from_token(jwt_token_no_bearer)

    #print('payload_from_token', payload_from_token)

    userid_from_payload = get_user_id_hander(payload_from_token)

    user_from_payload = get_user_name_hander(payload_from_token)

    print('DjangoRestFramework user is ', user_from_payload, 'id is ', userid_from_payload)
    return user_from_payload


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
    

