from django.db import models

class Post_QuerySet(models.QuerySet):
    def published(self):
        return self.filter(published = True)
    
    def recent (self) :
        return self.order_by("-created_at")
    
class Post_Manager(models.Manager) :
    def get_queryset(self):
        return Post_QuerySet(self.model , using=self.db)
    
    def published(self):
        return self.get_queryset().published()
    