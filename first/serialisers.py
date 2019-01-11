from .models import Question, Choice
from rest_framework import serializers


class ChoiceSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text', 'votes')


class DynamicFieldsSerializerMixin(object):

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)
        print(fields)

        # Instantiate the superclass normally
        super(DynamicFieldsSerializerMixin, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class QuestionChoiceSerialiser(DynamicFieldsSerializerMixin, serializers.ModelSerializer):
    choice_set = ChoiceSerialiser(many=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choice_set')


class QuestionSerialiser(serializers.ModelSerializer):
    # choice_set = ChoiceSerialiser(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
