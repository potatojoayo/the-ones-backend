from django.db import models
from . import Book, Author

class Book_Author(models.Model): 
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('book','author'))
