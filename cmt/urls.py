from django.urls import path
from . import views

urlpatterns = [
    path('postcmt', views.postcmt, name='postcmt'),
]