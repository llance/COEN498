# Create your views here.
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne
from django.contrib.auth.models import User
from django.db import IntegrityError
import mongoengine
from django.contrib.auth import authenticate
from django.shortcuts import render
from shelvedApp.models import *
from shelvedApp.googleQuery import queryGoogle


@csrf_exempt
def set(request):
    if request.method == 'POST':
        print("POST Request body is : " + str(request.POST.get('foo')));
        myMongoClient = MongoClient()
        myMongoDb = myMongoClient.myMongoDb

        requests = [InsertOne({'y': str(request.POST.get('foo'))})]
        result = myMongoDb.test.bulk_write(requests)

        print('mongoDB write result is : ' + str(result));

        return HttpResponse("OK", status=200);
    else:
        return HttpResponse(status=400)

@csrf_exempt
def setwithMongoEngine(request):
    if request.method == 'POST':
        print("POST Request body is : " + str(request.POST.get('foo')));

        myPost = Post.objects.create(
            title="foo",
            text="bar",
        )

        my_con = mongoengine.connect(db='myMongoDb', alias='default')
        myPost.save()
        #my_con.disconnect()


        return HttpResponse("OK", status=200);
    else:
        return HttpResponse(status=400)



@csrf_exempt
def welcome(request):
    if request.method == 'GET':
        return render(request, 'index.html')

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

        return HttpResponse(status=201)



@csrf_exempt
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
            return HttpResponse("logged in!", status=200);


@csrf_exempt
def addIbsn(request):
    if request.method == 'POST':

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

