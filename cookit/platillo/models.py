from django.db import models

class Platillo(models.Model):
    nombre= models.CharField(max_length=70)
    ingrdiente= models.CharField(max_length=70)
