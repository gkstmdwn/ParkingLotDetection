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
    video = cv2.VideoCapture(video_path)
    success, frame = video.read()

    if success:
        frame_path = os.path.join(settings.MEDIA_ROOT, f"frames/frame_{parking_video.id}.jpg")
        cv2.imwrite(frame_path, frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result_path = os.path.join(settings.MEDIA_ROOT, f"result_images/result_{parking_video.id}.jpg")
        cv2.imwrite(result_path, gray)

        parking_video.result_image = f"result_images/result_{parking_video.id}.jpg"
        parking_video.processed = True
        parking_video.save()


def video_list(request):
    videos = ParkingVideo.objects.filter(processed=True)
    return render(request, 'video_list.html', {'videos': videos})
