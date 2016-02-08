# Create your views here.
from animalgame.models import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
# from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


def test(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def play(request):
    if request.method == 'GET':
        print('user clicked yes ');

        return HttpResponse("hello world",status=200)


    if request.method == 'POST':
        print('request body is : ' + request.body);

        #parse through the body

def test3(request):
    if request.method == 'GET':
        print("user clicked no");
        return HttpResponse("why you lyin",status=200)


def testDB(request):
    if request.method == 'GET':
        print("testdb called!");
        questions = Questions.objects.all();
        #print("question is : " + str(questions));
        for question in questions:
            print("question is : " + str(question.text));
        return HttpResponse("why you lyin",status=200)