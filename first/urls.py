from django.conf.urls import url
from django.urls import path
from first import views

app_name = 'first'

urlpatterns = [
    path('first/', views.links),
    path('api/<int:question_id>/', views.jtest, name='jsontest'),
    path('api/questions/', views.questions),
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^(?P<path>.*)/$', views.HomePageView.as_view()),
]

