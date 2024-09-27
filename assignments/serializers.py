from .models import Assignment
from rest_framework import serializers

class AssignmentSerializer(serializers.ModelSerializer):
    name_of_course = serializers.CharField(source='course.name',read_only=True)
    class Meta:
        model = Assignment
        fields = ['id','name','marks','course','name_of_course']

