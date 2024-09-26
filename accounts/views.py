from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializer import LoginSerializer,UserAccountSerializer
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token

User = get_user_model()

# to get the user object by id
class UserDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self,request,format=None):
        user_id = request.query_params.get('user_id')

        if not user_id:
            return Response({'error': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = UserAccountSerializer(user)
        print('user:', serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

# we can use from dj-rest-auth.views import LoginView
# in that way ,we dont need to create extra serializers or views 
class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        serialized_data = self.serializer_class(data=request.data)

        if serialized_data.is_valid():
            username = serialized_data.validated_data['username']
            password = serialized_data.validated_data['username']
            user = authenticate(username = username,password = password)

            if user:
                token, _ = Token.objects.get_or_create(user = user)   
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid credential'})
        
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutAPIView(APIView):
    def get(self,request):
        logout(request)
        return Response("Logout successful.")


