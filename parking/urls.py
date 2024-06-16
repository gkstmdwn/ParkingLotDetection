from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),

]

def home(request):
    return render(request, 'home.html')