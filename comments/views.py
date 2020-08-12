from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment


def comment(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        user_id = request.POST['user_id']
        post_title = request.POST['post_title']
        comment = request.POST['comment']

        query = Comment(post_id=post_id, user_id=user_id, post_title=post_title, comment=comment)
        query.save()

        messages.success(request, 'Thanks for your Comment about this post')

        return redirect('blogpost'+post_id)
