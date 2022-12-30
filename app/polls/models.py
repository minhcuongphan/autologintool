from django.db import models

# Create your models here.

class website_credentials(models.Model):
    name= models.CharField(max_length=100)
    url= models.CharField(max_length=300)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    website_type= models.IntegerField()