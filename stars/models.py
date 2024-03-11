from django.db import models

# Create your models here.
class Member(models.Model):
    firsname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    