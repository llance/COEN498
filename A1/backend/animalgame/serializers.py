__author__ = 'lanceli'

from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    id = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField()
