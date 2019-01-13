from rest_framework import viewsets, generics
from first.models import Question
from first.serialisers import QuestionSerialiser

# class QuestionViewSet(viewsets.ModelViewSet):
#     queryset = models.Question.objects.all()
#     serializer_class = serialisers.QuestionSerialiser


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerialiser

    @classmethod
    def get_extra_actions(cls):
        return []


# class QuestionChoiceViewSet(viewsets.ModelViewSet):
#     queryset = models.Question.objects.all()
#     serializer_class = serialisers.QuestionChoiceSerialiser


# class ChoiceViewSet(viewsets.ModelViewSet):
#     queryset = models.Choice.objects.all()
#     serializer_class = serialisers.ChoiceSerialiser
