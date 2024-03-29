__author__ = 'lanceli'

from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    id = serializers.CharField()
    text = serializers.CharField()
    created = serializers.DateTimeField()


class GuessSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    created = serializers.DateField()
    times_played = serializers.IntegerField()
    last_played = serializers.DateField()



