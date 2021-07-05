from django.db import models
from . import Post

class Reply(models.Model): 

    replied = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replied')
    replying = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replying')

    class Meta:
        unique_together = ('replied','replying')
