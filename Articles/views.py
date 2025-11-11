from django.views import View
from django.http import HttpResponse

# Create your views here.

class Article_View (View) :
    def get (self , req) :
        return HttpResponse("A Response Of Get Method On Article View!")
    
    def post(self, req) :
        return HttpResponse()
