from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('subjects/',
         views.SubjectListView.as_view(),
         name='subject_list'),

    path('subjects/<pk>/',
         views.SubjectDetailView.as_view(),
         name='subject_detail'),

    path('courses/',
         views.CourseListView.as_view(),
         name='course_list'),

    path('courses/<pk>/',
         views.CourseDetailView.as_view(),
         name='course_detail'),

    path('courses/<pk>/enroll/',
         views.CourseEnrollView.as_view(),
         name='course_enroll'),
]
