from .models import Dashboard
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class DashboardSerializer(ModelSerializer):
    student_name = serializers.CharField(source='student.user.username',read_only=True)
    course_name = serializers.CharField(source='course.name',read_only=True)
    class Meta:
        model = Dashboard 
        fields = ['id','drop_course','course','student','student_name','course_name']
