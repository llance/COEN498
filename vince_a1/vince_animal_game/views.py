# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . import game
from . import protoSerializer_pb2


def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404)

class get_question(APIView):
    def get(self, request, format=None):
        '''Displays the computer's guess of who the user is thinking of.'''
        jsondata = game.load_json()
        qs = jsondata["questions"]
        # questions = {i: q for i, q in zip(range(len(qs)), qs)}
        # animals = copy.deepcopy(jsondata["animals"])
        # responses = [None for i in range(len(questions))]
        # response_yes = None
        return Response(qs[1], status=200)

class protoBufTest(APIView):
    def post(self, request, format=None):
        country = protoSerializer_pb2.protoMessage()
        country.ParseFromString(request.body)
        print ("country is : " + country)
        return Response(country, status=200)
