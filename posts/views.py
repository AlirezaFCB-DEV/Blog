import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post

# Create your views here.
@csrf_exempt
@login_required
def create_post(req):
    if req.method != "POST" :
        return JsonResponse({"error": "Invalid request method"}, status=405)
    
    try :
        data = json.loads(req.body)
    except json.JSONDecodeError :
        return JsonResponse({"error" : "Invalid JSON data!"} , status=400)
    
    title = data.get("title")
    content = data.get("content")
    published = data.get("published" , False)
    
    errors = {}
    
    if not title :
        errors["title"] = "Title is required"
    elif len(title.strip()) < 5 :
        errors["title"] = "Title Must be at least 5 characters long"
    
    if not content :
        errors["content"] = "Content is required"
    
    if errors :
        return JsonResponse({"errors" : errors} , status=400)
    
    new_post = Post.objects.create(author=req.user , title=title , content=content , published=published)
    new_post.save()
    
    return JsonResponse({"msg" : "post created successfully!!" , "post" : {
        "id" : new_post.id,
        "title" : new_post.title,
        "content" : new_post.content,
        "published" : new_post.published
    }} , status=201)


@login_required
def delete_post(req, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != req.user:
        return JsonResponse({"error ": "You are not authorized to delete this post"}, status=403)

    post.delete()
    return JsonResponse({"msg": "Post deleted successfully !!"}, status=201)
