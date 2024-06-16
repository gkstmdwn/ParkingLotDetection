from django.db import models

class ParkingImage(models.Model):
    image = models.ImageField(upload_to='parking_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    result_image = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return f"Uploaded at {self.uploaded_at}"