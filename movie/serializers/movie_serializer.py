from rest_framework import serializers
from movie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id',
                  'title',
                  'title_original',
                  'rating',
                  'image',
                  'year',
                  'directors',
                  'actors']

