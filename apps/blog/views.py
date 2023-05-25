from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets


# Create your views here.
from .models import Post
from .serializers import PostSerializer
from .pagination import SmallPagination,MediumPagination,LargeePagination


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        return Post.postobjects.get_queryset().prefetch_related('comments') # Define el queryset utilizando el gestor PostObjects
        

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())    
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post creado'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Error al crear el post',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Post actualizado'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Error al actualizar el post',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs, ):
        instance = self.get_object()
        serializer = self.get_serializer(instance)  
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.status = 'draft'
            instance.save()
            return Response({
                'message': 'Blog cambiado a estado "draft" correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Error al cambiar el estado del post',
        }, status=status.HTTP_400_BAD_REQUEST)
    


""" class BlogListView(APIView):
    
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        post_serializer = PostSerializer(posts, many=True)
        return Response(post_serializer.data)
    
    def post(self,request):
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({
                    'message' : 'Post Creado'
                })
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            """

            
"""     def put(self, request, pk):
            post = get_object_or_404(Post, pk=pk)
            serializer = PostSerializer(post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """