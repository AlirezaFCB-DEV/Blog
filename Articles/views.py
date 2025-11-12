from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView

from .models import Article
# Create your views here.

class Article_List_View(ListView) :
    model = Article
    
    def render_to_response(self, context, **response_kwargs):
         data = list(context["object_list"].values())
         return JsonResponse(data , safe=False)