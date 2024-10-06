from django.shortcuts import render
from .models import Assignment
from .serializers import AssignmentSerializer
from rest_framework import viewsets
from students.models import Student

class AssignmentViewSet(viewsets.ModelViewSet):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    def get_queryset(self):
        queryset = Assignment.objects.all()
        course_id = self.request.query_params.get('course_id')
        course_name = self.request.query_params.get('course_name')
        teacher_id = self.request.query_params.get('teacher_id')
        teacher_username = self.request.query_params.get('teacher_username')
        student_username = self.request.query_params.get('student_username')

        if student_username:
            try:
                student = Student.objects.get(user__username=student_username)
                enrolled_courses = student.dashboard.filter(drop_course=False).values_list('course_id', flat=True)
                queryset = queryset.filter(course_id__in=enrolled_courses)
            except Student.DoesNotExist:
                return Assignment.objects.none()

        
        if teacher_id:
            queryset = queryset.filter(course__teacher_id=teacher_id)

        
        if teacher_username:
            queryset = queryset.filter(course__teacher__user__username__icontains=teacher_username)

        
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        if course_name:
            queryset = queryset.filter(course__name__icontains=course_name)

        return queryset
