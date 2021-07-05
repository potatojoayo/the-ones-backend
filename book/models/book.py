from django.db import models

# Create your models here.

class Book(models.Model):
    
    title = models.CharField(max_length=50, blank=False)
    sub_title = models.CharField(max_length=50, null=True)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_path = models.CharField(max_length=255)

