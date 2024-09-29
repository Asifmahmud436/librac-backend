from django.shortcuts import render
from .serializers import CourseSerializer
from .models import Course
from rest_framework import viewsets


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset =  super().get_queryset()
        teacher_id = self.request.query_params.get('teacher_id')
        teacher_name = self.request.query_params.get('teacher_name')
        if teacher_name:
            queryset = queryset.filter(teacher__user__username__icontains=teacher_name)
        if teacher_id:
            queryset = queryset.filter(teacher_id=teacher_id)
        return queryset
        
