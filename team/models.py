from django.db import models
from Xarale.settings import MEDIA_ROOT
import os
# Create your models here.

class Staff(models.Model):
    Staff_Name = models.CharField(max_length=200)
    Staff_Position = models.CharField(max_length=200)
    Staff_Pic = models.ImageField(upload_to= os.path.join(MEDIA_ROOT, 'team members') )
    Facebook = models.URLField("facebook", max_length=200, blank = True)
    Twitter = models.URLField("Twitter", max_length=200, blank = True)
    Linkedin = models.URLField("Linkedin", max_length=200, blank = True)
    Instagram = models.URLField("Instagram", max_length=200, blank = True)

    def __str__(self):
        return self.Staff_Name