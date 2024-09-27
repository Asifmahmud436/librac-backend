from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    USER_ROLES_FIELD = (
        ('Student','Student'),
        ('Teacher','Teacher'),
    )

    user_type = serializers.CharField()

    # retrieving and overriding the date in our registration serializer.the "" is for the default empty string
    def get_cleaned_data(self):
        data =  super().get_cleaned_data()
        data['user_type'] = self.validated_data.get('user_type','')
        return data
    
    # overriding and saving
    def save(self,request):
        user = super().save(request)
        user.user_type = self.validated_data.get('user_type')
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_type']
