from .models import Question
from rest_framework import serializers


class QuestionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')
