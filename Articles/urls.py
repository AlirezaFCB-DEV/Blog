from django.urls import path
from . import views

app_name = "Articles"
urlpatterns = [
    path("articles/" , views.article_list , name="article-list"),
]