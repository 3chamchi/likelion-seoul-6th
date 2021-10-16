from django.db import models

class Photolog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title