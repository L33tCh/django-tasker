from rest_framework import serializers
from ..models import Subject


class SubjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']
