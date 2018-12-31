from django.conf.urls import url
from first import views
 
urlpatterns = [
    url(r'^links/$', views.LinksPageView.as_view()),
    url(r'^(?P<path>.*)/$', views.HomePageView.as_view()),
]
