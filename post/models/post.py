from django.db import models
from book.models import Book
from movie.models import Movie
from user.models import User

class Post(models.Model):
    
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    movie = models.ForeignKey(Movie, on_delete=models.RESTRICT)
    contents = models.TextField()
    title = models.CharField(max_length=100)
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
