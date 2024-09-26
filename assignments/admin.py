from django.contrib import admin
from .models import Assignment

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ['name','marks','get_course_name']

    def get_course_name(self,obj):
        return obj.course.name
    get_course_name.short_description = "Course"

admin.site.register(Assignment,AssignmentAdmin)
