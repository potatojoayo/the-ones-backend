from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateField()
    image_path = models.CharField(max_length=255)
