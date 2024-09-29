from django.shortcuts import render
from .models import Dashboard
from .serializers import DashboardSerializer
from rest_framework.viewsets import ModelViewSet

class DashboardViewSet(ModelViewSet):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('student_id')
        student_name = self.request.query_params.get('student_name')
        if student_name:
            queryset = queryset.filter(student__user__username__icontains=student_name)
        if student_id:
            queryset = queryset.filter(student_id=student_id)
        return queryset