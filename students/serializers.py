from rest_framework import serializers
from .models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','user_type']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = '__all__'

class StudentRegistrationSerializer(serializers.ModelSerializer):
    librac_id = serializers.IntegerField()
    confirm_password = serializers.CharField(max_length=20,required=True)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','librac_id','email','password','confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        librac_id = self.validated_data['librac_id']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        
        if password != confirm_password:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched."})
        
        if User.objects.filter(email = email, user_type = 'employer').exists():
            raise serializers.ValidationError({'error' : "Email Already Exists."})
        
        account = User(
            username = username, first_name = first_name, last_name = last_name, email = email, 
            user_type = 'Student',
        )

        account.set_password(password)
        account.is_active = False 
        account.save()

        student_account = Student(
            user = account,
            librac_id = librac_id,
        )

        student_account.save()
        return account