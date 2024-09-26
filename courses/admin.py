from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','code','get_teacher_name']

    def get_teacher_name(self,obj):
        return obj.teacher.user.username
    get_teacher_name.short_description = "Faculty"

admin.site.register(Course,CourseAdmin)

