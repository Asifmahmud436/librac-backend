from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id','get_teacher','get_email','librac_id','get_user_type','designation']

    def get_teacher(self,obj):
        return obj.user.username
    def get_email(self,obj):
        return obj.user.email
    def get_user_type(self,obj):
        return obj.user.user_type

admin.site.register(Teacher,TeacherAdmin)

