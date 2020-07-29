from django.shortcuts import render


def index(request):
    return render(request, 'post/post.html')

def blogpost(request):
    return render(request, 'post/blogpost.html')

def search(request):
    return render(request, 'post/search.html')