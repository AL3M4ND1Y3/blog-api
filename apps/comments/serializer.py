from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')  # Campo de solo lectura para el nombre de usuario
    post_title = serializers.ReadOnlyField(source='post.title')

    class Meta: 
        model = Comment
        fields = '__all__'
        extra_kwargs = {
            'post_id': {'required': True},
            'author_id': {'required': True},
        }
        read_only_fields = ('author_id', 'post_id')
