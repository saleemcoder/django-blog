from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Post
from cmt . models import Cmt

def index(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts
    }

    return render(request, 'post/post.html', context)

def blogpost(request, post_id):
    post = get_object_or_404(Post, pk=post_id) 
    
    comments_query = Cmt.objects.order_by('-date')
    
    context = {
        'post' : post,
        'comments' : comments_query
    }


    if request.method == 'POST':
        comment = request.POST['comment']
        post_id = request.POST['post_id']
        user_name = request.POST['user_name']
        post_title = request.POST['post_title']
        
        query = Cmt(post_id=post_id, user_name=user_name, post_title=post_title, comment=comment)

        query.save();

        messages.success(request, 'Comment submitted successfully')

    return render(request, 'post/blogpost.html', context)



#def search(request):
#    return render(request, 'post/search.html')