# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from animalgame.models import *
from animalgame import serializers


def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404);

class testView(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        questions = [question.text for question in Questions.objects.all()]
        return Response(questions)

class startGame(APIView):
    def get(self, request, format=None):
        randomQuestionIndex = random.randint(1, Questions.objects.all().count())
        #print("randomQuestionIndex is : " + str(randomQuestionIndex))
        try:
            firstQuestion = Questions.objects.get(pk=randomQuestionIndex)
        except Questions.DoesNotExist:
            raise

        print("first questions is : " + firstQuestion.text)
        #print("first questions id is : " + str(firstQuestion.id))

        serializer = serializers.QuestionSerializer(firstQuestion)
        print("serializer data is : " + str(serializer.data))

        return Response(serializer.data)

class questionAnswer(APIView):
    def post(self, request, format=None):
        print('request body is : ' + request.body);


        return Response("HELLO WORLD",status=200)


