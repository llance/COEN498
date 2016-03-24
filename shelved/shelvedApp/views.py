# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne
# from rest_framework import status, serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from django.contrib.auth import get_user_model
import mongoengine

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

def welcome(request):
    if request.method == 'GET':
        return render(request, 'index.html')

