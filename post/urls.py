from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='post'),
    path('blogpost', views.blogpost, name='blogpost'),
    path('search', views.search, name='search'),
    
]