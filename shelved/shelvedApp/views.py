# Create your views here.
from django.http import HttpResponse
from django.db import models
from djangotoolbox.fields import ListField
from mongoengine import *
from shelvedApp.models import *


def play(request):
    if request.method == 'GET':
        print('user clicked yes ');

        connect('myMongoDb') #connect to db called myMongoDb
        post = Post.objects.create(
            title='Hello MongoDB!',
            text='Just wanted to drop a note from Django. Cya!',
            tags=['mongodb', 'django'])
        post.save()
        return HttpResponse("hello world",status=200)


def retrieve(request):
    if request.method == 'GET':
        print('retrieving from mongo');

    connect('myMongoDb') #connect to db called myMongoDb
    for post in Post.objects.all():
        print("post is : " + str(post.title))
    return HttpResponse("hello world",status=200)