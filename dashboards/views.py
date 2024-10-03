from .models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class DashboardViewSet(ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id')
        course_id = self.request.query_params.get('course_id')
        student_name = self.request.query_params.get('student_name')
        if student_name:
            queryset = queryset.filter(student__user__username__icontains=student_name)
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)
        return queryset
    
    @action(detail=True, methods=['patch'])
    def drop(self, request, pk=None):
        try:
            # Ensure only the logged-in student's course is dropped
            dashboard = Dashboard.objects.get(id=pk)
            print(f"Before Update: {dashboard.drop_course}")  # Add this line
            dashboard.drop_course = True
            dashboard.save()
            print(f"After Update: {dashboard.drop_course}")  # Add this line
            return Response({'message': 'Course dropped successfully'}, status=status.HTTP_200_OK)
        except Dashboard.DoesNotExist:
            return Response({"error": "You are not enrolled in this course or it does not exist."}, status=status.HTTP_404_NOT_FOUND)
