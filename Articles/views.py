from django.views import View
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Article_View (View) :
    def get (self , req) :
        return HttpResponse("A Response Of Get Method On Article View!")
    
    def post(self, req) :
        return HttpResponse()
    
#! A Class View For Test Mixins
class Profile_View (View , LoginRequiredMixin) :
    def get(self , req) :
        return HttpResponse("Profile View For Logged Users.!!")