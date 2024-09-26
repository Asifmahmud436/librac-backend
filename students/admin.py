from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','get_student','get_email','librac_id','get_user_type']

    def get_student(self,obj):
        return obj.user.username
        
    def get_email(self,obj):
        return obj.user.email

    def get_user_type(self,obj):
        return obj.user.user_type

admin.site.register(Student,StudentAdmin)

