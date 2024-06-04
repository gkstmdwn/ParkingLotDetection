from django.db import models

class ParkingVideo(models.Model):
    video = models.FileField(upload_to='parking_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    result_image = models.ImageField(upload_to='result_images/', blank=True, null=True)

    def __str__(self):
        return f"Uploaded at {self.uploaded_at}"