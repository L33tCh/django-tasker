from .models import Question, Choice
from rest_framework import serializers


class ChoiceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text', 'votes')


class QuestionSerialiser(serializers.ModelSerializer):
    choice_set = ChoiceSerialiser(many=True)
    # choice_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'choice_set')
