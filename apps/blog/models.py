from django.db import models
from django.utils import timezone
from apps.user.models import User
import uuid

# Create your models here.

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.title, filename)

class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status ='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    blog_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    title =     models.CharField(max_length=250)
    post_comments = models.ManyToManyField('comments.Comment', related_name='posts')
    thumnail =  models.ImageField(upload_to=user_directory_path, blank=True, null= True)
    video =     models.FileField(upload_to=user_directory_path, blank=True, null=True)
    exerpt =    models.TextField(null= True)
    content =   models.TextField()
    slug =      models.SlugField(max_length=250, unique_for_date='published', null= False, unique= True)
    published = models.DateTimeField(default=timezone.now)      
    author =    models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'post_user')
    status =    models.CharField(max_length=10, choices=options, default='draft')
    #Devuelve todos los blogs
    objects =   models.Manager()
    #Devuelve los Blogs mediante el PostObjects
    postobjects = PostObjects()

    class Meta:
        ordering = ('published',)



    def __str__(self) -> str:
        return self.title

    def get_video(self):
        if self.video:
            return self.video.url
        else:
            return ""
        
    def get_thumnail(self):
        if self.thumnail:
            return self.thumnail.url
        else:
            return ""