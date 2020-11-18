from django.db import models

# Create your models here.
class Users(models.Model):
    name= models.CharField(max_length=70)
    fullName= models.CharField(max_length=70)
    gener= models.CharField(max_length=70)
    correo= models.CharField(max_length=150)
    password= models.CharField(max_length=70)
    rol= models.CharField(max_length=1)