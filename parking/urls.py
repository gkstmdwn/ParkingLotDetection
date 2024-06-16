from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.image_list, name='image_list'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)