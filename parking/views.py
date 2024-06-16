import shutil

from django.shortcuts import render, redirect
from .forms import ParkingVideoForm
from .models import ParkingVideo
import cv2
import os
from django.conf import settings

def home(request):
    return render(request, 'home.html')


def upload_video(request):
    if request.method == 'POST':
        form = ParkingVideoForm(request.POST, request.FILES)
        if form.is_valid():
            parking_video = form.save()
            process_video(parking_video)
            return redirect('video_list')
    else:
        form = ParkingVideoForm()
    return render(request, 'upload_video.html', {'form': form})


def process_video(parking_video):
    video_path = parking_video.video.path
    result_video_dir = os.path.join(settings.MEDIA_ROOT, "result_videos")
    result_video_path = os.path.join(settings.MEDIA_ROOT, f"result_videos/result_{parking_video.id}.mp4")
    if not os.path.exists(result_video_dir):
        os.makedirs(result_video_dir)

    shutil.copy(video_path, result_video_path)

    if os.path.exists(result_video_path):
        parking_video.result_video = f"result_videos/result_{parking_video.id}.mp4"
        parking_video.processed = True
        parking_video.save()


def video_list(request):
    videos = ParkingVideo.objects.filter(processed=True)
    return render(request, 'video_list.html', {'videos': videos})
