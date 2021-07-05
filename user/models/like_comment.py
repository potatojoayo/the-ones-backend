from django.db import models
from . import User 
from comment.models import Comment

class Like_Comment(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','comment')
