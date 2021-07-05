from django.db import models
from . import Comment
from post.models import Post

class Comment_Of(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('post','comment')
