from rest_framework import response, viewsets,status    
from apps.user.models import User
from rest_framework.response import Response
from apps.user.api.serializers import UserListSerializer, UserSerializer,PasswordUserValidate
from rest_framework.decorators import action
from django.http import Http404


class UserViewSet(viewsets.GenericViewSet):
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    def get_object(self, pk):
        return self.serializer_class.Meta.model.objects.filter(id= pk)
    
    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.Meta.model.objects.filter(is_active=True).values('id', 'username', 'email', 'password', 'name', 'last_name')
        return self.queryset
    
    @action(detail=True, methods=['post'])
    def change_password(self, request, pk = None):
        user = User.objects.filter(id = pk).first()
        if not user:
            raise Http404
        password_serializer = PasswordUserValidate(data= request.data)
        if password_serializer.is_valid():
            user.change_password(password_serializer._validated_data['password'])
            user.save()
            return Response({
                'message' : 'Contraseña actualizada correctamente'
            })
        return Response(password_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    #GET
    def list(self, request):
        users = self.get_queryset()
        user_serializer = self.list_serializer_class(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    #POST   
    def create(self, request):
        user_serializer  = self.serializer_class(data= request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message' : "Usuario Creado correctamente"
            }, status= status.HTTP_201_CREATED)
        return Response({
            'message' : 'Ocurrio un error',
            'error ' : user_serializer.errors
        }, status= status.HTTP_400_BAD_REQUEST)
    #GET
    def retrieve(self, request, pk=None):
        user = User.objects.get(pk=pk)  # Obtener una instancia individual del modelo User por su clave primaria (pk)
        user_serializer = self.serializer_class(user)  # Serializar la instancia del usuario
        return Response(user_serializer.data, status=status.HTTP_202_ACCEPTED)

    #DELETE
    def delete(self, request, pk = None):
        user_destroy = User.objects.filter(id = pk).update(is_active = False)
        if user_destroy == 1:
            return Response({
                'message' : "El usuario a sido eliminado"
            },status=status.HTTP_202_ACCEPTED)
        return Response({
            'message' : 'no existe el usuario'
        }, status= status.HTTP_404_NOT_FOUND)