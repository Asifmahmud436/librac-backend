from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherRegistrationAPIView,TeacherDataByUserIDView,activate,TeacherViewSet

router = DefaultRouter()
router.register('list', TeacherViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('register/', TeacherRegistrationAPIView.as_view(), name='teacher_register'),
    path('active/<user_id>/<token>/', activate, name='teacher_account_activate'),

    path('by_user_id/', TeacherDataByUserIDView.as_view(), name='teacher_by_user_id'),
]