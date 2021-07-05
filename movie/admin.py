from django.contrib import admin
from movie.models import Movie, Director, Movie_Director

# Register your models here.

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Movie_Director)

