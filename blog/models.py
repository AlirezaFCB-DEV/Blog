from django.db import models

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created_at = modecls.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title