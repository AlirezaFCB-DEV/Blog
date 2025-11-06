from django.db import models

class Published_Manager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(published=True)