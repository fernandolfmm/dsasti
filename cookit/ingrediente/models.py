from django.db import models

class Ingrediente(models.Model):
    name = models.CharField(max_length=70)