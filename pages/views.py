from django.shortcuts import render
from post.models import Post

def index(request):
    posts = Post.objects.order_by('-date')[:3]
    
    context = {
        'posts':posts
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact-us.html')
