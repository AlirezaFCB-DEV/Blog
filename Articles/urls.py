from django.urls import path
from . import views

app_name = "Articles"
urlpatterns = [
    path("articles/" , views.Article_View.as_view() , name="article_view")
    
]