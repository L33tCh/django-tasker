from django.conf.urls import url
from django.urls import path, include
from first import views
from .api.urls import router

app_name = 'first'

urlpatterns = [
    path('first/', views.IndexView.as_view(), name='index'),
    path('first/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('first/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('first/<int:question_id>/vote/', views.vote, name='vote'),

    path('api/v1/', include(router.urls)),

    path('api/', views.test),
    path('api/questions/', views.questions),
    path('api/questions/<int:question_id>/', views.api_detail),
    path('api/questions/<int:question_id>/vote/', views.api_vote),
    url(r'^((?!api).)*$', views.HomePageView.as_view()),
    url(r'^((?!api).)*(?P<path>.*)/$', views.HomePageView.as_view()),
]

