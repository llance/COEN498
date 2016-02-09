# Create your views here.
from django.http import HttpResponse
from shelvedApp.models import *
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient, InsertOne, DeleteOne, ReplaceOne

@csrf_exempt
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
    if request.method == 'POST':

        print("POST Request body is : " + str(request.POST.get('foo')));

        myMongoClient = MongoClient()
        myMongoDb = myMongoClient.myMongoDb

        requests = [InsertOne({'y': str(request.POST.get('foo'))})]
        result = myMongoDb.test.bulk_write(requests)

        print('mongoDB write result is : ' + str(result));

        return HttpResponse("OK", status=200);

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