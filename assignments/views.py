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

        # Filter assignments based on student username
        if student_username:
            try:
                # Fetch the student based on the provided username
                student = Student.objects.get(user__username=student_username)
                
                # Fetch the IDs of all the courses the student is enrolled in
                enrolled_courses = student.dashboard.filter(drop_course=False).values_list('course_id', flat=True)
                
                # Filter assignments based on the student's enrolled courses
                queryset = queryset.filter(course_id__in=enrolled_courses)
            except Student.DoesNotExist:
                # If the student does not exist, return an empty queryset
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
