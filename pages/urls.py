from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs', views.blogs, name='blogs'),
    path('about-us', views.about, name='about-us'),
    path('contact-us', views.contact, name='contact-us'),
]