from django.db import models

class Movie(models.Model):

    title = models.CharField(max_length=100)
    title_original = models.CharField(max_length=100, null=True)
    year = models.IntegerField(default=0)
    image = models.CharField(max_length=255, null=True)
    rating = models.FloatField(default=0)
    directors = models.ManyToManyField('movie.Director', related_name='films', blank=True)
    actors = models.ManyToManyField('movie.Actor', related_name='films', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-rating']
