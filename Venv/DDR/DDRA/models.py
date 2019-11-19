from django.db import models
import uuid

# Create your models here.

class eye_images(models.Model): 
    image = models.ImageField(upload_to= 'datasetsImages/',null = True, blank = True)
   
    
    

    