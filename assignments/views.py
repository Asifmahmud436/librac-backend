from django.shortcuts import render
from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework import viewsets

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        course_id = self.request.query_params.get('course_id')
        course_name = self.request.query_params.get('course_name')
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        if course_name:
            queryset = queryset.filtere(course_name=course_name)
        return queryset


