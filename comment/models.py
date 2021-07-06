from django.db import models
from user.models import User

class Comment(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE) 
    contents = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey('post.Post', related_name='comments',on_delete=models.CASCADE, null=True)
    comment = models.ForeignKey('comment.Comment', related_name='comments',on_delete=models.CASCADE, null=True)

    def __str__(self):
        s = str(self.writer)
        if self.post:
             s = s + ' to post {}'.format(self.post)
        elif self.comment:
            s = s + ' to comment {}'.format(self.comment)
        return s



