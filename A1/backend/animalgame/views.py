# Create your views here.
from animalgame.models import *
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

# from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html')
    else:
        return HttpResponse(status=404);

def startGame(request):
    if request.method == 'GET':

        print("start game has been called")
        return render_to_response('test.html', context_instance=RequestContext(request))
    else:
        return HttpResponse(status=404);







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

        objects = Objects.objects.all();

        playlog = Playlog.objects.all();

        for pl in playlog:
            print("playlog is : " + str(pl.data));

        # for object in objects:
        #     print("object is : " + str(object.name));

        #print("question is : " + str(questions));
        #for question in questions:
        #    print("question is : " + str(question.text));
        return HttpResponse("why you lyin",status=200)