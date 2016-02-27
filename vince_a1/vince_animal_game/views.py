# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.six import BytesIO
from . import game
from . import protoSerializer_pb2

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404)

class get_question(APIView):
    def get(self, request, format=None):
        initialQuestion = game.first_question()
        print("first question is: " + initialQuestion)
        return Response(initialQuestion, status=200)

class proto(APIView):
    def post(self, request, format=None):
        protoBufMessage = protoSerializer_pb2.protoMessage()
        protoBufMessage.ParseFromString(request.body)
        print("Parsed protocol Buffer message is : " + str(protoBufMessage))
        return Response(str(protoBufMessage), status=200)

class json(APIView):
    def post(self, request, format=None):
        requestBody = BytesIO(request.body)
        jsonPayload = JSONParser().parse(requestBody)
        print("jsonPayload['question'].text is : " + str(jsonPayload['question']['text']))
        print("jsonPayload['answer'] is : " + str(jsonPayload['answer']))
        return Response(str(protoBufMessage), status=200)