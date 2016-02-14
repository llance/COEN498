__author__ = 'lanceli'

from rest_framework import serializers

from animalgame.models import *

class QuestionSerializer(serializers.Serializer):
    id = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField()
