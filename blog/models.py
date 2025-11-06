from django.db import models
from .managers import Post_Manager

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    published = models.BooleanField(default=False )
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = Post_Manager()
    
    def __str__(self):
        return self.title