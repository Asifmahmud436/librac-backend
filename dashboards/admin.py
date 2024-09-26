from django.contrib import admin
from .models import Dashboard

class DashboardAdmin(admin.ModelAdmin):
    list_display = ['get_course_name','get_student_name','drop_course']

    def get_course_name(self,obj):
        return obj.course.name
    get_course_name.short_description = "Course"

    def get_student_name(self,obj):
        return obj.student.user.username
    get_student_name.short_description = "Student"

admin.site.register(Dashboard,DashboardAdmin)