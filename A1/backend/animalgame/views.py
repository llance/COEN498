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
from animalgame import QnA_pb2

objects_values = {};
asked_questions= {};
initial_questions = [];
count = 1

def mainPage(request):
    if request.method == 'GET':
        return render(request, 'index.html', context={'foo':'bar'})
    else:
        return HttpResponse(status=404)

class qna_proto(APIView):
    def post(self, request, format=None):
        global count
        global question
        global objects_values

        print("request.body in protobuf is :  ", request.body)

        response = QnA_pb2.Carrier()
        response.ParseFromString(request.body)

        # print("response in protobuf is : " + str(response))
        # print("response.question in protobuf is : " + str(response.question))
        # print("response.id in protobuf is : " + str(response.id))
        # print("response.answer in protobuf is : ", type(response.answer))

        yes_no_answer = None;
        if (response.answer == 'true'):
            yes_no_answer = 1
        if (response.answer == 'false'):
            yes_no_answer = -1

        game.update_local_knowledgebase(objects_values, asked_questions, response.id, yes_no_answer)

        count += 1

        question = game.choose_question(initial_questions, objects_values, asked_questions)

        serializer = serializers.QuestionSerializer(question)

        print("serializer.data is :" + str(serializer.data))

        if question == None or count > 20:
            chosen = game.guess(objects_values)
            print("chosen is : " + str(chosen))
            return Response(status=200)

        return Response(serializer.data)

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

        stream = BytesIO(request.body)
        data = JSONParser().parse(stream)

        print("data['question'].text is : " + str(data['question']['text']))
        print("data['answer'] is : " + str(data['answer']))

        yes_no_answer = None;
        if (str(data['answer']) == 'True'):
            yes_no_answer = 1
        if (str(data['answer']) == 'False'):
            yes_no_answer = -1

        game.update_local_knowledgebase(objects_values, asked_questions, data['question']['id'], yes_no_answer)

        print("asked_questions is : " + str(asked_questions))

        count += 1

        question = game.choose_question(initial_questions, objects_values, asked_questions)

        serializer = serializers.QuestionSerializer(question)

        print("serializer.data is :" + str(serializer.data))

        if question == None or count > 20:
            chosen = game.guess(objects_values)
            print("chosen is : " + str(chosen))
            return Response(status=200)

        return Response(serializer.data)


class guess(APIView):
    def get(self, request, format=None):
        '''Displays the computer's guess of who the user is thinking of.'''
        global objects_values
        chosen = game.guess(objects_values)

        print("chosen is : " + str(chosen))

        serializer = serializers.GuessSerializer(chosen)

        # for elem in chosen:
        #     print("elem is : " + elem)
        #     print("content in elem is : " + str(chosen[elem]))
        return Response(serializer.data, status=200)
