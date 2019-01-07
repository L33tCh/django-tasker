from django.conf.urls import url
from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
    path('first/', views.IndexView.as_view(), name='index'),
    path('first/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('first/<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('first/<int:question_id>/vote/', views.vote, name='vote'),

    path('api/questions/', views.questions),
    path('api/questions/<int:question_id>/', views.jtest),
    path('api/questions/<int:question_id>/vote/', views.api_vote),
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^(?P<path>.*)/$', views.HomePageView.as_view()),
]

