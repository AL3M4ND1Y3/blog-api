from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.user.api.serializers import CustomTokenObtainPairSerializer,CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from apps.user.models import User
from rest_framework_simplejwt.tokens import RefreshToken




# Create your views here.

#########
#LOGIN
#########
class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    def post(self, request, *args, **kwargs):
        userername = request.data.get('username', "")
        password = request.data.get("password", "")
        user_id = request.data.get("id", "")
        user = authenticate(
            username = userername,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh_token' : login_serializer.validated_data.get('refresh'),
                    'user' : user_serializer.data,
                    'user_id': user.id,
                    'message' : 'Inicio Existoso'
                }, status= status.HTTP_202_ACCEPTED)
            return Response({
                'error' : 'Contraseña o nombre de usuarios incorrectos'
            }, status= status.HTTP_400_BAD_REQUEST) 
        return Response({
            'error' : 'Contraseña o nombre de usuarios incorrectos'
        }, status= status.HTTP_400_BAD_REQUEST)
    


#########
#LOGOUT
#########    

class Logout(GenericAPIView):
    def post(self,request, *args, **kwargs):
        #Filtramos el usuario y traemos el primero que obtuvimos, si no encontramos nada devolvemos un campo vacio
        user = User.objects.filter(id = request.data.get('user', 0)).first()
        if user:
                RefreshToken.for_user(user)  # Elimina el uso de .first()
                return Response({
                    'message': 'Sesión cerrada correctamente'
                }, status=status.HTTP_202_ACCEPTED)
        return Response({
            'error': 'No se ha encontrado un usuario con esos datos'
        }, status=status.HTTP_404_NOT_FOUND)