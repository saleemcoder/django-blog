from post.models import Post
    
def sidebar(request):
    posts = Post.objects.order_by('-date')[:7]
    sidecontent = {
        'sidebar':posts
    }
    return sidecontent
