from rest_framework import serializers
from apps.blog.models import Post
from apps.comments.serializer import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)  # Serializador para los comentarios

    class Meta:
        model= Post
        fields = ('id', 'title', 'thumnail', 'exerpt','content', 'slug', 'published', 'author', 'status', "video", "comments") 