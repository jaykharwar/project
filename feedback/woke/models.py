from django.db import models

# Create your models here.

class db(models.Model):
    name= models.CharField(max_length=30)
    dec = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
       
    def __str__(self):
        return self.name
    
    