from django.db import models

# Create your models here.
class StarDetails(models.Model):
    name = models.CharField(max_length = 255)
    surface_temperature = models.CharField(max_length = 255)

    