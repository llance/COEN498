# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from . import game
from . import protoSerializer_pb2
from . import serializers

iterations = 0

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404)

class get_question(APIView):
    def get(self, request, format=None):
        initialQuestion = game.first_question()
        initialQuestion = serializers.QuestionSerializer(initialQuestion)
        return Response(initialQuestion.data, status=200)

class proto(APIView):
    def post(self, request, format=None):
        payload = {}
        global iterations
        iterations += 1
        protoBufMessage = protoSerializer_pb2.query()
        protoBufMessage.ParseFromString(request.body)
        #next_question = game.play(protoBufMessage)
        payload['question'] = protoBufMessage.question
        payload['answer'] = protoBufMessage.answer
        print("Parsed protocol Buffer message is : " + str(protoBufMessage))
        next_question = game.play(payload)
        #next_question = {'question' : 'next question'}
        next_question = serializers.QuestionSerializer(next_question)
        return Response(next_question.data, status=200)

class json(APIView):
    def post(self, request, format=None):

        global iterations
        iterations += 1
        requestBody = BytesIO(request.body)
        jsonPayload = JSONParser().parse(requestBody)
        next_question = game.play(jsonPayload)
        print(next_question)
        #next_question = {'question' : 'next question'}
        next_question = serializers.QuestionSerializer(next_question)
        print(next_question.data)
        return Response(next_question.data, status=200)