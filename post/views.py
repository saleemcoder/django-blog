from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts
    }

    return render(request, 'post/post.html', context)

def blogpost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    context = {
        'post' : post
    }
    return render(request, 'post/blogpost.html', context)

#def search(request):
#    return render(request, 'post/search.html')