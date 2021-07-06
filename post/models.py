from django.db import models

class Post(models.Model):
    
    writer = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='writtens')
    book = models.ForeignKey('book.Book', on_delete=models.RESTRICT)
    movie = models.ForeignKey('movie.Movie', on_delete=models.RESTRICT)
    replying_to = models.ForeignKey('self',  related_name='replies', on_delete=models.SET_NULL, null=True)
    contents = models.TextField()
    title = models.CharField(max_length=100)
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        s = str(self.title)
        if self.book:
            s = s + ' on book {}'.format(self.book)
        elif self.movie:
            s = s + ' on movie {}'.format(self.movie)
        s = s + ' {}'.format(self.written_date)
        return s
