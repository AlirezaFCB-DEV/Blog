from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView

from .models import Article
# Create your views here.

class Article_List_View(ListView) :
    model = Article
    
    def render_to_response(self, context, **response_kwargs):
         data = list(context["object_list"].values())
         return JsonResponse(data , safe=False)
     
class Article_Create_View(CreateView) :
    model = Article
    fields = ["title" , "content"]
    success_url = reverse_lazy("article_list")
    
class Article_Delete_View(DeleteView) : 
    model = Article
    success_url = reverse_lazy("article_list")
    
class Article_Update_View(UpdateView) :
    model = Article
    fields = ["title" , "content"]
    success_url = reverse_lazy("article_list")
    