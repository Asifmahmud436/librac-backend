from rest_framework import serializers
from .models import Teacher
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','user_type','is_staff']

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = '__all__'

class TeacherRegistrationSerializer(serializers.ModelSerializer):
    librac_id = serializers.IntegerField()
    designation = serializers.CharField(max_length=60)
    confirm_password = serializers.CharField(max_length=20,required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','librac_id','designation','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        librac_id = self.validated_data['librac_id']
        designation = self.validated_data['designation']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password != confirm_password:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched."})
        
        if User.objects.filter(email = email, user_type = 'Teacher').exists():
            raise serializers.ValidationError({'error' : "Email Already Exists."})
        
        account = User(
            username = username, first_name = first_name, last_name = last_name, email = email, 
            user_type = 'Teacher',
        )

        account.set_password(password)
        account.is_active = False 
        account.save()

        teacher_account = Teacher(
            user = account,
            librac_id = librac_id,
            designation = designation,
        )

        teacher_account.save()
        return account