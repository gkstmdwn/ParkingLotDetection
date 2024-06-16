from django import forms
from .models import ParkingVideo

class ParkingVideoForm(forms.ModelForm):
    class Meta:
        model = ParkingVideo
        fields = ['video']