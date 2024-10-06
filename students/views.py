from django.shortcuts import render, redirect
from rest_framework import viewsets, status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Student
from .serializers import StudentRegistrationSerializer,StudentSerializer
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


from accounts.models import CustomUser

User = get_user_model()




# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        student_name = self.request.query_params.get('student_name')
        if student_name:
            queryset = queryset.filter(user__username__icontains=student_name)
        return queryset


class StudentRegistrationAPIView(APIView):
    serializer_class = StudentRegistrationSerializer

    def post(self, request):
        # form er moto kore 'serialized_data' nie nilam
        serialized_data = self.serializer_class(data = request.data)

        if serialized_data.is_valid():
            user = serialized_data.save()
            token = default_token_generator.make_token(user)
            print('token :', token)
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            print('user_id :', user_id)
            confirm_link = f'https://librac-backend.vercel.app/students/active/{user_id}/{token}/'
            email_subject = 'Confirm Your Account'
            email_body = render_to_string('student_confirmation.html', {
                'user': user,
                'confirm_link': confirm_link,
            })

            email = EmailMultiAlternatives(email_subject, '', to = [user.email])
            email.attach_alternative(email_body, 'text/html')
            email.send()


            return Response({'message': 'Check your mail for confirmation.'}, status=status.HTTP_201_CREATED)


        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


def activate(request, user_id, token):
    try:
        user_id = urlsafe_base64_decode(user_id).decode()
        user = CustomUser._default_manager.get(pk = user_id)
    except(CustomUser.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('user-login')
    else:
        return redirect('student_register')


class StudentDataByUserIDView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        
        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = Student.objects.get(user=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = StudentSerializer(user)
        print('user:', serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)