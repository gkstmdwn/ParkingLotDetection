from django.shortcuts import render, redirect

from parking_project import settings
from .forms import ParkingImageForm
from .models import ParkingImage
import cv2  # OpenCV for image processing
import numpy as np
from ultralytics import YOLO
import numpy as np
import os
import shutil

def home(request):
    return render(request, 'home.html')
def upload_image(request):
    if request.method == 'POST':
        form = ParkingImageForm(request.POST, request.FILES)
        if form.is_valid():
            parking_image = form.save()
            process_image(parking_image)
            return redirect('image_list')
    else:
        form = ParkingImageForm()
    return render(request, 'upload_image.html', {'form': form})

def process_image(parking_image):
    # 이미지 분석 및 처리 로직
    # AI 모델 로드 및 이미지 분석
    image_path = parking_image.image.path
    image = cv2.imread(image_path)
    model=YOLO(r'best.pt')
    results = model.predict(image, save=True, conf=0.25)
    try:
        os.remove("/parking/static/image/image0.jpg")
    except:
        pass
    try:
        os.remove("runs/detect/predict2")
    except:
        pass
    try:
        os.rmdir("runs/detect/predict2")
    except:
        pass
    try:
        shutil.move(r"./runs/detect/predict2/image0.jpg", "./parking/static/image/image0.jpg")
    except:
        pass
    try:
        os.remove("runs/detect/predict/parking_images")
    except:
        pass
    try:
        os.remove("runs/detect/predict2")
    except:
        pass
    try:
        os.rmdir("runs/detect/predict2")
    except:
        pass

    # Dummy processing: converting image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result_path = f"{settings.MEDIA_ROOT}/result_images/result_{parking_image.id}.jpg"
    cv2.imwrite(result_path, gray)

    parking_image.result_image = f"result_images/result_{parking_image.id}.jpg"
    parking_image.processed = True
    parking_image.save()

def image_list(request):
    processed_images = ParkingImage.objects.filter(processed=True)
    context = {
        'processed_images': processed_images
    }
    return render(request, 'image_list.html', {'images': processed_images})
