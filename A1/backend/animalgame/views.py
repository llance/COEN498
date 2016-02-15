# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from animalgame.models import *
from animalgame import serializers
from animalgame import game
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser

objects_values = {};

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

        global objects_values
        objects_values = game.load_objects_values();

        print("objects_values is : " + str(objects_values))
        #print("first questions is : " + firstQuestion.text)
        #print("first questions id is : " + str(firstQuestion.id))

        serializer = serializers.QuestionSerializer(firstQuestion)
        print("serializer data is : " + str(serializer.data))

        return Response(serializer.data)


class questionAnswer(APIView):
    def post(self, request, format=None):

        '''Updates the local knowledgebase with the answer given to the question_id.'''

        print("request.body is :  " + request.body)

        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)

        print("data['question'] is : " + str(data['question']))
        print("data['answer'] is : " + str(data['answer']))


        print("data['question'].text is : " + str(data['question']['text']))



        for elem in data['question']:
            print("elem is : " + str(elem))

        print("objects_values is : " + str(objects_values))

        if (str(data['answer']) == True):
            yes_no_answer = 'yes'
        if (str(data['answer']) == False):
            print('foo')
            yes_no_answer = 'no'


        game.update_local_knowledgebase(objects_values, data['question']['text'], data['question']['id'], -1)


        # question_id = int(question_id) # otherwise it's unicode
        # a = web.input().answer
        # if a in ['yes','no','unsure']: answer = eval('game.' + a)
        # else: answer = game.unsure
        # if answer != game.unsure:
        #     session.count += 1
        # game.update_local_knowledgebase(session.objects_values, session.asked_questions, question_id, answer)
        # raise web.seeother('/')

        return Response("HELLO WORLD",status=200)
