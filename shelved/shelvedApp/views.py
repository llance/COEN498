# Create your views here.
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView

from shelvedApp.googleQuery import queryGoogle
from shelvedApp.amazonQuery import queryAmazon
from shelvedApp.dbOperations import deleteItem
from shelvedApp import getFromMongo
from django.http import HttpResponse
from rest_framework_jwt.settings import api_settings

from rest_framework.authtoken.models import Token




@csrf_exempt
def register(request):
    if request.method == 'POST':
        print("register called!, body is :", request.body)

        requestbody = json.loads(request.body)

        # for elem in requestbody:
        #     print ('elem is ', elem, 'val is :',requestbody[elem])

        regUsername = requestbody['username']
        regPW = requestbody['password']

        # print('regUsername is ', regUsername, 'regPW is ', regPW)

        # password  = request.POST.get("password")
        # if password != request.POST.get("passwordConfirm"):
        #    return redirect("/?passwords_dont_match")

        try:
            user = User.objects.create_user(
                username=regUsername,
                email=regUsername,
                password=regPW)

        except IntegrityError:
            print("already registered")
            #return redirect("/?id_already_used")

        # print("jwt_auth.views.obtain_jwt_token is :", jwt_auth.views.ObtainJSONWebToken.post(request))
        user.save()

        return HttpResponse("user created!", status=201)


@csrf_exempt
#@method_decorator(ensure_csrf_cookie)
def login(request):
    if request.method == 'POST':
        requestbody = json.loads(request.body)

        for elem in requestbody:
            print ('elem is ', elem, 'val is :',requestbody[elem])

        regUsername = requestbody['username']
        regPW = requestbody['password']

        user = authenticate(
            username = regUsername,
            password = regPW)

        if user is None:
            return HttpResponse("you have either given wrong user name or wrong password", status=404);

        if user is not None and user.is_active:
            print("logging in ", user)
            auth_login(request, user)
            rest_token = Token.objects.create(user=user)
            print('rest_token key is : ', rest_token.key)


            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)

            print('jwt_token is ', jwt_token)

            data = {}
            data['resttoken'] = rest_token.key
            data['jwttoken'] = jwt_token

            json_data = json.dumps(data)
            return HttpResponse(json_data, status=201);

@csrf_exempt
#@csrf_protect
#@login_required(login_url='/login')
def addBook(request):
    print('called!', request.user.is_anonymous())
    requestbody = json.loads(request.body)
    print('jwt header is in',request.META['HTTP_AUTHORIZATION'])

    # for key in request.META:
    #     print('key', key, 'val', request.META[key])

    jwt_token = request.META['HTTP_AUTHORIZATION']

    print('jwt_token', jwt_token)
    jwt_token_no_bearer = jwt_token[7:]
    print('jwt_token_no_bearer', jwt_token_no_bearer)

    get_pay_load_from_token = api_settings.JWT_DECODE_HANDLER

    get_user_name_hander = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

    get_user_id_hander = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER

    payload_from_token = get_pay_load_from_token(jwt_token_no_bearer)

    print('payload_from_token', payload_from_token)

    userid_from_payload = get_user_id_hander(payload_from_token)

    user_from_payload = get_user_name_hander(payload_from_token)

    print('DjangoRestFramework user is ', user_from_payload, 'id is ', userid_from_payload)



    # for elem in requestbody:
    #     print ('elem is ', elem, 'val is :',requestbody[elem])
    """current user is always empty, no way to find the current user

    current_user = request.user
    import pdb; pdb.set_trace()
    print('User ID is : ' + current_user.id)
    """

    ibsnNumber = requestbody['ibsnNum']
    print("ibsnNumber is", ibsnNumber)
    booktitle = queryGoogle(ibsnNumber)

    data = {}
    data['title'] = booktitle
    json_data = json.dumps(data)
    return HttpResponse(json_data, status=200);

@csrf_exempt
#@csrf_protect
# @login_required(login_url='/login')
def addMovie(request):
    requestbody = json.loads(request.body)

    # for elem in requestbody:
    #     print ('elem is ', elem, 'val is :',requestbody[elem])
    """current user is always empty, no way to find the current user

    current_user = request.user
    import pdb; pdb.set_trace()
    print('User ID is : ' + current_user.id)
    """

    upc = requestbody['upcNum']
    print("movie upc is", upc)
    booktitle = queryAmazon(upc)

    data = {}
    data['title'] = booktitle
    json_data = json.dumps(data)
    return HttpResponse(json_data, status=200);

@csrf_exempt
#@csrf_protect
# @login_required(login_url='/login')
def delete(request):
    if request.method == 'DELETE':
        requestbody = json.loads(request.body)

        # for elem in requestbody:
        #     print ('elem is ', elem, 'val is :',requestbody[elem])
        """current user is always empty, no way to find the current user

        current_user = request.user
        import pdb; pdb.set_trace()
        print('User ID is : ' + current_user.id)
        """

        item_type = requestbody['item_type']
        unique_id = requestbody['unique_id']
        count = deleteItem(item_type, unique_id)

        data = {}
        data['deleted_count'] = count
        json_data = json.dumps(data)
        return HttpResponse(json_data, status=200);


class movies(APIView):

    def get(self, request, format=None):
        """
        Return a list of all movies.
        """
        getFromMongo.getMovies(request)

    def post(self, request, format=None):
        """
        Add a movie.
        """
        addMovie(request)

    def delete(self, request, format=None):
        """
        Delete a movie.
        """
        deleteMovie(request)


class books(APIView):
    #print('book called')
    def get(self, request, format=None):
        """
        Return a list of all books.
        """

        getFromMongo.getMovies(request)

    def post(self, request, format=None):
        """
        Add a book.
        """
        addBook(request)

    def delete(self,request, format=None):
        """
        delete a book
        """
        deleteBook(request)

