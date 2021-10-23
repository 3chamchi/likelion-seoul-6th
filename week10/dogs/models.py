from django.db import models

class DogImage(models.Model):
    url = models.CharField(max_length=500)
    