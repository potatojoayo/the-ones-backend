from django.db import models
from user.models import User

class Comment(models.Model):

    writer = models.ForeignKey(User, on_delete=models.CASCADE) 
    contents = models.TextField()
    written_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



