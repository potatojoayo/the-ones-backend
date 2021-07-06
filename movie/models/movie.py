from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    title_en = models.CharField(max_length=50, null=True)
    year = models.IntegerField(default=0)
    image_path = models.CharField(max_length=255, null=True)
    directors = models.ManyToManyField('movie.Director', related_name='films')

    def __str__(self):
        return self.title
