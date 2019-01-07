from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice
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
    try:
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('links.html')
        context = {
            'latest_question_list': latest_question_list,
        }
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, 'links.html', context)
    # return HttpResponse(template.render(context, request))


def test(request):
    return HttpResponse('{"text":"Test success!"}')


def jtest(request, question_id):
    try:
        q = str(Question.objects.get(pk=question_id))
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return JsonResponse({'text': "Test success!", 'Question': q})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('first:results', args=(question.id,)))
