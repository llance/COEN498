# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne
# from rest_framework import status, serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import IntegrityError
import mongoengine
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
import json

from shelvedApp.models import *


# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         print("username is : " + str(request.POST.get('username')));
#         print("password is : " + str(request.POST.get('password')));
#
#         return HttpResponse("OK", status=200);
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#
# @api_view(['POST'])
# def register(request):
#     VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
#     DEFAULTS = {
#         # you can define any defaults that you would like for the user, here
#     }
#     serialized = UserSerializer(data=request.DATA)
#     if serialized.is_valid():
#         user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
#         user_data.update(DEFAULTS)
#         user = get_user_model().objects.create_user(
#             **user_data
#         )
#         return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


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
def retrieve(request):
    if request.method == 'GET':
        print('retrieving from mongo');
        myMongoClient = MongoClient()
        myMongoDb = myMongoClient.myMongoDb
        insertedDatas = myMongoDb.test.find()

        for insertedData in insertedDatas:
            print("post title is : " + str(insertedData) )

        return HttpResponse("hello world",status=200)

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

        print("trying to save user")
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

