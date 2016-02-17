# Create your views here.
import random
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from animalgame.models import *
from animalgame import serializers
from animalgame import game
from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser
from animalgame import json_pb2

objects_values = {};
asked_questions= {};
initial_questions = [];
count = 1

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        return HttpResponse(status=404);

@csrf_exempt
def prototest(request):
    if request.method == 'POST':
        print("request.body is :  " + request.body)
        car = json_pb2.Car();

        car.ParseFromString(request.body)

        print("car is : " + car);
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404);


# class mainPage(RetrieveAPIView):
#     def get(self, request, *args, **kwargs):
#         global initial_questions
#         global objects_values
#         global asked_questions
#         global count
#
#         print('foo');
#
#         renderer_classes = (TemplateHTMLRenderer,)
#
#         return Response(template_name='mainPage.html')
#
#         #'''Shows the index page and asks the questions.'''
#
#         # if config.DISPLAY_CANDIDATES: # clean up this section somehow
#         #     nearby_objects_values = game.get_nearby_objects_values(session.objects_values, how_many=10)
#         # else:
#         #     nearby_objects_values = None
#
#         # if not(session.get('asked_questions')) and not(session.get('initial_questions')):
#         #     question = 'begin'
#         # else:
#         #question = game.choose_question(initial_questions, objects_values, asked_questions)
#         # if question == None or count > 20:
#         #     chosen = game.guess(objects_values)
#         #     print("chosen is : " + str(chosen))
#         #     return Response(str(chosen), status=200)
#
#         #return render.index(question, session.get('count'), nearby_objects_values)
#
#         #return render(request, 'index.html')

# class askQuestion(APIView):
#     def get(self, request, format=None):
#         global initial_questions
#         global objects_values
#         global asked_questions
#
#         question = game.choose_question(initial_questions, objects_values, asked_questions)
#         if question is not None
#         return Response(question, status=200)


class startGame(APIView):
    def get(self, request, format=None):
        global initial_questions
        global objects_values
        initial_questions = game.load_initial_questions()
        objects_values = game.load_objects_values()

        randomQuestionIndex = random.randint(1, Questions.objects.all().count())
        #print("randomQuestionIndex is : " + str(randomQuestionIndex))
        try:
            firstQuestion = Questions.objects.get(pk=randomQuestionIndex)
        except Questions.DoesNotExist:
            raise

        print("objects_values is : " + str(objects_values))
        #print("first questions is : " + firstQuestion.text)
        #print("first questions id is : " + str(firstQuestion.id))

        serializer = serializers.QuestionSerializer(firstQuestion)
        print("serializer data is : " + str(serializer.data))

        return Response(serializer.data)



class questionAnswer(APIView):
    def post(self, request, format=None):
        '''Updates the local knowledgebase with the answer given to the question_id.'''
        global count
        global question
        global objects_values

        print("request.body is :  " + request.body)

        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)

        #print("data['question'] is : " + str(data['question']))
        print("data['question'].text is : " + str(data['question']['text']))
        print("data['answer'] is : " + str(data['answer']))

        # for elem in data['question']:
        #     print("elem is : " + str(elem))
        #
        # print("objects_values is : " + str(objects_values))

        yes_no_answer = None;
        if (str(data['answer']) == 'True'):
            yes_no_answer = 1

        if (str(data['answer']) == 'False'):
            yes_no_answer = -1

        game.update_local_knowledgebase(objects_values, data['question']['text'], data['question']['id'], yes_no_answer)

        count += 1

        question = game.choose_question(initial_questions, objects_values, asked_questions)

        if question == None or count > 20:
            chosen = game.guess(objects_values)
            print("chosen is : " + str(chosen))
            return Response(status=200)

        return startGame.as_view()(self.request)


class guess(APIView):
    def get(self, request, format=None):
        '''Displays the computer's guess of who the user is thinking of.'''
        global objects_values
        chosen = game.guess(objects_values)

        print("chosen is : " + str(chosen))
        return Response(str(chosen), status=200)
