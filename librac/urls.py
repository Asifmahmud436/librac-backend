from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('students/',include('students.urls')),
    path('teachers/',include('teachers.urls')),
    path('courses/',include('courses.urls')),
    path('assignments/',include('assignments.urls')),
    path('dashboards/',include('dashboards.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)