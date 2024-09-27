from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DashboardViewSet

router = DefaultRouter()
router.register('list',DashboardViewSet)

urlpatterns = router.urls
