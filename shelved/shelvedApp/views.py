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
from shelvedApp import getFromMongo
from django.http import HttpResponse


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


#@csrf_exempt
@method_decorator(ensure_csrf_cookie)
def login(request):
    if request.method == 'POST':
        # c = {}
        # c.update(csrf(request))
        #
        # print('csrf is ', c)
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
            token = Token.objects.create(user=user)
            print('token key is : ', token.key)
            data = {}
            data['token'] = token.key
            json_data = json.dumps(data)
            # data['csrf'] = c
            return HttpResponse(json_data, status=201);

@csrf_exempt
#@csrf_protect
#@login_required(login_url='/login')
def addBook(request):
    print('called!', request.user.is_anonymous())
    requestbody = json.loads(request.body)

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

    upc = requestbody['upc']
    print("movie upc is", upc)
    booktitle = queryGoogle(ibsnNumber)

    data = {}
    data['title'] = booktitle
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


class books(APIView):
    print('book called')
    def get(self, request, format=None):
        """
        Return a list of all books.
        """

        getFromMongo.getMovies(request)

    def post(self, request, format=None):
        """
        Add a movie.
        """
        addBook(request)

