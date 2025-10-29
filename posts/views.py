from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Post

# Create your views here.


@login_required
def delete_post(req, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != req.user:
        return JsonResponse({"error ": "You are not authorized to delete this post"}, status=403)

    post.delete()
    return JsonResponse({"msg": "Post deleted successfully !!"}, status=201)
