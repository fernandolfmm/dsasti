from django.db import models

# Create your models here.
class Ingredientes(models.Model):
    title= models.CharField(max_length=100)
    description= models.TextField()
class Ingredientes2(models.Model):
    Comida= models.CharField(max_length=100)
    descripcion2= models.TextField()
    

    

    
