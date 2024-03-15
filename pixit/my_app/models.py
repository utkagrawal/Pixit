from django.db import models

# Create your models here.
class mydata(models.Model):
    image= models.ImageField(upload_to="touse/images", default='')