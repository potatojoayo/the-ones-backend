from django.db import models
from . import Movie, Director

class Movie_Director(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
