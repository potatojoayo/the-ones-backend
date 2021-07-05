from django.contrib import admin
from book.models import Book, Book_Author, Author

# Register your models here.

admin.site.register(Book)
admin.site.register(Book_Author)
admin.site.register(Author)

