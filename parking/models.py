from django.db import models
from django.utils.translation import gettext_lazy as _

class ParkingVideo(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to='parking_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    result_image = models.ImageField(upload_to='result_images/', blank=True, null=True)
    result_video = models.FileField(upload_to='result_videos/', blank=True, null=True)
    class Meta:
        verbose_name = _("Parking Video")
        verbose_name_plural = _("Parking Videos")

    def __str__(self):
        return self.title if self.title else f"Uploaded at {self.uploaded_at}"

    def delete(self, *args, **kwargs):
        self.video.delete(save=False)
        if self.result_image:
            self.result_image.delete(save=False)
        super().delete(*args, **kwargs)