from django.db import models
from . import User

class Follow(models.Model): 

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followee')

    class Meta:
        unique_together = ('follower','followee')
