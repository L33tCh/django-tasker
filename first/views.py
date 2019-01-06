from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Question
from .serialisers import QuestionSerialiser


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)


class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)


# class QuestionSerialiser(serializers.Serializer):
#     question_text = serializers.CharField(max_length=255)
#
#     def create(self, validated_data):
#         return Question.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.question_text = validated_data.get('question_text', instance.question_text)
#         instance.save()
#         return instance


def questions(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('links.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    s = QuestionSerialiser(latest_question_list, many=True)
    # print(s.data)
    # return s.data
    return JsonResponse(s.data, safe=False)
    # return context


def links(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('links.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def test(request):
    return HttpResponse('{"text":"Test success!"}')


def jtest(request, question_id):
    return JsonResponse({'text': "Test success!", 'Question': str(Question.objects.get(pk=question_id))})
