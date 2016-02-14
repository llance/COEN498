# Create your views here.
from animalgame.models import *
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import random
import json
from animalgame import serializers
# from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response



def mainPage(request):
    if request.method == 'GET':
        return render(request, 'mainPage.html')
    else:
        return HttpResponse(status=404);

class testView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        questions = [question.text for question in Questions.objects.all()]
        return Response(questions)


def startGame(request):
    if request.method == 'GET':
        print("start game has been called");

        randomQuestionIndex = random.randint(1, Questions.objects.all().count())
        #print("randomQuestionIndex is : " + str(randomQuestionIndex))
        #print("total number of questions is : ", Questions.objects.all().count())
        #print("first questions is : " + str(Questions.objects.get(pk=randomQuestionIndex)))

        try:
            firstQuestion = Questions.objects.get(pk=randomQuestionIndex)
        except Questions.DoesNotExist:
            raise

        print("first questions is : " + firstQuestion.text)
        #print("first questions id is : " + str(firstQuestion.id))

        serializer = serializers.QuestionSerializer(firstQuestion)
        print("serializer data is : " + str(serializer.data))

        # data = {}
        # data['question'] = firstQuestion.text
        # json_data = json.dumps(data)

        return render(request, 'index.html', context={"my_data": data} )
    else:
        return HttpResponse(status=404);


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