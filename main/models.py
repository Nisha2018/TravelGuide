from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='location_images',
                            default='media/default.png')
    description = models.CharField(max_length=1000)
    Best_Time_to_Visit = models.CharField(max_length=100)

    def __str__(self):
        return self.name 
