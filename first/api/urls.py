from rest_framework import routers
from first.api.views import QuestionListView

router = routers.DefaultRouter()
# router.register(r'questions', views.QuestionViewSet)
router.register(r'question_list', QuestionListView)
# router.register(r'questions_choices', views.QuestionChoiceViewSet)
# router.register(r'choices', views.ChoiceViewSet)
