from django.db import models
from apps.user.models import User
from apps.blog.models import Post

class Comment(models.Model):
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=False, blank=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField()
    
    def __str__(self) -> str:
        return self.content
    
    def get_author(self) -> str:
            return self.author.username