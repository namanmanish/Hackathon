from django.db import models

class Image(models.Model): 
	soil_image = models.ImageField(upload_to='images/') 