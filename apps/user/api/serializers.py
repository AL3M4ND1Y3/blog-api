from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from apps.user.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','name','last_name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'name', 'last_name']
        
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password'],
            'name' : instance['name'],
            'last_name': instance['last_name']
        }
    
class PasswordUserValidate(serializers.ModelSerializer):
    password = serializers.CharField(max_length= 128, min_length= 6, write_only = True)
    password1 = serializers.CharField(max_length= 128, min_length= 6, write_only = True)

    def validate(self, data):
        if data['password'] != data['passowrd1']:
            raise serializers.ValidationError(
                {'password': 'Las contraseñas tienen que ser iguales'}
            )
        return data