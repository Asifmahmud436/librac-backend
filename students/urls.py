from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentDataByUserIDView,StudentRegistrationAPIView,StudentViewSet,activate


# Create a router
router = DefaultRouter()

# register ViewSets with the router.
router.register('list', StudentViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),

    path('register/', StudentRegistrationAPIView.as_view(), name='student_register'),
    path('active/<user_id>/<token>/', activate, name='student_account_activate'),

    path('by_user_id/', StudentDataByUserIDView.as_view(), name='student_by_user_id'),
]