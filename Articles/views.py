from django.core.paginator import Paginator
from django.http import JsonResponse

from .models import Article

def article_list (req) :
    articles = Article.objects.all()
    paginator = Paginator(articles , 5)
    
    page_number = req.GET.get("page" , 1)
    page_obj = paginator.get_page(page_number)
    
    data = {
        "page" : page_obj.number,
        "num_pages" : paginator.num_pages,
        "articles" : list(page_obj.object_list.values())
    }
    
    return JsonResponse(data)

    