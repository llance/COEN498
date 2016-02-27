from rest_framework import serializers

#Serialize question to JSON
class QuestionSerializer(serializers.Serializer):
    question = serializers.CharField()


class GuessSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    created = serializers.DateField()
    times_played = serializers.IntegerField()
    last_played = serializers.DateField()
