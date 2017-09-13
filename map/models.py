from django.db import models

# Create your models here.
from django.db import models

class Address(models.Model):
    address = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()
