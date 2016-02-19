from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import serializers


def janice(request):
    return render(request, 'home.html', {})


class start(APIView):
    def get(self, request, format=None):
        print("objects_values is : " + str("weh"))

        # serializer = serializers.QuestionSerializer("testId")
        # print("serializer data is : " + str(serializer.data))
        return Response("hello")
