from django import forms 
from .models import *
  
class Imageform(forms.ModelForm): 
  
    class Meta: 
        model = Image 
        fields = ['soil_image'] 
