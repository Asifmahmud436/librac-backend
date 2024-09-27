from django.urls import path,include
from .views import AssignmentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('list',AssignmentViewSet)

urlpatterns = router.urls

