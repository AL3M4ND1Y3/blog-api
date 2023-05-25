from django.shortcuts import render
from rest_framework import viewsets,status
from .serializer import CommentSerializer
from .models import Comment
from rest_framework.response import Response
from rest_framework.decorators import action
from apps.blog.models import Post
from django.shortcuts import get_object_or_404



class CommentsViewSet(viewsets.ModelViewSet):
    list_serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def list(self, request):
        comments = self.queryset
        user_serializer = self.list_serializer_class(comments, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        post_id = request.data.get('post')
        post = get_object_or_404(Post, id = post_id )
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            comment = serializer.save()
            comment.author = request.user  # Asignar el autor como el usuario autenticado
            comment.save()
            
            return Response({
                'message': 'Comentario agregado al post'
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

