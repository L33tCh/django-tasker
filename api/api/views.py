from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from ..models import Subject, Course
from .serialisers import SubjectSerialiser, CourseSerialiser, CourseWithContentsSerialiser
from .permissions import IsEnrolled

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework.decorators import action


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerialiser


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerialiser

    @action(detail=True,
            methods=['post'],
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})

    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerialiser,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated,
                                IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

