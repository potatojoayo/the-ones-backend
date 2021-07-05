from django.db import models

class Director(models.Model):
    
    name = models.CharField(max_length=50)
